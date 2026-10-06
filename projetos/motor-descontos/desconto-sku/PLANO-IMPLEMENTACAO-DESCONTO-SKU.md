# Motor de Descontos nível SKU — plano de implementação

*Var Retaguarda · 09/09/2026 · plano de implementação*

> **Documentos irmãos** (em `/Volumes/WD500GB/VERZEL/GAV/`): `PLANO-MOTOR-DESCONTOS-SKU.md` (investigação, 08/09), `MOTOR-DESCONTOS-SKU-RESUMO.md`, `MOTOR-DESCONTOS-SKU-DUVIDAS.md`.
> **DDL aplicado em homologação:** `/Volumes/WD500GB/DONATO/CLAUDE/Motor de Descontos SKU - DDL aplicado.pdf`.

## Contexto

Uma campanha de desconto (PRO014) hoje vale para o código de produto inteiro. Um produto com 10
cores que precisa de ação só na vermelha recebe a ação nas 10 — perda de margem nas cores
saudáveis. A EF §3.2 pede seleção por **cor**, **tamanho** ou **cor + tamanho**; a §3.1 manda
manter o cadastro por produto completo exatamente como está.

A investigação de ontem deixou decisões em aberto. **Três foram respondidas** desde então:

| Aberto ontem | Fechado hoje |
|---|---|
| Fonte da grade: `DOC002`, `LOGIX.CD_GRADE` ou catálogo Kafka? | **`XCOR001`/`XTAM001`** alimentam os selects; **`DOC002`** valida se a grade já vendeu (query do Fábio) |
| Como o usuário escolhe a grade — matriz cor × tamanho? | **Botão por item + modal com dois selects.** Sem matriz |
| Onde fica a marca de "item com grade"? | **Coluna nova 0/1 na `PRO0141`** |

E quatro decisões de comportamento fechadas com o dono do card:

- **Bloqueio parcial:** bloqueia só se o item nunca vendeu naquela cor (nenhum tamanho) ou
  naquele tamanho (nenhuma cor) — é erro de digitação. Se vendeu na cor mas nunca naquela
  combinação exata, **avisa e deixa confirmar** — esse é o SKU encalhado, o alvo do projeto.
- **Alcance:** rede toda, histórico completo. Sem filtro de loja nem de data.
- **Selects:** primeiro o que existe naquele item (com nº de vendas), depois o catálogo inteiro.
- **Remover a última grade** → a flag volta a 0 e o item volta a valer para o produto completo,
  na mesma transação.

**Resultado esperado:** cadastrar uma campanha em que a camiseta amarela tamanho M ganha 10% e
as demais cores e tamanhos do mesmo código continuam a preço cheio — sem tocar em preço,
estoque ou estrutura fiscal (EF §3.5 e §4).

---

## Rastreabilidade contra a Especificação Funcional

Conferi o plano regra a regra contra a EF rev. 1 (08/09/2026, Ozéias Tavares). **Nada do que
ela pede ficou de fora, e nada do que ela exclui entrou.**

| EF | O que exige | Onde no plano |
|---|---|---|
| §2, passo 4 | *"Quando aplicável, seleciona as grades específicas"* | **"quando aplicável" é a própria flag `P14GRADE`** — item com grade e item sem grade convivem na mesma campanha (F4 §3.1) |
| §2, passo 5 | disponibilizar ao VAR *"conforme o processo já utilizado"* | `OPERACAOLOG` + triggers — D2/D3, não mexemos na arquitetura |
| §2, passos 6-9 | VAR identifica a grade, verifica campanha ativa, aplica ou não | matcher do F5 |
| §3.1 | cadastro por produto completo **mantido** | `P14GRADE = 0`; `PRO0141` intacta |
| §3.2 | cor · tamanho · cor + tamanho | `NULL` nas duas colunas dá exatamente as 3 combinações |
| §3.3 | código principal + cor + tamanho; sem mexer em fiscal/estoque | decomposição do barcode; nada escrito em `PRE0021`/`ITE003` |
| §3.4 | validar **Produto + Cor + Tamanho**; grade não cadastrada ⇒ **nenhum desconto daquela campanha** | `alvoQueCasa` + o *fail-closed* do `temGrade()` |
| §3.5 | não altera o preço cadastrado | o desconto nasce e morre em `ORC002.ORCVALDSC` |
| §3.6 | aproveitar o motor, não recriar cálculo | só o predicado de casamento muda; rateio, tipos e `ORC014` intocados |
| §3.7 | *"estrutura/tabela filha vinculada à campanha"*, desenho a cargo do desenvolvimento | `VAR.PRO0144`, filha do item — que é filho da campanha |
| §3.8 | seleção de lojas não é obrigatória | herda `P14LOJCOD` do cabeçalho, custo zero |
| §4 | fora: remarcação, fiscal, estoque, Logix, hierarquia, mecânicas novas | nada disso é tocado |
| §6 | Portal: cadastrar com grades e relacionar cor/tamanho · VAR: identificar, consultar, aplicar só quando elegível | F2/F3/F4 e F5 |
| §8 | *"a aplicação depende da correta identificação da grade no VAR"* | é o que a validação contra `DOC002` ataca antes de salvar |
| §9 | risco de **cadastro incorreto de grade** | validação com bloqueio e aviso (§2.2) |
| §9 | risco de **volume de parametrizações** | o curinga `NULL`: "toda a cor amarela" grava **1 linha**, não N |
| §9 | *"a nova regra não pode interferir nas campanhas existentes"* | `P14GRADE = 0` em 1.628.562 linhas + **os testes de paridade da Onda 1B** |

**Duas coisas no plano vão além do que a EF pede** — de propósito, e vale saber:

1. **A validação "esta grade já foi vendida?"** A EF não pede. Ela existe para atacar o risco que
   a própria EF §9 registra (*"cadastro incorreto de uma grade"*) e a Restrição única da TAP.
2. **Os selects mostrando o histórico do item.** Idem — é a *"visão para facilitar o cadastro
   desses códigos"* que a TAP pedia e a EF não menciona.

Se o escopo precisar encolher, é por aí que se corta — e o custo é o comprador digitar no escuro.

## A ideia central

`PRO0141` ganha `P14GRADE` (0/1). Com `0`, tudo funciona como hoje. Com `1`, aquela linha
**deixa de casar sozinha** no motor do PDV e passa a exigir uma linha da tabela nova `PRO0144`
casando por cor/tamanho.

A regra no Java é o **OR das duas fontes**, e é o que torna a feature *fail-closed*:

```java
private boolean temGrade() {
    return (p14grade != null && p14grade == 1) || !grades.isEmpty();
}
```

Isso importa porque **a `PRO0144` pode não ter chegado a uma loja** (DDL fora de ordem,
replicação atrasada). Se a regra fosse "sem grades ⇒ casa o item inteiro", uma campanha restrita
a uma cor aplicaria em **todas** as cores naquela loja — over-discount, com efeito fiscal, sem
erro e sem log. Com o OR, as duas direções de dessincronia falham para o lado conservador:
flag=1 com lista vazia não aplica desconto nenhum; flag perdida com grades presentes, as grades
mandam. Nenhuma gera desconto a mais.

---

## F1 — Oracle · ✅ **APLICADO EM HOMOLOGAÇÃO EM 09/09/2026 14:18**

> **As triggers de replicação (`KAFKA_PRO0144`, `TG_PRO0144`) não são nossas** — quem cria é
> outro time. Ficam registradas como dependência externa (D2), fora deste escopo.

### 1.1 A coluna nova vai na `PRO0141` — a tabela de itens

| | O que guarda | PK | Volume |
|---|---|---|---|
| `VAR.PRO014` | cabeçalho: vigência, tipo, percentual, leve/pague, loja | `(P14LOJCOD, P14PROCOD)` | 2.808 |
| `VAR.PRO0141` | **uma linha por item × loja** | `(P14LOJCOD, P14PROCOD, P14ITECOD)` — constraint `SYS_C00112510171` | **1.628.562** |

