# Desconto por SKU/grade — tarefas do lado Portal Retaguarda

> Recorte de [`PLANO-IMPLEMENTACAO-DESCONTO-SKU.md`](PLANO-IMPLEMENTACAO-DESCONTO-SKU.md) só com o que é
> `ConciliaçãoCaixaAPI` + `ConciliaçãoCaixaFront` (banco central + portal). O que roda no PDV da loja
> está em [`TAREFAS-VAR.md`](TAREFAS-VAR.md). Dependências que nenhum dos dois lados destrava sozinho
> ficam listadas nos dois arquivos.

## F1 — Oracle (banco central) · ✅ feito, resta conferir

- [x] `ALTER TABLE VAR.PRO0141 ADD (P14GRADE ...)` + `CHECK` — aplicado e conferido em homologação
      09/09/2026 14:18 (`172.16.10.2/teste`, Oracle 19c). 1.628.562 linhas, todas em `P14GRADE = 0`.
- [x] `CREATE TABLE VAR.PRO0144` + `UX_PRO0144` + `IX_PRO0144_ITE`.
- [ ] **Repetir as mesmas conferências no `10.150.10.126`** — o driver `node-oracledb` em thin mode não
      alcança esse servidor (versão anterior à 12.1). Rodar as queries do documento de handoff via SQL
      Developer.
- [ ] `SELECT COUNT(*) FROM ORC002 WHERE NVL(TRIM(ORCGRAHOR),'') = ''` numa loja real — se existir
      caminho que grava `ORC002` sem cor (mobile, troca, importação), esse item nunca casa e o desconto
      some sem erro.
- [ ] Confirmar se `addItems` (`pro014-items.repository.ts:90-146`) valida contra `ITE001` — o `create`
      já valida (`pro014.service.ts:218-230`); se `addItems` não validar, a FK nova derruba a transação
      inteira da campanha com `ORA-02291` no primeiro item inexistente.
- [ ] Esclarecer layout físico `PRO014` central × loja — `pro014.repository.ts:184-214` escreve
      `P14DTINIC/P14DTTERM/P14PERC` no central e `Pro014DaoImpl.java:29-39` lê as mesmas colunas na
      loja, mas o comentário de `campaign-columns.constant.ts:8-9` fala em "moderno em PROD, legado em
      DEV/lojas antigas".
- [ ] 15 min com o DBA sobre `ITE001.ITEGRAHOR`/`ITEGRAVER` — hoje medidas como `CHAR(1)` vazias
      (303.033 NULL de 364.722), parecem flag legada e não cadastro de grade; só vale confirmar porque,
      se existir tabela de grade por trás, o select do modal cairia de 375 cores para 6.

## F2 — API de leitura (desbloqueia o front no dia 1, independe do rollout de DDL nas lojas)

- [ ] `GET /campaigns/grade/catalog` — `XCOR001` + `XTAM001` inteiros (~25 KB), cache 12h no RTK Query.
- [ ] `GET /campaigns/grade/items/:itemCode/sold` — histórico de vendas por cor/tamanho/combinação do
      item, vindo de `DOC002` (bind numérico explícito — ver alerta abaixo).
- [ ] `POST /campaigns/grade/validate` — roda o algoritmo do §2.2 do plano (bloqueio/aviso) no servidor,
      síncrono, **antes do enqueue** do job de criação (`pro014.service.ts:135-158` enfileira sempre que
      `items × lojas >= 100`, que é quase sempre).
- [ ] Registrar os 3 endpoints novos **antes** do `@Get(":id")` de `campaign.controller.ts:299`, como já
      acontece com `@Get("items/search")`.
- 🚩 **Bind numérico explícito no `DOCITECOD`.** `campaign-conflict-validator.service.ts:118` interpola
  itemCodes com aspas; se `DOC002.DOCITECOD` for `NUMBER` e o bind vier string, o Oracle converte
  implicitamente e descarta o índice `IDOC0021` (full scan em 1,28 M linhas).
- Estimativa do plano: **3-4 dias**.

## F3 — API de escrita

- [ ] Repositório novo pra `PRO0144`, seguindo o padrão de `provider/sold-items/queries/get-sold-items.ts`
      (SQL em const nomeada de módulo).
