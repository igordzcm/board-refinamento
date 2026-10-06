# Automação de Faturas de Concessionárias — contexto geral

> Arquivo de contexto do projeto. Ler antes de qualquer reunião sobre este projeto.

## Documentos

- [TAP](TAP_Automacao_de_Faturas_Concessionarias.docx) (28/09/2026, v1.0). Solicitante: Gestão Imobiliária.
- [Especificação Funcional](Especificacao_Funcional_Automacao_de_Faturas_Concessionarias.docx) (28/09/2026, Ozéias Tavares).
- [Plano de modularização da ali-api](2026-09-30-plano-modularizacao-ali-api.pdf) (30/09/2026, Diego, pro Igor e o tech lead). Os anexos citados no PDF ("Mapa de acoplamento" e "Estudo e prova do deploy isolado") não vieram junto.

## O que é

Um robô que busca as **faturas de energia** das lojas nos **portais das concessionárias** e as sobe no [Envio de Contas](../envio-contas/contexto.md) do Portal Conexão. Hoje a equipe entra em cada portal, se autentica, baixa a fatura e faz o upload na mão. Depois do upload, a fatura segue o fluxo que já existe: leitura pela IA, validação manual da Gestão Imobiliária e OC no Oracle.

**Concessionárias no escopo:** EDP, Energisa, Equatorial e Neoenergia, com suas variações regionais. O TAP prevê **usar API quando a concessionária oferecer e automação de tela quando não oferecer**.

**Origem do pedido:** foi este mesmo projeto que o Luiz Spineli pediu pra retomar na daily de 25/09. Nas palavras dele: "é a automação com os portais de energia (...) é entrar lá, sei lá, no portal da Enel e pegar a conta para que o cara não precise entrar". A Enel foi só um exemplo. **O escopo é o do TAP e da Especificação** (EDP, Energisa, Equatorial e Neoenergia). Até 30/09 isso estava registrado como uma frente separada e foi unificado aqui.

## Escopo

**Entra:**
- Agenda recorrente e parametrizável, sem mexer em código. Configuração inicial: dias 05, 15 e 25. Horário a definir.
- Base operacional por loja: concessionária/site, CNPJ, unidade consumidora e credenciais. Só lojas ativas e autorizadas.
- Um conector por concessionária (cada portal tem layout, URL e autenticação próprios).
- Controle de duplicidade por **Site/Concessionária + Loja + CNPJ + Data de Geração**.
- Download da fatura (preferencialmente PDF) e upload automático no Envio de Contas, na loja certa, com tipo Energia. Depois a IA atual faz a leitura.
- Resultado por loja em 4 status: Processado com sucesso, Sem nova fatura, Falha de acesso (inclui MFA/CAPTCHA não automatizável) e Erro de processamento.
- Consolidado ao fim de cada execução, destacando as lojas não processadas.
- Tela de acompanhamento no Portal:
  - resumo por execução;
  - detalhe por loja: Loja, CNPJ, Concessionária/Site, Data/Hora, Status, Data geração, Upload, Detalhe/Arquivo;
  - link pro documento já armazenado no Envio de Contas, sem guardar cópia.
- Falha não impede as outras lojas, e a loja volta a ser elegível na próxima execução.

**Não entra:**
- automação da conferência e aprovação depois da IA;
- automação até o Oracle nesta entrega;
- contas que não sejam de energia;
- mudança no motor de IA;
- quebra de CAPTCHA/MFA quando não houver forma segura;
- alertas por e-mail/SMS (evolução futura).

## Status atual (29/09/2026) — TAP e especificação recebidos, pareceres pendentes

- **Parecer de TI:** pendente.
- **Parecer de Arquitetura:** pendente.
- **Prazo, custo e tempo de desenvolvimento:** "em levantamento".
- **Tecnologia e infraestrutura:** "a definir pela Arquitetura".
- **Credenciais:** armazenamento seguro obrigatório. O cofre ainda vai ser definido com Arquitetura e Segurança, e isso precisa estar resolvido antes de ir pra produção.

## 🆕 Plano de modularização da ali-api (Diego, 30/09) — pré-requisito proposto pra captura

**Decisão técnica já alinhada:** a captura vai ser feita **na ali-api**, o back-end do Portal Conexão que hoje faz a leitura das contas pela IA e a criação da OC no Oracle. O deploy da captura não pode afetar os outros módulos.

**Problema:** hoje a ali-api tem **uma imagem, um pipeline e um deploy único**, então qualquer commit reinicia a API e o worker juntos. Nos últimos 12 meses, 54% dos commits (52 de 97) mexeram no Oracle, e cada um reiniciou também a leitura pela IA, que só mudou 5 vezes no período.

**Acoplamentos mapeados:**
- **Deploy único:** API, worker e infra (Redis, logs, nginx) no mesmo compose.
- **Configuração única:** 12 segredos obrigatórios, e nenhum processo sobe sem todos.
- **Worker único:** a leitura e a OC rodam no mesmo processo.
- **API carregando tudo:** 105 módulos, incluindo a leitura por IA, por causa de 2 rotas antigas que o WordPress não chama mais.
- **Disco compartilhado:** a API e o worker precisam ficar na mesma máquina.
- **Cache do Oracle no Redis sem contrato.**

O que ajuda: a API e o worker já conversam por fila com contratos versionados, e a leitura e o Oracle só dividem 12 módulos de base. Isso deixa a separação viável e barata.

**Proposta:** manter **um repositório**, mas separar o deploy em **unidades independentes**:
- API;
- worker de leitura (IA/Textract);
- worker de Oracle (OC);
- infra (Redis, logs, nginx);
- **Captura**, uma unidade nova que recebe só o cofre de credenciais e o acesso ao WordPress.

