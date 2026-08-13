# Daily Retaguarda — 12/08/2026

> Resumo (não transcrição literal), convertido de `RETAGUARDA - Daily (2025) q.docx` (raiz do workspace, movido pra cá). 8m36s. Não confundir com a reunião transversal de planejamento de sprint do mesmo dia ([2026-08-12-planejamento-sprint.md](2026-08-12-planejamento-sprint.md)) — são duas sessões diferentes no mesmo dia.

**Participantes:** Igor (PO), Diego, Kauã, Kovalski, Matheus Donato, JB, Fernando, Danilo, Leonardo, Spin.

## Por pessoa

- **Diego** — Investigou com o Danilo um erro de permissionamento no usuário de teste dele durante homologação da Conciliação Fase 2. **Causa raiz identificada: tamanho do token quebra a montagem do permissionamento das rotas do portal.** Sem fix ainda, só a causa raiz levantada. Terminou as últimas validações da Conciliação Fase 2; passou a acompanhar Leonardo/Kauã na implementação de testes unitários automatizados na pipeline do portal.
- **Kauã** — Muitos PRs atrasados (inclusive do Victor), corrigiu pipeline apontando pra branch errada (main em vez de develop). Criou padrões de PR pro portal (CLOUD.md, estrutura de pasta). Resolveu o job que não pegava algumas lojas — vai subir com o Leonardo hoje/amanhã.
- **Kovalski** — Terminou a arquitetura do Siga ontem; hoje começa o desenvolvimento com o Spin, meta sexta (14/08). Fortnite/licença pode liberar hoje — possível deploy do Rodrigo trocando o DNS do SSO. Corrigiu "erro 400" — não era problema do SSO; causa real era precisar retirar/separar grupos dentro do próprio Retaguarda (Leonardo detalha; pode ser a mesma frente do bug de "muitos grupos no usuário" que o Leonardo segue corrigindo em 13/08).
- **Matheus Donato** — Possível 4ª tela nas rotas de etiqueta remarcada, conversando com o Spin (relacionado ao card #12506).
- **JB** — Continuou Migração VarRet, presencial mas isolado. Faltam só mais 2 PRs, ambos já abertos.
- **Igor** — Confirma com o time o combinado com a Maria (Dashboard CDs) sobre a planilha.
- **Fernando** — Finalizou teste do campo de datas em algumas telas, dev boxes concluídos. Corrigiu **um bug de contagem de linhas** — mesma área citada depois pelo Ozéias na reunião de planejamento do mesmo dia como "bug na parte das linhas" (ver [conciliacao-fase-2/contexto.md](../conciliacao-fase-2/contexto.md)). Ficou sem teste no fim do dia, aguardando o Leonardo passar algo.
- **Danilo (QA)** — 2 cards de Conciliação precisam de teste com dado de área/prod (não dá pra testar local) — já sinalizado no card. Revisou cards de Ready for Dev, devolveu 1 pra refinamento (precisava de mais cenários). Fez devbox com Diego/Fernando; **achou o "problema dos tokens" junto com o Diego** (mesmo achado do Diego acima).
- **Leonardo** — GNRE resolvido — infra ajustou a rota no firewall depois de uma semana sem retorno. Trabalhando em config de teste do portal (CloudMD, com Kauã) pra reduzir o que sobe direto pra prod. Começando a config/arquitetura de sincronização do Motor de Descontos nas lojas (ver [motor-descontos/contexto.md](../motor-descontos/contexto.md)).

## Pontos de atenção

- **Bug de token quebrando permissionamento de rotas** — causa raiz confirmada (Diego+Danilo), sem fix ainda nesta data. Acompanhar em 13/08.
- Bug de "contagem de linhas" (Fernando) parece ser o mesmo citado pelo Ozéias na reunião de planejamento do mesmo dia.
- "Erro 400" do SSO não era do SSO — era grupos duplicados no Retaguarda (Leonardo corrigindo).
