---
work_item_id: 12405
project: Var Retaguarda
work_item_type: Product Backlog Item
snapshot_date: 2026-08-11
snapshot_reason: "Backup da versão original antes da reescrita de escopo (propagação para loja removida do card)"
url: https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12405
---

# Card #12405 — versão original (antes da edição de 2026-08-11)

## Metadados

| Campo | Valor |
|---|---|
| ID | 12405 |
| Tipo | Product Backlog Item |
| Estado | Ready for Dev |
| Responsável | Leonardo Henrique da Silva |
| Prioridade | 2 |
| Esforço | 8 |
| Tags | motor de descontos |
| Epic pai | #6669 — Motor de Descontos (Doing) |
| Task filha | #12435 — "ref" (To Do) |
| Criado em | 2026-07-21 por Igor Diniz Camargo |
| Última alteração | 2026-08-11 por Danilo Santos Manzoli |
| Revisão (rev) | 9 |

## Título original

> Motor de Descontos - Refazer propagação: gravar direto no banco Retaguarda e replicar para loja via trigger

## Descrição original

> Refazer o fluxo de propagação de campanhas do Motor de Descontos. Na criação ou edição de campanha, gravar os dados diretamente no banco da Retaguarda; a propagação para a loja deixa de ser feita no ato e passa a ocorrer via uma trigger no banco da Retaguarda que duplica os dados diretamente para o banco da loja.

## Critérios de Aceite originais

- Criação de campanha grava diretamente no banco Retaguarda
- Edição de campanha grava diretamente no banco Retaguarda
- Trigger no banco Retaguarda propaga (duplica) os dados para o banco da loja, sem envio direto na hora da criação/edição
- Fluxo de propagação atual é substituído sem perda de dados ou inconsistência entre Retaguarda e loja
- Cenário de teste cobrindo criação, edição, e confirmação de que os dados chegaram corretamente na loja via trigger

## Por que este backup existe

Em 2026-08-11 o escopo do card foi corrigido: a propagação/replicação dos dados para o banco da loja deixou de ser responsabilidade desta story e passou a ser processo de outra equipe. O card foi reescrito para refletir isso (ver histórico de revisões no Azure DevOps, rev 9 → rev seguinte). Esta versão é preservada aqui para referência caso seja necessário entender a intenção original ou reverter.
