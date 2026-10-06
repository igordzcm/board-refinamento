# Desconto por SKU/grade — tarefas do lado VAR (motor do PDV)

> Recorte de [`PLANO-IMPLEMENTACAO-DESCONTO-SKU.md`](PLANO-IMPLEMENTACAO-DESCONTO-SKU.md) só com o que é
> `Var3.VendaMercantil/.../desconto/` (o motor de desconto que roda dentro da loja, em Java). O que é
> Portal/API/banco central está em [`TAREFAS-PORTAL-RETAGUARDA.md`](TAREFAS-PORTAL-RETAGUARDA.md).

## F5 — Motor do PDV (`Var3.VendaMercantil/.../desconto/`)

### Decisão de desenho: aninhar, não anexar linhas

`PRO0144` **não** entra como linhas extras na `ArrayList<PromocaoPro014>` — isso quebra em silêncio em
4 pontos (`Ppro014cCalculator.java:204-213`, `Ppro014LCalculator.java:224-231`, `Ppro014cCalculator.java:194-202`,
`Ppro014ACalculator.java:211-215` — todos assumem uma linha por `(loja, procod, itecod)` e nenhum lança
exceção se essa premissa quebrar; o desconto simplesmente sai errado). Em vez disso, a grade **fica
aninhada dentro da linha do item na `PRO0141`**, preservando a cardinalidade que os filtros de header
(`p.getP14itecod() == null`) já assumem hoje.

### Tarefas

- [ ] **`GradePro014.java`** (novo, em `desconto/domain/`) — `@Value @Builder`, campos `cor`/`tam`,
      método `aceita(corItem, tamItem)` com `null` = curinga, `especificidade()` pra ordenar
      cor+tam > cor > tam > produto inteiro, `normalizar()` resolvendo `CHAR` padded + case + branco.
      Constante `SEM_RESTRICAO` só existe em memória (nunca gravada — o `CK_PRO0144_ALVO` do banco
      garante isso).
