# Pauta — Call Igor + Arthur (quarta, 02/09/2026)

> Preparada em 01/09, ajustada no mesmo dia pra refletir a pauta real do Igor (mais enxuta do que a primeira versão). Preencher "Decisões" depois da call e sincronizar com [contexto.md](contexto.md).

## Épico: [#6669 — Motor de Descontos](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/6669)

## 1. Explicar a mudança de arquitetura de propagação

A Retaguarda não propaga mais campanha/desconto direto pra loja. Fluxo atual: Retaguarda só grava no banco da Retaguarda (card [#12405](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12405), Leonardo — já Ready for Dev); **Thalison (DB)** propaga pra loja de acordo com a necessidade.

## 2. Melhorias no sistema e passos futuros — conversa aberta com Arthur

Sem pauta fechada — deixar o Arthur trazer prioridades. Se for útil puxar assunto, já existem 2 itens de backlog 100% refinados esperando só priorização:

| Card | Título | Estimativa |
|---|---|---|
| [#11813](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/11813) | Interface para gerenciar destinatários de e-mail | 3 pts |
| [#11818](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/11818) | Relatório de performance de campanhas | 13 pts |

## Decisões (preencher após a call)

-
