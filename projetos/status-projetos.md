# Status dos Projetos

> Visão de portfólio por estágio. Fonte: estado dos cards no ADO (consulta de 29/09/2026), `contexto.md` de cada projeto e dailies até 28/09. Quando a informação é antiga, a data da última atualização aparece no detalhe. Para prioridades de sprint, ver [prioridades-sprint.md](prioridades-sprint.md). Índice de pastas: [README.md](README.md).
>
> **Critério dos estágios** (pelo estado dominante dos cards do projeto):
> - **A refinar:** sem card, ou com cards em To do/Refinement, ou esperando definição, TAP ou especificação.
> - **Pronto para iniciar:** cards refinados, em Ready for Dev.
> - **Em andamento, dev:** Doing, Dev Box ou Dev Review.
> - **Em andamento, teste:** In Test ou Rework (voltou do QA).
> - **Em homologação:** Verified (aprovado pelo QA, aguardando validação da área ou GMUD) ou piloto em loja.
> - **Sustentação:** em produção, com bugs e melhorias pontuais.
> - **Feito:** entregue e encerrado.

## Visão geral

### 🧭 A refinar
- Envio de Contas — Requisição + OC automáticas (nova fase; detalhe em Sustentação › Envio de Contas)
- Automação de Faturas de Concessionárias
- Pesquisa Colaboradores RH
- Overlimit — RPA
- Infra — pipelines e deploy
- Dashboard CDs
- Novo Dashboard CDs — Marcelo
- SSO — melhorias do sso-hub (nova rodada; detalhe em Feito › SSO / Keycloak)
- VAR 3.0 — Padronização de Retornos HTTP

### ✅ Pronto para iniciar
- Engine — NFe tipo 2

### 🔨 Em andamento

**Dev**
- Motor de Descontos
- Engine — Webhook direto (substituição do Invoicy) e Doc Pendentes
- Overlimit — VAR

**Teste**
- Gamificação (Roleta 3.0)
- Conciliação Fase 2
- Etiqueta Remarcados / App de remarcação
- Migração VarRet

### 🧪 Em homologação
- API Retaguarda — incidente de instabilidade
- Tap on Phone + VAR 4G (piloto)
- Markdown / Remarcação de Preços

### 🛠️ Sustentação
- Portal Retaguarda — evolução contínua (Conciliação, Acessos, Tesouraria)
- SIGA
- Envio de Contas (Portal Conexão)
- Automação Planilha Fiscal

### 🏁 Feito
- SSO / Keycloak
- Tesouraria — migração para o novo sistema
- Engine Fiscal — CNPJ Alfanumérico

---

## Detalhe por projeto

### 🧭 A refinar

