# Prioridades e Planejamento de Sprint

> Visão acionável — atrasado/bloqueado, o que está sendo feito agora, e o que precisa virar reunião, card novo ou card refinado. Complementa o [dashboard executivo](dashboard-executivo.html) (status/stakeholder) e o [índice de projetos](README.md) (navegação).

**Última atualização:** 08/09/2026, a partir de 4 dailies novas cobrindo 01–08/09 (2 Retaguarda: 01/09 e 03/09; 2 VAR 3.0: 01/09 e 04/09; mais a leva de hoje, 1 Retaguarda + 1 VAR 3.0 de 08/09). **Não há transcrição de daily Retaguarda pra 02/09** (o squad teve Sprint Planning nesse dia em vez de standup) **nem de VAR 3.0 pra 02–03/09** (não achadas, não necessariamente que não houve daily). Ver digests em [dailies/2026-09-01-e-03-digest-retaguarda.md](dailies/2026-09-01-e-03-digest-retaguarda.md), [dailies/2026-09-01-e-04-digest-var3.md](dailies/2026-09-01-e-04-digest-var3.md), [dailies/2026-09-08-digest-retaguarda.md](dailies/2026-09-08-digest-retaguarda.md) e [dailies/2026-09-08-digest-var3.md](dailies/2026-09-08-digest-var3.md). O snapshot de 31/08 abaixo (13 transcrições, 24–31/08) segue como referência histórica onde ainda relevante.

---

## ✅ Novidades 01–08/09 (desde o snapshot de 31/08)

