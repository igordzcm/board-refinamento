# Digest — Dailies Retaguarda, 28/09 a 02/10/2026

> Síntese de 4 dailies do squad Retaguarda: 28/09 (seg), 29/09 (ter, 7m21s), 01/10 (qui, 10m42s) e 02/10 (sex, 8m48s). Em 30/09 não há daily (dia de planning, ver [`../reviews-retros-planning/2026-09-30-planning-retaguarda.md`](../reviews-retros-planning/2026-09-30-planning-retaguarda.md)); em 29/09 há também review/retro à tarde ([`2026-09-29-review-retro-retaguarda.md`](../reviews-retros-planning/2026-09-29-review-retro-retaguarda.md)).
> Fontes: `RETAGUARDA - Daily (2025)  (18).docx` e `(22).docx` (mesma daily de 28/09, **duplicata exata**, digerida uma vez; o cabeçalho diz 1h14m30s mas a fala termina em ~10min, provável gravação deixada aberta), `(23).docx` (29/09), `(24).docx` (01/10), `(25).docx` (02/10). Datas confirmadas pelo cabeçalho interno, não pelo sufixo do arquivo. Participantes: Igor (PO), Diego, Fernando, Kauã, Kovalski, Donato, JB, Danilo (QA), Filipe de Lacerda, Francisco Sola e, só em 02/10, Franklin.
> A transcrição automática tem muito ruído; trechos incertos estão marcados.

## Siga / SSO — SSO em produção, queda de rede/DC na segunda, PoC de pipeline pronta

- **28/09 (Kovalski):** "fizemos o deploy do SSO ontem. Deu boa": quem cadastrou OTP no sso-hub já pode usar o SSO Avenida e trocar senha. Houve uma "mini warroom": caiu a rede e, em consequência, o DC de Osasco 3. Com o Keycloak atualizado agora é possível apontar mais de um DNS (apontados 1 e 2; tentará o 3 quando arrumarem). Serviço ficou fora cerca de 1h30; já voltou.
- **29/09:** PoC da pipeline de certificado digital **finalizada**; atualizou o Siga público e o Siga HML com a nova versão. Pretende mostrar na retro, diz que é fácil integrar os outros portais e que "falta 44 dias" (para o certificado digital vencer, segundo a fala). Pede a Igor que crie tasks.
- **01/10:** tarefa de remover o banco de usuários/grupos do Keycloak quase pronta ("não vai existir mais banco para usuário e grupo, vai usar direto a API"), sobe para HML em minutos; depois pega a refatoração visual. **Quem perder o TOTP agora só resolve por chamado ao N1**; senha pode ser resetada pelo portal.
- **02/10:** refatoração visual do SSO concluída ("basicamente tudo mudou"); nova feature de **reset de TOTP** sem passar pelo Keycloak; cadastro completo (CPF/endereço) no Keycloak. Vai apresentar ao Spin hoje e fazer devbox com Danilo. **Bug aberto:** Gui e Lacerda tentaram trocar a senha e deu erro de LDAP, com data de troca de senha em 1600; Kovalski investiga e vai repassar a quem cuida do AD. A máquina 10.150.x.x citada (mesma do webhook) segue inacessível, ninguém sabe a senha ("na batalha há dias").
- **Ciacom:** em 28/09 segue **blocked**; em 29/09 o fornecedor respondeu o chamado, mas sem previsão ("a gente acessa a máquina, roda dois comandos, a máquina morre, volta, morre").
- **Siga, rework:** 28/09 Kovalski devolveu a correção do Siga para teste; 29/09 Danilo achou novo impedimento ("coisa de registro") e devolveu para rework. Em 30/09 houve discussão sobre ser bug ou comportamento idêntico ao de produção (ver planning).
- **Siga/Conexão, deploy:** 28/09 Diego informa que o que estava programado para subir não aconteceu e ficou aguardando; em 29/09: "ontem à noite teve a GMUD do Siga e do Conexão, deu tudo certo, foi bem rápido, testamos e foi sucesso". Ou seja, a GMUD ocorreu na noite de 28/09, não em 27/09 como previsto no digest anterior.

