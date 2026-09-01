# Métricas do time

> Métricas operacionais do time (lead time, throughput etc.), calculadas sob demanda a partir do Azure DevOps. Não é status de projeto — isso fica nos `contexto.md` e no [README.md](README.md).

## Lead time médio de entrega

> ⚠️ **Definição mudou em 01/09/2026.** A partir desta data, lead time = **primeira transição pra `Doing` → primeira transição pra `Accepted`** (histórico de revisão do work item), não mais `ClosedDate − CreatedDate`. Motivo: a definição antiga contava tempo que o card passou parado no backlog antes de alguém pegar pra trabalhar, o que não é lead time de entrega de verdade. **O cálculo abaixo (31/08) usa a definição antiga e não é comparável a recálculos futuros** — mantido aqui só como registro histórico.

### Cálculo de 31/08/2026 (definição antiga — Created→Closed, não usar como comparação)

A partir de todos os itens do projeto "Var Retaguarda" com estado Done/Closed/Accepted/Verified e `Microsoft.VSTS.Common.ClosedDate` desde **01/08/2026** (122 itens). Lead time = `ClosedDate − CreatedDate`, em dias corridos.

| Métrica | Valor |
|---|---|
| Itens analisados | 122 |
| Média bruta | 29,4 dias |
| Mediana bruta | 11,6 dias |
| Média excluindo outliers (>60 dias) | **22,5 dias** |
| Mediana excluindo outliers | 10,3 dias |

**Por tipo de work item:**

| Tipo | Qtd | Média |
|---|---|---|
| Task | 66 | 8,2 dias |
| Product Backlog Item (história) | 39 | 59,1 dias |
| Bug | 8 | 35,8 dias |
| Nonfunctional Item | 5 | 55,9 dias |
| Technical Enabler | 4 | 43,2 dias |

**Outliers (>60 dias) — backlog antigo fechado em lote, não trabalho recente:**