- **🆕 Apoio pra Wanderleia (tratamento de erros, VAR 3.0) resolvido (08/09).** Ela tinha pedido apoio na daily de 04/09 pra revisar as 8 atividades antes do PR; hoje (08/09), por orientação do Felipe, 4 foram passadas pro Walter e 4 pro Wesley testarem/revisarem. Ver [dailies/2026-09-08-digest-var3.md](dailies/2026-09-08-digest-var3.md).
- **🆕 Novo dev Diogo (VAR 3.0) integrado.** Apresentado em 04/09 (dev de Ubiratã/PR, ~3-5 anos de carreira); Kovalski já fez onboarding (Portal Retail + Portal de Gestão de Insumos). Em 08/09, Gustavo confirmou acesso permanente no lugar do Matheus Martins (já desligado). Tarefas iniciais são "coisas do futuro" (otimização de front, log, limpeza de código duplicado) — não fazem parte da release do piloto de 14/09. Ver [dailies/2026-09-08-digest-var3.md](dailies/2026-09-08-digest-var3.md).
- **🆕 Doc Pendentes / Engine — dono de execução confirmado (08/09).** Kovalski: "devo pegar as coisas de doc pendentes pra fazer da engine" — resolve a ambiguidade que vinha desde 03/09 (lá era só um "talvez"). Ainda não houve reunião formal. Ver [engine-doc-pendentes-migrate/contexto.md](engine-doc-pendentes-migrate/contexto.md).
- **🆕 Tap on Phone/4G — sem novo problema em produção reportado até 04/09.** O fix de NSU (backend retornava `0` como sucesso quando deveria ser erro) parece ter resolvido o crash-ao-abrir relatado antes. **Ressalva mantida:** o rebuild definitivo do `.ar` com o esquema correto (em todos os arquivos que acessam banco) + novo code review **ainda está pendente** — não tratar como 100% fechado.
- **Conciliação Fase 2 — nova task #12887 (08/09), divergência manual cai como "operador vazio".** Diego juntou um caso trazido pelo Ozéias (sexta 04/09) à task #12887 (mesma tela de aprovar divergências/gerenciar perda); testando hoje (08/09) e preparando GMUD prevista pro mesmo dia — sem confirmação de que subiu nem do que mais compõe essa GMUD. Ver [conciliacao-fase-2/contexto.md](conciliacao-fase-2/contexto.md).
- **🆕 Conciliação Fase 2 — bug novo (09/09): "Perda" cai na fila de Aprovação de Vales.** Reportado pela Midia (RH) por telefone; card criado 09/09: [#12912](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12912), Diego, Sprint 28, Ready for Dev — possível regressão do módulo de RH que subiu na GMUD de 31/08 (#12808–#12811), a confirmar. Ver [conciliacao-fase-2/contexto.md](conciliacao-fase-2/contexto.md).

---

## ✅ Resolvido desde a última atualização (24/08 → 31/08)

- **Conciliação Fase 2 (módulo RH) — pronta, sobe pra produção na GMUD de hoje (31/08).** Pacote completo (#12800, #12808–#12811) aceito após QA com o Danilo. 2 bugs pré-existentes achados na validação viraram cards próprios (#12882, #12884), não bloqueiam.
- **Migração VarRet — testada, aprovada, sobe pra produção na mesma GMUD de hoje.**
- **Tesouraria — rollout 100% do parque concluído** (25/08 à noite).
- **Overlimit — RPE liberou credenciais/webhooks.** Testes de endpoint em produção já começaram, direto no Kong, sem precisar de credencial. Sai da lista de bloqueios críticos.
- **Motor de Descontos — job de duplicação desativado** pelo Leo (mitigação), como combinado com Thalison/Fábio.
- **Reunião com o Arthur realizada (02/09)** — confirmou a correção do bug de propagação de campanha; **não** cobriu US5 nem o job de duplicação (ver riscos). Gerou 2 itens prontos pra dev e vários pontos que o Igor precisa confirmar internamente antes de responder ao Arthur. Ver [motor-descontos/2026-09-02-call-arthur.md](motor-descontos/2026-09-02-call-arthur.md).
- **Ciacon — integração fechada, PR aberto pro Spin.** Cards #12813/#12814 criados e linkados ao Epic SSO (#11853).
- **Gamificação T1–T10** — avançaram todos pra QA/In Test no board; painel administrativo já subiu no portal.
- **🆕 Tap on Phone / VAR 4G — causa raiz do bug do "acordo" encontrada e corrigida via deploy emergencial (01/09 à noite).** Causa: config. da IDE do GeneXus sem o esquema do banco definido, `.ar` compilado com esquema default (usuário de loja batia no esquema errado). Sem novo problema relatado em prod até 04/09. **Ressalva:** o rebuild definitivo do `.ar` com o esquema correto (em todos os arquivos que acessam banco) + novo code review **ainda está pendente** — não tratar como 100% fechado. Ver [dailies/2026-09-01-e-04-digest-var3.md](dailies/2026-09-01-e-04-digest-var3.md).

---

## 🔴 Atrasado / Bloqueado

| Item | Desde quando | Trava | Status/ação |
|---|---|---|---|
| **NFe — rejeição em massa pela Migrate (VAR 3.0)** | 21/08 | Documentos antigos travando o DocPay identificados; pedido de limpeza feito ao Vini pra liberar notas represadas. Levantamento (02/09) achou ~6.000 notas "mortas" (10-28/08) na pasta de pendentes por loja da Migrate — provável mesma raiz, a confirmar | Card [#12901 (VAR 3.0)](https://dev.azure.com/GrupoAvenida/VAR%203.0/_workitems/edit/12901) criado — direção proposta: tirar a lógica de doc pendentes da Migrate, deixar na própria loja, possível job de hora em hora. 🆕 **Kovalski confirmou início de execução em 08/09** ("devo pegar as coisas de doc pendentes pra fazer da engine"), ainda sem reunião formal. Ver [engine-doc-pendentes-migrate/contexto.md](engine-doc-pendentes-migrate/contexto.md) |
| **SmileGo (NeuroTech)** | +5 semanas sem retorno | Ambiente de teste do fornecedor não funciona | Sem qualquer menção desde 10/08, inclusive nas dailies de 01–08/09 revisadas agora — confirmar se segue parado ou foi abandonado silenciosamente |
| **Tap on Phone / VAR 4G — regressão "537" no Desconto de Gerente + rebuild pendente do fix do "acordo"** 🆕 (atualizado 08/09) | Regressão "537" achada 01/09; bug do "acordo" achado no retro de 28/08 (causa raiz já corrigida via emergencial, ver Resolvido acima) | **537:** tasks do Donato subiram pra produção "de forma equivocada" em 01/09, causando erros de arredondamento (537) no cálculo/gravação do desconto de gerente — Donato esclarece que a rotina que subiu é só mensagem/trava, não cálculo, mas **causa raiz da regressão ainda sem confirmação fechada na transcrição** (Gustavo ia confirmar). 🆕 Em 08/09, Filipe reporta que o "537" do fim de semana já foi ajustado ("ninguém gritou... só aquele problema do 537 no sábado... mas aí a gente ajustou, tudo certo") — **tratado como corrigido, mas sem causa raiz documentada na transcrição**; combinado fazer double-check na sexta sobre o que está de fato na release. **Acordo:** emergencial já subiu, mas rebuild definitivo do `.ar` ainda pendente (sem novo problema em prod reportado até 04/09) | **Release/piloto do Tap on Phone confirmado pra 14/09.** 🆕 Em 08/09 o PO Gustavo reforçou: "extrema importância esses quatro dias... conseguir concluir tudo até segunda-feira que vem" — lista Overlimit, tratamento de erros, consulta automática, Pix no TEF e um item de "voucher" (nome garbled na transcrição, não confirmado) como o que precisa subir até lá. Migração GeneXus→Java **não sobe nessa release**. Ver [dailies/2026-09-08-digest-var3.md](dailies/2026-09-08-digest-var3.md) |
| **SSO SIGA — deploy bloqueado** | 28/08 | Pablo (deploy) de férias + WAF bloqueando acessos por questão de contrato | Implementação pronta (Dev Review), só falta destravar o deploy — sem menção nova nas dailies de 01–08/09 revisadas, confirmar se segue parado |
| **Ciacon — self-review sem segunda pessoa** | 28/08 | Kovalski descreveu o fluxo como "eu faço, eu valido e eu aprovo" | Vale pedir revisão de outro dev antes de mesclar definitivamente — sem atualização nova nas dailies de 01–08/09 revisadas; Kovalski segue com a carga do Siga por cima (03/09) |
| **Venda técnica (VAR 3.0) — correção subiu desabilitada** 🆕 | 08/09 | Parâmetro (WS) da venda técnica corrigido e subiu na engine, mas está **desabilitado** e **ainda não foi testado**; falta avisar o Juliano. Também pendente validar a questão do "retrai" (termo pouco claro na transcrição) antes de habilitar | Ver [dailies/2026-09-08-digest-var3.md](dailies/2026-09-08-digest-var3.md) |

---

## 📅 Reuniões a ter / agendar

- [x] **Igor + Arthur — Motor de Descontos, novas etapas.** Realizada **02/09**. Confirmou a correção de propagação e levantou vários pedidos de usabilidade + 1 dúvida técnica do Arthur (ver [motor-descontos/2026-09-02-call-arthur.md](motor-descontos/2026-09-02-call-arthur.md)) — **mas não tratou nem a US5 nem o job de duplicação desativado pelo Leo**, contrário ao que se esperava. Ambos seguem sem data de alinhamento.
- [ ] **Alinhar reativação do job de duplicação (Motor de Descontos)** 🆕 — com Thalison/Fabio, separado da call do Arthur (não foi pauta). Ver [motor-descontos/contexto.md](motor-descontos/contexto.md).
- [ ] **Cobrar formalização da documentação do Ciacon no ADO** — Kovalski diz que terminou (28/08), mas o card #12813 segue com 0 comentários no Azure.
- [ ] **Definir apoio ao Kovalski pras máquinas do Siga** — a partir de 31/08 SigaPub + resto do Siga viram responsabilidade direta da Retaguarda; Kovalski já sinalizou que não dá conta sozinho, precisa de Diego/Kauã. 🆕 Em 03/09 ele reclamou de estar uma semana inteira sem card formal, atolado entre Siga, Ciacon e agora Doc Pendentes/Engine (confirmado 08/09) — segue sem esse apoio definido.
- [ ] **Endereçar "se tudo é urgente, nada é urgente"** — reclamação #1 do retro VAR 3.0 (28/08). Cards sem critério de aceite criados tarde demais; Gustavo (PO) sobrecarregado cobrindo 2 projetos + infra à noite. 🆕 Sem sinal de melhora até 08/09 — Gustavo segue reforçando prazo apertado do piloto de 14/09.
- [ ] **🆕 Reunião Jeferson/Gustavo/Nicolas — bug de validação de devolução de TEF com cartão de terceiros** (Migração GeneXus→Java). Marcada em 08/09, sem data confirmada na transcrição.
- [ ] **🆕 Confirmar com o Igor se #12887 (Conciliação Fase 2) subiu na GMUD de 08/09** e o que mais compunha essa GMUD — a transcrição da daily não detalha. Ver [conciliacao-fase-2/contexto.md](conciliacao-fase-2/contexto.md).
- [ ] **🆕 Igor revisar o material Donato/Ozéias (remarcação) repassado em 08/09** antes de criar os cards — ver [etiqueta-remarcados/contexto.md](etiqueta-remarcados/contexto.md).

---

## 🃏 Cards a criar

- [x] **Conciliação Fase 2 — 2 bugs pré-existentes achados na validação do #12810.** Criados 31/08: [#12882](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12882) (can-close sem validar status) e [#12884](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12884) (erro genérico em vez da mensagem real).
- [x] **Ciacon — Kovalski, documentação e implementação.** Criados 27/08: [#12813](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12813) e [#12814](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12814), linkados ao Epic SSO (#11853).
- [ ] **VAR 3.0 — Epic de migração GeneXus → Java.** Ainda sem Epic formal. Jeferson já começou a 1ª tarefa (tabela de Feature Flag) a pedido do Walter — Igor pediu card formal pra não perder rastreio.
- [ ] **Tesouraria — regra de NSU padronizada em 8 dígitos.** Pedido do Financeiro (4 dígitos loja + 4 dígitos comprovante GVT); vai numa release separada (3.0.1→3.0.2) por ser mudança de risco assumido — Sola: "provavelmente vai dar rollback depois".
- [ ] **SIGA — Indicadores de Performance, em Ready for Dev.** Segue sem dono/card formal confirmado.
- [ ] **Motor de Descontos — 2 itens levantados na call de 02/09, prontos pra virar card sem dependência externa** 🆕: permitir campanha/combo com 1 item só (hoje mínimo 2); corrigir e-mails de notificação (assunto/conteúdo/destinatários). Ver [motor-descontos/2026-09-02-call-arthur.md](motor-descontos/2026-09-02-call-arthur.md).
- [x] **Engine — Doc Pendentes da Migrate, levantamento de requisitos.** Criado 02/09: [#12901 (VAR 3.0)](https://dev.azure.com/GrupoAvenida/VAR%203.0/_workitems/edit/12901), filho da Epic #9605 (Engine Fiscal), relacionado ao #12466.
- [x] **API Retaguarda — 5 cards do incidente de instabilidade (01/09), em Ready for Dev.** Criados 04/09, atribuídos ao Fernando, Sprint 28, filhos da Epic #10542 (Infraestrutura), estimativas Fibonacci propostas pelo PO: [#12902](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12902) (healthcheck nginx, 2pt), [#12903](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12903) (thread pool Oracle, 3pt), [#12904](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12904) (foto do /me, 5pt), [#12905](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12905) (liveness, 2pt), [#12906](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12906) (StoreJobProcessor no worker, 5pt). Ver [api-retaguarda-incidente/contexto.md](api-retaguarda-incidente/contexto.md).
- [x] **🆕 Conciliação Fase 2 — bug "Perda" na fila de Aprovação de Vales.** Criado 09/09: [#12912](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12912), Diego, Sprint 28, Ready for Dev. Ver [conciliacao-fase-2/contexto.md](conciliacao-fase-2/contexto.md).
- [ ] **🆕 App de remarcação do Donato — card ainda não criado.** Pedido repetido nas dailies de 01/09 e 03/09 e reforçado na planning de 02/09; segue sem criação confirmada nas dailies de 08/09 revisadas. Ver [minhas-pendencias.md](minhas-pendencias.md) e [etiqueta-remarcados/contexto.md](etiqueta-remarcados/contexto.md).

---

## 🔍 Cards a refinar / decisões do PO pendentes

- [ ] **Conciliação Fase 2 #12812 (planilha Contábil).** Bloqueado até a Adriana levantar o layout exato — ⚠️ ainda em aberto se "Arco" (citado por Diego em 28/08 como destino da integração) é o mesmo que o layout Oracle original ou uma mudança de abordagem (integração direta em vez de planilha exportável). Precisa esclarecer com o Diego/Ozéias antes de reescrever o card.
- [ ] **Dashboard CDs — validação final com a Maria.** JB diz que já fez quase tudo, só falta agendar a conferência final. 🆕 Bloqueio persiste até 08/09 — Maria segue sem responder ("sumiu"), padrão recorrente desde 13/08. Ver [dashboard-cds/contexto.md](dashboard-cds/contexto.md).
- [ ] **🆕 Etiqueta Remarcados — épico #12428 vs. trabalho paralelo do Donato/Ozéias.** Igor recebeu em 08/09 o conteúdo do WhatsApp repassado pelo Ozéias sobre remarcação; ainda precisa revisar antes de criar os cards e confirmar se é a mesma frente do épico #12428. Ver [etiqueta-remarcados/contexto.md](etiqueta-remarcados/contexto.md).

---

## 🔄 Em andamento agora (por pessoa)

### Retaguarda

| Pessoa | Frente | Status em 31/08 |
|---|---|---|
| **Diego** | Conciliação Fase 2 (produção hoje) + SIGA Indicadores | Fase 2 pronta e aceita, indo pra GMUD; SIGA Indicadores em segundo plano, ~30% |
| **Kauã** | Gamificação (todos os T1-T10 em QA) | Painel administrativo no ar, bugs de auto-increment em ajuste; teste ponta a ponta previsto pra semana de 01/09 |
| **JB** | Dashboard CDs + Migração VarRet (produção hoje) | CDs quase pronto, falta validação final com a Maria; Migração VarRet aprovada, sobe hoje |
| **Fernando** | Automação de testes do portal (8 fases) | Todas as 8 fases concluídas, Playwright (E2E) quase pronto |
| **Kovalski** | SigaPub/SSO, Ciacon (integração fechada) | SSO bloqueado por deploy (Pablo férias + WAF); Ciacon com PR aberto; chegada das máquinas físicas do Siga aumenta a carga |
| **Danilo (QA)** | Testes cruzados — foco intenso em Conciliação Fase 2 essa semana | Validou o pacote completo da Fase 2 até aceitar em 31/08; segue revisando cards de Automação Fiscal pra "teste com área" |
| **Léo** | Motor de Descontos (job desativado) | Reunião de 02/09 com o Arthur aconteceu, mas **não** tratou do job desativado — mapeamento segue sem data de formalização, precisa de alinhamento separado com Thalison/Fabio |

### VAR 3.0

| Pessoa | Frente | Status em 31/08 |
|---|---|---|
| **Caixeta** | Overlimit (agora liberado) | Testando endpoints direto no Kong, sem credencial |
| **Donato** | Desconto de Gerente (Java) + apoio Ozéias/Kovalski | Desenvolvimento terminado, aguardando aprovação de review; ajudando na engenharia reversa do Ciacon/loja 208 |
| **Moises + Jeferson** | Testes automatizados mobile + migração GeneXus | POC de teste entregue ao Lacerda; Jeferson iniciou tarefa de Feature Flag da migração |
| **Walter** | Migração GeneXus (documentação) | Documentação atualizada, 1ª tarefa (Feature Flag) já delegada ao Jeferson |
| **Wesley** | Pix pelo Pinpad (TEF) | Bug de truncamento de ID de transação achado, em correção |
| **Nicolas / Felipe** | Tap on Phone / 4G | Bugs críticos novos de fatura/acordo — foco total em estabilizar |
| **Gustavo (PO)** | Cobrindo 2 projetos + infra à noite | Sinal de sobrecarga real — retro de 28/08 votou isso como problema #1 |

### 🆕 Atualização 01–08/09 (por pessoa) — deltas em relação à tabela de 31/08 acima

> Fontes: [dailies/2026-09-01-e-03-digest-retaguarda.md](dailies/2026-09-01-e-03-digest-retaguarda.md), [dailies/2026-09-01-e-04-digest-var3.md](dailies/2026-09-01-e-04-digest-var3.md), [dailies/2026-09-08-digest-retaguarda.md](dailies/2026-09-08-digest-retaguarda.md), [dailies/2026-09-08-digest-var3.md](dailies/2026-09-08-digest-var3.md).

**Retaguarda:**
- **Diego** — nova task #12887 (divergência manual "operador vazio"), testando e preparando GMUD prevista pra 08/09 (sem confirmação de que subiu). Novo bug #12912 (Perda na fila de Aprovação de Vales) criado 09/09, Ready for Dev.
- **Kauã** — job noturno não rodou na sexta (04/09, motivo diferente do TTL 24h de "Bools" já visto antes); limpou e corrigiu pra próxima subida. Pegou reworks pequenos do Danilo ("não mostrar lojas"). 08/09: task de "ajustar comprimento do menu"; portal caiu de manhã (banco travando, API entupida) — precisou reiniciar. Igor reforçou: foco em fechar o rework de Conciliação, só desviar se surgir hotfix urgente.
- **JB (Dashboard CDs)** — segue sem falar com a Maria (01/09 e 08/09, "sumiu") — ver [dashboard-cds/contexto.md](dashboard-cds/contexto.md) pra detalhe do padrão recorrente. PR do Diego a revisar; verificou exportar Excel/PDF do "demonstrativo do caixa" e concluiu que já está tudo correto.
- **Fernando** — 01/09 resolvendo conflitos de merge nos testes automatizados de front; 03/09 em devbox com o Danilo, começou novo card; 04/09 (sexta, presencial) trabalhou pendências com o Danilo e pegou tarefas simples do JB, seguindo nelas em 08/09.
- **Kovalski** — 01/09 subiu portal de aprovações urgente (Spin) + refatorou módulo em Python; começou deploy da máquina do Siga. 03/09: uma semana sem card formal (tudo pra prioridades do Spin); fechou deploy Siga+SigaPublic (02/09); ainda sem acesso pra engenharia reversa de "Campos"; resolveu bug de grupos que travava o Gaspar; LDAP sincronizando muito devagar (deveria ser 2 em 2 min). 08/09: Ciacon aguardando máquina; fez onboarding do Diogo (força-tarefa Portal Retail + Portal Gestão de Insumos); **confirmou início em Doc Pendentes/Engine** (ver Novidades acima).
- **Danilo (QA)** — bug de permissionamento/usuário próprio (grupos quebrados, mesmo resetando) o travou boa parte de sexta (04/09); Kauã confirma recorrência. Não fica claro se é o mesmo #12514 (owner Leonardo) ou um caso novo — a confirmar. 08/09: achou forma de testar as tasks normalmente, focando primeiro no portal retaguarda antes das tasks do Diego. Fez Devbox com o Fernando na sexta. Aguardando doc do Gui sobre "visu". Ainda deve a Igor o relatório de hotfixes do portal (pendência antiga).
- **Léo (Motor de Descontos)** — sem menção nova nas 4 dailies revisadas (só "um item aguardando retorno" citado por Filipe de Lacerda em 01/09); a call com o Fabio (08/09) foi tratada fora da daily — ver [motor-descontos/2026-09-08-call-fabio.md](motor-descontos/2026-09-08-call-fabio.md) e [minhas-pendencias.md](minhas-pendencias.md).

**VAR 3.0:**
- **Overlimit (Gui Oliveira)** — RPE liberou credenciais de produção (01/09); Gui retomou o projeto em 04/09 (backend com endpoint adicional pronto, trabalhando no front de validação de elegibilidade); confirmado 08/09 como prioridade da semana do PO, junto com o piloto de 14/09. Detalhe completo e ressalva sobre percentual em [overlimit/contexto.md](overlimit/contexto.md).
- **Donato** — 01/09: atualizações no firmware da impressora do app de remarcação (resolvendo atraso na emissão de cupons), novo APK pro Ozéias. 03/09: ajustes cosméticos (velocidade de impressão, delay de telas), contornando perda de informação de firmware não-original. Tasks do Desconto de Gerente ligadas à regressão "537" de 01/09 (ver tabela de bloqueados) — Donato esclarece que a rotina que subiu é só mensagem/trava, não cálculo.
- **Moises** — 04/09 formalizando comparação desktop x mobile da rotina fiscal; 08/09 pausou brevemente (Nicolas marcou um bug pra rework), retomando a comparação com ajustes pendentes, depois mapeia fluxos exclusivos do mobile.
- **Jeferson** — revisando PR do Walter (tabela de Feature Flag); segue no bug de validação de devolução de TEF com cartão de terceiros (achado 04/09) — marcou reunião com Gustavo e Nicolas (Gustavo decidiu não puxar o Gui, prefere trazer o Fábio).
- **Walter** — 03/09 corrigiu bug de endpoint só-Retaguarda sendo chamado em "modo loja"; mesclou branches paralelas Centre/GetNet do 4G. 08/09: recebeu 4 das 8 atividades de tratamento de erros da Wanderleia pra revisar/testar antes do PR.
- **Wesley** — 04/09 corrigiu bug do comprovante que não saía no cancelamento (quebrado por alteração anterior do Fábio) — testado, indo pra dev review/release. 08/09: recebeu 4 das 8 atividades de tratamento de erros da Wanderleia (mesmo pacote acima).
- **Wanderleia** 🆕 — trouxe as 8 atividades de tratamento de erros pra revisão em 08/09; por orientação do Felipe, 4 foram pro Walter e 4 pro Wesley — resolve o pedido de apoio que ela tinha feito em 04/09.
- **Nicolas / Felipe** — 04/09: erro intermitente investigado não era bug novo (celular reconectou em outra rede ao trocar de loja fisicamente) — reforçado nunca reiniciar o app pra "resolver" erro, sempre reportar primeiro; fix de NSU parece ter resolvido o crash-ao-abrir relatado antes.
- **Gustavo (PO)** — 08/09: alertou sobre o piloto da semana que vem, "extrema importância" fechar tudo até segunda; decidiu não puxar o Gui pra reunião de TEF com cartão de terceiros (traz o Fábio); revisão de licenças/acessos (housekeeping) não achou mais ninguém óbvio pra desativar.
- **Diogo** 🆕 — novo dev (ver Novidades acima); setup do projeto já rodando, vai receber acesso permanente no lugar do Matheus Martins (desligado).

---

## ⚠️ Riscos ativos (resumo)

1. **NFe/Migrate** — segue sem confirmação total de resolução, prazo do fechamento fiscal se aproximando. 🆕 Kovalski confirmou início de execução em 08/09 (ver Novidades acima), mas sem reunião formal nem desenho técnico fechado ainda.
2. **Tap on Phone/4G** — bugs críticos novos, achados no retro de 28/08. 🆕 Regressão "537" tratada como corrigida em 08/09, mas sem causa raiz documentada; rebuild definitivo do `.ar` do "acordo" ainda pendente. Release/piloto confirmado pra 14/09, só 4 dias úteis restantes a partir de 08/09 conforme o PO.
3. **Sobrecarga da equipe VAR 3.0** — "se tudo é urgente, nada é urgente" foi a reclamação #1 do retro; PO cobrindo demais. Sem sinal de melhora nas dailies de 01–08/09 — Gustavo segue reforçando prazo apertado do piloto.
4. **Ciacon sem segunda revisão** — Kovalski aprovando o próprio trabalho, somado à chegada das máquinas do Siga (mais carga pra ele). Sem atualização nova nas dailies de 01–08/09 revisadas.
5. **NSU 8 dígitos (Tesouraria)** — mudança que o próprio time já espera precisar de rollback; mitigada por ir em release separada. Sem atualização nova.
6. **Motor de Descontos** — job desativado é mitigação, não solução definitiva; a reunião de 02/09 com o Arthur aconteceu mas não tratou disso, segue sem data de alinhamento com Thalison/Fabio. Ver também a call com o Fabio de 08/09 ([motor-descontos/2026-09-08-call-fabio.md](motor-descontos/2026-09-08-call-fabio.md)), fora do escopo das dailies revisadas aqui.
7. **🆕 Venda técnica (VAR 3.0)** — correção subiu desabilitada e não testada; falta avisar o Juliano antes de habilitar.
8. **🆕 Bug de permissionamento recorrente (Danilo)** — travou boa parte da sexta-feira (04/09) do Danilo; não confirmado se é recorrência do #12514 (owner Leonardo) ou caso novo.

---

## Fontes

**Snapshot de 31/08 (histórico):**
- [dailies/2026-08-24-a-28-digest-retaguarda.md](dailies/2026-08-24-a-28-digest-retaguarda.md) — digest das 5 dailies Retaguarda.
- [dailies/2026-08-24-a-28-digest-var3.md](dailies/2026-08-24-a-28-digest-var3.md) — digest das 5 dailies VAR 3.0.
- [dailies/2026-08-25-tesouraria-daily.md](dailies/2026-08-25-tesouraria-daily.md) — daily Tesouraria (regra de NSU + rollout 100%).
- [reviews-retros-planning/2026-08-31-planning-var.md](reviews-retros-planning/2026-08-31-planning-var.md) — planning VAR 3.0.
- [reviews-retros-planning/2026-08-28-retro-var.md](reviews-retros-planning/2026-08-28-retro-var.md) — retro VAR 3.0 (sobrecarga, critério de aceite).

**🆕 Atualização 01–08/09:**
- [dailies/2026-09-01-e-03-digest-retaguarda.md](dailies/2026-09-01-e-03-digest-retaguarda.md) — digest das 2 dailies Retaguarda (01/09, 03/09).
- [dailies/2026-09-01-e-04-digest-var3.md](dailies/2026-09-01-e-04-digest-var3.md) — digest das 2 dailies VAR 3.0 (01/09, 04/09).
- [dailies/2026-09-08-digest-retaguarda.md](dailies/2026-09-08-digest-retaguarda.md) — digest da daily Retaguarda de 08/09.
- [dailies/2026-09-08-digest-var3.md](dailies/2026-09-08-digest-var3.md) — digest da daily VAR 3.0 de 08/09.

- [dashboard-executivo.html](dashboard-executivo.html) — dashboard de status.
- [README.md](README.md) — índice de todos os projetos com `contexto.md` próprio.
