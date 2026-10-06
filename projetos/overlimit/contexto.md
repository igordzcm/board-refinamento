# Overlimit — contexto geral

> Arquivo de contexto do projeto. Atualizado a partir do dashboard executivo e das transcrições de daily do VAR 3.0 (05/08 e 06/08). Ler antes de qualquer reunião sobre este projeto.

## O que é

Funcionalidade de crédito na venda (Overlimit) no PDV VAR 3.0.

## Dono

**Gui Oliveira**.

## Frentes

O projeto tem duas frentes:

- **Overlimit — VAR:** oferta e uso do crédito no PDV VAR 3.0. É do Gui, no squad VAR 3.0, e saiu da release do piloto em 21/09.
- **Overlimit — RPA:** portal do RPA de cartões. A área de Cartões sobe um CSV com os clientes elegíveis, o conteúdo vai pra uma tabela do RPA e o VAR consulta essa tabela. É da Retaguarda e é **a frente que vamos fazer agora** (decisão do Igor em 29/09). Aguardando definição do Spin pra criar os cards. Desenho técnico em "Status atual" abaixo.

## Status atual (25/09/2026) — frente Retaguarda aberta, desenho técnico definido, prazo curto

> Fontes: daily Retaguarda de 25/09 ([`../dailies/2026-09-24-a-25-digest-retaguarda.md`](../dailies/2026-09-24-a-25-digest-retaguarda.md)), anotações do alinhamento do Igor em 25/09, digest VAR 3.0 de 17–22/09 ([`../dailies/2026-09-17-a-22-digest-var3.md`](../dailies/2026-09-17-a-22-digest-var3.md)).

**Contexto:** Overlimit é o crédito emergencial do **Cartão Avenida**. No VAR 3.0, a área de negócio mudou o escopo em 21/09 e o Overlimit **saiu da release do piloto**, com retrabalho de front e de testes (Gui). Em 25/09, o Spineli pediu à Retaguarda a parte do **portal do RPA de cartões**: "a mesma ideia do blacklist, só que pra fornecer um produto". **Prazo pedido: segunda/terça (28–29/09).** O detalhamento fica com JB e "Higuinho", falando com Gui e Gustavo. Antes de iniciar, falta confirmar com o Gui. Mais pra frente, o valor deve vir automatizado por um projeto chamado **"Behavior"**.

### Desenho técnico combinado

- **Carga:** a área de **Cartões sobe um CSV** no portal do RPA, e o conteúdo vai para uma tabela do RPA (mesmo modelo do blacklist).
- **Consulta:** o **Gui sobe um serviço** que consulta essa tabela. O **VAR chama o back**, que consulta a tabela do RPA.
- **Identificador do cliente:** id do cliente = **número da RPE**.
- **Campos da tabela:** `idconta`, `dt vigencia`, `cpf`, `porcentagem`, `limite atual`, `validade`, `dt aceite`, `loja aceite`, `status`.
- **`over_status`:**
  - `0` = não foi ofertado ou não aceitou
  - `1` = overlimit ativo

### Decisões de 29/09/2026 (Igor) — frente RPA

- **Tela (30/09):** além do upload, precisa de uma **tabela com todos os CPFs já cadastrados** na base do Overlimit.
- **CSV:** traz **id da conta, CPF e porcentagem**. A área sobe o arquivo numa tela do **portal do RPA**. O código do RPA não está neste workspace, então o card não tem nota técnica.
- **Datas de vigência e de validade:** talvez não sejam necessárias. **As colunas vão existir na tabela mesmo assim**, e a decisão de usar ou não fica pra depois.
- **Tabela:** vai ser criada primeiro na **base da Retaguarda de QA**, com o **Thalison** (DB). Isso fica fora do card.
  - O **Gui** pega o modelo de dados e monta o e-mail pro Thalison criar a tabela na base de QA.
  - O Igor fala com o Thalison.

