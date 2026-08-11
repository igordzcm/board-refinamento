---
work_item_id: 12489
project: Var Retaguarda
work_item_type: Product Backlog Item
snapshot_date: 2026-08-11
snapshot_reason: "Backup antes de corrigir nome de coluna e causa raiz (overflow-auto já existe; falta largura mínima de coluna)"
url: https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12489
---

# Card #12489 — versão original (antes da edição de 2026-08-11)

## Metadados

| Campo | Valor |
|---|---|
| ID | 12489 |
| Tipo | Product Backlog Item |
| Esforço | 2 |
| Tags | CONCILIAÇÃO; Front-end; QA |
| Epic pai | #6640 — Portal de Retaguarda (Sustentação) |

## Título

> Tabela de Justificativas corta colunas sem scroll horizontal

## Descrição original

> **Como** usuário do módulo Conciliação (Administrativo › Justificativa)
> **Quero** que a tabela de justificativas tenha rolagem horizontal quando o conteúdo excede a largura da tela
> **Para que** eu consiga visualizar todas as colunas, incluindo "Pode Fechar / Reabrir", sem perda de informação
>
> Na tela `/conciliacao/justificativas`, a tabela estoura a largura disponível e a última coluna aparece cortada, sem barra de rolagem horizontal nem indicação visual de que há mais conteúdo à direita. Adicionar `overflow-x` na tabela, no mesmo padrão já usado em outras telas do sistema.
>
> _Achado do levantamento de QA (Danilo) de 05/08/2026._

## Critérios de Aceite originais

**Cenário 1 — Tabela com muitas colunas**
Dado que acesso Conciliação › Administrativo › Justificativa com a tela em resolução padrão,
Quando a soma da largura das colunas excede a largura do container,
Então a tabela deve exibir rolagem horizontal, permitindo visualizar por completo a coluna "Pode Fechar / Reabrir".

**Cenário 2 — Sem quebra de layout**
Dado que a correção de scroll foi aplicada,
Então o comportamento das demais colunas não deve ser alterado, nem o alinhamento do cabeçalho com o corpo da tabela.

## Por que este backup existe

Investigação no código (`ConciliaçãoCaixaFront`) mostrou que:
1. O nome real da coluna é "Pode Fechar com Falta" (não "Pode Fechar / Reabrir").
2. `overflow-auto` já existe no wrapper da tabela — a instrução original ("adicionar overflow-x") não teria corrigido nada. A causa real é ausência de largura mínima por coluna.

Versão preservada aqui para referência.