- [ ] **`PromocaoPro014`** — dois campos novos (`Integer p14grade`, `List<GradePro014> grades`) e dois
      métodos: `casaCom(item)` e `alvoQueCasa(item)` (retorna o alvo mais específico entre os que
      aceitaram, usado por log/`ResultadoMetro` — ponto de extensão pronto pro dia em que pedirem "20%
      na cor e 30% no SKU").
- [ ] **Regra fail-closed em `temGrade()`:** `(p14grade == 1) || !grades.isEmpty()` — as duas fontes em
      OR. Isso importa porque a `PRO0144` pode não ter chegado numa loja (DDL fora de ordem, replicação
      atrasada): se a regra fosse "sem grades ⇒ casa o item inteiro", uma campanha restrita a uma cor
      aplicaria em **todas** as cores naquela loja (over-discount, com efeito fiscal, sem erro e sem
      log). Com o OR, as duas direções de dessincronia falham pro lado conservador.
- [ ] **`Pro014DaoImpl`** — `SQL_GRADE` novo, carrega grades num `Map<ChaveItem, List<GradePro014>>` via
      `JOIN pro0144 → pro0141 → pro014` filtrando `i.p14ativ = 1` (quem decide participação é a
      `PRO0141`, não a `PRO0144`). `mapear()` anexa a lista só nas linhas de item. `SQL_ITEM` ganha
      `i.p14grade`.
- [ ] **Detecção de layout com fallback**, uma vez por processo (molde de `pro014-sync.repository.ts:33,100-121`):
      se a loja ainda não tem `PRO0144` (`ORA-00942`) ou a coluna (`ORA-00904`), cachear
      `gradeDisponivel = false`, logar `warn`, seguir com mapa vazio. Combinado com o fail-closed de
      `temGrade()`, a campanha restrita simplesmente **não aplica** naquela loja em vez de aplicar no
      produto inteiro — elimina a dependência de ordem entre DDL e publicação do JAR.
- [ ] `ItemPreVenda` ganha `orcgrahor`/`orcgraver`; `ContextoPreVendaLoaderImpl.java:47-51` traz as
      colunas, `:126-138` mapeia com `trim()` (`:145-147`). **Convenção contraintuitiva: `HOR` = cor,
      `VER` = tamanho** (`PreVendaItemDAOImpl.java:101-102`) — fácil de inverter por engano.

### Os 10 pontos a trocar (filtro passa a ser `promo.casaCom(item)`)

| Arquivo | Linhas | Cuidado |
|---|---|---|
| `Ppro014LCalculator` | `:213-222`, `:224-231` | assinatura passa a receber `ItemPreVenda` |
| `Ppro014cCalculator` | `:194-202`, `:204-213` | linha de gatilho com cor errada é descartada aqui, antes do `seqConsumida[wseq]` (`:66`) |
| `Ppro014cCalculator` | `:225-234`, `:236-245` | **atenção:** o predicado certo não é "mesma cor do gatilho" — pra alvo nível 2 (só cor), tamanhos P e M **devem** agrupar juntos |
| `Ppro014ACalculator` | `:236-240`, `:254-259`, `:261-266` | idem acima |
| `Ppro014BCalculator` | `:34` | o mais simples — bom primeiro spike |

- ⚠️ **Não tocar em `Ppro014ACalculator.java:211-215`.** É o bug do Genexus reproduzido de propósito
  (`BUG_GENEXUS_PPRO014A_WINDPROM.md`) — sem grade, continua reproduzindo igual. Precisa de teste
  explícito provando isso, senão alguém "conserta" no futuro achando que é bug novo.
- ⚠️ **Leve/pague com grade:** só as peças da grade contam pra fechar o combo. Numa "leve 3 pague 2"
  restrita à cor amarela, 2 amarelas + 1 preta **não fecha** — a peça preta está fora da campanha, não
  só fora do desconto (EF §3.2 e §3.4; TAP §III). Isso cai naturalmente de `promo.casaCom(it)` nos 4
  pontos item×item — mas só se o agrupamento (`buscarItensOutrasSequencias`) também filtrar, não só o
  item gatilho.

### Rede de segurança

- 🚩 **`DescontoSinteticoService.java:34-41`** tem `catch (Exception)` cobrindo o `calcular()` inteiro:
  se o DAO estourar, **toda a venda da loja cai no Genexus** e o motor Java fica desligado de fato,
  visível só num `log.error`. Este projeto introduz um ponto novo de falha (`SQL_GRADE`) bem dentro
  desse `try` — **precisa de contador/métrica**, não só log, senão a regressão passa despercebida em
  produção.

## Testes (Java — `mvn test`, `JAVA_HOME` no openjdk@17)

1. `Pro014DaoImplTest:83` — `hasSize(2)` vira `hasSize(3)`. Novo teste: loja sem `PRO0144` cai pra
   produto inteiro e **não repete** a `SQL_GRADE` na segunda chamada (mock lança `ORA-00942` só uma vez).
2. `GradePro014Test` — tabela-verdade do `aceita` (curinga × valor, padding, case, null, branco) e
   `especificidade()` ordenando 1→2→3→4.
3. **O teste que prova a não-aplicação:** header leve 2 pague 1 vigente; item com `p14grade=1` e grade
   `(cor=437, tam=NULL)`; pré-venda com 2 linhas em **cor 435**. Assert: `BigDecimal.ZERO` **e**
   `getParticipantes()` vazio — só o valor não basta, um bug de rateio pode zerar o valor e ainda marcar
   participantes, deixando `ORCVALDSC` inconsistente com o header.
4. Espelho positivo: 2 linhas cor 437 ⇒ desconto cheio.
5. **A mistura** — 1 linha 437 + 1 linha 435, leve 2 pague 1 ⇒ **zero**, porque a 435 não é participante
   e o combo não fecha. Se filtrar só o item gatilho e esquecer o agrupamento, passa em verde errado
   dando desconto. **Este é o teste que decide a regra da EF §3.4 — obrigatório.**
6. Mesmos casos em `Ppro014c` (foco `:225-245`) e `Ppro014A` (foco `:254-266`).
7. **Paridade:** todos os testes existentes de `Ppro014L/c/A/B` passam **sem uma linha editada** — se
   algum precisar mudar, é regressão, esse é o critério de aceite (Onda 1B roda com `grades` sempre
   vazio e `p14grade` sempre null, byte a byte igual ao comportamento de hoje).
8. Teste explícito de que o bug do `windprom` continua reproduzido com `grades` vazio.
9. Métrica/contador novo no `DescontoSinteticoService` sendo incrementado quando o fallback do item 1
   dispara.

## Verificação de banco (na loja, sem subir API)

```sql
SELECT NVL(TRIM(DOCGRAHOR),' ') COR, NVL(TRIM(DOCGRAVER),' ') TAM,
       COUNT(*) VENDAS, MAX(DOCDTOP1) ULTIMA
  FROM VAR.DOC002 WHERE DOCITECOD = :item AND NVL(DOCINDEXC1,0) <> 9
 GROUP BY NVL(TRIM(DOCGRAHOR),' '), NVL(TRIM(DOCGRAVER),' ') ORDER BY 3 DESC;

SELECT OPERACAOLOGTAB, OPERACAOLOGKEY, OPERACAOLOGTIPO, OPERACAOLOGDATA
  FROM VAR.OPERACAOLOG WHERE OPERACAOLOGTAB = 'PRO0144'
 ORDER BY OPERACAOLOGDATA DESC FETCH FIRST 5 ROWS ONLY;
```

## Ponta a ponta (loja piloto)

- Cadastrar campanha de grade **numa loja só** (via portal) e, no caixa, bipar dois códigos de barra do
  mesmo produto em cores diferentes na mesma venda — uma sai com desconto, a outra a preço cheio.
- Uma loja com o JAR novo e a `PRO0144` **ausente** — provar o fallback e que o motor Java **não** caiu
  no Genexus (assert no contador da rede de segurança, não no log).
- Conferir no banco da loja: `ORC002.ORCVALDSC` só na linha certa; `ORC014.ORC14ORI = "PRO014 -
  <procod>"`; Σ `ORC002.ORCVALDSC` = `ORC001.ORCTOTDSCO` (SEFAZ 537).

## Dependências que este lado não resolve sozinho

- **D1 — DDL nas 200+ lojas** (DBA/Infra). Sem isso, este código nunca vê a `PRO0144` na loja — cai
  sempre no fallback do item 1.
- **D2 — Triggers `KAFKA_PRO0144`/`TG_PRO0144`.** Não são criadas por este time; sem `TG_*` a promoção
  não sai da central e o Java nunca recebe nada pra testar em produção. **Risco nº 1 do projeto** — o
  `PRO017` é a prova viva: existe, cadastra, zero linhas no log de replicação.
- **D3 — Consumidor do `OPERACAOLOG`.** Busca em todo o workspace de código não achou quem lê o log e
  aplica na loja — só existe como entidade JPA passiva no `Var3.Common`. Se for gerado por metadata, é
  configuração; se for Delphi/Genexus, é outro time e outro sprint. **Descobrir na semana 1.**
- **D4 — Publicação do JAR nas lojas** (TI/Infra).
- **D5 — Assinatura de paridade do E1.** `application.yml` marca `desconto-sintetico-java` como
  "transcrito do .gx; PARIDADE REAL PENDENTE" — sem essa assinatura formal, o botão de emergência
  (`features.desconto.desconto-sintetico-java`) pode desligar o motor Java inteiro e a grade não sai do
  papel em loja mesmo com tudo pronto.

## Riscos específicos deste lado

1. Trigger da `PRO0144` não sair (D2) — feature presa na central sem erro nenhum.
2. Anexar `PRO0144` como linhas soltas na lista do motor — 4 pontos quebram em silêncio (resolvido pelo
   aninhamento, mas é o erro natural de quem chegar depois sem ler este documento).
3. `P14GRADE = 1` sem nenhuma linha em `PRO0144` — com fail-closed o desconto não sai (comportamento
   certo), mas o usuário não vê motivo nenhum na tela. Precisa de mensagem clara do lado API/front.
4. Fallback silencioso do `DescontoSinteticoService` mascarando exatamente o erro que este projeto
   introduz, se a métrica do item "Rede de segurança" não for adicionada.

## Ordem sugerida

**Onda 1B — fase de risco zero, pode rodar em paralelo com o F2 do Portal:** `GradePro014`,
`ItemPreVenda`, `SQL_ITEM`/`SQL_GRADE`, o matcher e a troca dos 10 pontos, com `grades` sempre vazio e
`p14grade` sempre null. Testes existentes verdes **sem uma linha editada** é o critério de aceite —
entrega o refactor de maior risco fiscal isolado, com prova de paridade, antes de ligar a tabela de
verdade. Só depois disso liga a leitura real (`SQL_GRADE` com dados) na Onda 2, junto com D1-D5
resolvidos o suficiente pra ao menos uma loja de teste.