**Ação:** [`../siga/contexto.md`](../siga/contexto.md) e [`../sso-keycloak/contexto.md`](../sso-keycloak/contexto.md): registrar SSO em produção (deploy 27/09, multi-DNS), GMUD Siga+Conexão em 28/09 com sucesso, Ciacom ainda bloqueado sem previsão, bug de data de senha no LDAP, remoção do banco de usuários do Keycloak, reset de TOTP, PoC de certificado digital pronta.

## Conexão / Contas de energia (Diego, Fernando) — fluxo intermediário descoberto; refatoração para monorepo

- **29/09 (Diego):** reunião com Ozéias e uma pessoa da gestão imobiliária validou o fluxo de envio de contas do Conexão e viu que **falta um fluxo intermediário** que ninguém conhecia; saíram com um plano que Ozéias levou às "meninas" para validar. Diego passou a estudar a documentação **Oracle** para integrar esse fluxo.
- **01/10 (Diego):** após a planning recebeu os cards do Conexão; decidiu (com Igor e Lacerda) implementar a feature das concessionárias no projeto "API" já existente, mas antes reorganizar a arquitetura: **monorepo por unidades, cada módulo com deploy independente**, para o deploy do módulo novo não afetar os outros. Previsão: validado em HML "no máximo terça (06/10)", e só então implementa a extração de contas das concessionárias; código e testes "entre hoje e amanhã".
- **02/10 (Diego):** escrita local da refatoração concluída, testes batendo no código novo sem quebrar nada; infra (serviços e rotas) preparada em HML; **PROD não preparado** por falta de acesso à máquina (só para checar portas livres); "ainda temos tempo antes do deploy de PROD". Abre PR para HML hoje para o primeiro teste de deploy por unidade.
- **Fernando:** **sem acesso ao projeto Conexão** (01/10 e 02/10); Jesus (infra) ia abrir chamado; Igor orienta cobrar todo dia. Enquanto isso fez cards pequenos: ordenar lojas na extensão fiscal (pronto, PR aberta em 02/10) e botão de encerrar campanha (pegou em 02/10).

**Ação:** [`../conexao-contas-energia/`](../conexao-contas-energia/) e [`../faturas-concessionarias/contexto.md`](../faturas-concessionarias/contexto.md): fluxo intermediário descoberto, refatoração em monorepo antes da feature, dependência do acesso do Fernando e de PROD; [`../envio-contas/contexto.md`](../envio-contas/contexto.md) se for o mesmo escopo (confirmar).

## Motor de Descontos (Donato) — banco reestruturado liberado, desenvolvimento em fase final

- **28/09:** Donato segue aguardando Fábio enviar as alterações de banco; sugere, em vez de devolver cards ao bloqueio, criar cards novos para finalizar sem subir.
- **01/10:** Fábio liberou as tabelas na véspera: **removeu um campo de uma tabela "PRO0141" e acrescentou dois na "PRO014"** (nomes como transcritos, podem estar imprecisos); já alterado nos dois bancos de homologação. Quem mexer em motor de desconto e vir erro de salvamento, é por isso. Donato fala em 4 tabelas (uma nova, uma removida, duas alteradas); na daily VAR de 01/10 fala em 5. Começou pelo Venda Mercantil e agora toca o portal; entrega prevista entre 01/10 e 02/10. Pediu um card único (Igor cria no nome dele). Danilo testa a parte do portal; Venda Mercantil provavelmente fica com o time VAR.
- **02/10:** fechando os últimos testes; entrega em breve, depende do card/estrutura de testes para ir à devbox.

