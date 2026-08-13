# Markdown / Remarcação de Preços — contexto geral

> Arquivo de contexto do projeto. Atualizado a partir do board técnico consolidado (TF-01 a TF-10) e do dashboard executivo. Ler antes de qualquer reunião sobre este projeto.

## O que é

Sistema de Gestão de Markdown (Fase 2) — ferramenta de central planning para remarcação de preços: motor de cálculo (preço final, valor de markdown, margem), telas de Overview (matriz ST × Idade) e Indicadores, tela de Seleção com edição de desconto individual/em lote, camada de sugestões para o papel Membro, aprovação/efetivação pelo Central Planning e exportação da Carta de Oferta no layout da Tela 0012 do Logix.

Módulo NestJS em `ConciliacaoDeCaixaAPI/src/modules/price-markdown/` + páginas React em `ConciliacaoDeCaixaFront/src/pages/business-planning/price-markdown/`. 10 tasks consolidadas (TF-01 a TF-10, a partir de 15 histórias de usuário originais).

**Não confundir com "Etiqueta Remarcados"** ([#12428](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12428) no Azure) — são dois projetos diferentes que só compartilham a palavra "remarcação": este aqui (Markdown) é a ferramenta de **planejamento central** de preço/desconto por família de produto; o outro é a **tela de pendências de etiquetas físicas em loja** (chão de loja, impressão de etiqueta). Ver `projetos/etiqueta-remarcados/contexto.md`.

## Dono

**Victor de Moraes** (interno) + **Hudá** (PO externo, Verzel).

## Status atual (12/08/2026, via dashboard executivo)

**55%** — sem atualização na última rodada. Segue em homologação com débito técnico. **Prazo revisado de 24/07 para 15/08/2026** (marco listado no dashboard executivo como "Prazo revisado da Remarcação de Preços").

## Particularidade de processo — roda fora do board do Retaguarda

Este projeto roda **fora do board Azure DevOps do Retaguarda por decisão da área** (conduzido por Victor com a área de expansão). Isso já foi **flagado como ponto de atrito conhecido em retro de Sprint 25**: rodar fora do board principal gera confusão de QA — o time de QA do Retaguarda não tem visibilidade padrão sobre o que está em teste neste projeto, diferente do que ocorre com os demais épicos do board.

## Estrutura técnica (TF-01 a TF-10)

| Task | Escopo | Bloqueadores (`D-XX`) |
|---|---|---|
| TF-01 | Bootstrap do módulo (feature flag, seed) | `D-NOVA-1` (nome do Assignment) |
| TF-02 | Autenticação e autorização por papel/família | — |
| TF-03 | Ingestão da Matriz de Itens (DW Gold) | `D-08`, `D-17`, `D-NOVA-2`, `D-NOVA-3` |
| TF-04 | Motor de cálculo com reconciliação (já convertida em Story BMAD `2.5.motor-calculo.md`, Approved) | `D-03`, `D-12`, `D-15` |
| TF-05 | Overview + Indicadores | `D-08`, `D-17` |
| TF-06 | Seleção — listagem, filtros, export Excel | `D-17` |
| TF-07 | Seleção — edição de desconto, verba, submissão | `D-03`, `D-07`, `D-13`, `D-14`, `D-19` |
| TF-08 | Camada de sugestões (papel Membro) | `D-04` (Should — condicional) |
| TF-09 | CP — aprovação, efetivação, exportação Logix | `D-02`, `D-10`, `D-14` |
| TF-10 | Trilha de auditoria e histórico | — |

## Bloqueios e pendências

- Confusão de QA por rodar fora do board do Retaguarda (retro Sprint 25) — sem solução definida.
- Débito técnico acumulado em homologação (citado no dashboard, sem detalhamento).
- Decisões críticas em aberto no plano técnico (`D-NOVA-1/2/3`, `D-03`, `D-07`, `D-10`, `D-12`, `D-14`, `D-15`, `D-19`) — cada uma trava uma ou mais tasks; ver `docs/board/00-open-decisions.md` no repositório de origem para detalhamento completo.

## Reuniões

Nenhuma reunião registrada ainda.

## Próxima atualização

Preencher aqui depois de uma atualização de status com o Victor: o que mudou desde a última rodada, se o prazo de 15/08 vai se confirmar, e se o atrito de QA (projeto fora do board) foi endereçado.
