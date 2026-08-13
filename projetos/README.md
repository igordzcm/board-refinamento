# Índice de Projetos

> Atualizado a partir de dailies, reuniões e do [dashboard executivo](dashboard-executivo.html). Cada linha é uma pasta de projeto — abra o `contexto.md` de cada uma antes de uma reunião sobre aquele projeto. Ver também [prioridades-sprint.md](prioridades-sprint.md) — visão de prioridades/planejamento (atrasado, em andamento, próxima sprint).

| Projeto | Prazo | Status atual | Arquivo |
|---|---|---|---|
| Dashboard CDS | — | Reunião com a Maria (12/08) descartou a premissa de trocar de fonte/eliminar o FTP — ela não mudou o WMS. Prioridade agora é replicar no sistema 8 mudanças que ela já fez na planilha (data, tabela de lojas, gráfico, rotas unificadas, PROCV, lead time ponderado); planilha ainda não chegou (Maria confirmou em 13/08 que segue esperando resposta da área dela); #11973 (FTP) segue sem decisão | [dashboard-cds/contexto.md](dashboard-cds/contexto.md) |
| Conciliação Fase 2 | Semana de 10/08 (US8-12) | 90% — bug de "linhas" (12/08) resolvido pelo Fernando; 2 bugs achados na demo do Ozéias (12/08) corrigidos e em teste desde a manhã de 13/08; bug novo de token quebrando permissionamento de rotas (achado 11-12/08) ainda sem fix. Reunião Diego↔Wagner hoje (13/08) às 14h pra validar o fluxo | [conciliacao-fase-2/contexto.md](conciliacao-fase-2/contexto.md) |
| Migração VARRet (lote 2) | — | 90%+ — **Lote 2 concluído pelo JB**, em code review/QA (Ozéias vai marcar call com JB pra subir tudo). JB já ativo em 13/08 no card #12484 (worker+e-mail do lote 1), depois volta pro Dashboard CDs | [migracao-varret/contexto.md](migracao-varret/contexto.md) |
| Motor de Descontos | — | Maior parte do escopo priorizado entregue em 22/06 sob Kauã; falta só a US5 (notificação automática às lojas na vigência), com escopo pendente de call entre Igor e Arthur. Em paralelo, Leonardo iniciou em 12/08 a arquitetura de sincronização nas lojas (#12405) e o time VAR 3.0 testa a integração pelo lado loja/PDV, sem gaps até 12/08 | [motor-descontos/contexto.md](motor-descontos/contexto.md) |
| Automação Planilha Fiscal | — | Entregue 22/06 (Épico #11103, 9 itens Done), mas em sustentação ativa — bugs recorrentes ("Pendente" falso-positivo, campo isentas/não-tributadas, "Loja 01/13 não bate"). Ozéias triando ao vivo ~40 cards de backlog do Kovalski (12/08), prazo até 14/08 pra decidir o que descarta vs. move pra Refinement | [automacao-fiscal/contexto.md](automacao-fiscal/contexto.md) |
| Gamificação (Roleta 3.0) | — | 40% — **decisão do Igor (13/08): volta a ser prioridade do Kauã**, T1-T10 movidos de Refinement pra Ready for Dev (planejamento pré-existente ao processo, considerado pronto). Achado técnico grande: já existe módulo `campaign-roulette` em produção que pode servir de base pra T5-T10. Seguem valendo: rework de QA em T1-T3, bloqueios externos de T8/T9, e a pendência de visibilidade do portal em homolog (Ozéias, 12/08) | [gamificacao/contexto.md](gamificacao/contexto.md) |
| Markdown / Remarcação de Preços | 15/08 (revisado) | 55% — sem atualização na última rodada, segue em homologação com débito técnico; roda fora do board do Retaguarda por decisão da área (atrito de QA já flagado em retro de Sprint 25) | [markdown-precos/contexto.md](markdown-precos/contexto.md) |
| Etiqueta Remarcados | — | Card #12506 (Doing, Sprint 26, Matheus Donato) — plano técnico N1/N2/N3 da tela de pendências reescrito em 12/08, com protótipo navegável publicado; 4 pendências (índices, DBA, medição de performance, dono da cobrança) rodam em paralelo, não bloqueiam o início do dev | [etiqueta-remarcados/contexto.md](etiqueta-remarcados/contexto.md) |
| VAR 3.0 — Padronização de Retornos HTTP | — | ⚠️ Sem card no Azure, sem menção em daily até 10/08 — confirmar com o time se ainda é prioridade antes de agendar qualquer reunião | [var3-http-status/contexto.md](var3-http-status/contexto.md) |
| Engine Fiscal — CNPJ Alfanumérico | — | Arquivo/referência — SHIPPED em 23/06/2026 (13 PBIs Done); mantido como padrão técnico reutilizável (função canônica de CNPJ, checklist DDL, dependência InvoiCy), não é projeto ativo | [engine-fiscal-cnpj/contexto.md](engine-fiscal-cnpj/contexto.md) |
| Tap on Phone + VAR 4G | Piloto desde 10/08 | Tap on Phone 95% / VAR 4G — segurança 92% — pilotos rodando juntos por decisão do Spin (não rodar mobile separado); risco aberto: instabilidade de cache no app da GetNet, escalada por e-mail | [tap-on-phone-var4g/contexto.md](tap-on-phone-var4g/contexto.md) |
| Overlimit (crédito na venda) | **Set/2026 (release VAR, antes do freeze)** — meta nova definida 12/08 | 🔴 5% — bloqueio de fundo (RPE sem resposta sobre credencial de teste, trava validação da limitação do Kong) segue sem novidade, mas escopo foi destrinchado em 12/08: tela de import Excel + distribuição pra loja igual à blacklist | [overlimit/contexto.md](overlimit/contexto.md) |
| SIGA | — | 3 frentes distintas (levantamento completo 13/08): **SSO no SIGA** em andamento com o Kovalski (#12499, meta 14/08); **Performance de Indicadores** (#10373) 🔴 bloqueado — 18 cards todos "To do", o que foi feito antes estava errado, conversas pra retomar em andamento; **Sustentação** (#7330) majoritariamente entregue, 1 item em Dev Review | [siga/contexto.md](siga/contexto.md) |

## Outras frentes ativas (ainda sem pasta própria)

Do [dashboard executivo](dashboard-executivo.html) de 10/08 — criar pasta quando alguma virar foco de reunião:

| Projeto | Squad | Prazo | Status |
|---|---|---|---|
| SSO / Keycloak | Retaguarda | Esta semana | 97% — só falta remover regra de prazo mínimo de troca de senha |
| SIGA · Indicadores | Retaguarda (Kovalski) | Sem data | 🔴 Bloqueado — sem fonte de dados confiável |
| Release fiscal (Engine + Portal Automação) | VAR 3.0 (Donato) | Piloto desde 03/08 | 95% |
| Pix pelo Pinpad | VAR 3.0 | — | 15% — entrou no meio da sprint |
| SmileGo (NeuroTech) | VAR 3.0 | — | 🔴 Bloqueado — ambiente de teste do fornecedor não funciona há 4+ semanas |
| Migração pra novo sistema | Tesouraria (Walter) | — | 55% — sem atualização, depende de decisão sobre incluir o GSX |

## Pastas de apoio

- [dailies/](dailies/) — cole as transcrições de daily (ou de reuniões transversais, tipo planejamento de sprint) aqui; usadas pra manter o dashboard, o `prioridades-sprint.md`, os `contexto.md` e o `minhas-pendencias.md` atualizados.
- [dashboard-executivo.html](dashboard-executivo.html) — dashboard vivo, atualizado a partir das dailies e reuniões.
- [prioridades-sprint.md](prioridades-sprint.md) — o que está atrasado/bloqueado, o que está em andamento, e o planejamento da próxima sprint (backlog priorizado, decisões de triagem). Complementa o dashboard executivo com uma visão mais acionável.
- [minhas-pendencias.md](minhas-pendencias.md) — pendências **pessoais** do Igor: reuniões a marcar, devolutivas que ele deve pra alguém, coisas que alguém prometeu entregar pra ele. Não é status de projeto — é a lista de "não posso esquecer disso". Consultar diariamente.