A `PRO0141` tem **7 colunas**, não 4 como a constante do código sugere: `P14LOJCOD`,
`P14PROCOD`, `P14ITECOD`, `P14ATIV`, `LAST_UPDATED`, `CREATED_AT` e agora `P14GRADE`. As duas de
timestamp já existiam e são de replicação.

O mapeamento está no próprio código: `campaign-types.constant.ts:64` (`CAMPAIGN_TABLES`) e
`:74` (`CAMPAIGN_ITEM_TABLES`).

A flag é *"aquele **item** foi criado com grade específica"* — logo, `PRO0141`. Na `PRO014` ela
significaria "esta campanha tem alguma grade", e quebraria o caso normal: uma campanha com 500
itens em que só 3 têm grade e 497 valem para o produto completo.

```sql
ALTER TABLE VAR.PRO0141 ADD (P14GRADE NUMBER(1,0) DEFAULT 0 NOT NULL);
ALTER TABLE VAR.PRO0141 ADD CONSTRAINT CK_PRO0141_GRADE CHECK (P14GRADE IN (0,1));
```

Com `DEFAULT` + `NOT NULL`, o Oracle 11gR2+ resolve por metadados: **não reescreve as 1.607.486
linhas**. Roda na central **e** no Oracle de cada loja (200+).

**Nada quebrou — conferido no banco depois de aplicado (`172.16.10.2/teste`, Oracle 19c):**

| Verificação | Resultado |
|---|---|
| Objetos tocados hoje | só `PRO0141`, `PRO0144`, `UX_PRO0144`, `IX_PRO0144_ITE` — **os 4 VALID** |
| `P14GRADE` | `NUMBER(1,0) NOT NULL DEFAULT 0` · **1.628.562 linhas, todas em 0** |
| Triggers da `PRO0141` | `TG_PRO0141` e `KAFKA_PRO0141` **VALID e ENABLED**, DDL intacto de 12/03 |
| `LOGIX.V_PROMO_VAR_ITEM` (view que lê a `PRO0141`) | **VALID**, e usa colunas explícitas — `select 3 Base, p14lojcod, p14procod, To_Char(p14itecod) from var.pro0141`. Sem `SELECT *` |
| `LOGIX.TIP_DESC_VAR` (função que lê `PRO014` + `PRO0141`) | **INVALID — mas desde março.** Não cita `SELECT *` nem `P14GRADE`, e `ALL_ERRORS` está vazio |
| 35 objetos `INVALID` no schema `VAR` | 14 de **12/03/2026** e 21 de **16/03/2026**. Nenhum de hoje |
| `UX_PRO0144` (índice funcional) | **VALID**, `FUNCIDX_STATUS = ENABLED` |

E as queries reais do código, executadas contra a tabela alterada:

| Query | Resultado |
|---|---|
| Listagem paginada da API (`pro014-items.repository.ts:435`) | ✅ 89 ms |
| `columnList(PRO014_ITEM_COLUMNS)` do sync (`:465`) | ✅ 126 ms |
| Checksum `ORA_HASH` do sync (`:273`) | ✅ 45 ms |
| `SQL_ITEM` atual do Java (`Pro014DaoImpl:34`) | ✅ 904 ms |
| **`SQL_ITEM` com `i.p14grade`** (proposto) | ✅ 912 ms — **mesma performance** |
| **`SQL_GRADE`** com os dois JOIN (proposto) | ✅ 51 ms (tabela vazia) |

**Ainda falta conferir o `10.150.10.126`.** O driver `node-oracledb` em thin mode não conecta lá
(versão do servidor anterior à 12.1, exige Instant Client). As queries de conferência estão no
documento de handoff — rodar no SQL Developer.

Restam dois consumidores fora dos nossos repos: o processo legado do `OPERACAOLOG`
(`matualiz.exe`/`mcaseli`) e o motor **Genexus** do `/api/descontoSinteticoELista`. Se algum
fizer `SELECT *` na `PRO0141`, a coluna nova aparece no resultado.

### 1.2 A tabela `VAR.PRO0144`

```sql
CREATE TABLE VAR.PRO0144 (
  P14LOJCOD     NUMBER(3,0)   NOT NULL,
  P14PROCOD     NUMBER(10,0)  NOT NULL,
  P14ITECOD     NUMBER(10,0)  NOT NULL,
  P144COR       VARCHAR2(3),                -- NULL = todas as cores
  P144TAM       VARCHAR2(3),                -- NULL = todos os tamanhos
  CREATED_AT    TIMESTAMP(6)  DEFAULT SYSTIMESTAMP,
  LAST_UPDATED  TIMESTAMP(6),
  CONSTRAINT FK_PRO0144_PRO0141 FOREIGN KEY (P14LOJCOD, P14PROCOD, P14ITECOD)
      REFERENCES VAR.PRO0141 (P14LOJCOD, P14PROCOD, P14ITECOD),
  CONSTRAINT CK_PRO0144_COR  CHECK (P144COR IS NULL OR REGEXP_LIKE(P144COR, '^[A-Z0-9]{3}$')),
  CONSTRAINT CK_PRO0144_TAM  CHECK (P144TAM IS NULL OR REGEXP_LIKE(P144TAM, '^[A-Z0-9]{3}$')),
  CONSTRAINT CK_PRO0144_ALVO CHECK (P144COR IS NOT NULL OR P144TAM IS NOT NULL)
);

CREATE UNIQUE INDEX VAR.UX_PRO0144 ON VAR.PRO0144
  (P14LOJCOD, P14PROCOD, P14ITECOD, NVL(P144COR, '-'), NVL(P144TAM, '-'));

CREATE INDEX VAR.IX_PRO0144_ITE ON VAR.PRO0144 (P14ITECOD, P144COR, P144TAM);
```

**Sete colunas, e cinco delas são a chave.** O que foi cortado do rascunho de ontem, e por quê:

| Coluna cortada | Por quê |
|---|---|
| `P144ATIV` | **Quem decide participação é `PRO0141.P14ATIV`.** Não existe caso de uso de "desativar a cor amarela mantendo a azul" — remover é remover. Item inativo já não aplica nenhuma grade |
| `P144NIVEL` | 100% derivável de cor/tamanho. Tanto a API quanto o `especificidade()` do Java calculam em memória; materializar seria um segundo lugar para a mesma verdade divergir |
| `P144USRCAD` / `DTCAD` / `USRATU` / `DTATU` | A própria `PRO0141` **não tem** auditoria em coluna — são só 4 colunas. E o rastro completo (antes/depois, e-mail, IP) já vive no Postgres via `AuditService` |

Fica só um trade-off, e é pequeno: sem `P144ATIV`, remover uma grade é `DELETE` de verdade, e o
módulo hoje só faz soft-delete (`pro014-items.repository.ts:284-369`). Funciona igual — a
`TG_PRO0144` loga o delete como tipo `3` no `OPERACAOLOG`, que é exatamente como o replicador
aprende a apagar na loja.

**`CREATED_AT`/`LAST_UPDATED` eu manteria.** Todas as tabelas replicadas do `VAR` têm esse par
(`ITE001`, `PRO012`, `PRO0121`, `PRO013`, `PRO014`, `PRO0141`, `PRO017`, `PRO0171`, `PRO01711`),
e as duas que não têm — `PRO0142` e `PRO0143` — não são replicadas. São 26 triggers `KAFKA_*`
ativas alimentando isso. **Se o DBA confirmar que o CDC não precisa, saem também e ficam as 5.**

**`NULL` em vez de `'***'`.** O único motivo do asterisco era que o Oracle proíbe `NULL` em
coluna de PK. Trocando a PK natural por um **unique index funcional** com `NVL`, o `NULL` passa a
funcionar — e é semanticamente o certo: "não informado" é literalmente o que `NULL` significa. De
quebra, `'***'` era um valor mágico, que a R3 do `CLAUDE.md` proíbe.