**Ação:** [`../motor-descontos/contexto.md`](../motor-descontos/contexto.md): bloqueio de banco **resolvido** (tabelas alteradas em HML em 30/09-01/10); nova previsão de entrega 01-02/10; escopo de 4-5 tabelas, portal + Venda Mercantil.

## Gamificação / Fechamento contábil / Conciliação (Kauã)

- **28/09:** o script de correção "para o fim" não funcionou na DR (Kauã diz que rodou bem na máquina dele, "erro meu provavelmente"); um rework voltou porque a **migration não rodou** (precisa entrar na pipeline). O job principal da conciliação não rodou: o **TTL** do job travou depois de mudança no Kong; segue para a próxima GMUD. Critérios de card de gamificação desatualizados (ex.: opção que não existe mais): pede regra de como tratar critério alterado.
- **29/09:** priorizou o job (TTL, limpeza, retry) em vez do rework; organizou reworks de gamificação, subiu e alinhou com Ozéias.
- **01/10:** arrumou reworks e foi para os dois cards de gamificação novos pedidos pelo Ozéias. Igor: a sprint deve ter bastante gamificação do lado do Kauã, podendo sobrar card para outros.
- **02/10:** limpou pendências; focou no card da **rede local** (confirmação de acesso à rede local pelo navegador), testando em navegadores antigos porque "em loja o pessoal abre num Edge de 2002", tentando rollback de versão. Falta a reunião Ozéias–Spin sobre as novidades. Igor pede que Kauã envie as anotações para ele criar os cards. Danilo iniciou os testes de gamificação.

**Ação:** [`../gamificacao/contexto.md`](../gamificacao/contexto.md) (ver também [`../gamificacao/2026-09-17-e-18-alinhamento-ajustes-portal-gamificacao.md`](../gamificacao/2026-09-17-e-18-alinhamento-ajustes-portal-gamificacao.md)); [`../conciliacao-fase-2/contexto.md`](../conciliacao-fase-2/contexto.md): job travado por TTL após mudança no Kong, correção na próxima GMUD.

## Overlimit / Concessão de Depósitos / Reenvio (JB)

- **28/09:** Igor sobre o card do Gui (Overlimit RPA): Spin ficou de fechar os pendentes no mesmo dia, depois Igor cria o card. **Concessão de Depósitos:** JB e João Brito, olhando extratos bancários, concluíram que a loja de cada depósito talvez se identifique pela **agência (número no final, talvez Santander)**; JB valida com Ozéias. Reunião às 14h30 (JB, Ozéias, Danilo) para mostrar o **reenvio**.
- **29/09:** devbox do reenvio com o time, ajustes, PR aberta; volta aos reworks que tinha pausado quando o sistema caiu (API da conciliação em HML).
- **01/10:** mexeu de novo no reenvio (em code review), pede nova revisão do Diego; começou a task do **upload de CSV**.
- **02/10:** sem fala (Igor: "nada para comentar").
- A planning de 30/09 fechou as definições do Overlimit RPA: inserir o que já existia na tabela; Gui fala com Thalison para criar a tabela no banco de teste.

**Ação:** [`../overlimit/contexto.md`](../overlimit/contexto.md): card de upload CSV no portal RPA iniciado em 01/10; definições fechadas em 29-30/09.

## Qualidade / fluxo

- Danilo (01/10): **zerou a fila de testes**, todos os cards com evidência; desenvolvendo uma skill com o Claude para atuar nos cards Ready for Dev (criação de cenários); devolveu alguns cards ao refinamento avisando no Slack.
- Danilo (02/10): perdeu testes em 01/10 por problema de VPN.
- Igor (29/09): conversou com Ozéias sobre novos projetos; um "teoricamente pronto" vai para Fernando e Diego (os de Conexão), para começar a sprint com ele andando.

## Pontos sem desfecho

- Trechos garbled (ex.: "a mão", "Filme") não foram interpretados.
- Conteúdo das reuniões de Ozéias com as áreas de gamificação só aparece de forma indireta.
