# Review e Retrospectiva Retaguarda — Sprint 29 (29/09/2026)

> Review + retro do squad Retaguarda, 47m54s (início 19:11 no horário do cabeçalho). Transcrição: `Review e Retrospectiva de Sprint (2).docx`. Participantes: Igor (PO/facilitador), Kovalski, JB, Diego, Fernando, Kauã, Danilo (QA); Donato e Filipe de Lacerda não aparecem falando. Quadro de retro: "Retrospectiva Sprint 29" (link no chat, conteúdo dos post-its não está na transcrição, só o que foi falado). Sequência: [`2026-09-30-planning-retaguarda.md`](2026-09-30-planning-retaguarda.md). Anterior: [`2026-09-15-review-retro-retaguarda.md`](2026-09-15-review-retro-retaguarda.md).

## Review — o que cada um entregou

- **Kovalski (infra/DevOps, SSO, Siga):** mudança do **SSO e do DNS** concluída (acabou o "sso-hub", só SSO Avenida). Siga mexido de novo, "se Deus quiser vai até homologação" (bloqueio de Ciacom tomou dias). Desenhou a **nova arquitetura do back office**: tirar todos os nginx, ficar só com Traefik e uma única máquina de Portainer (Swarm), organizando managers/workers. Primeiro passo: **certificado digital via pipeline** com Azure DevOps (deployment group, tags HML/PROD, template de pipeline) e trouxe a biblioteca de UI do Siga para dentro do Azure, aplicada no Siga HML e público. Terminou a PoC dias antes por limitação de permissão.
- **JB (reenvio):** duas semanas inteiras no **reenvio para aprovação**: ao mexer na conciliação depois de aprovada, agora fica registrado o que foi alterado e, dependendo do que mexeu, volta para aprovação com histórico. Código "foi de boa", o que mais demorou foi testar (muitos cenários; testes Playwright no front e muito teste manual). Em code review; agora migrando uma tabela própria para usar o **audit log** e removendo magic strings no front e na API.
- **Diego:** cards de portal, Conexão e Siga. **Conexão e Siga completaram todo o ciclo**, subiram na GMUD de 28/09. Conexão: telas de revisão reformuladas com **categorização das linhas da fatura direto no front** (mais confiança antes de chegar ao Oracle) — "finalmente uma solução boa". Siga: novo **cargo** no lotacionograma replicado em exports/imports. Portal: **menu lateral do módulo de conciliação** agrupado em tabs, primeira tela a ser enxugada, pensado para outros módulos depois.
- **Fernando:** cards pequenos do Ready for Dev: substituição do saldo da loja (CPF do responsável, facilidade de trocar o arquivo do termo assinado, manter estado do menu lateral ao recarregar). Passou a semana sem card próprio.
- **Kauã:** sprint que ele considera de pouco progresso por falta de organização para passar à devbox; foco em **fechamento contábil (Oracle)** e **gamificação** (muito vai-e-volta por critérios atualizados) e em problemas da **conciliação** (job que não rodava, TTL travado após mexer no Kong). Subiu na GMUD grande de um terceiro (Vitor), que classifica como arriscada; código dele "não estava legal" e Kauã acredita que não será corrigido.
- **Danilo (QA):** sprint mais rigorosa nos testes, recebeu feedback construtivo; vai atuar de nova forma com cards em Ready for Dev (ampliar cenários, não só caminho feliz), combinando com os QAs; quer mostrar o levantamento a Igor.

## Retrospectiva — o que foi falado

**Bom:**
- Fila de code review mais rápida (5 votos). Diego citado como quem mais mudou o ritmo de revisão.
- **Uso de IA em code review:** balanço positivo; consenso de que revisão própria dos padrões segue válida e a IA entra como auxiliar para achados mais profundos; lembrar de rodar nos dois lados (back e front). PR muito grande (remarcação, do Vitor) é impossível de revisar inteira.
- **Cards bem escritos** fizeram diferença (Diego integra o card com MCP do Azure e quase não sai código errado). Igor atenta para não escrever "nota técnica" quando não tem o código do repositório.
- Elogios a Diego e Kauã pela entrega; "muito rework do lado do Danilo, muito bug encontrado, correção bem feita".

**Ruim / a melhorar:**
- **Falta de cards para trabalhar:** Fernando ficou a semana inteira sem card próprio (Diego em parte também). Igor está criando **cerca de 36 cards de refinamento** (fora 3 que não vai usar) para ter fila e já ter o que puxar, mas reconhece que está difícil planejar duas semanas fechadas.
- **Kovalski sobrecarregado e concentrado em DevOps:** pediu ajuda para absorver SSO (API Nest + front React, "não é um monstro"); problema: PR sem revisor que entenda a regra de negócio. Danilo sugeriu envolver JB. Igor propõe tentar que alguém trabalhe junto com ele ou que cards de SSO entrem em fila geral.
- **QA pede identificação do que vai testar:** cards na coluna de QA que não são dele sujam a fila; pede indicar em comentário/descrição quem testa.
- **Crítica pública do Kauã sobre o QA ir atrás do código:** Kauã retirou a crítica, reconhecendo que acaba ajudando para reproduzir bugs, e pediu desculpas ao Danilo.
- Acesso: máquina do RPA/"CA" segue desabilitada após a virada; Kovalski diz que agora está mais difícil e que é chamado.

## Decisões e ideias de processo

- **Sprint 30:** cards disponíveis em Ready for Dev sem dono, para quem ficar sem tarefa puxar; projetos grandes já em nome de cada dev (os dois de Conexão para Diego e Fernando, SSO sob demanda). Igor quer opinião do time sobre preferir fila sem nome ou pré-atribuição.
- **Estimativa:** Igor usa **Fibonacci de esforço** (não horas); JB sugere poker planning, limite de 13 para quebrar card, e "leilão de horas". Igor quer testar na sprint atual começando pelo card mais fácil como referência. Sem decisão formal.
- Itens a verificar: um card antigo (número citado como "1254", incompleto) que Kauã diz já ter resolvido e que pode ser removido.

## Resumo

Sprint 29 fechou com SSO em produção, ciclo completo Siga+Conexão, reenvio em code review, nova arquitetura de DevOps desenhada, mas com o gargalo claro de **falta de backlog pronto**, **dependência do Kovalski** e **instabilidade de ambiente/infra** (Kong, VPN, acessos). Próximo passo: [`planning de 30/09`](2026-09-30-planning-retaguarda.md).