O que muda por causa disso:

- A proteção contra alvo duplicado sai da PK e vai para o `UX_PRO0144`. O `'-'` do `NVL` é
  seguro porque não casa o regex do `CHECK`, então nunca colide com código real.
- `CK_PRO0144_ALVO` substitui o antigo check de nível: os dois `NULL` seriam "produto inteiro",
  que é a `PRO0141` com `P14GRADE = 0` — proibido aqui.
- A `TG_PRO0144` monta a chave do log com `NVL(:NEW.P144COR, '*')`, para o campo não sair vazio
  na concatenação. **O asterisco passa a existir só na chave de replicação, não nos dados.**
- No Java, `casa()` fica `if (alvo == null) return true;` — mais limpo que comparar com string.
- No fio da API, `null` já era o que estava proposto; agora não há mais tradução nenhuma.

**`VARCHAR2(3)`, não `CHAR(3)`.** `XTAM001.XTAMCOD` é `CHAR(4)` e vem com padding;
`XCOR001.XCORCOD` é `VARCHAR2(4)`; `DOC002.DOCGRAHOR`/`DOCGRAVER` são `CHAR(10)`. A query do
Fábio faz `TRIM(xtamcod) = trim(docgraver)` exatamente por isso. Gravar `'042 '` em `CHAR(3)`
produz um alvo que **nunca casa** no PDV, sem erro nenhum. `VARCHAR2` + normalização (`TRIM` +
`UPPER`) num ponto único da escrita elimina a classe inteira de bug.

**Os `CHECK` de formato fecham o branco**, e aqui eles são obrigatórios: `DOC002` tem venda com
cor/tamanho em branco (`get-sold-items.ts:34-35` faz `NVL(TRIM(...), ' ')` por isso), e sem o
regex uma cor em branco viraria `NULL` — ou seja, **"todas as cores", silenciosamente**. `' '`
não casa `^[A-Z0-9]{3}$`, então o banco recusa.

**A FK aponta para `PRO0141`, não para `PRO014`** — a grade é filha do *item*.

> 🚩 **A FK tem um efeito colateral que precisa ser fechado antes de codar.**
> `insertItemsBatchFromIte001` (`pro014-items.repository.ts:230-260`) é o caminho **default**,
> não o excepcional: `insertItemsBatch:158` desvia para ele sempre que todos os códigos são
> numéricos, e `isNumericItemCode` (`:262-264`) é `/^\d+$/` — ITECOD de 6 dígitos sempre passa.
> Ele faz `INSERT … SELECT … FROM VAR.ITE001 WHERE ITECOD IN (…)`: item que não existe na
> `ITE001` **não vira linha e não gera erro**. Hoje é uma perda tolerada; com a FK, o INSERT da
> grade daquele item estoura `ORA-02291` e **derruba a transação da campanha inteira**.
>
> Mitigação: garantir que todo caminho de entrada valide contra a `ITE001` antes. O `create` já
> faz (`pro014.service.ts:218-230`, 400 quando a contagem diverge); **conferir se o `addItems`
> (`pro014-items.repository.ts:90-146`) também faz** — se não, adicionar. Se o DBA preferir não
> ter a FK, cai para validação em aplicação e a garantia vira teste.

**Nada de FK para `XCOR001`/`XTAM001`:** 202 cores e 354 tamanhos já vendidos não constam nesses
catálogos.

### 1.3 Uma linha por alvo

Nunca N linhas materializadas. O nível não é uma coluna — é a leitura de onde está o `NULL`:

| Intenção | `P144COR` | `P144TAM` | linhas |
|---|---|---|---|
| Camiseta amarela tamanho M | `437` | `042` | 1 |
| A amarela, todos os tamanhos | `437` | `NULL` | **1**, não N |
| O tamanho M, todas as cores | `NULL` | `042` | **1**, não N |
| Produto completo | *fica na `PRO0141`, com `P14GRADE = 0`* | — | 1 |

Sem o curinga, um tamanho que ainda não vendeu ficaria fora da promoção — justamente o item de
baixo giro que o projeto quer atacar.

**Subsunção:** `(437, NULL)` e `(437, 042)` podem coexistir, e a segunda é redundante. A API
rejeita o alvo subsumido, senão a contagem de grades que o usuário vê no card mente.

### 1.4 As triggers — fora do nosso escopo, mas precisam existir

Não somos nós que criamos. O que precisa ser pedido a quem cria, com o motivo:

| Trigger | Para quê |
|---|---|
| `KAFKA_PRO0144` · `BEFORE UPDATE` | carimbar `LAST_UPDATED`. Molde exato da `KAFKA_PRO0141` |
| `TG_PRO0144` · `AFTER INSERT/UPDATE/DELETE` | gravar em `VAR.OPERACAOLOG` com `OPERACAOLOGTAB = 'PRO0144'` e chave de **5 campos**: `lojcod;procod;itecod;NVL(cor,'*');NVL(tam,'*')` |

O `NVL(...,'*')` existe só na chave do log: sem ele, um alvo "todas as cores" vira chave com
campo vazio (`1;8801;993753;;042`) e fica ambíguo para quem consome.

**Por que isso não pode ser esquecido:** `PRO017` tem `KAFKA_*`, não tem `TG_*`, e tem **zero
linhas** no `OPERACAOLOG`. A tabela existe, o cadastro funciona, e nada chega à loja — sem erro
nenhum. É o mesmo destino da `PRO0144` sem a `TG_*`.

**E a `PRO0141` também precisa de atenção**, mesmo já tendo suas duas triggers: elas logam só a
**chave**, não os valores. Quem consome o log vai buscar a linha na central — se usar lista fixa
de colunas, não traz o `P14GRADE`.

---

## F2/F3 — API (`ConciliaçãoCaixaAPI/src/modules/campaign/`)

### 2.1 Duas famílias de query, não uma

Meu desenho inicial usava uma query só. Está errado para o bloqueio: o bloqueio pergunta sobre a
**projeção** ("já vendeu na cor X com qualquer tamanho?"), e responder isso trafegando o produto
cartesiano de N itens é desperdício.

**Para a UI** (um item por vez, ao abrir o modal):

```sql
SELECT NVL(TRIM(d.DOCGRAHOR), ' ') AS "COR",
       NVL(TRIM(d.DOCGRAVER), ' ') AS "TAM",
       COUNT(*)                    AS "VENDAS",
       MAX(d.DOCDTOP1)             AS "ULTIMA"
  FROM VAR.DOC002 d
 WHERE d.DOCITECOD = :1
   AND NVL(d.DOCINDEXC1, 0) <> :2
 GROUP BY NVL(TRIM(d.DOCGRAHOR), ' '), NVL(TRIM(d.DOCGRAVER), ' ')
```

**Para o bloqueio** (N itens de uma vez, uma query por eixo):

```sql
SELECT d.DOCITECOD AS "ITEM", NVL(TRIM(d.DOCGRAHOR), ' ') AS "COR", COUNT(*) AS "VENDAS"
  FROM VAR.DOC002 d
 WHERE d.DOCITECOD IN (:1, :2, :3)
   AND NVL(d.DOCINDEXC1, 0) <> :4
 GROUP BY d.DOCITECOD, NVL(TRIM(d.DOCGRAHOR), ' ')
```

> 🚩 **Bind numérico, explicitamente.** `campaign-conflict-validator.service.ts:118` interpola
> itemCodes **com aspas** contra `P14ITECOD`, enquanto `pro014-items.repository.ts:185` faz
> `Number(row.itemCode)` com `bindDefs: { itemCode: { type: oracledb.NUMBER } }`. Se
> `DOC002.DOCITECOD` for `NUMBER` e bindarmos string, o Oracle converte implicitamente e
> **descarta o índice `IDOC0021`** — os 109-117 ms medidos viram full scan em 1,28 M linhas.

