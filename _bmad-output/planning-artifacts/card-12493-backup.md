---
work_item_id: 12493
project: Var Retaguarda
work_item_type: Product Backlog Item
snapshot_date: 2026-08-11
snapshot_reason: "Backup antes de registrar causa raiz confirmada no código (descompasso pagination vs meta entre backend e frontend)"
url: https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12493
---

# Card #12493 — versão original (antes da edição de 2026-08-11)

## Metadados

| Campo | Valor |
|---|---|
| ID | 12493 |
| Tipo | Product Backlog Item |
| Esforço | 2 |
| Tags | Front-end; Planejamento Comercial; QA |
| Epic pai | #6640 — Portal de Retaguarda (Sustentação) |

## Título

> Contador de resultados dessincronizado em Auditoria de Propagação

## Descrição original

> **Como** usuário do módulo Planejamento Comercial (Campanhas › Auditoria de Propagação)
> **Quero** que o contador de campanhas encontradas reflita o número real de linhas exibidas na tabela
> **Para que** eu confie no resultado da consulta sem precisar contar manualmente as linhas
>
> O rodapé da tabela mostra "0 campanha(s) encontrada(s)" mesmo havendo 7 linhas de dados visíveis na tabela acima — o contador aparenta vir de uma fonte de dado diferente da que popula a tabela.
>
> _Achado do levantamento de QA (Danilo) de 05/08/2026._

## Critérios de Aceite originais

**Cenário 1 — Contador correto**
Dado que a tabela de Auditoria de Propagação exibe N linhas de resultado,
Quando o rodapé exibir a contagem,
Então o valor deve corresponder exatamente a N (ex.: 7 linhas → "7 campanha(s) encontrada(s)").

**Cenário 2 — Investigação da causa raiz**
Então o time deve identificar e alinhar a origem dos dois valores (o que popula a tabela vs. o que popula o contador), corrigindo a fonte incorreta.

**Cenário 3 — Estado vazio**
Dado que não há nenhuma linha na tabela,
Então o contador deve exibir "0 campanha(s) encontrada(s)" corretamente, sem regressão.

## Por que este backup existe

Investigação no código (`ConciliaçãoCaixaAPI` + `ConciliaçãoCaixaFront`) encontrou a causa raiz exata: o backend retorna `{ data, pagination: { page, limit, total, totalPages } }` (`campaign-propagation.service.ts:176-184`), mas o frontend lê `response.meta.total` (`campaign-propagation/index.tsx:26-31`). `response.meta` é sempre `undefined` — daí o fallback `|| 0`. O Cenário 2 original ("investigar causa raiz") deixa de ser necessário, já que a causa já está identificada.

Versão preservada aqui para referência.
