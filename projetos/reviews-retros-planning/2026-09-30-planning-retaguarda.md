# Planning Retaguarda — Sprint 30 (30/09/2026)

> Planning do squad Retaguarda, ~19min. Transcrição: `Sprint Planning  (3).docx` (cabeçalho: 30 de setembro de 2026, 12:37). Participantes: Igor (PO), Danilo, Kovalski, JB, Kauã, Donato, Diego, Fernando. Vem da retro do dia anterior ([`2026-09-29-review-retro-retaguarda.md`](2026-09-29-review-retro-retaguarda.md)).

## Organização do board

- Igor arrastou tudo de "A para trás" para a sprint atual, para despoluir o dashboard. Pede foco em: **terminar o que está em andamento, retrabalhar o que está em rework e tirar o que der de code review**.
- QA (Danilo): pode testar tudo na coluna de QA **exceto** os de Donato (remarcação). Em homologação, tudo que está "Done em homologação" foi testado por ele; só os cards "de Victor" ele não tocou.
- Code review travado: dois cards do Siga (dependência do Valdo/Diego) e um card de JB (planilha com muitos itens) parado desde 29/07.
- Igor criou muitos cards no dia anterior (maioria de projetos específicos, todos em Ready for Dev) com ajuda do Claude; pede que todos leiam e corrijam descrição/critérios. Danilo vai revisar os cenários de teste.

## Por pessoa

- **JB:** card de engenharia reversa para identificar a **loja de cada depósito** (Conciliação de Depósitos) permanece com ele; fala com Ozéias para confirmar a abordagem (ver daily 28/09: identificação pela agência). Reenvio em code review. Card do **Overlimit RPA** (tela de upload no portal RPA): definições de 29/09 fechadas, "inserir o que existia na tabela", depois decide o uso dos campos; Gui fala com Thalison para criar a tabela no banco de testes.
- **Kauã:** card da **confirmação de rede local** na roleta (alguns usuários não aceitam a permissão e o navegador trava; portal deve avisar para reconfirmar). Gamificação: Ozéias teve reunião com área de negócio e criou card novo (#13452 e ajustes adicionais, mais devem vir do Diego/Ozéias e Jonas). **Subida prevista para domingo (04/10)**; Kauã e Danilo ressaltam que as **horas do mês já estouraram**. Igor: trabalhar normalmente nesta manhã para evitar correria quinta/sexta; confirma com Spin.
- **Danilo:** card de geração de link de acesso do SSO: se não houver mais o que fazer, move para Done; cenários de teste serão modelados com base na descrição.
- **Kovalski (SSO):** tem ~4 cards de SSO; o card "gerar link de acesso" foi mexido por ele ontem: o SSO terá uma versão "antiburro", refatorada em visual e funcionalidade, e ele já criou outro card (final 433); Danilo testa nesse card e faz um regressivo completo depois. **Siga, rework do Danilo:** o comportamento apontado já existe em PROD; Spin pediu uma réplica idêntica; Igor sugere **manter como está (idêntico a PROD)** e tratar os dois de uma vez se necessário, confirmando após ler o que Danilo enviou. Sem acesso à máquina de PROD do webhook (Donato sem acesso); o chamado depende de terceiros.
- **Donato:** engine travado (time estudando); **webhook** pronto, vai para HML, aguarda aprovação para subir com o fechamento. **Motor de descontos:** Fábio já fez as alterações de banco; Donato e Igor criam os cards no Slack.
- **Fernando e Diego:** os **dois projetos de Conexão**, um para cada: (1) **automatizar faturas de concessionária** (conta de energia por API para o portal Conexão) e (2) projeto de **envio de contas** (OC). Podem trabalhar juntos; Diego apoia Fernando com a configuração do fluxo existente.
- **Fila de 6 cards em Ready for Dev sem dono:** alguns de motor de desconto, um de gamificação (já com banco existente), um de infra (pedido do Spin, "mais chatinho"), uma revisão de segurança, e automação fiscal que ficou parada. Para quem ficar sem tarefa.

## Pendências / riscos

- Subida de gamificação no domingo com a equipe sem horas (risco de pressão).
- Acesso do Fernando ao projeto Conexão e do Donato à máquina de PROD do webhook.
- Rework do Siga: definir se vira bug ou fica igual a PROD.