O `NVL(…, 0) <> 9` é essencial: em Oracle `NULL <> 9` é UNKNOWN e excluiria silenciosamente toda
linha com o flag nulo. Reusar `EXCLUDED_RECORD_FLAG` de
`src/modules/sold-items/constants/sold-items.constants.ts:3` (R4 — não redigitar o `9`).

### 2.2 O algoritmo da validação

```
vendas[] do item

vendas vazio         →  AVISO  ITEM_NEVER_SOLD, nunca bloqueio
                        (produto novo: ausência de histórico não é evidência de grade errada)

nível 1 (cor C + tamanho T)
  C ∉ cores do item     → BLOQUEIA  COLOR_NEVER_SOLD
  T ∉ tamanhos do item  → BLOQUEIA  SIZE_NEVER_SOLD
  (C,T) ∉ vendas        → AVISA     COMBINATION_NEVER_SOLD
  senão                 → OK

nível 2 (só cor C)      C ∉ cores do item     → BLOQUEIA · senão OK
nível 3 (só tamanho T)  T ∉ tamanhos do item  → BLOQUEIA · senão OK
```

> **O caso que quase escapou:** produto novo em campanha de lançamento tem zero linhas em
> `DOC002`. Bloquear ali inviabilizaria o cadastro sem nenhum ganho.

A validação roda **no servidor**, sempre. O front replica em memória só para feedback instantâneo
— regra permanente 5 do front: a API é a autoridade.

> 🚩 **A validação tem que ser síncrona, ANTES do enqueue.** `pro014.service.ts:135-158` enfileira
> a criação quando `items × lojas >= 100` — que é quase sempre — e
> `create-pro014-form.tsx:305-312` fecha o modal e devolve o controle ao usuário na hora. Se a
> validação de grade viver dentro do job (`campaign-creation.processor.ts:85-136`), o usuário
> descobre o bloqueio por notificação, horas depois.

### 2.3 Endpoints novos

Todos declarados **antes** do `@Get(":id")` de `campaign.controller.ts:299`, como já acontece com
`@Get("items/search")` (`:198`) — senão o `ParseIntPipe` devolve 400.

```
GET  /campaigns/grade/catalog
     → { colors: [{ code, description }], sizes: [{ code, description }] }
       XCOR001 + XTAM001 inteiros (375 + 122 ≈ 25 KB). Cache 12 h no RTK Query

GET  /campaigns/grade/items/:itemCode/sold
     → { itemCode, hasHistory, totalSales,
         colors:       [{ code, description, sales, lastSaleDate }],
         sizes:        [{ code, description, sales, lastSaleDate }],
         combinations: [{ color, size, sales, lastSaleDate }] }

POST /campaigns/grade/validate
     body { targets: [{ itemCode, color: string|null, size: string|null }] }
     → { blocked:  [{ itemCode, color, size, reason }],
         warnings: [{ itemCode, color, size, sales, reason }] }
```

`description` vem do cruzamento **na resposta**, com o catálogo já em memória — nunca por `JOIN`
no SQL. É por isso que a query de referência do Fábio não enxerga as 202 cores e 354 tamanhos
órfãos: o `INNER JOIN` com os catálogos descarta exatamente esses casos, que são os que o
comprador mais vai procurar. `null` é o curinga no fio **e no banco** — não há tradução em
lugar nenhum.

### 2.4 Os DTOs existentes **não mudam de tipo**

`items: string[]` e `itemCodes: string[]` ficam como estão. A grade entra num campo **paralelo**:

```ts
gradeTargets?: Array<{ itemCode: string; color: string | null; size: string | null }>
```

Assim o import de Excel, o `validateSkus`, o `@ArrayMinSize(2)`, o `@NoDuplicateItems` e a
pré-validação de conflito em chunks continuam intactos, e o DTO viaja de graça na serialização
do job em Redis. `P14GRADE` é **derivada** de `gradeTargets` no INSERT — nunca digitada.

### 2.5 Arquivos a tocar

| Arquivo | Mudança |
|---|---|
| `constants/campaign-columns.constant.ts:100-104` | `P14GRADE` em `PRO014_ITEM_COLUMNS` |
| `pro014-items.repository.ts:170`, `:206`, `:245` | os 3 caminhos de INSERT em `PRO0141` |
| `pro014.repository.ts:227-285` | a FASE 3 monta `pendingRows` do cartesiano `lojas × itens`; a linha ganha `hasGrade`, e entra uma **FASE 4** com `lojas × gradeTargets` para a `PRO0144` — antes do `commitTransaction` de `:288` |
| `pro014.repository.ts:339-382` (`addStores`) | **o mais fácil de esquecer:** ao adicionar loja, copia header e itens por `INSERT…SELECT`; tem que copiar `PRO0144` também, senão a loja nova aplica no produto inteiro |
| `pro014-items.repository.ts:374-471` | a listagem paginada devolve `P14GRADE` e as grades — **segunda query batched pelos itens da página, não `LISTAGG`** (limite de 4000 caracteres) |
| `pro014-sync.repository.ts:729-745` | ver §2.6 |
| `src/workers/worker.module.ts:18,91` | **registrar o repositório novo no módulo do worker** — hoje só `CampaignComparisonWorkerModule` está lá; sem isso o job de criação morre no bootstrap com `Nest can't resolve dependencies`, e **isso não aparece rodando só a API** |
| `src/provider/campaign-grade/queries/` (novo) | SQL em const nomeada de módulo, no molde de `provider/sold-items/queries/get-sold-items.ts` — é o padrão que a R3 manda |
| `docs/adr/` | ADR obrigatório. **Não existe grupo de campanhas** — combinar se cria `groups/campaign/` ou entra em `infrastructure` |

> 🚩 **`PRO014_ITEM_COLUMNS` já está errada hoje** (falta `P14LOJCOD`), e `addStores`
> (`pro014.repository.ts:366-370`) **não usa a const** — escreve a lista literal com o
> `${storeCode}` em posição fixa no `SELECT`. Adicionar `P14GRADE` à const e trocar o literal por
> ela sem reordenar o `SELECT` faz o código da loja entrar na coluna errada. **Mexer numa coisa
> só:** ou o literal em todos os INSERTs, ou a const em todos. Nunca metade.

**Reusar, não reinventar:** `BaseOracle` + `@Inject("VarDataSource")` como em
`sold-items.repository.ts:9-12`; `handleError` de `src/utils/treat.exceptions.ts` (R13);
`MessagesHelper` (R7); o `QueryRunner` já montado em `pro014.repository.ts:142-314`.

> Sobre o `DynamicOracleService`: o `CLAUDE.md` proíbe `DataSource` TypeORM apontando para
> Oracle, mas todo o módulo campaign e o `sold-items` leem o VAR central por `VarDataSource`.
> Seguir o vizinho e **registrar a divergência no ADR** — é exceção legada consolidada.

### 2.6 A propagação da API — **fora do escopo**

Os processors Bull estão com o corpo comentado (`campaign-propagation.processor.ts:31-40`,
`campaign-edit-propagation.processor.ts:33-36`): os jobs são enfileirados e ninguém consome.
Hoje **nada do PRO014 chega às lojas pela API** — quem replica é o `OPERACAOLOG`. Não mexemos
nesse código; ele fica como está.

### 2.7 Conflito entre campanhas: **passa a considerar a grade**

Hoje `campaign-conflict-validator.service.ts:126-149` reprova por `(SKU, campanha, loja)`, sem
noção de cor/tamanho — ou seja, *"20% na amarela"* e *"30% na preta"* do mesmo código se
barrariam mutuamente, o que contraria o próprio objetivo do projeto. Entra no escopo.

Quatro pontos, e nenhum deles é trivial:

