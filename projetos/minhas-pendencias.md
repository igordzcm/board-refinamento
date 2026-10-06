# Pendências dos projetos — Var Retaguarda

> O que está em aberto em cada projeto e depende de uma ação: decisão a tomar, conversa a marcar, card a criar ou refinar, resposta que alguém deve. Status geral de cada projeto fica no `contexto.md` da pasta dele; aqui só o que precisa de alguém agir. Ao resolver um item, apague a linha.
>
> Situação conforme as dailies até 02/10/2026 e o ADO em 29/09/2026. Confira o card antes de agir.

## Time e processo

- [ ] **Distribuir os cards em Ready for Dev sem dono** para quem terminar primeiro: [#13419](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13419) (variáveis dos pipelines, combina com o Kovalski), [#13425](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13425) (bug do caça-níquel), [#13117](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13117) (boot da API sem Redis).
- [ ] **Alinhar com o Ozéias o que está planejado** antes de distribuir cards novos, para não passar card sem relevância. Em 28/09 o Fernando estava sem card e o Kovalski tinha espaço.
- [ ] **Formalizar os cards "livres" em Ready for Dev**, para cada um pegar quando terminar o que está fazendo em vez de ter tudo pré-atribuído (levantado na planning de 16/09).
- [ ] **Combinar como dev e área avisam o PO quando mudam algo que está no card**, para o card ser atualizado antes do teste (pedido do Kauã em 28/09, depois do caso "Indique e ganhe" no #13118).
- [ ] **Levar para a retro a validação de PR**: hoje usam IA para validar PR e não está funcionando bem. Acompanhar também a fila de code review (16 cards parados na retro de 15/09).
- [ ] **Enviar ao Spin as atas das retros de 01/09 e 15/09.** A de 01/09 fala da compressão de prazo da Conciliação Fase 2 (de 3 meses para 2 dias). Atas em [reviews-retros-planning/](reviews-retros-planning/).
- [ ] **Falar com o Spin sobre os testes automatizados do Danilo.**
- [ ] **Levar à diretoria a necessidade de um banco de teste separado para a Tesouraria**: vários devs disputam o mesmo ambiente (relato do Nicolas, VAR 3.0, em 15/09).
- [ ] **Endereçar "se tudo é urgente, nada é urgente"**, reclamação número 1 da retro do VAR 3.0 de 28/08. Ver [reviews-retros-planning/2026-08-28-retro-var.md](reviews-retros-planning/2026-08-28-retro-var.md).
- [ ] **Reatribuir o [#12514](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12514)** (tamanho do token quebrando a permissão de rotas): em Refinement, ainda no nome do Leonardo, que saiu em 14/09.

## Motor de Descontos

- [ ] **Nomear os 3 donos externos do cadastro por SKU/grade.** Os cards do Portal ([#12913](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12913)–[#12916](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12916)) estão em Verified, mas a funcionalidade não chega às lojas sem:
  1. quem cria as triggers `KAFKA_PRO0144`/`TG_PRO0144`;
  2. quem consome o `OPERACAOLOG` para replicar à loja;
  3. quem assina a paridade do motor E1 Java.

  Levar ao Spin e ao Ozéias. Ver [motor-descontos/desconto-sku/PLANO-IMPLEMENTACAO-DESCONTO-SKU.md](motor-descontos/desconto-sku/PLANO-IMPLEMENTACAO-DESCONTO-SKU.md), seção "Dependências que não destravamos sozinhos".
- [ ] **Confirmar o escopo do [#13422](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13422)** (UI do Motor com base na Gamificação, 8 pts): hoje traz o estado de lista vazia e o rascunho automático no wizard. Decidir se é só isso ou se entra algo mais visual.
- [ ] **Confirmar com o Caixeta e os QAs a validação da PRO013 no VAR.** Destrava o [#13429](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13429) (reativar campanha por departamento).
- [ ] **Decidir o mock do [#13428](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13428)** (restringir campanha global a lojas específicas): é fluxo de tela novo. Definir de onde o usuário começa e como aparece o passo de encerrar a campanha original.
- [ ] **Mudar o [#13424](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13424) para Removed pela interface do ADO.** O trabalho foi entregue no #12914 e no #12916, e o card está como Done.
- [ ] **Avisar o Fabio que a verificação de conflito de itens com as campanhas PRO013 já existe no código.** Na call de 08/09 ele apontou como falha.
- [ ] **Responder ao Arthur** com o que o Fabio disse na call de 08/09: campanha por departamento já está no planejamento; cancelamento real de campanha não existe e o mecanismo foi mantido; edição de lojas de campanha ativa tem dois cenários. Confirmar também que "campanha por grade" é o mesmo projeto que ele chama de "cadastro por SKU". Ver [motor-descontos/2026-09-08-call-fabio.md](motor-descontos/2026-09-08-call-fabio.md).
- [ ] **Alinhar com Thalison e Fabio o job de duplicação de desconto/cupom**, desativado desde 24/08 sem reativação formal. Ver [motor-descontos/contexto.md](motor-descontos/contexto.md), seção "Risco ativo".
- [ ] **Bug de desconto duplicado do lado da loja** (trazido pelo Caixeta em 01/09): o Gustavo ia abrir card no VAR. Confirmar se abriu e se é a mesma causa do job acima.
- [ ] **Resolver o cadastro da campanha #923**, que ficou global quando deveria ser de um grupo de lojas (levantado pelo Fabio em 08/09).

## Gamificação

- [ ] **Confirmar o resultado do go-live previsto para 04/10** com o Kauã e o Danilo: se subiu e o que ficou pendente.
- [ ] **[#13118](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13118) (ajustes para o go-live, em Rework com o Kauã): decidir o que entra no card e o que vira card próprio.**
  - Observações do Danilo (25/09): o contador de jogadas parece somar jogadas de campanha oculta; o checklist de publicação aceita início e fim no mesmo dia, mas o servidor recusa.
  - Das reuniões de 17 e 18/09 com o Ozéias: compra mínima fixa no código; arquivo de agenda (.ics) ao gerar o cupom.
  - "Não ter bloco de campanha por quantidade": ninguém lembrou o que era. Confirmar com o Ozéias ou descartar.
- [ ] **Conversar com o Marcos (site Avenida)** sobre colocar as landing pages da gamificação no domínio e no site Avenida, a maior dependência da revisão de UX. Ver [gamificacao/2026-10-02-resumo-apresentacao-portal-gamificacao.md](gamificacao/2026-10-02-resumo-apresentacao-portal-gamificacao.md).
- [ ] **Decisões com o CRM**: quais campos do cadastro são obrigatórios e como campanhas segmentadas por CPF aparecem, ou não, no site aberto.
- [ ] **Levar ao jurídico a LGPD do login por CPF + data de nascimento**: o nome do cliente aparece depois do login sem segunda validação. Ver [gamificacao/2026-09-02-demo-crm-ana-marcos.md](gamificacao/2026-09-02-demo-crm-ana-marcos.md).
- [ ] **Ozéias deve duas decisões da demo de 02/09**: se dá para ter várias campanhas ativas do mesmo jogo ao mesmo tempo, e se o banner por campanha aceita imagem própria.
- [ ] **Ana e Marcos devem a bateria de testes em homologação** combinada na demo de 02/09.

## Overlimit

- [ ] **Fechar as regras do card da tela de upload do RPA, [#13447](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13447)** (5 pts):
  - nova carga substitui, acumula ou atualiza por conta/CPF?
  - linhas inválidas: aceita em parte ou recusa o arquivo inteiro?
  - faixa válida da porcentagem;
  - conta ou CPF repetido no arquivo é erro?
- [ ] **Tabela do Overlimit na base de QA da Retaguarda**: o Gui monta o modelo de dados e manda por e-mail ao Thalison, que cria a tabela.
- [ ] **Decidir o uso das datas de vigência e validade.** As colunas já entram na tabela.
- [ ] **Checagem de crédito no VAR** depende do ambiente de teste da NeuroTech (SmileGo), parado há semanas.

Desenho técnico em [overlimit/contexto.md](overlimit/contexto.md).

## Faturas de Concessionárias e Envio de Contas (Portal Conexão)

- [ ] **Destravar o levantamento técnico [#13438](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13438)**, que segura os outros 8 cards do épico #13434: cobrar os pareceres de TI e Arquitetura e a definição do cofre de credenciais.
- [ ] **Confirmar com a Gestão Imobiliária se alguma loja é atendida pela Enel.** A Enel não está na lista do TAP (EDP, Energisa, Equatorial, Neoenergia); se houver loja, entra mais um conector.
- [ ] **Definir a plataforma do robô, o horário das execuções e quais portais têm MFA ou CAPTCHA.**
- [ ] **Envio de Contas, [#13435](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13435) e [#13436](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13436) bloqueados**: permissões do usuário técnico no Oracle, mapeamento dos campos e parecer de Arquitetura. O fluxo intermediário descoberto em 29/09 com a Gestão Imobiliária está em validação com o Ozéias.

Ver [faturas-concessionarias/contexto.md](faturas-concessionarias/contexto.md) e [envio-contas/contexto.md](envio-contas/contexto.md).

## Conciliação Fase 2

- [ ] **Job noturno**: travou por TTL depois de mudança no Kong. Confirmar com o Kauã se a correção entrou na GMUD. Há também relato de que a última loja não é processada (daily de 24/09): se for bug novo, criar card.
- [ ] **Revisar o [#12892](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12892) (fechamento contábil) com o Alex, do Contábil.** Em Rework com o Kauã.
- [ ] **Checar a sobreposição entre o [#12812](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12812) e o #12892** antes de estimar o #12812, e esclarecer "Arco" vs. planilha Oracle com o Diego e o Ozéias.
- [ ] **Conciliação de depósitos**: o JB valida com o Ozéias a identificação da loja pela agência ([#12890](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12890)).
- [ ] **Decidir com o Ozéias se o valor positivo é validado já na tela de conciliação de caixa**, e não só na aprovação do RH (sugestão do Wagner, 13/08).
- [ ] **Esclarecer com o Wagner a fila do RH pós-reversão.** O dono provável era o Leonardo; definir quem assume.
- [ ] **Fechar os cards em Bloqueado** quando a Fase 2 confirmar que não são mais necessários (combinado com o Kauã em 13/08).
- [ ] **Francisco Sola espera a previsão de subida da correção do conciliador que duplica saldos da Tesouraria** (JB desenvolvendo). Sem resposta desde 17/09.

## SIGA e SSO

- [ ] **Definir apoio ao Kovalski** no Siga e no SigaPub: ele sinalizou que não dá conta sozinho.
- [ ] **Rework do Siga ([#13049](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13049))**: manter idêntico à produção ou tratar como bug. Confirmar depois de ler o que o Danilo enviou.
- [ ] **Ciacon ([#12814](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12814))** bloqueado pelo fornecedor, sem previsão. Entender por que voltou para To do.
- [ ] **Bug na troca de senha** (erro de LDAP, data de troca em 1600): repassar a quem cuida do AD.
- [ ] **Decidir o mock do [#13450](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13450)** (cadastro de usuário e grupo em tela própria) e qual é a dor da tela atual.
- [ ] **Passar o [#13433](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13433)** (link de uso único) para o template atual e estimar.
- [ ] **Acesso ao portal de administração do Siga (Apex Oracle)** se perdeu com a saída de quem o tinha. Definir quem recupera.

## Infra: pipelines e deploy

- [ ] **Certificado digital vence em meados de novembro.** Criar com o Kovalski os cards para integrar a pipeline de certificado aos outros portais.
- [ ] **[#13423](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13423) com estado errado**: está Verified, mas o Kovalski relatou que seguia travado pela permissão do devbox. Conferir quem mudou e voltar ao estado certo.
- [ ] **[#13426](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13426) (migrations no deploy): responder o cenário 5.** A aprovação manual antes do deploy de produção basta, ou a GMUD exige passo próprio para alterar o banco? Perguntar ao Spin ou ao Kovalski.

## API Retaguarda e Portal Retaguarda (sustentação)

- [ ] **Refinar e atribuir o [#13117](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13117)** (boot da API quando o Redis está fora). Ver [api-retaguarda-incidente/contexto.md](api-retaguarda-incidente/contexto.md).
- [ ] **Refinar a parte de usuário do [#11941](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/11941)** (reset de senha): a de operadores foi feita; a de usuário usa outro mecanismo e ainda não tem solução.
- [ ] **Refinar o [#12910](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12910)** (saldo parcial de caixa derrubando o portal).

## Etiqueta Remarcados

- [ ] **Confirmar com o Donato e o Ozéias se o app do coletor entra no épico #12428.** Os cards #13042–#13046 foram ligados a ele como melhor palpite.
- [ ] **Confirmar que o Bruno recebeu a decisão de tamanho de etiqueta**: pequena em produção, grande via seletor em homologação.
- [ ] **Limitar o acesso de homologação da área de remarcação** a gerente e analista principal (hoje pedem para 8 pessoas, todo dia).

## Dashboard CDs

- [ ] **Planilha corrigida da Maria**: confirmar com o JB se ela respondeu em 18/09. Destrava o refino do #12509, #12510, #12511 e #12513.
- [ ] **Alinhar com o Sergio da Silva** para refinar o [#12512](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12512) (relatório WMS com nova data).
- [ ] **Novo Dashboard CDs (Marcelo)**: reunião para definir escopo, dados e prazo, e se é dashboard novo ou evolução do atual.

## Migração VarRet

- [ ] **Validar o card do JB** ([#12437](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12437) e [#12484](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12484) em Rework). Ver [migracao-varret/contexto.md](migracao-varret/contexto.md).

## Engine

- [ ] **Acesso à máquina de produção do webhook**: o Donato não tem acesso e ninguém sabe a senha; o chamado depende de terceiros.
- [ ] **Pegar com o Donato o documento de refatoração da Troca** (devolução e troca de produto).

## Pesquisa Colaboradores (RH)

- [ ] **Nova call com a Thaís** já com proposta de telas e textos. Ver [pesquisas-colaboradores/2026-09-11-call-thais-francisco.md](pesquisas-colaboradores/2026-09-11-call-thais-francisco.md).
- [ ] **Levar ao jurídico o disparo das pesquisas por contato pessoal** (e-mail e celular da folha) e o anonimato. Pode mudar o rumo do projeto.
- [ ] **Definir dono para a criação automática de usuário via Senior.**

## Automação Planilha Fiscal

- [ ] **Ozéias deve a triagem dos ~40 cards de backlog** (prazo era 14/08). Ver [automacao-fiscal/contexto.md](automacao-fiscal/contexto.md).