**Passos** (P = até 2 dias, M = 3 a 5 dias, G = mais de uma semana):
- **M0 Decisão (P):** ADR com as unidades e confirmação no log de que as rotas antigas não têm quem chame.
- **M1 Higiene do deploy (M):** segredos fora da imagem, deploy pela tag, infra num compose próprio.
- **M2 Rotas antigas (P):** remover `/energy-extract` e `/extract-water`. A API cai de 105 pra 61 módulos e deixa de precisar das chaves da AWS.
- **M3 Configuração por unidade (M):** cada unidade sobe só com as próprias variáveis.
- **M4 Worker dividido (P/M):** um worker de leitura e um de Oracle.
- **M5 Pipeline por unidade (M):** só é publicado o que mudou.
- **M6 e M7 (opcionais, depois):** tirar o Oracle do processo da API; o arquivo viajar na mensagem, sem disco compartilhado.

A ordem é M0 → M5, e M1 e M2 podem andar juntos.

**Limite:** até o M6, uma mudança no Oracle ainda reinicia a API. O M4 e o M5 protegem a leitura e a captura, não a API.

**Segurança da mudança:**
- um passo por PR, com ADR e a suíte de testes da ali-api;
- HML antes de PRD, e PRD à noite;
- o worker antigo continua no ar até os novos provarem em HML;
- as filas, as rotas usadas pelo WordPress e os callbacks não mudam.

O isolamento foi testado localmente em 30/09: 3 deploys seguidos com 446 requisições e 0 falhas.

**Impacto no cronograma do épico #13434:**
- **Sprint 30:** M0, M1 e M2. O discovery (#13438) segue em paralelo.
- **Sprint 31:** M3, M4 e M5, mais a fundação da captura (chave do robô no Conexão, cliente do Conexão, cofre, navegador, banco de provas).
- **Sprint 32:** #13439 base de lojas, #13440 agenda, início do #13441 motor e do #13443 conector EDP.
- **Sprint 33 em diante:** os outros conectores e a tela.
- **Resultado:** o código da captura começa **cerca de uma sprint depois** do planejado, e o discovery não atrasa.

**Riscos e dependências:**
- mexer no deploy de produção;
- um processo Python a mais na VM (a infra precisa confirmar a folga);
- pipelines novos que precisam ser registrados e autorizados no Azure DevOps;
- onde construir as imagens (a infra decide);
- alguém de fora ainda chamar as rotas antigas (o M0 confere).

**Decisões pedidas:**
- **Ao Igor:**
  - aprovar a trilha como card(s) próprio(s), **antes** do código da captura;
  - aceitar o atraso de cerca de uma sprint no épico;
  - criar os cards da trilha.
- **Ao tech lead:**
  - aprovar as unidades, a ordem M0–M5 e os ADRs;
  - autorizar a remoção das rotas antigas;
  - decidir sobre o M6 e o M7.
- **À infra e ao Azure** (via tech lead): folga das VMs, onde construir as imagens e registro dos pipelines.

**Status (30/09):** o Igor aprovou a trilha. Cards criados com o Diego, na Sprint 30, filhos do #13434:
- #13454 M0 (2 pts);
- #13455 M1 (5 pts);
- #13456 M2 (2 pts);
- #13457 M3 (3 pts);
- #13458 M4 (3 pts);
- #13459 M5 (5 pts).

Os 6 estão em Refinement, por decisão do Igor. O M5 também está bloqueado pela administração do Azure DevOps (registro dos pipelines).

Continuam pendentes do tech lead e da infra:
- aprovação do ADR e das rotas;
- onde construir as imagens;
- folga da VM.

## Cards (criados 29/09, épico [#13434](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13434), tag CONEXÃO; desde 30/09 em Ready for Dev, Sprint 30, com o Diego)

- #13438: levantamento técnico e arquitetura, bloqueado. Destrava os demais.
- #13439: base de lojas e acessos.
- #13440: agendamento.
- #13441: motor de execução.
- #13443–#13446: conectores EDP (modelo), Energisa, Equatorial e Neoenergia.
- #13442: tela de acompanhamento.

## Em aberto

- [ ] Quem é o "José" que, segundo o Diego (25/09), já tinha comentado informalmente sobre essa automação.
- [ ] **Plano de modularização da ali-api:** aprovar ou não a trilha M0–M5 antes do código da captura, aceitar ou não o atraso de cerca de uma sprint, e criar os cards da trilha.
- [ ] Arquitetura: se usa API ou automação de tela em cada portal. Onde a captura roda já está definido: na ali-api, como unidade própria.
- [ ] Cofre de credenciais (Arquitetura + Segurança).
- [ ] Horário das execuções.
- [ ] O que fazer quando o dia configurado não existe no mês (ex.: dia 31).
- [ ] Como a Gestão Imobiliária mantém a base de lojas (tela, planilha?) e quem faz a carga inicial.
- [ ] Quais perfis acessam a tela de acompanhamento.
- [ ] Levantamento de quais portais exigem MFA ou CAPTCHA, que define quanto dá pra automatizar de fato.
- [ ] Quantidade de lojas e unidades consumidoras por concessionária, e quem mantém essa base (Gestão Imobiliária).

## Riscos (da especificação)

- Mudança de layout ou de autenticação nos portais para a captura.
- Credenciais expiradas geram muitas falhas de acesso.
- MFA/CAPTCHA pode deixar parte das lojas de fora.
- Falha de duplicidade pode gerar upload repetido.
- Falha entre o download e o upload.
- Credencial exposta em log.
- O tempo total da rotina cresce com o número de lojas.

## Reuniões

(nenhuma ainda)