#### Automação de Faturas de Concessionárias
- **Status (29/09):** TAP e especificação recebidos (Gestão Imobiliária / Ozéias). Épico [#13434](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13434) criado com 9 PBIs, todos em To do:
  - [#13438](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13438) levantamento técnico e arquitetura: 5 pts, **bloqueado** (pareceres de TI e Arquitetura, cofre de credenciais). Destrava todos os outros;
  - [#13439](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13439) base de lojas e acessos: 5 pts;
  - [#13440](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13440) agendamento: 3 pts;
  - [#13441](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13441) motor de execução: 13 pts;
  - conectores [#13443](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13443) EDP (modelo), [#13444](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13444) Energisa, [#13445](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13445) Equatorial e [#13446](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13446) Neoenergia: 8 pts cada;
  - [#13442](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13442) tela de acompanhamento: 8 pts.

  As estimativas são provisórias até o fim do levantamento técnico.
- **30/09:** os 9 PBIs foram pra **Ready for Dev**, na Sprint 30, com o **Diego**. O bloqueio do #13438 continua aberto.
- **🆕 Plano de modularização da ali-api (Diego, 30/09), aprovado pelo Igor como pré-requisito da captura.** A captura roda na ali-api, que hoje tem um deploy único: qualquer commit reinicia a API e o worker juntos, e 54% dos commits do último ano mexeram no Oracle e derrubaram junto a leitura por IA. A trilha separa o deploy em unidades independentes (API, worker de leitura, worker de Oracle, infra e captura), num repositório só.
  - **Cards** (Diego, Sprint 30, filhos do #13434):
    - [#13454](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13454) M0 decisão/ADR: 2 pts;
    - [#13455](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13455) M1 higiene do deploy: 5 pts;
    - [#13456](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13456) M2 remover as rotas antigas: 2 pts;
    - [#13457](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13457) M3 configuração por unidade: 3 pts;
    - [#13458](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13458) M4 worker dividido: 3 pts;
    - [#13459](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13459) M5 pipeline por unidade: 5 pts.

    Os 6 estão em **Refinement**, por decisão do Igor em 30/09. O M5 também está bloqueado pela administração do Azure DevOps (registrar e autorizar os pipelines). M6 e M7 ficam pra depois.
  - **Impacto:** o código da captura começa **cerca de uma sprint depois**. O discovery (#13438) não atrasa.
  - **Dependências externas:** aprovação do tech lead (unidades, ADRs, remoção das rotas), folga da VM e local do build (infra), registro dos pipelines (administração do Azure DevOps).
  - Plano: [2026-09-30-plano-modularizacao-ali-api.pdf](faturas-concessionarias/2026-09-30-plano-modularizacao-ali-api.pdf).
- **O que é:** robô que busca as faturas de energia nos portais da EDP, Energisa, Equatorial e Neoenergia e sobe no Envio de Contas, rodando nos dias 05, 15 e 25 (configurável), com tela de acompanhamento.
- **Origem:** é a automação de contas de energia que o Spineli pediu pra retomar na daily de 25/09. O escopo segue o TAP e a especificação.
- **Pendentes:**
  - pareceres de TI e de Arquitetura;
  - cofre de credenciais;
  - plataforma do robô;
  - horário das execuções;
  - levantamento de quais portais têm MFA ou CAPTCHA.
- **Prazo e custo:** em levantamento.
- [contexto](faturas-concessionarias/contexto.md)

#### Pesquisa Colaboradores RH
- **Status (11/09, sem novidade desde então):** em descoberta, sem código e sem card.
  - Calls: 08/09 (interna) e 11/09 (Thaís/Francisco, RH).
  - Cronograma interno: ~640h, ~18 semanas com 1 dev. Ainda não apresentado ao RH.
  - Meta informal de documento especificado: fim de setembro.
- **Travas:**
  - criação automática de usuário via Senior (maior risco, sem dono);
  - uso de contato pessoal pra disparo, que depende do jurídico e pode mudar o rumo do projeto;
  - anonimato (modelo proposto, sem fechamento formal com jurídico);
  - "nuvem de palavras", que não está na especificação.
- **Próximo passo:** nova call com a Thaís com proposta concreta (telas e textos). Sem data.
- [contexto](pesquisas-colaboradores/contexto.md) · [cronograma](pesquisas-colaboradores/cronograma-desenvolvimento.md)

#### Overlimit — RPA
- **Status (29/09):** frente da Retaguarda, **a iniciar agora**. Cartões sobe um CSV com os clientes elegíveis no portal do RPA de cartões, o conteúdo vai pra uma tabela do RPA (modelo do blacklist) e o VAR consulta essa tabela.
- **Prazo pedido pelo Spineli:** 28–29/09.
- **Definido em 29/09:**
  - o CSV traz id da conta, CPF e porcentagem, e sobe numa tela do portal do RPA;
  - as colunas de vigência e validade vão existir na tabela, mas o uso fica pra decidir depois.
- **Tabela:** vai ser criada primeiro na **base da Retaguarda de QA** com o **Thalison**. O **Gui** monta o e-mail com o modelo de dados, e o Igor fala com o Thalison.
- **Card da tela de upload:** [#13447](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13447), filho do épico #12110 "Portal RPA", 8 pts (subiu de 5 com a tabela de CPFs cadastrados, incluída em 30/09). Desde 30/09 está em **Ready for Dev**, na Sprint 30, com o **JB**. Falta decidir a regra de nova carga (substitui, acumula ou atualiza por conta/CPF).
- **Quem detalha:** JB e "Higuinho", com o Gui e o Gustavo.
- [contexto](overlimit/contexto.md)

#### Infra — pipelines e deploy
- **Status (29/09):** cards novos, ainda sem dev.
  - [#13419](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13419) revisão de segurança das variáveis de ambiente nos pipelines: **Refinement**, 8 pts.
  - [#13426](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13426) migrações de banco automáticas no deploy da API: **To do**, 5 pts. Em aberto se a GMUD de produção exige passo próprio pra migração.
  - [#13423](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13423) pipeline de certificado digital (POC do Kovalski): está como **Verified** no ADO, mas na daily de 28/09 o Kovalski disse que segue travado pela permissão do devbox. ⚠️ **Estado no ADO não bate com a realidade: conferir.**
- **Épico:** INFRA (#9314).
- **Observação:** o Kovalski quer revisar todas as pipelines com o Kauã.

#### Dashboard CDs
- **Status (08/09, sem novidade):** bloqueado. Os 4 cards ([#12509](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12509)–[#12513](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12513), JB) estão em **To do** esperando a planilha corrigida da Maria.
- **Histórico:** o JB diz que "já fez quase tudo" do escopo anterior. A Maria some com frequência (13/08, 27/08, 01/09, 08/09). Possível resposta dela ao JB em 18/09, a confirmar.
- **Também destrava o refino do #12512:** alinhamento com Sergio da Silva.
- [contexto](dashboard-cds/contexto.md)

#### Novo Dashboard CDs — Marcelo
- **Status (29/09):** a definir. O Igor ainda vai ter reunião com o Marcelo pra definir o escopo. Sem card, sem pasta e sem documento.
- **Em aberto:**
  - o que o Marcelo precisa;
  - se é um dashboard novo ou uma evolução do Dashboard CDs atual (JB/Maria);
  - quais dados e fontes;
  - prazo.

#### VAR 3.0 — Padronização de Retornos HTTP
- **Status:** sem card, sem início e sem nenhuma menção em daily. Confirmar com Spin/Gustavo se ainda é prioridade. Se não for, arquivar como referência.
- [contexto](var3-http-status/contexto.md)

### ✅ Pronto para iniciar

#### Engine — NFe tipo 2
- **Status (29/09):** [#13127](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13127) (desenho da implementação) e [#13134](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13134) (implementação) em **Ready for Dev**, com o Donato.
- **Épico:** Engine Fiscal (#9605).
- **Fila:** entra depois do trabalho de Webhook (ver Em andamento).

### 🔨 Em andamento — Dev

#### Motor de Descontos
- **Status (29/09):** várias frentes em paralelo, todas no épico #6669.
  - **Melhorias do Diego:** [#13064](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13064) combo com um item, [#13065](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13065) e-mails de notificação e [#13066](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13066) filtro de estado multisseleção, todos em **Dev Review**.
  - **Cadastro por SKU/grade, lado Portal:** [#12913](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12913)–[#12916](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12916) (Donato) em **Verified**. A PRO014_CONTROLE (loja 999 + trava de edição) está na develop, ainda não em produção.
  - **Cadastro por SKU/grade, lado VAR:** fica **fora deste board**, por decisão do Igor em 30/09. Os cards #13420 e #13421 foram apagados.
  - **Funcionalidades da call com o Fabio, em To do:**
    - [#13427](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13427) Encerrar campanha: 3 pts, pronto.
    - [#13428](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13428) restringir campanha global a lojas específicas: 8 pts, mock pendente de decisão.
    - [#13429](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13429) reativar PRO013: 3 pts, bloqueado pela confirmação do Caixeta e dos QAs.
  - **UI com base na Gamificação:** [#13422](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13422) em **Refinement**, escopo a confirmar.
- **Bloqueios e riscos:**
  - **Reestruturação de banco** (Fabio/Donato): ainda sem detalhes, pode afetar cards já testados. O Donato sugeriu criar card novo em vez de voltar os existentes pra "bloqueado".
  - **3 donos externos do SKU/grade** (triggers PRO0144, consumidor do OPERACAOLOG, paridade do motor E1 Java): sem eles a feature não sai da central.
  - **Job de duplicação de desconto/cupom:** desativado desde 24/08, sem reativação formal.
- [contexto](motor-descontos/contexto.md) · [plano SKU](motor-descontos/desconto-sku/PLANO-IMPLEMENTACAO-DESCONTO-SKU.md)

#### Engine — Webhook direto (substituição do Invoicy) e Doc Pendentes
- **Status (29/09):** com o Donato.
  - [#13131](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13131) revalidar implementações de webhook e [#13132](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13132) webhook de rejeição: **Doing**.
  - [#13129](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13129) layout NFCe na contingência offline: **Ready for Dev**.
  - Já Done: [#13125](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13125) framework, [#13126](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13126) monitoramento da Doc Pendentes, [#13128](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13128) log do retorno 999, [#13135](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13135) bitmap.
  - **Épicos:** #13130 (substituição do Invoicy por webservice direto) e #9605 (Engine Fiscal).
- **Doc Pendentes da Migrate:** ~6.000 notas "mortas" (10–28/08). A direção é tirar a lógica da Migrate. Card de levantamento [#12901 (VAR 3.0)](https://dev.azure.com/GrupoAvenida/VAR%203.0/_workitems/edit/12901), Kovalski confirmou início em 08/09.
- **Obs.:** o Donato disse em 28/09 que está trabalhando na "troca lá no VAR" (refatoração da Troca). Falta pegar com ele o documento.
- [contexto Doc Pendentes](engine-doc-pendentes-migrate/contexto.md)

#### Overlimit — VAR
- **Status (25/09):** frente do Gui, no squad VAR 3.0. A área de negócio mudou o escopo em 21/09 e o Overlimit **saiu da release do piloto**, com retrabalho de front e de testes.
- **Checagem de crédito:** depende do SmileGo/NeuroTech. O card #12104 está bloqueado porque o ambiente de teste do fornecedor não funciona.
- **Futuro:** o valor deve vir automatizado pelo projeto "Behavior".
- [contexto](overlimit/contexto.md)

### 🔨 Em andamento — Teste

#### Gamificação (Roleta 3.0)
- **Status (29/09):** reta final pro go-live (meta informal era fim de setembro).
  - Os cards T ([#12179](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12179), [#12181](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12181), [#12182](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12182), [#12185](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12185)–[#12189](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12189)) estão em **Verified**.
  - O [#13118](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13118) (ajustes de UX pro go-live) está em **Rework** com o Kauã:
    - o Danilo reprovou em 25/09 os cenários 5 (saída do wizard pelo navegador) e 8 (carrosséis por grupo);
    - o Kauã corrigiu os dois;
    - o critério do "Indique e ganhe" foi corrigido pelo PO em 28/09;
    - a API e o front precisam subir juntos.
  - O bug [#13425](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13425) (edição de símbolo no caça-níquel) está em **Refinement**, 3 pts, com a causa provável já mapeada.
- **🆕 Apresentação do portal + revisão de UX** (data não informada, resumo recebido em 02/10): as regras de negócio estão aprovadas, mas a experiência não está fechada. Os 5 grandes temas, todos ainda sem card:
  - landing page antes do cadastro (com página e QR Code por campanha);
  - gamificação dentro do domínio Avenida (integração com o site, com o Marcos);
  - design + Mobile First (o #13452 cobre parte e está em Verified);
  - analytics do funil inteiro;
  - elegibilidade regional antes de jogar.

  Ver [resumo](gamificacao/2026-10-02-resumo-apresentacao-portal-gamificacao.md).
  - **Cards criados em 02/10** (Kauã, Sprint 30, Ready for Dev, épico #11950):
    - [#13464](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13464) landing page antes da identificação: 5 pts, mock necessário e não feito, layout depende das artes;
    - [#13465](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13465) QR Code por campanha: 3 pts, depois do #13464;
    - [#13466](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13466) domínio Avenida: 5 pts, 🔴 bloqueado pelo Marcos/site;
    - [#13467](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13467) funil de analytics: 5 pts, depende da conta do GA e do plano de tags com o Marketing;
    - [#13468](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13468) não pedir identificação de novo: 3 pts, risco de LGPD;
    - [#13469](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13469) elegibilidade regional: 5 pts, 🔴 falta decidir como identificar a região.
- **Decisões pendentes:**
  - observações do Danilo: contador de jogadas e checklist que aceita início e fim no mesmo dia;
  - compra mínima fixa no código e arquivo .ics: entram no card ou não;
  - LGPD do login por CPF + data de nascimento (jurídico);
  - banner por campanha;
  - permitir várias campanhas simultâneas do mesmo jogo.
- [contexto](gamificacao/contexto.md)

#### Conciliação Fase 2
- **Status (29/09):** módulo RH em produção desde a GMUD de 31/08. Ainda tem itens voltando do QA:
  - [#12892](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12892) fechamento contábil + integração com Oracle: **Rework**. A migration não rodou em HML, o que originou o [#13426](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13426).
  - [#12399](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12399) performance/homologação técnica: **Rework**.
  - [#12395](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12395), [#12397](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12397) e [#12398](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12398): **Verified**.
  - [#12812](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12812) planilha do Contábil: em Refinement, sem dono. Checar sobreposição com o #12892.
- **Riscos:**
  - job noturno instável: travou por TTL na noite de 27/09 e não rodou em 28/09;
  - bug de "última loja não processada" (Kauã/Danilo, 24/09).
- **Conciliação de depósitos (JB):** os extratos bancários não identificam a loja. A ideia é identificar pela agência, e o JB vai validar com o Ozéias. [#12890](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12890) está em To do.
- [contexto](conciliacao-fase-2/contexto.md)

#### Etiqueta Remarcados / App de remarcação
- **Status (29/09):** os 5 cards do app do coletor ([#13042](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13042)–[#13046](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13046), Donato) estão em **In Test**. O #12506 (tela de pendências no portal) foi aprovado pelo QA em 25/08.
- **Em aberto:**
  - se o app do coletor entra formalmente no épico #12428;
  - repassar ao Bruno a decisão de tamanho de etiqueta.
- [contexto](etiqueta-remarcados/contexto.md)

#### Migração VarRet
- **Status (29/09):** lote 2 em produção desde 31/08. Ainda tem itens em **Rework** com o JB:
  - [#12437](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12437) Demonstrativo de Caixa;
  - [#12484](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12484) exportações Excel/PDF via worker + e-mail.
- **Pendência:** validar o card do JB de Migração Var Ret.
- [contexto](migracao-varret/contexto.md)

### 🧪 Em homologação

#### API Retaguarda — incidente de instabilidade
- **Status (29/09):** os 5 cards de contenção ([#12902](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12902)–[#12906](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12906), Fernando) e o [#13115](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13115) (conexão dedicada ao VAR, Diego) estão em **Verified**, aguardando GMUD.
- **Em Refinement, sem dono:** [#13117](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13117), resiliência do boot da API quando o Redis está fora (incidente de HML de 17/09).
- [contexto](api-retaguarda-incidente/contexto.md)

#### Tap on Phone + VAR 4G (piloto)
- **Status (última info: 28/08):** piloto em loja desde 10/08. Bugs críticos achados na retro de 28/08 (fatura, acordo, transações canceladas com pagamento ativo). O squad VAR 3.0 está dedicado a estabilizar antes do rollout.
- ⚠️ Sem atualização há um mês.
- [contexto](tap-on-phone-var4g/contexto.md)

#### Markdown / Remarcação de Preços
- **Status (última info: 12/08):** 55%, em homologação com débito técnico. Prazo revisado (15/08) vencido sem confirmação. Roda fora do board da Retaguarda (Victor + área de expansão).
- **Não confundir** com o app de remarcação do Donato.
- ⚠️ Sem atualização há mais de um mês.
- [contexto](markdown-precos/contexto.md)

### 🛠️ Sustentação

#### Portal Retaguarda — evolução contínua (Conciliação, Acessos, Tesouraria)
- **Status (29/09):** fluxo contínuo de melhorias nos épicos #7032 e #6640.
  - **Dev Review:**
    - [#12793](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12793) desbloqueio de usuário/operador pela loja (Diego);
    - [#13112](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13112) reorganização dos menus da Conciliação (Diego);
    - [#12797](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12797) CPF do novo responsável no termo de tesouraria (Fernando).
  - **Doing:**
    - [#13085](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13085) reprocessamento de lojas não listadas (Kauã);
    - [#12795](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12795) reenvio pra aprovação após alteração (JB).
  - **Verified:** [#13017](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13017), [#13032](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13032), [#13056](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13056), [#13058](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13058), [#11933](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/11933), [#11935](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/11935), [#12190](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12190), [#12909](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12909), [#12912](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12912).
  - **Refinement:**
    - [#11941](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/11941) reset de senha de usuário;
    - [#12910](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12910) saldo parcial de caixa derrubando o portal;
    - [#12514](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12514) tamanho do token: ainda no nome do Leonardo, reatribuir.
- **Observação:** o Fernando está sem card (daily de 28/09).

#### SIGA
- **Status (29/09):**
  - **SSO:** subiu em 27/09 e funcionou. Quem tem OTP no sso-hub já usa o novo login.
  - **Sustentação** (#7330, Diego):
    - [#13062](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13062) último quadro do lotacionograma: **Dev Review**;
    - [#13060](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13060) cargo Líder Operações: Done;
    - [#13049](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13049) comparação SigaPub × interno: **Rework** (hoje no nome do Danilo).
  - **Ciacon:** "blocked" (Kovalski, 28/09). O [#12814](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12814) voltou pra To do.
  - **Performance de Indicadores** (#10373): parada.
- **Risco:** o Kovalski está sobrecarregado (SigaPub agora é da Retaguarda). Definir apoio.
- [contexto](siga/contexto.md)

#### Envio de Contas (Portal Conexão)
- **Status (29/09):** em uso. A loja envia a fatura, a IA lê, a Gestão Imobiliária aprova e a OC é criada no Oracle. Os 5 cards do Diego (tag CONEXÃO) estão Done.
- **🆕 Nova fase (TAP e especificação de 28/09): Requisição + OC automáticas.** Ao aprovar a conta, o sistema cria a Requisição no Oracle (uma por conta, uma linha por componente) e, no mesmo processamento, a OC vinculada a ela. O Histórico de Contas ganha a coluna "Nº Requisição".
  - **Parecer de TI:** aprovado com ressalvas (permissões do usuário técnico no Oracle, mapeamento dos campos, falha parcial).
  - **Cards** (filhos do #9745 "Envio de Contas Fase 3", em To do):
    - [#13435](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13435) Requisição automática: 8 pts, **bloqueado**;
    - [#13436](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13436) OC a partir da Requisição + reprocessamento: 8 pts, **bloqueado**;
    - [#13437](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13437) coluna Nº Requisição: 2 pts, pronto.

    Bloqueio dos dois primeiros: permissões do usuário técnico no Oracle, mapeamento dos campos e parecer de Arquitetura.
  - **30/09:** os 3 foram pra **Ready for Dev**, na Sprint 30, com o **Fernando**.
- **Frente relacionada:** Faturas de Concessionárias, que vai alimentar este mesmo fluxo com as faturas de energia capturadas automaticamente.
- [contexto](envio-contas/contexto.md)

#### Automação Planilha Fiscal
- **Status (última info: 31/08):** entregue em 22/06 (épico #11103), em sustentação ativa com bugs recorrentes:
  - "Pendente" falso-positivo;
  - campo Isentas/Não Tributadas;
  - "Loja 01/13 não bate".
- **Em aberto:** triagem do Ozéias dos ~40 cards do Kovalski (prazo 14/08), sem confirmação.
- [contexto](automacao-fiscal/contexto.md)

### 🏁 Feito

#### SSO / Keycloak
- Concluído nos portais; o SIGA entrou em 27/09. Sobra só o teste regressivo [#13055](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13055) (Danilo, Ready for Dev).
- **🆕 Nova rodada de melhorias do sso-hub** (Kovalski, Sprint 30, **Ready for Dev** desde 30/09):
  - link de uso único: já existia no [#13433](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13433), que está na Sprint 29, no template antigo e sem estimativa;
  - [#13448](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13448) mensagens de erro claras ao gerar link: 3 pts;
  - [#13449](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13449) investigação: usuários e grupos direto do Keycloak ou com cópia no banco: 3 pts;
  - [#13450](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13450) cadastro em tela própria: 5 pts, mock pendente.
- [contexto](sso-keycloak/contexto.md)

#### Tesouraria — migração para o novo sistema
- 100% do parque em produção (25/08). Próxima frente: NSU padronizado em 8 dígitos, em release separada.
- **Pendência herdada:** correção do conciliador que duplica saldos da tesouraria. Devo ao Sola a previsão de subida.

#### Engine Fiscal — CNPJ Alfanumérico
- Entregue em 23/06 (13 PBIs). Mantido como referência técnica reutilizável.
- [contexto](engine-fiscal-cnpj/contexto.md)

---

## Frentes do VAR 3.0 sem acompanhamento próximo

Informação do dashboard executivo de 10/08, sem atualização desde então. Confirmar antes de citar:
- **Pix pelo Pinpad (Wesley):** 70%, PIX por TEF em teste ponta a ponta.
- **SmileGo / NeuroTech:** bloqueado. O ambiente de teste do fornecedor não funciona. Ligado ao Overlimit — VAR.
- **Release fiscal (Engine + Portal Automação, Donato):** piloto desde 03/08, última info 95%.