| Onde | Mudança |
|---|---|
| `campaign-conflict-validator.service.ts:126-149` | a query self-PRO014 passa a trazer `P144COR`/`P144TAM` por `LEFT JOIN` na `PRO0144`, e a comparação vira **sobreposição de alvos**, não igualdade de item |
| `:155-166` | o `Map` de agrupamento é chaveado só por `itemCode` — precisa da grade na chave |
| `:574` | o dedupe `${type}-${code}-${storeCode}-${listNumber}` ganha `cor|tam` |
| `step-four.tsx:399-416` + `utils/conflict-resolution.ts` | o botão "Remover da anterior" passa a remover **uma grade** da campanha anterior — e hoje `pro014-items.repository.ts:284-369` só sabe soft-delete de `PRO0141`, não existe remoção de grade |

**A regra de sobreposição** (dois alvos colidem se existe algum SKU que ambos alcançam):

```
colidem(A, B) = eixoColide(A.cor, B.cor) && eixoColide(A.tam, B.tam)
eixoColide(x, y) = x IS NULL || y IS NULL || x = y
```

Assim `(437, NULL)` × `(435, NULL)` não colidem; `(437, NULL)` × `(NULL, 042)` **colidem** (a
amarela M cai nas duas); e item sem grade colide com tudo daquele código, que é o comportamento
de hoje preservado.

> ⚠️ **PRO013 e PRO017 continuam colidindo por item inteiro.** O `PRO013` mira
> departamento/grupo e nem tem tabela de itens; o `PRO017` tem estrutura própria. Só o
> self-PRO014 ganha granularidade de grade — e isso precisa estar explícito na mensagem que o
> usuário vê, senão ele não entende por que às vezes barra e às vezes não.

Custo: **~3 dias**, num validador de 675 linhas sem cobertura de teste. É o item de maior risco
de regressão do lado da API, e o que mais pede teste antes de código.

---

## F4 — Front (`ConciliaçãoCaixaFront/src/pages/business-planning/campaigns/`)

### 3.1 Botão por item, não checkbox

O card pede "checkbox ao gravar". Um checkbox por item numa lista que aceita 15.000 SKUs via
Excel é a UX errada — e o estado "tem grade" é **derivável de "tem alvos"**. Traduzo para um
botão por item que abre o modal, com badge de contagem; a flag sai disso. O efeito para o
usuário é o mesmo, com menos clique e sem estado inconsistente possível.

Dois hosts, os dois em página, nenhum dentro de outro `Dialog`:

1. **Wizard, step 4** — `steps-pro014/step-four.tsx`, na barra de ações da linha (`:398-428`),
   ao lado do `X`. `key={item.sku}` (`:363`) continua válido porque as grades ficam **aninhadas**
   no item — não viram linhas duplicadas, o que é obrigatório dado o `@NoDuplicateItems`.
   Badge de contagem ao lado do SKU (`:375-380`), onde já aparecem os badges de conflito.
2. **Tela de produtos** — `products/index.tsx` (rota `/:type/:code/produtos`), coluna **Grade** no
   `<thead>` (`:344-358`) e botão no `<tbody>` (`:359-403`). Chave da linha (`:365`) inalterada.

Dentro de `add-item-modal.tsx` (que **é** um `Dialog`), a variante aninhada usa o
`DialogPrimitive` com `z-[60]` de `create/components/shared/excel-upload-preview.tsx:52-76` ou
`src/components/ui/sub-modal.tsx`. Um componente só,
`campaigns/components/grade-target-modal.tsx`, com o wrapper escolhido por `Record` (R1 proíbe
ternário para escolher o que renderizar).

`pro014-items-modal.tsx` (textarea em massa) e o **import de Excel** ficam fora da v1 — o
template `/templates/sku-import-template.xlsx` só tem a coluna SKU. Declarar isso explicitamente,
senão vira expectativa.

### 3.2 O modal

**Padrão B** — `Dialog` shadcn local controlado por prop, no molde de
`add-item-modal.tsx:177-321`. O padrão A (singleton Redux) está fora: dois hosts com estados-pai
diferentes forçariam uma slice global para o que é rascunho de formulário.

```
┌─ Grade específica — 993753 CAMISETA BÁSICA ──────────────┐
│  Cor       [ AMARELO (437) · 128 vendas · últ. 14/08 ▾ ]  │
│  Tamanho   [ M (042) · 12 vendas · últ. 02/07        ▾ ]  │
│            ☐ Todas as cores    ☐ Todos os tamanhos       │
│                                                          │
│  ⚠ Vende na cor AMARELO, mas nunca no tamanho M.         │
│    Confirma mesmo assim?                                 │
│                                                          │
│  Grades já adicionadas:  437/042  ·  437/todos           │
│                          [ Cancelar ]  [ Adicionar ]     │
└──────────────────────────────────────────────────────────┘
```

- Cada select tem dois grupos: **"Deste produto"** no topo (com nº de vendas e última venda) e
  **"Todo o catálogo"** abaixo. Base: `src/components/ui/select.tsx`, o mesmo de
  `step-three.tsx:169-196`, que já injeta cabeçalhos de grupo.
- Cor presente no histórico e ausente do catálogo aparece com **"(fora do catálogo)"** — são os
  202/354 órfãos, e são justamente os que o comprador procura.
- "Todas as cores" define nível 3, "Todos os tamanhos" nível 2. Marcar os dois é inválido (seria
  o produto completo, que é `P14GRADE = 0`).
- **Bloqueio:** inline `text-sm text-destructive` + `AlertCircle` e confirmar desabilitado —
  markup de `step-four.tsx:222-227`. **Aviso:** bloco `bg-destructive/10 border-destructive/20`
  de `add-item-modal.tsx:275-295`, confirmar habilitado. Toast só para falha de rede.
- **React Hook Form + zod** (R5 do front). O wizard em volta continua com `useState` — o modal é
  código novo e a regra vale para o arquivo tocado.
- Totalmente controlado: `{ isOpen, itemCode, itemName, initialTargets, variant, onConfirm, onClose }`.
  Sem Redux, sem `useEffect` de fetch (R7).

### 3.3 O que muda nos dados

- `GradeTarget = { color: string | null; size: string | null }` — `null` é o curinga no fio.
  Tipo do item: `{ sku, name?, grades? }`. Hoje está declarado em **três** lugares
  (`step-four.tsx:17-19`, `step-five.tsx:44`, `create-pro014-form.tsx:109`) — centralizar em
  `campaigns/types/grade.ts`. `useExcelImport(data.items)` continua compilando (campo opcional).
- Payload: `items` continua `.map(i => i.sku)` em `create-pro014-form.tsx:295`; `gradeTargets`
  entra ao lado, achatado. Idem `addItems` (`:347-354`).
- `src/services/campaign.ts`: 3 endpoints novos, tags no padrão granular existente. Catálogo com
  `keepUnusedDataFor: 43200`, como `src/services/store/select-options.ts`.
- Mensagens em `campaigns/utils/messages.ts`; tradução de `reason` em
  `campaigns/utils/error-messages.ts`.

**Spec Playwright obrigatória** (regra permanente 7), `e2e/tests/business-planning/`. Usar
`<Label htmlFor>` acessível — é como `campaigns-create.spec.ts` navega.

---

## F5 — Motor do PDV (`Var3.VendaMercantil/.../desconto/`)

### 5.1 A decisão que mudou: **aninhar, não anexar linhas**

Minha proposta inicial era colocar as linhas de `PRO0144` na mesma
`ArrayList<PromocaoPro014>`. **Isso quebra em quatro lugares, em silêncio:**

| Ponto | O que faz hoje | O que quebra com linhas extras |
|---|---|---|
| `Ppro014cCalculator.java:204-213` | `return` no primeiro (loja, procod, itecod) | pode retornar a linha de grade; `:109` lê `getP14leve()` → `wleve = 0` → muda o desvio de `:111` |
| `Ppro014LCalculator.java:224-231` | `findFirst()` por (itecod, lojcod, procod) | idem: `wtipoprom = 0` → cai no `else` de `:208` e soma zero |
| `Ppro014cCalculator.java:194-202` | monta candidatos por itecod | lista cresce, o `break` de `:56` pega outra linha |
| `Ppro014ACalculator.java:211-215` | bug do Genexus reproduzido | a cardinalidade da lista deixa de ser invariante testável |

