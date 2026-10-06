# Digest — Dailies Retaguarda, 17–23/09/2026

> Síntese das 5 dailies do squad Retaguarda nesse período (17, 18, 21, 22, 23/09 — sem daily 19–20/09, fim de semana). Fontes: `RETAGUARDA - Daily (2025)  (11).docx` (17/09, 10m37s), `(15).docx` (18/09, 8m42s — atenção: numeração de arquivo fora de ordem cronológica, confirmado pelo cabeçalho de data dentro do docx, não pelo sufixo do nome), `(12).docx` (21/09, 9m0s), `(14).docx` (22/09, 6m36s), `(13).docx` (23/09, 12m54s). Participantes ao longo do período: Igor, Diego, Kauã, Fernando, JB (João Bernardo), Kovalski, Danilo, Donato, Francisco Sola, Filipe de Lacerda.

## 🔴 Siga — tentativa de migração de SSO falhou de madrugada (20→21/09), retry adiado pra segunda que vem

Na daily de 21/09, Kovalski relata: tentaram migrar o SSO do Siga de um ambiente pro outro à noite, ficaram **até 4h da manhã** e "deu ruim" — sem entender a causa do erro, mesmo tendo replicado o ambiente "tudo igual" do antigo. Fizeram o Retaguarda funcionar, mas o **RPA continuou retornando 502** mesmo após rollback completo; não sabem se é algo próprio do RPA (sem acesso à máquina pra investigar) ou algo que a migração causou. Kovalski precisa de ajuda de alguém identificado só como "JV" pra entender o ponto; pretendia mexer em arquitetura de manhã e falar com o Spin à tarde — possível solução (custosa) é replicar os portais em outra máquina.

Na mesma daily, Igor pede pro Danilo comparar os dados entre as duas versões do Siga (pendência desde a semana anterior) — Kovalski pede pra **não testar ainda**: quer alinhar antes com o Spin porque o portal é público e uma mudança de última hora pode invalidar o teste do Danilo.

**23/09 (recap):** Kovalski avisa que o board "precisa ser atualizado". Resumo do que rodou entre 21-23/09:
- **"Criar admin" foi liberado** (ele + alguém) — esperavam ~2 usuários, veio "uma porrada"; tiveram que criar **regra especial no Kong** pra tratar grupos. Também acharam um **bug numa "CVR"** que não respeitava o tempo de atualização da versão do Keycloak.
- **Atualização do Keycloak não subiu** de domingo (20/09) pra segunda (21/09) — deu erro. De segunda pra terça (22/09) subiram de novo só pra testar a questão do "consumer" — deu certo. **Retry completo fica pra segunda-feira que vem (28/09)** — motivo não detalhado na transcrição, só "vamos dar esse espaço aí".
- Máquina com problema sério de acesso — conexão "do nada dropa e não volta mais", sem acesso pra diagnosticar.
- **No Siga propriamente**: atualizou a lib de homologação usando a nova lib de engenharia reversa (mesma da Gavi Components); ao aplicar a mesma lib no Siga, descobriu que **o Valdo guardou 24 módulos diferentes** — teve que fazer engenharia reversa de cada um e subir todos. Kovalski descreve o repositório resultante como "uma salada" (organização por pasta quebrada), mas funcional; já está em homologação, pediu pro Daniel testar. Plano de limpeza futura com Kauã/JB/Diego, possivelmente um "design system".

**18/09:** Kovalski havia finalizado a engenharia reversa da lib do Valdo/UAI ("rodou local, funcionou 100%") e iniciado o deploy real do Siacom/Ciacom — mas perdeu acesso à máquina no meio do processo, travando tudo; prometeu fechar "hoje" (18/09). Também gerando usuário de SSO pra tirar dúvidas do time de sustentação — reclama que já são **3 reuniões sobre o mesmo assunto** sem resolução.

