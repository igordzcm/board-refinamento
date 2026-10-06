# Planning Retaguarda (16/09/2026)

> Planning de sprint do squad Retaguarda, ~11min. Transcrição: `Sprint Planning  (2).docx`. Participantes: Igor Diniz Camargo (PO), Diego Oliveira Andrade Rafael, Kauã Miguel da Cunha, Fernando Caetano de Lima, João Bernardo Ferreira Neto (JB), Gabriel Aparecido Kovalski Lopes, Matheus Gabriel Donato Alves, Danilo Santos Manzoli. Acontece no dia seguinte à Review/Retro (ver [`2026-09-15-review-retro-retaguarda.md`](2026-09-15-review-retro-retaguarda.md)).

## Distribuição por pessoa

- **Diego**: sem tarefa no momento. Aguardando card do Ozéias sobre "Siga"/algo relacionado a um "cargo" (Ozéias ainda não criou o card).
- **Kauã**: fechamento contábil "pronto, só testar algumas coisas a mais e fazer a devbox". Igor pergunta sobre um card antigo ("Estreito") que Kauã tinha esquecido completamente — vai retomar.
- **Fernando**: transferência Tesouraria "quase basicamente pronta" — falta devbox com Danilo e ajustes pequenos.
- **JB**: chegou atrasado (esqueceu de entrar apesar de já estar acordado desde 8h40). Trabalhando na tarefa "envio para aprovação" (nome em inglês) — espera terminar código e ficar testando essa semana, code review na semana seguinte. **Maria segue sem responder** (mesmo padrão recorrente desde início de setembro). Item novo "**Conciliação de Depósitos**" — Ozéias vai falar diretamente com "João" sobre isso, ainda não formalizado pro JB.
- **Kovalski**: "perdido" nos cards do Siga — Danilo vai testar futuramente. Descoberta: uma **componentização do Siga trava porque a máquina não alcança o IP do Valdo** — Kovalski cogita que vai precisar de refatoração pra remover essa dependência, quebrando em várias tasks novas. Deploy do Siga basicamente pronto, falta só o front. 2 bugs pequenos do Siga corrigidos: divergência de valores era **timezone** (Siga usa Cuiabá, Itava, São Paulo — corrigido) e a diferença de nº de lojas entre usuário/ambiente era esperada (DHML tem mais lojas que produção), não bug. **Apex Oracle segue sem solução** — quem tinha acesso ao UI já saiu da empresa, ninguém sabe o acesso; Daniel foi a Cuiabá só pra tentar homologar — "acho que não tem muito que a gente possa fazer" (mesmo achado da Review/Retro do dia anterior).
- **Donato**: parte de review do Motor de Descontos (SKU) concluída, subiu ontem, já no Pereira também. Nada mais pendente de motor de desconto por ora. Está tocando uma parte de "engine" que o Filipe (Fio) pediu. Aguardando retorno pro app de marcação; depois volta pras coisas do VAR que estavam passando pro time.
- **Danilo**: sem fala própria nessa planning além de confirmações.

## Cards novos e pendências de processo

- Igor criou **3 cards** com base em conversa que teve com Ozéias — pede pro Donato só confirmar se estão na coluna certa do board (sem necessidade de mais nada).
- Igor reconhece de novo a dificuldade de preparar a sprint com antecedência (mesma pauta da retro do dia anterior) — cogita deixar cards "livres" em Ready for Dev pra cada um escolher conforme for terminando o que está fazendo, em vez de pré-atribuir (ideia que o time já tinha sugerido antes) — possível reunião pra formalizar isso ainda essa semana ou na próxima.
- Retomando o card de **reset de senha de usuário** (JB) — parte de operadores já foi feita (era só ajuste de tela, funcionalidade já existia); a parte de **usuário** é mecanismo diferente e "voltou pra refinamento" — JB confirma que comentou isso no card, mas segue sem solução.
- **3 cards de Motor de Descontos** sendo finalizados pra Ready for Dev (revisão do Igor antes de liberar): combo com item único, corrigir e-mails, filtro de estado com seleção múltipla. Qualquer um do time pode pegar, não só o Kauã — Igor alerta pra cuidado porque o time de VAR 3.0 também mexe em Motor de Descontos em paralelo, "mas acho que nada que afete um ou outro".
- **Filipe (Fio) está em Cuiabá essa semana** — Igor avisa que vai ser mais difícil alinhar pendências com ele; vai verificar se ele tem algo pendente pro time antes de cobrar.

## Cruzamentos a verificar

- Card do Ozéias sobre "Siga"/"cargo" mencionado a Diego ainda não existe — confirmar quando Ozéias criar.
- Componentização do Siga bloqueada pelo IP do Valdo — vai gerar várias tasks novas; ainda sem cards formais no momento da planning.
- Reset de senha de usuário (JB) segue sem solução técnica definida, mesmo depois de voltar pra refinamento.