Nenhum lança exceção. Todos mudam o valor do desconto.

O que **não** quebra: todos os filtros de header são `p.getP14itecod() == null`
(`Ppro014L:95`, `Ppro014c:24`, `Ppro014A:222/230/244`, `Ppro014B:18`). **Aninhar a grade dentro
da linha de `PRO0141`** mantém a cardinalidade intacta e nenhum desses filtros muda.

### 5.2 `GradePro014.java` (novo, em `desconto/domain/`)

```java
@Value
@Builder
public class GradePro014 {

    public static final GradePro014 SEM_RESTRICAO = GradePro014.builder().build();

    String cor;
    String tam;

    public boolean aceita(String corItem, String tamItem) {
        return casa(cor, corItem) && casa(tam, tamItem);
    }

    public int especificidade() {
        if (cor != null && tam != null) return NIVEL_COR_TAM;
        if (cor != null) return NIVEL_COR;
        if (tam != null) return NIVEL_TAM;
        return NIVEL_PRODUTO;
    }

    private static boolean casa(String alvo, String valor) {
        if (alvo == null) return true;
        return normalizar(alvo).equals(normalizar(valor));
    }

    private static String normalizar(String v) {
        return v == null ? "" : v.trim().toUpperCase();
    }
}
```

`normalizar` resolve de uma vez o `CHAR(10)` padded do `ORC002`, o null e o branco. `alvo == null`
é o curinga, e ele aceita item com cor em branco de propósito: "todas as cores" inclui "sem cor".
`SEM_RESTRICAO` só existe em memória, para representar "casou sem grade" — nunca é gravado, e o
`CK_PRO0144_ALVO` garante que uma linha assim não pode existir no banco.

### 5.3 `PromocaoPro014` — dois campos e dois métodos

```java
    Integer p14grade;
    @Singular("grade") List<GradePro014> grades;

    public boolean casaCom(ItemPreVenda item) {
        return alvoQueCasa(item).isPresent();
    }

    public Optional<GradePro014> alvoQueCasa(ItemPreVenda item) {
        if (p14itecod == null || item == null || p14itecod != item.getOrcitecod()) {
            return Optional.empty();
        }
        if (!temGrade()) return Optional.of(GradePro014.SEM_RESTRICAO);
        return grades.stream()
                .filter(g -> g.aceita(item.getOrcgrahor(), item.getOrcgraver()))
                .min(Comparator.comparingInt(GradePro014::especificidade));
    }

    private boolean temGrade() {
        return (p14grade != null && p14grade == 1) || !grades.isEmpty();
    }
```

**Sobre a precedência 1 → 2 → 3:** para *casar*, a semântica é OR — se qualquer alvo aceita, o
item entra, e a precedência é irrelevante para o booleano, porque o valor do desconto mora no
cabeçalho. A precedência existe em `alvoQueCasa`, que devolve o alvo **mais específico** entre os
que aceitaram. Hoje serve para log e `ResultadoMotor`; no dia em que pedirem "20% na cor e 30% no
SKU", é o ponto de extensão pronto — sem o `Optional`, seria reabrir os 10 pontos de novo.

### 5.4 `Pro014DaoImpl` — mapa lateral e fallback cacheado

O `SQL_GRADE` novo carrega as grades num `Map<ChaveItem, List<GradePro014>>`, e `mapear()` anexa
a lista só nas linhas de item (header nunca tem grade, por construção). O `SQL_ITEM` ganha
`i.p14grade`.

```java
private static final String SQL_GRADE =
        "SELECT g.p14lojcod, g.p14procod, g.p14itecod, g.p144cor, g.p144tam " +
        "FROM pro0144 g " +
        "JOIN pro0141 i ON i.p14lojcod = g.p14lojcod AND i.p14procod = g.p14procod " +
        "               AND i.p14itecod = g.p14itecod " +
        "JOIN pro014 h  ON h.p14lojcod = i.p14lojcod AND h.p14procod = i.p14procod " +
        "WHERE i.p14ativ = 1 AND h.p14dtinic <= ? AND h.p14dtterm >= ?";
```

O filtro de ativo é `i.p14ativ` — **quem decide participação é a `PRO0141`**, e por isso a
`PRO0144` não precisa de coluna própria de status.

**Detecção de layout com fallback**, uma vez por processo, no molde de
`pro014-sync.repository.ts:33,100-121`: se a loja ainda não tem a `PRO0144` (`ORA-00942`) ou a
coluna (`ORA-00904`), cacheia `gradeDisponivel = false`, loga `warn` e segue com mapa vazio.
Combinado com o *fail-closed* de `temGrade()`, campanha restrita a grade simplesmente **não
aplica** naquela loja, em vez de aplicar no produto inteiro. Isso elimina a dependência de ordem
entre DDL e publicação do JAR.

### 5.5 Os 10 pontos

| Arquivo | Linhas | Mudança |
|---|---|---|
| `Ppro014LCalculator` | `:213-222`, `:224-231` | assinaturas passam a receber `ItemPreVenda`; filtro vira `p.casaCom(item)` |
| `Ppro014cCalculator` | `:194-202`, `:204-213` | idem; é em `:194-202` que a linha gatilho de cor errada é descartada, antes do `seqConsumida[wseq]` de `:66` |
| `Ppro014cCalculator` | `:225-234`, `:236-245` | **atenção:** o predicado certo **não** é "mesma cor do gatilho" — para um alvo nível 2 (só cor), tamanhos P e M **devem** agrupar. As funções passam a receber a `PromocaoPro014` e filtram por `promo.casaCom(it)` |
| `Ppro014ACalculator` | `:236-240`, `:254-259`, `:261-266` | idem |
| `Ppro014BCalculator` | `:34` | o mais simples — bom primeiro spike |

> **Leve/Pague com grade: só as peças da grade contam para fechar o combo.** Numa campanha
> "leve 3 pague 2" restrita à cor amarela, 2 amarelas + 1 preta **não fecha** — a peça preta está
> fora da campanha, não apenas fora do desconto. É o que a EF sustenta em três lugares: §3.2
> fala em *"quais grades participarão da promoção"*; §3.4 diz que *"caso a grade não esteja
> cadastrada, **nenhum desconto referente àquela campanha** deverá ser aplicado"*; e a TAP §III
> justifica o projeto por *"preservar margem nas cores que não demandam intervenção"* — se a
> peça preta viabiliza o leve 3, ela está subsidiando a ação.
>
> Isso cai naturalmente do `promo.casaCom(it)` nos 4 pontos item×item: peça que não casa o alvo
> não entra na lista de participantes, logo não conta. **É exatamente por isso que o teste da
> mistura (§Verificação, item 8) é obrigatório** — se filtrarmos só o item gatilho e esquecermos
> o agrupamento, o combo fecha errado e passa em verde.

**Não tocar em `Ppro014ACalculator.java:211-215`** — é o bug do Genexus reproduzido de propósito
(`BUG_GENEXUS_PPRO014A_WINDPROM.md`). Com item na cor errada ele deixa de disparar porque não há
candidato, não porque foi corrigido; sem grade, reproduz igual. Precisa de teste explícito, senão
alguém "conserta" no futuro.

`ItemPreVenda` ganha `orcgrahor`/`orcgraver`; `ContextoPreVendaLoaderImpl.java:47-51` traz as
colunas e `:126-138` mapeia com o `trim()` de `:145-147`.
**Convenção contraintuitiva: HOR = cor, VER = tamanho** (`PreVendaItemDAOImpl.java:101-102`).

### 5.6 Sem flag nova — ver F6