**17/09:** Diego pegou 2 cards do Siga (#13060, #13062) — resolvidos rápido, pendente devbox com Danilo. Kovalski orienta Diego sobre o novo ambiente de homologação do Siga (que vira o novo PROD) — desenvolvimento acontece numa branch separada por segurança, ainda não mesclada em develop. Kovalski também fechou a "questão dos cálculos" (sexta anterior) e mediu retomar o Ciacom.

**Ação:** [`../siga/contexto.md`](../siga/contexto.md) precisa desses 5 achados — a tentativa de migração de SSO falhou e segue sem causa raiz confirmada, o retry ficou pra 28/09, e a frente "Ciacom" (item 1.1 do contexto) segue sem confirmação de conclusão apesar do "vou fechar hoje" de 18/09.

## Fechamento Contábil / Gamificação (Kauã) — código subiu fora do padrão, GMUD sem intercorrência mas bloqueada por AD

**23/09:** Kauã relata que ontem (22/09) teve **GMUD** — "felizmente não quebrou nada", mas o **pessoal esqueceu de criar o grupo no AD**, então não deu pra testar o que precisava (ligado ao "app de remarcação do Victor" — ver seção própria abaixo). Além disso, admite: **"a gente subiu com código ruim mesmo... o código está fora do padrão"** — reconhece que precisa decidir como vai ser a estrutura pra não deixar isso passar de novo, mas o item já está em produção funcionando.

**22/09:** Kauã acompanhava a "história do Gustavo" (PO do VAR 3.0) sobre subir código do Victor — a PR não estava em dia, então não subiu ontem, vai subir hoje; Kauã queria muito que essa PR estivesse em homologação (HML) por ser "muita coisa", com risco de quebrar outros ambientes/melhorias — pede que alguém fale com o Victor pra pelo menos subir em HML também. Também começou foco em teste de "unificação" e regressivo pra bugs de rota; devbox com Danilo marcado pra hoje sobre o card #12892.

**17/09:** Kauã passou a task de contabilidade pra frente, falta mostrar pro Danilo e Ozéias; pegou a task de "timeout", revisando "em batch" pra não quebrar nada; reworks pendentes: chave de e-mail expirada em HML (a de PROD já foi corrigida, precisa gerar uma nova exclusiva pra HML).

Sem menção nova ao risco de "job de duplicação de desconto" nem ao filtro de estado múltiplo já rastreados em [`../motor-descontos/contexto.md`](../motor-descontos/contexto.md) — seguem sem confirmação de resolução neste período.

## App de Remarcação de Preços (Donato / Victor / Ozéias / Thalison) — GMUD sem AD, testes de notificação em andamento

**23/09:** Danilo pergunta ao Donato se os cards do "App de Remarcação" devem continuar em QA. Donato confirma: **Ozéias e Thalison fizeram uma atualização nos bancos de homologação ontem (22/09)** pra Ozéias conseguir testar mais uma parte relacionada a **notificações** — segue em teste, cards continuam em QA.

**Cruzamento com a seção acima:** o bloqueio de "grupo do AD não existia" (relatado por Kauã em 23/09) parece se referir a esse mesmo fluxo ("está em prol de ato de remarcação do Victor" — trecho de transcrição um pouco confuso, não dá pra confirmar 100% sem checar com o time). Vale confirmar diretamente se é a mesma frente.

## Reenvio para Aprovação / "Revisão" (JB) — achado grande: Maria pode ter finalmente respondido

**18/09:** No meio de uma frase sobre a task de revisão (front-end), JB diz: **"a Maria me respondeu finalmente, eu tô marcando segunda-feira, tô aí com ela pra gente ver de novo, porque ela falou que de novo houve um monte de mudança, por isso que ela sumiu. Então a gente vai ter que mudar tipo de novo um monte de coisa."**

**Isso é potencialmente muito relevante pra [`../dashboard-cds/contexto.md`](../dashboard-cds/contexto.md)** — esse arquivo rastreia, desde 13/08, um bloqueio recorrente de "Maria sumida" sem responder JB (reconfirmado em 27/08, 01/09 e 08/09). **Ressalva:** a transcrição não deixa claro se essa "Maria" e essa conversa são sobre o Dashboard CDs especificamente, ou sobre a task de "reenvio para aprovação"/"revisão" que JB vinha tocando nesses mesmos dias (que pelo digest anterior de 09-15/09 também é dele, mas não estava claramente ligada à Maria). **Não dá pra confirmar só pelo conteúdo da transcrição — recomendo perguntar direto ao JB** antes de tratar isso como resolução do bloqueio do Dashboard CDs.

**21/09:** JB segue no "reenvio pra aprovação" — "falta pouquíssimo", front terminado na sexta (18/09), testando localmente todos os cenários; planeja devbox com Danilo hoje ou amanhã, depois code review.

**22/09:** JB continua "na revisão" — testou bastante de manhã, não conseguiu trabalhar à tarde (mal-estar/dor de cabeça), ainda testando.

**23/09:** JB segue testando antes de chamar o Danilo pra devbox, pra não ter que voltar atrás depois de mostrar algo quebrado — "acredito que agora está realmente fechado".

## Dev Conexão / Homolog (Diego)

**17/09:** Diego tem agenda com gestão imobiliária + Ozéias sobre o "sistema do conexão" (envio de contas).

**18/09:** Diego limpou a fila de code review de API/APP (só falta o "Vitão"); testou o fluxo completo do "conexão" com o Danilo pra apresentar às 15h "com as meninas" — reunião correu muito bem ("uma das melhores que a gente teve"). No fim do dia, achou a **pipe do portal de Homolog falhando no deploy** — causa: lock no I/O do Redis — resolvido; deixou documentação preparada e propostas de solução pra não repetir.

**22/09:** Diego revisou o código do "Vitão" o dia todo — o plano era ele corrigir e subir na GMUD do dia, mas ficou só na revisão, não entrou na GMUD. Fez devbox com Danilo sobre o card **#13115** ("deu tudo certo"), PR em homologação; deixou descritivos no card de fluxo de teste e definiu módulo-piloto pra testar a nova conexão com o retaguarda. Valdo aprovou um dos cards do Siga (#13062). Começou o card novo **#12793**.

**23/09:** Diego seguiu no #12793, "quase finalizando"; revisou PRs (incluindo uma do Fernando); planeja falar com Ozéias hoje sobre subir a atualização do "conexão".

## Automação Fiscal / Engine / Webhook (Donato) — atualizando produção sem teste em homologação

**23/09:** Donato começou a atuar no **portal de automação fiscal pra atualizar em produção, mesmo sem o pessoal ter testado em homologação** — está corrigindo pipelines que o Kovalski deixou quebradas. Vai olhar depois a pipe de webhook "junto com a Madame" pra confirmar que dá pra atualizar tudo hoje. Menciona também ter mexido ontem (22/09) na **Engine**, a pedido do "Fiz" (Filipe?/Spin — nome não claro na transcrição): (1) passar a retornar também o status do próprio invoice, não só da Sefaz; (2) **2 endpoints novos** — um pra visualizar a quantidade de itens dentro da pasta de "pendentes e erro", outro pra "fazer essa pasta andar" (processar as pendências).

**Isso bate quase exatamente com o escopo de [`../engine-doc-pendentes-migrate/contexto.md`](../engine-doc-pendentes-migrate/contexto.md)** (card #12901) — o contexto registra que o **Kovalski** confirmou início em 08/09, mas agora é o **Donato** quem relata execução concreta (endpoints de quantidade de itens + "andar" a pasta). Vale confirmar se houve troca de dono ou se é trabalho conjunto.

**17/09:** Donato passou o dia acompanhando o time da Migrate (com Lacerda/Walter/Kovalski), validando cenários pedidos por eles; ouviu que pode vir uma reestruturação grande — trocar o framework atual pelo uso direto de web service — ainda em avaliação, sem desenvolvimento efetivo nesse dia.

## Tesouraria / Conciliador — pendência sem dono confirmado (17/09)

Francisco Sola pergunta a Kovalski o status de um card do "conciliador" que soma valores de fechamento de tesouraria. Kovalski responde que **não mexe nem em Tesouraria nem em Conciliação** — Sola diz que vai perguntar direto ao Igor depois. **Mesma pendência sem dono já registrada em 09/09** (ver [`2026-09-09-a-15-digest-retaguarda.md`](2026-09-09-a-15-digest-retaguarda.md), seção "Sola / Conciliador de Tesouraria") — segue sem resolução confirmada 8 dias depois.

## Motor de Desconto (Danilo)

**18/09:** Danilo diz que vai fazer "esse teste de motor de desconto aí do lanchinho também" logo mais, depois de finalizar 3 cards do Kauã e um regressivo de "gerar link de acesso" no SSO. Ao fim do dia, planeja "finalizar esse card de motor de desconto". Sem mais detalhe técnico — nenhuma contradição com o que já está em [`../motor-descontos/contexto.md`](../motor-descontos/contexto.md).

## Cruzamentos a verificar

- **Siga — SSO**: tentativa de migração falhou na madrugada de 20→21/09 (RPA em 502 pós-rollback, causa não identificada); retry adiado pra segunda-feira 28/09; "criar admin" foi liberado com volume muito maior que o esperado, exigiu regra especial no Kong.
- **Dashboard CDs — Maria**: possível fim do bloqueio de semanas ("Maria sumida"), mas contexto ambíguo — confirmar com JB se a "Maria" de 18/09 é a mesma do Dashboard CDs antes de atualizar o arquivo.
- **App de Remarcação**: GMUD de 22/09 não quebrou nada, mas faltou criar grupo no AD — bloqueou teste; Ozéias/Thalison seguem testando notificações via bancos de homologação atualizados em 22/09.
- **Engine/Doc Pendentes (#12901)**: Donato relata execução concreta dos 2 endpoints e do retorno de status do invoice — confirmar se ele é o novo dono de execução (era Kovalski desde 08/09).
- **Automação Fiscal**: Donato atualizando produção sem teste prévio em homologação (23/09) — risco a registrar.
- **Sola/Conciliador de Tesouraria**: segue sem dono confirmado desde pelo menos 09/09.
- **Gamificação/App Remarcação**: Kauã admite código "fora do padrão" subiu em produção (23/09) — sem plano formal de correção ainda.
