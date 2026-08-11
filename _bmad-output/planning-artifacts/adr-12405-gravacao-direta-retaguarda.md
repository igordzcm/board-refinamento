---
adr: AD-1
title: Gravação direta na Retaguarda substitui propagação síncrona para loja
card: 12405
epic: 6669
project: Var Retaguarda
date: 2026-08-11
status: Adotado
---

# AD-1 — Gravação direta na Retaguarda substitui propagação síncrona para loja

## Contexto

O Motor de Descontos propagava campanhas (criação/edição) diretamente para o banco da loja no momento da gravação. Essa escrita síncrona acoplava o fluxo de negócio da Retaguarda à disponibilidade do banco da loja e criava risco de inconsistência quando a escrita na loja falhava.

## Decisão

- **Binds:** o fluxo de criação, edição e exclusão de campanhas do Motor de Descontos.
- **Rule:** toda escrita de campanha (criação, edição, exclusão) grava direto e exclusivamente no banco da Retaguarda. Exclusão é soft delete — o registro é marcado inativo, nunca removido fisicamente. Falha de gravação na Retaguarda é reprocessada automaticamente até sucesso, sem perda do dado.
- **Prevents:** reintrodução de escrita síncrona da Retaguarda para o banco da loja dentro deste fluxo; qualquer código que passe a depender da disponibilidade do banco da loja para confirmar a gravação de uma campanha.

## Fora de escopo / propriedade

A propagação/replicação dos dados da Retaguarda para o banco da loja passa a ser responsabilidade de **outra equipe**, consumindo os dados já gravados na Retaguarda pelo mecanismo que ela definir. Este card e esta decisão não incluem esse mecanismo nem garantem SLA de chegada na loja.

## Cutover

Substituição direta: o fluxo antigo de propagação é desligado assim que o novo fluxo (gravação direta na Retaguarda) entra em produção. Não há período de convivência entre os dois fluxos.

## Consequências

- **Positivo:** a Retaguarda deixa de depender da disponibilidade do banco da loja para persistir uma campanha; simplifica o modelo de falha do lado da Retaguarda.
- **Atenção:** a equipe consumidora (loja) precisa ser avisada formalmente da mudança de contrato — ela passa a puxar/replicar os dados da Retaguarda, em vez de recebê-los por escrita direta.
- **Em aberto:** o mecanismo exato de reprocessamento (fila, job agendado, retry inline) fica a critério de quem implementa as tasks abaixo; esta decisão fixa o comportamento observável — reprocessa até sucesso, sem perda — não a implementação.

## Rastreabilidade

- Card: [#12405](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12405) (Var Retaguarda)
- Epic: #6669 — Motor de Descontos
- Tasks: #12500 (gravação direta), #12501 (soft delete), #12502 (reprocessamento), #12503 (cutover)
