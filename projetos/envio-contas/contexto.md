# Envio de Contas (Portal Conexão) — contexto geral

> Arquivo de contexto do projeto. Ler antes de qualquer reunião sobre este projeto.

## O que é

Módulo **Envio de Contas** do **Portal Conexão**. As lojas enviam as faturas de consumo (água, energia), e uma IA lê cada fatura e identifica os dados gerais e os itens de cobrança. O analista da **Gestão Imobiliária** revisa e aprova, e a integração cria a **Ordem de Compra no Oracle**, com consumo, multas, juros e encargos em linhas separadas.

Fluxo atual: loja envia → revisar contas → Gestão Imobiliária revisa e aprova → aparece em "Visualizar" → OC criada no Oracle.

## Dono

- **Dev:** Diego Oliveira Andrade Rafael.
- **Área:** Gestão Imobiliária ("as meninas"), com o Ozéias.

## Status atual (30/09/2026) — em uso, com duas evoluções

Hoje o processo depende de **a loja enviar a conta**. Duas evoluções estão abertas:
- **Automação de Faturas de Concessionárias:** um robô busca as faturas de energia nos portais das concessionárias e faz o upload aqui, sem depender da loja. Ver [../faturas-concessionarias/contexto.md](../faturas-concessionarias/contexto.md).
- **Requisição + OC automáticas no Oracle:** ver a seção abaixo.

**Back-end:** a **ali-api** faz a leitura das contas pela IA e a criação da OC no Oracle. Em 30/09, o Diego propôs separar o deploy dela em unidades independentes: API, worker de leitura, worker de Oracle, infra e captura. O plano completo está em [../faturas-concessionarias/](../faturas-concessionarias/contexto.md), e afeta também os cards de Requisição + OC.

- 18/09: fluxo completo testado com o Danilo e apresentado à área. A reunião correu muito bem ("uma das melhores que a gente teve").
- 15/09: PR no sistema de conexão com o ERP Oracle, esperando review do Valdo. Deve "resolver de vez" a abertura de contas no Oracle.
- 23/09: Diego ia falar com o Ozéias sobre subir a atualização do Conexão.

## 🆕 Nova fase — Requisição + Ordem de Compra automáticas (TAP e especificação de 28/09/2026)

Documentos: [TAP](TAP_Envio_de_Contas_Requisicao_OC.docx) (solicitante: Expansão/Imobiliária) e [Especificação Funcional v2](Especificacao_Funcional_Envio_de_Contas_Requisicao_OC_v2.docx) (Ozéias Tavares).

**Problema:** hoje, ao aprovar uma conta, o Conexão cria só a OC no Oracle. A área também precisa de uma **Requisição** pra toda conta, e abre na mão. Isso pesa mais em Multa/Juros, porque a Requisição é a referência pra pedir verba ao Financeiro.

**O que muda:**
- Ao aprovar a conta, o sistema cria automaticamente **uma Requisição por conta**, com uma linha por componente (Consumo, Taxa de Lixo e/ou Multa/Juros). Isso vale pra toda conta, mesmo com verba já provisionada.
- **No mesmo processamento**, cria a **OC a partir dessa Requisição**, herdando as linhas e mantendo o vínculo. O vínculo é sempre pelo identificador que o Oracle devolve, nunca por valor ou semelhança.
- O Conexão guarda os números da Requisição e da OC.
- **Histórico de Contas:** entra a coluna "Nº Requisição" antes de "Nº OC", na ordem Data/Hora | Loja | Tipo | Mês Ref. | Nº Requisição | Nº OC | Responsável | Ação. Mostra "—" quando ainda não há número.
- **Falha parcial:** se a Requisição foi criada e a OC falhou, a Requisição é preservada e o reprocessamento cria só a OC, sem duplicar. Se a Requisição falha, a OC não é criada.
- **Auditoria:** registra conta, loja, data/hora, aprovador, os dois números, o resultado e a etapa da falha.

**Fora:**
- solicitação de verba ao Financeiro (continua manual, usando o nº da Requisição);
- mudança nas regras de aprovação da conta;
- regras de orçamento/verba;
- redesenho do Histórico.

**Pessoas:**
- Giulyana Amorim Barbosa Costa (usuária-chave);
- Isa / Maria Isabella Roque Lombardi (validação do negócio);
- Ozéias (responsável);
- Diego (implementação);
- Diego Aoki (aprovação).

**Parecer de TI:** aprovado com ressalvas. Condicionado a validar as permissões do usuário técnico no Oracle (requisitante + comprador), o mapeamento dos campos da Requisição e o reprocessamento em falha parcial. Arquitetura pendente. Prazo em levantamento.

**Cards da nova fase** (criados 29/09, filhos do #9745 "Envio de Contas Fase 3"):
- [#13435](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13435): Requisição automática, bloqueado.
- [#13436](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13436): OC a partir da Requisição, bloqueado.
- [#13437](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13437): coluna Nº Requisição.

## Cards anteriores (todos Done, tag CONEXÃO, Diego)

- [#12255](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12255): disparo de e-mails de cobrança só para lojas reais + link do "Resolve Aqui".
- [#12426](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12426): agrupamento automático das linhas da fatura na OC do Oracle.
- [#12624](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12624): classificação e dados obrigatórios (Data da Leitura, CNPJ) antes da OC.
- [#12899](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12899) (Bug): lojas não apareciam no módulo.
- [#13013](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13013): ajustes na listagem, no histórico e no upload de arquivos pelas lojas (condição de pagamento, lote limitado a 20 MB).

## Reuniões

- 17/09: agenda do Diego com a Gestão Imobiliária e o Ozéias sobre o sistema do Conexão.
- 18/09: apresentação do fluxo completo à área. Ver [../dailies/2026-09-17-a-23-digest-retaguarda.md](../dailies/2026-09-17-a-23-digest-retaguarda.md).
