# Migração VARRet — contexto geral

> Arquivo de contexto do projeto. Atualizado a partir do backlog técnico original, de dailies e do dashboard executivo. Ler antes de qualquer reunião sobre este projeto.

## O que é

Migração de funções do VAR Retaguarda legado para o Portal Nova Retaguarda, por lotes de funções (Financeiro/Auditoria/ADM). Cada função vira endpoints novos (às vezes lendo direto o banco da loja) + tela no portal, eliminando a necessidade de acessar o sistema legado.

Épico: **[#11985 — Migração VAR Ret](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11985)** (Var Retaguarda). 32 itens ativos em Sprint23-26: 10 Done, 7 Verified, 10 To Do, 3 In Test, 1 Approved, 1 Rework.

## Dono

**JB (João Bernardo Ferreira Neto)** — depois de fechar o lote 2 deste projeto, volta para o Dashboard CDS.

## Lotes (do backlog técnico original, 151h em 3 sprints)

| Lote | Funções | Status |
|---|---|---|
| Lote 1 | Funções 1 (Demonstrativo de Caixa), 3 (Movimento de Caixa e Crediário), 16 (Listagem de Itens Vendidos), 21 (Contas Bancárias), 35 (NSU "Mais Informações") | **Entregue e testado por Danilo** |
| Lote 2 | Funções 31 (Troca de Mercadoria), 0 (Opção de Depósito da Loja), Caixas em Aberto, 9 (Vincula NSU Depósito), 79 (Consulta NFe) | **Em andamento** |
| Sprint 3 | QA e homologação (plano de testes, testes funcionais L1/L2, testes de integração, homologação com Financeiro/ADM, correções pós-homologação) | Conforme lotes acima avançam |

## Status atual (12/08/2026, via reunião de planejamento de sprint)

> Fonte: [`../dailies/2026-08-12-planejamento-sprint.md`](../dailies/2026-08-12-planejamento-sprint.md).

**Lote 2 concluído pelo JB — agora em code review e QA.** Igor confirmou pra Ozéias: "o lote 1 já tá pronto, o lote 2 ele acabou, terminou esses dias, tá tudo em processo de code review e QA." Ozéias vai marcar uma conversa direta com o JB pra "subir tudo" (não tinham conseguido se falar na sexta anterior).

**Próxima tarefa do JB, já combinada com o Léo:** pegar tudo que já estava pronto no **lote 1** e que ainda exporta Excel/PDF direto na tela, e migrar pro padrão **worker + envio por e-mail** (mesmo padrão já usado na Automação Planilha Fiscal — `ExcelGenerationQueue`/`BullExcelGenerationQueue` + `ExcelNotifier`/`GraphExcelNotifier`, ver card **#12484** no board de refinamento do Var Retaguarda, já refinado e faltando só estimativa). Depois disso, o JB volta pro Dashboard CDs (que também tem "umas coisinhas" pra ele corrigir, mas nada grande — ver `../dashboard-cds/contexto.md`).

## Bloqueios e pendências

- **Instabilidade recorrente do banco em homolog** — bloqueio recorrente citado nas dailies anteriores (10/08), impacta testes do lote 2. Não mencionado na reunião de 12/08 — status não confirmado, mas o lote 2 seguiu até QA, então pode ter sido contornado.
- **Revisão de código do lote 2** — concluída/em fechamento; Ozéias vai marcar conversa com JB pra subir tudo.
- **Dependências originais do backlog**: ETL da Função 21 dependia de alinhamento com Fábio/Gustavo (Sprint 1); Função 0 dependia de alinhamento de escopo com Fábio/Taunay; Funções 31 e 9 exigem credenciais de acesso ao banco da loja em homolog.

## Reuniões

Nenhuma reunião dedicada registrada ainda — status vem da reunião de planejamento de sprint de 12/08 (transversal, não específica deste projeto).

## Próxima atualização

Preencher aqui: se a conversa Ozéias↔JB aconteceu e o lote 2 subiu; se a migração do lote 1 pro padrão worker+e-mail (card #12484) começou; e se a instabilidade do banco em homolog (10/08) foi de fato resolvida ou só contornada.
