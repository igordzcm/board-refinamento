# Retro + Planning adiantada — Retaguarda (14/08/2026, sexta)

> Sprint 26 retro + planejamento da sprint seguinte. Transcrição bruta em `2026-08-14-retro-planning-retaguarda.docx`. Participantes: Igor (PO), Kauã, JB, Fernando, Danilo (QA), Léo, Diego, Kovalski.

## Retro — o que foi bem

- **Léo organizou o repositório do portal** — limpou pipe/CI, padronizou decisões técnicas: toda decisão técnica que impacta o portal agora vira automaticamente uma **DR (decision record)** rastreada em backlog próprio.
- **Conciliação Fase 2 entregue** — Diego + Kauã entregaram em ~2 semanas algo estimado em 3 meses. Passou com Ozéias e Wagner, bem avaliado, só pequenas correções. "Nosso lado pronto agora com a área."
- **Fila de code review destravada** — Kauã revisando em horário fixo todo dia, DB ajudando, Diego revisando PRs — fila visivelmente menos travada.

## Retro — o que pode melhorar / padrão pra todo card

Igor apresentou o novo processo de refinamento via skill (Cenário+GWT, rótulo, nota técnica) e pediu input do time sobre o que todo card deveria ter:

- **Bugs**: sempre com prints/evidência do estado atual e do esperado após correção — menos genérico. Danilo já usa esse formato ao criar cards; Igor reconhece que falta mais prints nos que ele mesmo escreve.
- **De onde vem a informação técnica**: JB pediu pra sempre citar se o bug foi analisado em qual branch/ambiente (dev, homolog, prod) — evita a IA (ou o próprio Igor) apontar o módulo errado por engano (aconteceu no #12484: achou "invoice" quando o certo era "store invoice").
- **Impacto/a quem afeta**: sugestão de nomear quem é impactado pelo card (ex.: "facilita o trabalho das meninas do financeiro") — a maioria dos cards já traz isso na história.
- **Correlação/dependência entre cards**: ideia (não implementada) de um "mapa mental" das dependências entre cards, tipo o que já existe pra RPG — ajudaria tanto o time quanto a IA a identificar que um card só pode avançar depois de outro.
- **Evidência de teste com dado real**: sugestão de sempre registrar que foi testado com tal loja/CPF/dado específico, pra ter comparativo se surgir um bug depois.
- Igor confirmou o plano de, no futuro, ter o próprio **time revisando os cards antes da planning** (hoje só o Danilo faz essa revisão), não só a IA.
- Quando fizer sentido (tela nova ou mudança visual grande), sempre fazer um mock/protótipo — mesma regra já formalizada no `refinement-checklist`.

## Planning — alocação por pessoa

- **Kauã**: Conciliação Fase 2 finalizada → **100% foco em Gamificação**. Só volta pra Conciliação se surgir problema junto com o Diego. Moveu todos os cards de Gamificação de "Bloqueado" pra "Ready for Dev".
- **Diego**: segue apoiando Conciliação Fase 2 (correções/apresentações). A partir de segunda (18/08) retoma o projeto SIGA — **Performance de Indicadores** — bloqueio de fonte de dados já resolvido pelo Ozéias.
- **Fernando**: focus 1 = sustentação do portal (pequenas correções conforme surgem). Focus 2 = **projeto grande de automação de testes do portal**, estruturado por Igor em 8 fases com subtarefas por módulo (ver `board-refinamento/referencias/roadmap-testes-portal-retaguarda.md`) — trabalha nisso entre correções.
- **JB**: Migração VarRet segue como foco (exportações lote 1 → worker, já em code review). Depois volta pra **Dashboard CDs** (ainda sem a planilha atualizada da Maria nesse momento — Igor vai criar os cards de qualquer forma pra JB ter onde trabalhar).
- **Danilo**: sem mudança de foco — QA de tudo, retoma testes de indicadores com Diego semana que vem.
- **Ozéias**: tem tarefas de backlog pra reescrever, pode continuar.
- Card antigo "upstream" mencionado pra Kauã trabalhar se sobrar tempo (não resolvido, ninguém tem certeza do status).
- Cards de Conciliação já testados (QA) e aprovados foram movidos de QA pra Dev Box pra reteste, já que subiu tudo pra ambiente de homolog ("UAT").

## Fontes

Ver também os digests diários 14–24/08 em `2026-08-14-a-24-digest-retaguarda.md` e `2026-08-14-a-24-digest-var3.md`.