> 🚩 **O fallback silencioso esconde exatamente o erro que vamos introduzir.**
> `DescontoSinteticoService.java:34-41` tem um `catch (Exception)` cobrindo o `calcular()`
> inteiro: se o DAO estourar, **toda a venda da loja cai no Genexus** e o E1 Java fica desligado
> de fato, visível só num `log.error`. Precisa de **contador/métrica**, não só log.

---

## F6 — Rollout: **a própria campanha é o controle**

Nada de `PARAMETROWS` nem `W04EST`. A `PRO014` já tem `P14LOJCOD` na PK: cadastrar a campanha de
grade **para uma loja só** já é o piloto, e é reversível pela tela. Não faz sentido construir uma
segunda camada de flag por loja para controlar algo que o próprio dado controla.

Isso corta trabalho real: o `ContextoPreVendaLoaderImpl` **não precisa** injetar o
`ParametroWSDAO` (hoje nenhum ponto do módulo `desconto/` lê `PARAMETROWS`), e some a decisão
§5.6 do plano de ontem.

Também não entra flag de código nova: a feature já nasce inerte por construção — sem linha na
`PRO0144` e com `P14GRADE = 0` em tudo, o comportamento é byte a byte o de hoje. O botão de
emergência que já existe (`features.desconto.desconto-sintetico-java`) continua desligando o
motor Java inteiro se precisar.

**A sequência:**

1. DDL aplicada nas lojas. Tabela vazia é inerte.
2. Campanha de teste **em uma loja**, nível 2 (uma cor), num produto de grade larga.
3. Conferir no banco da loja: `ORC002.ORCVALDSC` só na linha certa, `ORC014.ORC14ORI` =
   `"PRO014 - <procod>"`, Σ `ORC002.ORCVALDSC` = `ORC001.ORCTOTDSCO` (SEFAZ 537).
4. Ampliar cadastrando para mais lojas — que é o fluxo normal da tela.

---

## Ordem de implementação

**✅ Onda 0 — feita.** DDL aplicada e conferida em `172.16.10.2` (§F1). `DOC002.DOCITECOD` é
`NUMBER(10)`, `DOCDTOP1` é `DATE`, `DOCINDEXC1` é `NUMBER(1)`, `DOCGRAHOR`/`DOCGRAVER` são
`CHAR(10)`. Falta rodar as mesmas conferências no `10.150.10.126` e o
`SELECT COUNT(*) FROM ORC002 WHERE NVL(TRIM(ORCGRAHOR),'') = ''` numa loja real — se houver
caminho que insere `ORC002` sem cor (mobile, troca, importação), esse item nunca casa e o
desconto some sem erro.

**Onda 1 — duas frentes em paralelo.**

- **1A · API de leitura.** Os endpoints de catálogo, histórico e validação só leem `DOC002`,
  `XCOR001` e `XTAM001`. **Desbloqueia o front no dia 1.**
- **1B · Java, fase de risco zero.** `GradePro014`, `ItemPreVenda`, `SQL_ITENS`, o matcher e a
  troca dos 10 pontos — **com `grades` sempre vazio e `p14grade` sempre null**. Comportamento
  byte a byte idêntico, **testes existentes verdes sem uma linha editada**. É a jogada do plano:
  entrega o refactor de maior risco fiscal isolado, com prova de paridade, antes de ligar a
  tabela. Se algum teste precisou mudar, houve regressão — e esse é o critério de aceite.

**Onda 2.** Escrita na API (repositório `PRO0144`, DTO, validação síncrona pré-enqueue,
`create`/`addItems`/`addStores`, registro no worker module) + `SQL_GRADE` no `Pro014DaoImpl` com
a detecção cacheada + front consumindo os endpoints reais.

**Onda 3 — calendário externo.** DDL nas lojas; triggers criadas pelo time responsável;
replicação do `OPERACAOLOG` validada; §2.6 resolvido; campanha de teste numa loja.

### Esforço — insumo para o §7 da EF (*"Em levantamento"*)

| Frente | Dias de dev | Observação |
|---|---|---|
| ~~F1 · DDL~~ | ✅ feito | rollout nas lojas: 1-3 semanas de calendário, não é dev |
| F2 · API leitura | 3-4 | independe da DDL; desbloqueia o front |
| F3 · API escrita | 5-6 | |
| **F3b · Conflito com grade** | **3** | validador de 675 linhas sem cobertura — maior risco de regressão da API |
| F4 · Front | 5-7 | começa com mocks, fecha com F2. Os dois hosts (wizard + tela de produtos) |
| F5 · Java | 5-6 (+2-3 de shadow) | maior risco fiscal |
| — · ADR | 1 | grupo novo em `docs/adr/` |

**≈ 23-28 dias-homem. Calendário realista: 5 a 6 semanas com 2 devs** — agora dominado pelo
código, já que o DDL saiu do caminho crítico.

### Dependências que não destravamos sozinhos

| | Dependência | Dono |
|---|---|---|
| **D1** | **DDL em 200+ lojas.** Sem isso o Java nunca vê a `PRO0144` e a feature existe só na retaguarda | DBA / Infra |
| **D2** | **As triggers `KAFKA_PRO0144` e `TG_PRO0144`** (§1.4). Não são nossas, e sem a `TG_*` a promoção nunca sai da central — o `PRO017` é a prova | time que cria triggers |
| **D3** | **Consumidor do `OPERACAOLOG`.** Busquei em todo `/Volumes/WD500GB/VERZEL/GAV`: só existe como entidade JPA passiva no `Var3.Common`. **Quem lê o log e aplica na loja não está em nenhum repo nosso.** Alguém precisa ensiná-lo a replicar a `PRO0144` com chave de 5 campos e a coluna nova da `PRO0141`. Se for gerado por metadata, é configuração; se for Delphi/Genexus, é outro time e outro sprint. **Descobrir na semana 1** | a definir |
| **D4** | **Publicação do JAR nas lojas** | TI / Infra |
| **D5** | **Assinatura da paridade do E1.** `application.yml` marca `desconto-sintetico-java` como *"transcrito do .gx; PARIDADE REAL PENDENTE"*. Se ninguém assinar, a flag pode ser desligada e a grade não sai do papel na loja mesmo com tudo pronto | TI |

---

## Riscos

1. **As triggers da `PRO0144` não saírem.** Não é código nosso, mas é o risco nº 1 do projeto: a
   promoção fica presa na central, sem erro nenhum. `PRO017` existe, cadastra, e tem zero linhas
   no log de replicação. Precisa de dono e data, não de lembrete.
2. **O validador de conflito** (§2.7). 675 linhas sem cobertura de teste, e agora ele passa a
   decidir por sobreposição de alvos em vez de igualdade de item. Errar para o lado frouxo deixa
   duas campanhas se sobreporem no mesmo SKU; errar para o lado apertado barra cadastro legítimo
   e a feature parece quebrada. **Teste antes de código, sem exceção.**
3. **A FK derrubando a campanha inteira** por um item que não existe na `ITE001` (§1.2).
4. **Anexar `PRO0144` como linhas na lista do motor** — quatro pontos quebram em silêncio
   (§5.1). Resolvido pelo aninhamento, mas é o erro natural de quem chegar depois.
5. **`P14GRADE = 1` sem nenhuma linha em `PRO0144`.** Com o *fail-closed*, o desconto não sai —
   que é o comportamento certo, mas o usuário não vê motivo na tela. Precisa de mensagem.
6. **`addStores` esquecido** (`pro014.repository.ts:339-382`): a loja nova aplicaria no produto
   inteiro. É a falha mais silenciosa do lado da API.
7. **O worker é outro processo.** Repositório não registrado em `worker.module.ts` derruba o job
   de criação no bootstrap — e não aparece rodando só a API.
8. **Corrida na geração do código.** `pro014.repository.ts:161-165` faz
   `SELECT NVL(MAX(P14PROCOD),0)+1` sem lock. Não é regressão nossa, mas mais um INSERT em chunks
   aumenta a janela de `ORA-00001`. Tratar com retry ou registrar no ADR.