- [ ] Novo campo paralelo no DTO: `gradeTargets?: Array<{ itemCode, color: string|null, size: string|null }>`
      — **sem mudar o tipo de `items`/`itemCodes` existentes.** `P14GRADE` é sempre derivado no INSERT,
      nunca digitado.
- [ ] `constants/campaign-columns.constant.ts:100-104` — adicionar `P14GRADE` em `PRO014_ITEM_COLUMNS`.
- [ ] `pro014-items.repository.ts:170,206,245` — os 3 caminhos de INSERT em `PRO0141`.
- [ ] `pro014.repository.ts:227-285` — nova **FASE 4** (`lojas × gradeTargets` → `PRO0144`), antes do
      `commitTransaction` de `:288`.
- [ ] `pro014.repository.ts:339-382` (`addStores`) — **o mais fácil de esquecer:** ao adicionar loja,
      copiar `PRO0144` também (hoje só copia header + itens), senão a loja nova aplica o desconto no
      produto inteiro.
- [ ] `pro014-items.repository.ts:374-471` — listagem paginada devolve `P14GRADE` + grades via segunda
      query batched por página (não `LISTAGG`, estoura o limite de 4000 caracteres).
- [ ] `pro014-sync.repository.ts:729-745` — ajuste de sync (ver §2.6 do plano).
- [ ] `src/workers/worker.module.ts:18,91` — **registrar o repositório novo no módulo do worker.** Sem
      isso o job de criação morre no bootstrap com "Nest can't resolve dependencies" — e isso **não
      aparece rodando só a API**.
- [ ] ADR obrigatório em `docs/adr/` — decidir se cria `groups/campaign/` ou entra em `infrastructure`.
- 🚩 **`PRO014_ITEM_COLUMNS` já está errada hoje** (falta `P14LOJCOD`) e `addStores` não usa essa const —
  escreve a lista literal no `SELECT`. Ao adicionar `P14GRADE`, mexer numa coisa só (const em todos os
  INSERTs, ou o literal em todos) — nunca metade, senão o código da loja entra na coluna errada.
- Estimativa do plano: **5-6 dias**.

## F3b — Conflito entre campanhas passa a considerar grade

- [ ] `campaign-conflict-validator.service.ts:126-149` — query self-`PRO014` ganha `LEFT JOIN` em
      `PRO0144`; comparação vira **sobreposição de alvos**, não igualdade de item.
- [ ] `:155-166` — `Map` de agrupamento passa a ser chaveado também pela grade, não só por `itemCode`.
- [ ] `:574` — dedupe `${type}-${code}-${storeCode}-${listNumber}` ganha `cor|tam`.
- [ ] `step-four.tsx:399-416` + `utils/conflict-resolution.ts` — botão "Remover da anterior" passa a
      remover **uma grade**, não o item inteiro (hoje `pro014-items.repository.ts:284-369` só sabe
      soft-delete de `PRO0141`).
- [ ] Regra de sobreposição: `colidem(A,B) = eixoColide(cor) && eixoColide(tam)`, `eixoColide(x,y) = x
      IS NULL || y IS NULL || x = y`. `PRO013` e `PRO017` continuam colidindo por item inteiro — deixar
      isso explícito na mensagem que o usuário vê.
- Validador de 675 linhas **sem cobertura de teste hoje** — maior risco de regressão do lado API.
  **Escrever os testes antes do código** (ver seção de testes).
- Estimativa do plano: **3 dias**.

## F4 — Front (`ConciliaçãoCaixaFront/.../business-planning/campaigns/`)

- [ ] Componente único `campaigns/components/grade-target-modal.tsx` — botão por item (não checkbox;
      15.000 SKUs via Excel tornam checkbox inviável) que abre modal com dois selects (cor/tamanho),
      badge de contagem, aviso/bloqueio conforme validação do servidor.
- [ ] Host 1 — wizard `steps-pro014/step-four.tsx`, barra de ações da linha (`:398-428`).
- [ ] Host 2 — `products/index.tsx` (`/:type/:code/produtos`), coluna "Grade" no `<thead>` (`:344-358`)
      e botão no `<tbody>` (`:359-403`).
- [ ] Padrão B (Dialog shadcn local controlado por prop, molde de `add-item-modal.tsx:177-321`) — não
      Redux global.