**Card:** [#13447](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13447), "[RPA][OVERLIMIT] Upload de CSV de clientes elegíveis ao Overlimit no portal RPA". Filho do #12110 "Portal RPA" e relacionado ao blacklist (#9220, #9528) e ao #12117 (VAR). O #11289 "Overlimit" (projeto "Projetos - Geral", épico RPA) é só um guarda-chuva sem descrição.

### Em aberto

- [ ] **Regras da carga do #13447:** nova carga substitui, acumula ou atualiza? Linhas inválidas: aceitar em parte ou recusar tudo? Qual a faixa da porcentagem? Duplicados no arquivo são erro?
- [ ] **Decidir se as datas de vigência e de validade vão ser usadas.** As colunas já nascem na tabela.
- [ ] **Gui → e-mail pro Thalison com o modelo de dados**, pra criar a tabela na base da Retaguarda de QA.
- [ ] **Igor → falar com o Thalison** sobre a criação da tabela em QA.

## Status anterior (08/09/2026) — não mais bloqueado, tratado como prioridade semanal ativa

> Fontes: [`../dailies/2026-09-08-digest-var3.md`](../dailies/2026-09-08-digest-var3.md), [`../prioridades-sprint.md`](../prioridades-sprint.md) (seção "Resolvido desde a última atualização", 31/08).

**A trava de fundo (fornecedor RPE) já foi resolvida.** Per o `prioridades-sprint.md`: a RPE liberou credenciais/webhooks em 31/08; testes de endpoint em produção já começaram, direto no Kong, sem precisar de credencial de teste — Overlimit saiu da lista de bloqueios críticos. Isso bate com o digest VAR 3.0 de 01/09 ("RPE liberou as credenciais de produção pra uso direto") e de 04/09 (Gui Oliveira retomou o projeto, backend com endpoint adicional já pronto, trabalhando no front de validação de elegibilidade).

**Confirmado como prioridade ativa em 08/09:** na daily VAR 3.0, o PO Gustavo listou Overlimit entre os itens que precisam subir antes do piloto de 14/09 (junto com tratamento de erros, consulta automática, Pix no TEF). Não é mais tratado como bloqueado — é tratado como trabalho corrente da semana.

**O "5% — bloqueado" de 12/08 abaixo está desatualizado e não deve mais ser citado como status atual.** O dashboard executivo traz 45% — confirmado via ADO (16/09) que é a mesma frente: o dono é **Guilherme Oliveira de Souza**, o "Gui Oliveira" deste arquivo (não é o Caixeta, essa dúvida antiga está resolvida).

**Confirmado via ADO (16/09) — SmileGo/NeuroTech é parte deste mesmo projeto, não um bloqueio solto.** Todos os PBIs de Overlimit (#12117-#12123) e o card #12104 ("Mapeamento dos endpoints e retornos da SmileGO na P1") compartilham o mesmo épico pai, **#4195 "Melhorias"**, e o mesmo dono (Guilherme Oliveira). SmileGo é o intermediário atual da checagem de crédito — recebe o CPF e direciona pro motor de crédito de verdade, a **NeuroTech**. O card #12104 é o trabalho de cortar esse intermediário e chamar a NeuroTech direto; está com **Bloqueado = Sim** no ADO, responsável Wesley Silva Alves, por causa do ambiente de teste do fornecedor não funcionar. Isso trava a checagem de crédito de que o Overlimit depende — ver bloqueio correspondente no dashboard executivo.

## Status anterior (12/08/2026, via reunião de planejamento de sprint)

**5% — bloqueado, mas escopo agora está mais claro e ganhou prazo-alvo.** Projeto seguia parado desde antes de 04/08 por falta de resposta do fornecedor RPE; a reunião de 12/08 não resolveu esse bloqueio, mas destrinchou o que precisa ser construído e definiu meta de entrega.

> Fonte: [`../reviews-retros-planning/2026-08-12-planejamento-sprint.md`](../reviews-retros-planning/2026-08-12-planejamento-sprint.md).

**Escopo confirmado por Ozéias (12/08):**
1. Tela de **import de planilha Excel** — lista de clientes elegíveis a receber o bônus/crédito do overlimit (leitura + [trecho da gravação inaudível, provavelmente "validação/aplicação" — confirmar]).
2. **Distribuição pra loja** — mecanismo pra levar essa base até o PDV VAR, igual ao que já existe pra **blacklist** (RPA): "muda só que aqui vai ser outra base, e o VAR tem que consumir essa base." Léo sugere partir do que já foi feito pra blacklist, deve ser mais rápido de adaptar.
3. **Prazo-alvo: release de setembro do VAR**, antes do code freeze — prazo definido nesta reunião, não confirmado se é compromisso firme ou meta de planejamento.

**Possível sobreposição:** Ozéias mencionou "acho que até o Gui estava mexendo nisso" — não confirmado se é retrabalho ou continuação do que Gui Oliveira (dono do projeto) já vinha fazendo antes do bloqueio da RPE. Vale confirmar com o Gui antes de iniciar.

## Bloqueio — RESOLVIDO em 31/08

> Ver Status atual (08/09) no topo do arquivo pra fonte e detalhe.

**Fornecedor RPE respondeu e liberou credenciais/webhooks em 31/08** — o bloqueio abaixo (histórico, até 12/08) não reflete mais a situação atual, mantido só como registro de como o bloqueio evoluiu.

~~**Fornecedor RPE sem resposta — segue sem atualização.** O bloqueio técnico de fundo é uma limitação do gateway Kong, que não suporta duas credenciais simultâneas — a validação da solução pra essa limitação depende da credencial de teste que a RPE prometeu enviar em 04/08 e não enviou. Não foi mencionado na reunião de 12/08 (que foi sobre planejamento/escopo, não sobre status do fornecedor) — sem confirmação de que avançou.~~

Citado no dashboard executivo (10/08) como um dos três fatores externos recorrentes que travavam múltiplos projetos do VAR (junto com a instabilidade de cache da GetNet no Tap on Phone e o fornecedor do SmileGo). **Atualização 16/09:** o SmileGo não é um fator externo solto — é a mesma frente deste projeto (ver seção "Status atual" acima, card #12104).

## Reuniões

- [`../reviews-retros-planning/2026-08-12-planejamento-sprint.md`](../reviews-retros-planning/2026-08-12-planejamento-sprint.md) — reunião de planejamento de sprint (transversal, não específica deste projeto) onde o escopo foi destrinchado e o prazo de setembro definido.

## Próxima atualização

Registrar as respostas de Spin, Cartões e Aislan (seção "Em aberto" do status de 25/09) e o card da tela/serviço no portal do RPA quando for criado. Pendências antigas, ainda sem resposta: (1) se o item "voucher" citado pelo PO em 08/09 (nome incompleto/garbled na transcrição) é parte deste projeto ou outra coisa; (2) status do teste com os 3 CPFs controlados pela área de negócio mencionado em 04/09; (3) status do bloqueio de ambiente de teste do fornecedor NeuroTech (card #12104) — segue sem previsão de resolução.