9. **O preço não muda em lugar nenhum** — é requisito (EF §3.5), não limitação. Mas etiqueta,
   consulta de preço (F-key) e `GET /bipagem` continuam mostrando o preço cheio. **Alinhar com a
   operação de loja antes do piloto**, senão vira chamado.

---

## Verificação

**Banco** — sem subir a API, no molde de `medir-oracle-teste-direto`:

```sql
SELECT NVL(TRIM(DOCGRAHOR),' ') COR, NVL(TRIM(DOCGRAVER),' ') TAM,
       COUNT(*) VENDAS, MAX(DOCDTOP1) ULTIMA
  FROM VAR.DOC002 WHERE DOCITECOD = :item AND NVL(DOCINDEXC1,0) <> 9
 GROUP BY NVL(TRIM(DOCGRAHOR),' '), NVL(TRIM(DOCGRAVER),' ') ORDER BY 3 DESC;

SELECT OPERACAOLOGTAB, OPERACAOLOGKEY, OPERACAOLOGTIPO, OPERACAOLOGDATA
  FROM VAR.OPERACAOLOG WHERE OPERACAOLOGTAB = 'PRO0144'
 ORDER BY OPERACAOLOGDATA DESC FETCH FIRST 5 ROWS ONLY;
```

*Hoje não deu para medir: o Oracle `172.16.10.2:1521` não responde fora da VPN. Rodar antes de
fechar a F2.*

**API** — `npm run typecheck` + `npm run lint`. Nunca a suíte completa. Specs:

1. `pro0144.repository.spec.ts`: INSERT com binds nomeados; alvo subsumido é rejeitado; remover a
   última grade zera `P14GRADE` **na mesma transação** (assert de ordem, sem commit intermediário).
2. `campaign-grade-validator.service.spec.ts`, nomes declarando o critério (R12): *"item sem
   nenhuma venda não bloqueia, só avisa"*; *"cor nunca vendida em item com histórico bloqueia"*;
   *"cor vendida com combinação inédita avisa e permite confirmar"*; *"cor fora do XCOR001 mas
   presente no DOC002 não bloqueia"*; *"cor em branco é rejeitada no DTO"*.
3. `gradeTargets` sobrevive ao round-trip de serialização do job em Redis.
4. **Regressão:** campanha sem `gradeTargets` não emite nenhum SQL contra `PRO0144` e o SQL de
   `PRO0141` sai idêntico ao de hoje.
5. `campaign-conflict-validator.spec.ts` — a tabela-verdade inteira do `colidem`:
   *"cor 437 e cor 435 do mesmo item não colidem"*; *"cor 437 e tamanho 042 colidem, porque a
   amarela M cai nas duas"*; *"item sem grade colide com qualquer grade do mesmo item"*;
   *"item sem grade colide com item sem grade, como hoje"*; *"PRO013 e PRO017 continuam colidindo
   por item inteiro"*. **Este é o de maior risco de regressão da API — escrever antes do código.**

**Java** — `mvn test`, `JAVA_HOME` no openjdk@17:

6. `Pro014DaoImplTest:83` assere `hasSize(2)` — vira 3. Novo teste: *"loja sem PRO0144 cai para
   produto inteiro e não repete a query"* (mock lança `ORA-00942`; a segunda chamada a `buscar()`
   **não** reexecuta `SQL_GRADE`).
7. `GradePro014Test`: tabela-verdade do `aceita` — curinga × valor, padding, case, null, branco;
   e `especificidade()` ordenando 1 → 2 → 3 → 4.
8. **O teste que prova a não-aplicação.** Header tipo 3 leve 2 pague 1 vigente; `PRO0141` do
   item com `p14grade = 1` e grade `(cor=437, tam=NULL)`; pré-venda com duas linhas do mesmo item
   em **cor 435**. Assert: `BigDecimal.ZERO` **e `getParticipantes()` vazio** — só o valor não
   basta, um bug de rateio pode zerar o valor e ainda marcar participantes, e aí `ORCVALDSC` fica
   inconsistente com o header (origem do `BUG_537_PERCENTUAL_SEM_ARREDONDAMENTO`).
9. Espelho positivo: duas linhas cor 437 ⇒ desconto cheio.
10. **A mistura — o teste que decide a regra da EF §3.4.** Uma linha 437 + uma 435, leve 2 pague 1
    ⇒ **zero**, porque a peça 435 não é participante e o combo não fecha. Se filtrarmos só o item
    gatilho e esquecermos o agrupamento (`buscarItensOutrasSequencias`), ele passa em verde
    errado dando desconto.
11. Os mesmos casos em `Ppro014c` (foco em `:225-245`) e `Ppro014A` (foco em `:254-266`).
12. **Paridade:** todos os testes existentes de `Ppro014L/c/A/B` passam **sem uma linha editada**.
13. Teste explícito de que o bug do `windprom` continua reproduzido com `grades` vazio.

**Front** — `npx tsc -b` (nunca `tsc --noEmit`: a raiz tem `"files": []` e dá falso verde) +
`npm run lint --max-warnings 0`. Vitest no modal (só cor ⇒ `{color, size: null}`; bloqueio ⇒
confirmar desabilitado; aviso ⇒ habilitado). Playwright em
`e2e/tests/business-planning/campaigns/pro014-grade.spec.ts`: caminho feliz e caminho de
bloqueio. Sem overflow horizontal em 320/768/1280/1536 com a coluna nova (R13).

**Ponta a ponta** — cadastrar campanha de grade **para uma loja só**, e no caixa **bipar dois
códigos de barras do mesmo produto em cores diferentes na mesma venda**. Uma sai com desconto, a
outra a preço cheio. Mais: uma loja com o JAR novo e a `PRO0144` **ausente**, para provar o
fallback e que o E1 Java **não** caiu no Genexus — assert no contador, não no log.

---

## A conferir

**✅ Resolvidos no banco em 09/09:**

- PK da `PRO0141` é `(P14LOJCOD, P14PROCOD, P14ITECOD)` — constraint `SYS_C00112510171`. A FK
  funcionou.
- `DOC002`: `DOCITECOD NUMBER(10)`, `DOCDTOP1 DATE`, `DOCINDEXC1 NUMBER(1)`,
  `DOCGRAHOR`/`DOCGRAVER` `CHAR(10)`. A coluna de data da query do Fábio existe e é a certa.
- A `PRO0141` já tinha `CREATED_AT` e `LAST_UPDATED` — a constante do código é que está
  desatualizada.

**Em aberto:**

1. **As mesmas conferências no `10.150.10.126`** — o driver thin não alcança aquele servidor;
   as queries estão no documento de handoff.
2. **`addItems` valida contra a `ITE001`?** O `create` valida; se o `addItems` não validar, a FK
   derruba a transação (§1.2).
3. **Layout físico da `PRO014` central × loja.** `pro014.repository.ts:184-214` escreve
   `P14DTINIC/P14DTTERM/P14PERC` **no central** e `Pro014DaoImpl.java:29-39` lê as mesmas colunas
   **na loja** — mas o comentário de `campaign-columns.constant.ts:8-9` diz "moderno em PROD,
   legado em DEV/lojas antigas".
4. **`ITE001.ITEGRAHOR`/`ITEGRAVER`** — lidas em `ProdutoDAOImpl.java:69-70,139-140`, e o nome
   bate com a convenção HOR/VER. *A medição de ontem diz que são `CHAR(1)` e estão vazias
   (303.033 NULL de 364.722), ou seja, flags legadas — não cadastro de grade.* Ainda assim vale
   15 minutos com o DBA: se existir uma tabela de grade por trás delas, o select do modal cairia
   de 375 cores para 6.
5. **Grupo de ADR** — não existe `docs/adr/groups/campaign/`. Combinar se cria ou se entra em
   `infrastructure`.
6. **Dono do consumidor do `OPERACAOLOG`** (D3) e **das triggers** (D2) — o gargalo real.
