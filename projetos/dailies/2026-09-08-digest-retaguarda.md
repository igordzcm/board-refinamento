# Digest — Daily Retaguarda, 08/09/2026

> Daily curta (8m54s). Fonte: `RETAGUARDA - Daily (2025)  (5).docx` (participantes: Igor, Filipe de Lacerda, Kauã, Diego, Fernando, Kovalski, Donato, JB, Danilo, Franklin, Sola — os 3 últimos sem ponto de conteúdo claro, ver nota no fim). Squad estava presencial na sexta-feira anterior (04/09).

## Conciliação Fase 2 — novo caso + GMUD hoje (Diego)

Sexta (presencial), Diego pegou uma task passada pelo Ozéias: melhoria no "aprovar divergências" / "gerenciar perda" — caso específico em que a analista de conciliação adiciona uma divergência manualmente, cai como "operador vazio" e não estava sendo mapeado nesse caminho. Juntou esse caso à **task #12887** (mesma tela). Hoje de manhã: testando o #12887 pra cobrir tudo e preparar a **GMUD prevista pra hoje (08/09)** — sem mais detalhe na transcrição sobre o que mais compõe essa GMUD.

## Bug de permissionamento/usuário do Danilo — ainda sem fechar

Sexta à tarde, Diego investigou com Kauã e JB o problema de usuário do Danilo — "aparentemente tem relação com os grupos dele", ficou pendência pra concluir. Kauã confirma o mesmo: "o Danilo... o dele está muito quebrado, mesmo que a gente apaga, reseta, troca grupo lá, fica permissionamento errado". Danilo (ver abaixo) confirma que isso o travou boa parte de sexta. Não fica claro na transcrição se é o mesmo bug já reclassificado como **#12514** (bug de tamanho de token / permissionamento, owner Leonardo) ou uma recorrência nova — vale conferir.

## Job noturno (Kauã)

Sexta o job não rodou — motivo diferente do travamento de TTL 24h já visto antes ("Bools"). Limpou o Bools, investigou e fez fix pra subir na próxima. Também pegou reworks pequenos apontados pelo Danilo (itens de "não mostrar lojas"). Hoje: task rápida de "ajustar o comprimento do menu"; de manhã o portal caiu (travando conexão no banco, entupindo a API) — precisou reiniciar a API. Igor reforça: Kauã deve focar em fechar o rework de Conciliação, só desviar se surgir hotfix urgente.

## Doc Pendentes / Engine — Kovalski confirma que começa hoje

Kovalski: Ciacon aguardando máquina. Sexta fez onboarding do Diogo (força-tarefa de configuração de Portal Retail + Portal de Gestão de Insumos — máquina Windows, projeto em APX Oracle, "dor de cabeça", mas integrado; falta só o que o Daniel apontar). **Hoje ele confirma: "devo pegar as coisas de doc pendentes pra fazer da engine"** — isso resolve a ambiguidade deixada em aberto no digest de 01-03/09 (lá era só um "talvez"; agora é uma ação do dia). Cruza com [`../engine-doc-pendentes-migrate/contexto.md`](../engine-doc-pendentes-migrate/contexto.md), que hoje registra "nenhuma reunião formal ainda" e trata o levantamento como sem dono de execução confirmado.

## App de remarcação (Donato) — Ozéias finalmente respondeu

Donato segue sem pendência formal, esperando o Ozéias desde a semana passada — "tá tranquilo". Igor: conseguiu falar com o Ozéias na sexta, que extraiu do WhatsApp toda a conversa que tiveram sobre remarcação; Igor vai revisar pra poder criar os cards. Cruza com [`../etiqueta-remarcados/contexto.md`](../etiqueta-remarcados/contexto.md) (que ainda trata essa frente do Donato/Ozéias como "força-tarefa a confirmar se é dentro do mesmo épico #12428 ou trabalho paralelo").

## Dashboard CDs — Maria segue sem resposta (JB)

JB trabalhou no PR do Diego (a revisar) e no "demonstrativo do caixa" — verificou o item de exportar Excel/PDF e concluiu que já está tudo correto, nada a fazer. Ainda não conseguiu falar com a Maria — "sumiu" — vai tentar mandar mensagem hoje. Igor reforça pra ser incluído quando a reunião com ela for marcada. Padrão que se repete desde as dailies anteriores (ver [`2026-09-01-e-03-digest-retaguarda.md`](2026-09-01-e-03-digest-retaguarda.md)).

## Outras notas

- **Fernando** — sexta (presencial) trabalhou pendências com o Danilo e pegou tarefas simples passadas pelo JB; segue nelas hoje.
- **Danilo** — sexta não conseguiu avançar muito por causa do próprio bug de usuário (acima). Hoje achou forma de testar as tasks (rodando normal), focando primeiro no portal retaguarda antes das tasks do Diego (Dev Conexão). Fez Devbox com o Fernando na sexta. Aguardando resposta de documentação do Gui sobre "visu" pra seguir. Ainda deve a Igor o relatório de hotfixes do portal (pendência que já vinha de antes).
- **Franklin / Sola** — presentes, sem ponto de conteúdo recuperável na transcrição (fala do Franklin saiu garbled — "and I passed a look"; Sola só se despede). Não incluído como achado por falta de conteúdo claro.

## Cruzamentos a verificar

- Bug de permissionamento do usuário do Danilo (recorrente) — confirmar se é o mesmo #12514 (já reclassificado, owner Leonardo) ou um caso novo/recorrência.
- Task #12887 (Diego) é card novo não documentado em [`../conciliacao-fase-2/contexto.md`](../conciliacao-fase-2/contexto.md) — o contexto atual só cobre o pacote RH (#12800/#12808–12811) já aceito em 31/08; vale confirmar se #12887 é módulo separado (Gerenciar Perdas/divergências) e o que mais sobe na GMUD de hoje (08/09).