| ID | Tipo | Lead time | Título |
|---|---|---|---|
| [#8311](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/8311) | PBI | 469,2 dias | Relatório sem operador (compromisso/filial) |
| [#10624](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/10624) | PBI | 192,8 dias | Keycloak not public |
| [#11568](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11568) | PBI | 90,0 dias | Backoffice - Configuração de Campanhas Chute ao Gol |
| [#11847](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11847) | PBI | 75,0 dias | [GESTÃO DE CAMPANHAS] Teste Regressivo (Roleta e Chutou Ganhou) |
| [#11854](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11854) | PBI | 74,8 dias | Configuração da Máquina de Vinhedo p/ Keycloak Not Public |
| [#11833](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11833) | Bug | 70,9 dias | [BUG] Corrigir upload, download e vínculo de anexos — Termo Assinado |

## ⚠️ Ressalva de qualidade do dado — importante ao reusar este número

Boa parte das `ClosedDate` está concentrada em **rajadas** — dezenas de itens fechados em segundos de diferença nos dias 05/08, 11/08 e 20-21/08. Isso tem cara de **fechamento em lote/retroativo** (alguém passando vários cards de uma vez pro estado final), não de conclusão item a item no momento real. Ou seja: **o número é uma aproximação razoável de ordem de grandeza, não uma métrica de precisão de engenharia** — não usar pra comparar sprints ou avaliar performance individual sem antes confirmar se o time está fechando cards no dia real da entrega.

## Como recalcular (definição atual — Doing → Accepted)

WIQL no projeto "Var Retaguarda" pra achar candidatos (itens que já passaram por Accepted em algum momento):
```
SELECT [System.Id], [System.Title], [System.WorkItemType], [System.State]
FROM WorkItems
WHERE [System.TeamProject] = 'Var Retaguarda'
AND [System.State] IN ('Accepted','Verified','Done','Closed')
AND [System.ChangedDate] >= '<data de corte>'
```
Depois, **por item** (não tem endpoint em lote pra histórico de revisão): `wit_work_item` `list_revisions`, achar a primeira revisão em que `System.State` vira `Doing` (início) e a primeira em que vira `Accepted` (fim), usar `System.ChangedDate` de cada uma. Isso é o que o agente `portfolio-report` (modo Métricas) já faz automaticamente.

## Próxima atualização

Recalcular periodicamente (sugestão: mensal) pra ter uma série histórica de verdade, em vez de um ponto isolado — agora comparável de fato, já que a definição não muda mais entre rodadas. Vale rodar uma vez logo já com a definição nova pra ter o primeiro ponto real da série.

---

## Effort entregue por sprint (velocidade do time)

> Cálculo de **01/09/2026**, sob pedido do Igor. Campo usado: **`Microsoft.VSTS.Scheduling.Effort`** (não `StoryPoints` — confirmado checando o schema do tipo "Product Backlog Item" no projeto "Var Retaguarda"; é esse o campo que o time preenche). Itens considerados: Product Backlog Item com estado `Done`/`Verified`/`Accepted`/`Closed`, agrupados por `System.IterationPath` (sprint), não por `ClosedDate` — pelos mesmos motivos de rajada/lote descritos na seção de lead time acima.

### Cobertura de dados por sprint

| Sprint | Itens entregues | Itens com Effort preenchido | Cobertura | Total de pontos (bruto) |
|---|---|---|---|---|
| Sprint 21 | 34 | 20 | 59% | 83 |
| Sprint 22 | 7 | 2 | 29% | **excluído — dado insuficiente** |
| Sprint 23 | 4 | 2 | 50% | **excluído — dado insuficiente** |
| Sprint 24 | 37 | 11 | 30% | 44 |
| Sprint 25 | 15 | 10 | 67% | 66 |
| Sprint 26 | 21 | 20 | 95% | 357 (ver ajuste abaixo) |
| Sprint 27 | 15 | 5 | 33% | 23 até agora — **sprint ativa, não contabilizada na média** (card #12892 ainda em Refinement nela) |

Sprints 22 e 23 têm só 2 itens pontuados cada — não dá pra tirar um total de sprint confiável disso, então ficaram de fora da média em vez de entrar como um número fraco disfarçado de real. A sprint 27 está em andamento (não fechada), então também fica de fora por definição ("sprints concluídas").

**Janela usada pro cálculo: Sprints 21, 24, 25 e 26** (4 sprints concluídas com dado suficiente, ainda que não contíguas — 22/23 puladas pelo motivo acima).

### ⚠️ Anomalia grave na Sprint 26 — não suavizada, tratada à parte

7 itens da Sprint 26 (#12388–#12394, todos "US1"–"US7" de um mesmo épico, todos atribuídos a Diego Oliveira Andrade Rafael, todos fechados no mesmo segundo em lote no dia 01/09) têm `Effort` = 56, 28, 44, 36, 48, 40, 44 — **fora de qualquer escala Fibonacci usada no resto do board** (o resto do dataset varia de 1 a 21). Ou é uma unidade diferente (parece mais hora do que ponto) ou um erro de preenchimento em lote. Não dá pra confirmar qual sem perguntar pro Diego ou ao Igor — por isso os dois números abaixo, bruto e ajustado (excluindo esse lote de 7 itens):

| | Sprint 21 | Sprint 24 | Sprint 25 | Sprint 26 | Média/sprint |
|---|---|---|---|---|---|
| **Bruto** (com a anomalia) | 83 | 44 | 66 | 357 | **137,5 pts/sprint** |
| **Ajustado** (sem os 7 itens #12388–#12394) | 83 | 44 | 66 | 61 | **63,5 pts/sprint** |

**Não decidi qual dos dois é "o número certo"** — isso depende de saber se aqueles 7 itens realmente valem ~40 pts cada ou se é erro/outra unidade. Recomendo confirmar com o Diego ou quem preencheu antes de citar a média de 137,5 em qualquer lugar; a de 63,5 é a mais defensável enquanto isso não é esclarecido.

### Effort por dev (dataset ajustado, janela Sprint 21/24/25/26)

| Dev | Total de pontos na janela | Sprints em que teve item entregue | Pontos/sprint (só nas sprints em que teve item) |
|---|---|---|---|
| Matheus Gabriel Donato Alves | 64 | 3 (21, 25, 26) | 21,3 |
| Kauã Miguel da Cunha | 41 | 2 (21, 25) | 20,5 |
| João Bernardo Ferreira Neto | 73 | 4 (21, 24, 25, 26) | 18,3 |
| Victor Moraes | 37 | 2 (24, 25) | 18,5 |
| Fernando Caetano de Lima | 12 | 1 (26 — entrou no time nessa sprint) | 12,0 |
| Danilo Santos Manzoli | 6 | 1 (21 — item avulso, não é dev fixo no board) | 6,0 |
| Gabriel Aparecido Kovalski Lopes | 11 | 4 (21, 24, 25, 26) | 2,8 — **ver ressalva abaixo, número não reflete o trabalho real dele** |
| Diego Oliveira Andrade Rafael | 10 (excl. anomalia) | 4 (21, 24, 25, 26) | 2,5 — **idem, ver ressalva** |

**Duas leituras da "média por dev por sprint":**
- **Por dev, só nas sprints em que ele teve entrega** (coluna acima): varia de 2,8 a 21,3 — mostra que o time é bem heterogêneo em quanto aparece pontuado, não que uns entregam 8x mais que outros (ver ressalva de cobertura abaixo).
- **Média geral do time** (total de pontos da janela ÷ (sprints × devs distintos ativos)) = 254 ÷ (4 × 9) = **≈7,1 pts/dev/sprint**. Essa conta assume que todo mundo dos 9 devs esteve ativo nas 4 sprints, o que não é verdade (Fernando só entrou na 26, Danilo e Leonardo aparecem uma vez só) — então é uma média "achatada", útil como ordem de grandeza de capacidade agregada do time, não como referência de desempenho individual.

### ⚠️ Ressalvas de qualidade do dado — importante ao reusar este número

1. **Cobertura de Effort é parcial e desigual por dev.** Gabriel Aparecido Kovalski Lopes tem ~25 PBIs entregues só na Sprint 24 e **nenhum** deles com Effort preenchido — o número de 2,8 pts/sprint dele não reflete o volume real de trabalho, só o que ficou registrado. Mesma lógica pro Diego fora da Sprint 26 (maioria dos itens dele em outras sprints está sem Effort). **Não usar esses dois números pra comparar desempenho individual.**
2. **Rajadas de fechamento em lote** (mesmo padrão já documentado na seção de lead time): dezenas de itens com `ClosedDate` idêntico ao segundo em datas como 01/06, 22/06, 11/08 e 01/09/2026. Isso sugere fechamento retroativo, não conclusão item a item no dia real — o que também levanta a dúvida de se o próprio `IterationPath` (sprint atribuída) foi preenchido retroativamente junto, e não necessariamente reflete em que sprint o trabalho foi de fato feito.
3. **Anomalia de escala na Sprint 26** (7 itens #12388–#12394) — ver seção acima, não resolvida.
4. **Política "Estimativa do PO" (sizing relativo, desde 12/08, pendente de confirmação do time técnico)** — conferido contra `boards/board-refinamento.html`: nenhum dos itens entregues/pontuados usados neste cálculo está marcado com o chip "Estimativa do PO" (essa política se aplica só a cards ainda em Refinement/Ready for Dev, ex: #12511, #12509, #12510, #12437, #12405, #12190 — nenhum deles chegou a Done/Verified/Accepted ainda). Ou seja, os pontos usados aqui não são estimativa não confirmada do PO — mas isso pode mudar em rodadas futuras conforme esses cards forem entregues, então vale reconferir a cada recálculo.
5. **Sprints 22 e 23 excluídas por dado insuficiente** (2 itens pontuados cada) — não é que a sprint não teve entrega, é que o registro de Effort nela é fraco demais pra virar número.

### Como recalcular

1. Confirmar o campo de pontos ainda é `Microsoft.VSTS.Scheduling.Effort` (`wit_work_item` `get_type` no tipo PBI, ou olhar um item concreto).
2. WIQL no projeto "Var Retaguarda": `System.WorkItemType = 'Product Backlog Item' AND System.State IN ('Accepted','Verified','Done','Closed')`, sem filtro de data (o filtro real é por `IterationPath`).
3. `wit_work_item` `get_batch` (até ~40 ids por chamada) trazendo `System.IterationPath`, `System.AssignedTo`, `Microsoft.VSTS.Scheduling.Effort`, `System.State`.
4. Agrupar por `IterationPath`, excluir a sprint ativa (a que tem cards ainda em Refinement/To Do) e qualquer sprint com poucos itens pontuados (regra prática: menos de ~5 itens pontuados = excluir e sinalizar).
5. Somar Effort por sprint e por dev; checar manualmente se algum item tem Effort fora da escala Fibonacci usual (1,2,3,5,8,13,21) antes de somar — se tiver, tratar como possível anomalia, não incluir sem investigar.
6. Cruzar os IDs entregues contra `boards/board-refinamento.html` procurando o chip "Estimativa do PO" — se algum item entregue tiver esse chip, sinalizar que aquele ponto é estimativa do PO ainda não confirmada pelo time técnico, não um número fechado.
