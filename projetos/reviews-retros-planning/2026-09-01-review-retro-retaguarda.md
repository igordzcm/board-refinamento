# Review/Retro Retaguarda (01/09/2026)

> Review + Retrospectiva de sprint do squad Retaguarda, ~35min. Transcrição original em `Review e Retrospectiva de Sprint (1).docx` (raiz do workspace) — **não excluída** por padrão (só transcrições já digeridas podem ser removidas, e mesmo assim só sob confirmação). Participantes: Igor Diniz Camargo (PO), Fernando Caetano de Lima, Kauã Miguel da Cunha, João Bernardo Ferreira Neto (JB), Diego Oliveira Andrade Rafael. Ausentes citados: Danilo, Donato, Victor, Gabriel/Kovalski, Marcos.

## Comunicados importantes

- **Reunião amanhã (02/09), 17h–18h, com Ana Carina e Marcos** sobre testes de Gamificação — Igor vai encaminhar o invite pro JB/Kauã, participação opcional.
- **Reunião amanhã (02/09) com o Arthur sobre Motor de Descontos** — Igor encaminhou o invite pro Kauã também, participação opcional.


## Review — o que foi feito na sprint

- **Board (antes da review formal):** ~16 cards em Done; os que estão "em teste" são todos de Gamificação — Danilo ia testar hoje mas teve que sair, reteste fica pra amanhã (não é atraso, pois o dev foi todo concluído dentro da sprint). 2 em Verified aguardando Kovalski/Donato. Migração VarRet tinha 3 itens bloqueados — JB ia checar de manhã. JB sinalizou um erro novo na "Pereira", vai investigar e depois passa card pro Igor. Card #12484 criado pra próxima sprint. Card de "envio de contas" (do Aline) em ambiente de dev, aguardando Danilo testar. Card testado com Ozéias e o time de expansão desde dia 21 — confirmado OK.

- **JB (João Bernardo):** trabalhou em Migração Lote 2 e avançou bastante na Dashboard de CDs (não conseguiu falar com a Maria hoje). Ozéias confirmou que o time de expansão testou praticamente tudo e funcionou perfeitamente, gostaram das telas. Migração VarRet: concluída, tudo certo (só uma pendência que já é do Thalison, não da Retaguarda).

- **Diego:** projeto de mapeamento de termos pra integração com Oracle — corrigido, campos agora obrigatórios; projeto entra em sustentação. **Conciliação Fase 2** foi o destaque conturbado da sprint: nasceu de um mapeamento urgente feito pelo Wagner (lado Versil), prazo original de 3 meses cortado pra 2 dias, força-tarefa com ajuda do Kauã, Léo e Higuinho. Primeira entrega foi validada com a área, mas a área apontou que a implementação estava errada nas regras de negócio (não no código) — precisou de outra rodada urgente de levantamento de requisitos. No fim, entrega boa foi feita, área validou e aprovou a versão atual.

- **Fernando:** sprint tranquila — subiu ontem os ajustes/bugs pequenos, tudo em produção. Focou em testes (API); Leo configurou os testes na pipeline, já rodando.

- **Kauã:** apoiou o Diego na Conciliação Fase 2 (correria, mas deu certo); usou o tempo restante da sprint pra fazer deploy da Gamificação, que já está em produção — passado pro Ozéias e pro Danilo, tudo em QA (TRM e gamificação em si).

- **Igor (fechamento da review):** parabenizou o time pela entrega sob pressão — destacou que não foi só entregar, mas entregar com qualidade, com correções rápidas de planejamento/código. Destacou também a Gamificação (rápida, mas bem entregue) e a **conclusão da migração VarRet** (projeto grande e tecnicamente desafiador, totalmente aprovado e em uso). Elogiou os testes automatizados do Portal (trabalho do Fernando) — pedido antigo do time.

## Retrospectiva

**O que foi bem:**
- Time muito unido em momentos de urgência — lidou bem com a sequência de projetos chatos da sprint (Conciliação Fase 2 principalmente, também a migração VarRet).
- Code review mais rápido — Igor percebeu a melhora desde que voltou de férias, menos coisa travando, inclusive em tarefas pequenas.
- Kauã adotou a sugestão do Spinter (retro anterior) de ter horário fixo pra revisar PR (11h todo dia); Léo voltou a ficar mais próximo do código no último mês e passou a ajudar a revisar PRs do Fernando, JB e Diego também — não ficou só na mão do Kauã.
- Entrega grande e bem executada: GMUD imensa (API com quase 600 arquivos, front com quase 500) entregue corretamente. Danilo teve papel importante além de testar — deixou processo automatizado e documentado, guiando o time em detalhes da migração VarRet 2.

**O que não foi bem:**
- **Mudança de prazo pra um cronograma quase insustentável** (Conciliação Fase 2) — ponto que Igor reforçou de propósito pra registrar na transcrição e levar pra cima. Nasceu errado, foi apresentado pra área, a área reprovou as regras de negócio, e precisou ser remapeado às pressas (uma tarde inteira) pra reapresentar no dia seguinte.
- Ponto positivo dentro do problema: Diego documentou tudo nos commits/PRs da API ("conciliação fase 2" e "conciliação fase 2 refactor"), servindo de base pra investigar futuramente onde a implementação falhou.
- Discussão em aberto (card de retro): **"Ser mais firme em decisões difíceis"** — Diego colocou que, quando a pressão pra acelerar a Fase 2 veio de cima, a liderança (Igor/Ozéias/Léo) deveria se posicionar mais firme, mesmo gerando atrito, defendendo o plano original combinado com o time. Igor concordou que é um ótimo ponto, mas explicou que nesse caso específico o time tentou negociar, e ainda assim não conseguiu barrar — a decisão veio de cima sem espaço pra mais discussão. Reconheceu que vale tentar mudar a abordagem de negociação numa próxima vez, mas foi transparente que nem sempre vai dar pra "vencer" esse tipo de imposição.
- Como ponto positivo recente citado no meio dessa discussão: as interferências do Diego pedindo prioridade fora do board diminuíram — agora ele pede prioridade e o time consegue encaixar na próxima sprint em vez de furar a fila.