- [ ] Centralizar `GradeTarget = { color, size }` em `campaigns/types/grade.ts` (hoje duplicado em 3
      lugares: `step-four.tsx:17-19`, `step-five.tsx:44`, `create-pro014-form.tsx:109`).
- [ ] `src/services/campaign.ts` — 3 endpoints novos (tags no padrão granular existente); catálogo com
      `keepUnusedDataFor: 43200`.
- [ ] Mensagens em `campaigns/utils/messages.ts` e `campaigns/utils/error-messages.ts`.
- [ ] **Fora da v1, declarar explicitamente:** `pro014-items-modal.tsx` (textarea em massa) e import de
      Excel — o template `/templates/sku-import-template.xlsx` só tem a coluna SKU.
- [ ] React Hook Form + zod no modal (regra do front); Vitest no modal; Playwright em
      `e2e/tests/business-planning/campaigns/pro014-grade.spec.ts` (caminho feliz + bloqueio); sem
      overflow horizontal em 320/768/1280/1536 com a coluna nova.
- Pode começar com mocks e fechar quando F2 estiver pronta. Estimativa do plano: **5-7 dias**.

## Fora de escopo (não mexer)

- Propagação da API pra loja (`campaign-propagation.processor.ts`, `campaign-edit-propagation.processor.ts`)
  — jobs enfileirados sem consumidor, hoje quem replica é o `OPERACAOLOG`. Fica como está.
- `DynamicOracleService`/`VarDataSource` apontando pra Oracle — exceção legada já existente no módulo
  `campaign` e em `sold-items`; só registrar a divergência no ADR, não corrigir agora.

## Testes (lado API/Front)

1. `pro0144.repository.spec.ts` — INSERT com binds nomeados; alvo subsumido rejeitado; remover a última
   grade zera `P14GRADE` na mesma transação.
2. `campaign-grade-validator.service.spec.ts` — nomes declarando o critério: item sem venda não bloqueia
   só avisa; cor nunca vendida bloqueia; combinação inédita avisa e permite confirmar; cor fora do
   `XCOR001` mas em `DOC002` não bloqueia; cor em branco rejeitada no DTO.
3. `gradeTargets` sobrevive ao round-trip de serialização do job no Redis.
4. **Regressão:** campanha sem `gradeTargets` não emite SQL contra `PRO0144`; SQL de `PRO0141` idêntico
   ao de hoje.
5. `campaign-conflict-validator.spec.ts` — tabela-verdade completa do `colidem` (é o de maior risco de
   regressão da API; escrever antes do código).
6. Front: Vitest do modal + Playwright do caminho feliz/bloqueio + checagem de overflow responsivo.
7. `npm run typecheck` + `npm run lint` (nunca a suíte completa como gate único).

## Dependências que este lado não resolve sozinho

- **D1 — DDL nas 200+ lojas.** Sem isso o Java (VAR) nunca vê a `PRO0144`; dono: DBA/Infra.
- **D2 — Triggers `KAFKA_PRO0144`/`TG_PRO0144`.** Não são criadas por este time; sem `TG_*` a promoção
  não sai da central (mesmo destino do `PRO017` hoje, que tem zero linhas no log de replicação).
- **D5 — Assinatura de paridade do motor E1** (TI) — sem ela a flag pode ser desligada e a feature não
  roda em loja mesmo com a API/front prontos.

## Riscos específicos deste lado

1. **`addStores` esquecido** — loja nova aplicaria desconto no produto inteiro. Falha mais silenciosa
   do lado API.
2. **Worker não registrado** — job de criação morre no bootstrap, só aparece rodando o worker separado.
3. **FK derrubando a campanha inteira** por item inexistente em `ITE001`, se `addItems` não validar antes.
4. **Corrida na geração de código** — `pro014.repository.ts:161-165` faz `SELECT NVL(MAX(...),0)+1` sem
   lock; mais um INSERT em chunks aumenta a janela de `ORA-00001`. Tratar com retry ou registrar no ADR.
5. **O preço não muda em lugar nenhum é requisito**, não bug — mas etiqueta, consulta de preço (F-key) e
   `GET /bipagem` continuam mostrando preço cheio. Alinhar com a operação de loja antes do piloto.

## Ordem sugerida

DDL (feito) → **1A: F2 em paralelo com F4 usando mocks** → F3 (destrava F4 real) → F3b (antes do código,
escrever os testes de conflito) → ADR.
