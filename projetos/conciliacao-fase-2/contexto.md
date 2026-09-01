# Conciliação Fase 2 — contexto geral

> Arquivo de contexto do projeto. Atualizado a partir de dailies, reuniões e do dashboard executivo. Ler antes de qualquer reunião sobre este projeto.

## O que é

Segunda fase do processo de Conciliação: envio automático de arquivos (cron + retry), webhooks de entrega/bounce/leitura, reenvio individual + download auditado + retenção, atualização em tempo real de Perdas e Vales, e o ciclo de homologação técnica → validação de negócio → go-live/hypercare.

Épico: **[#12387 — Conciliação Fase 2](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12387)** (Var Retaguarda). 29 itens ativos nos últimos 4 sprints.

## Time

**Diego, Kauã e Fernando** (novo dev, acompanhando os testes) — dedicação em tempo integral, adiantaram a entrega em relação ao esperado.

## As 7 histórias (US8–US14)

| US | Card | O que é | Status |
|---|---|---|---|
| US8 | [#12395](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12395) | Envio automático — cron + retry | In Test (QA) |
| US9 | [#12396](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12396) | Webhooks — entrega, bounce, leitura | In Test (QA) |
| US10 | [#12397](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12397) | Reenvio, download auditado, retenção | In Test (QA) |
| US11 | [#12398](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12398) | Tempo real — Perdas e Vales | In Test (QA) |
| US12 | [#12399](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12399) | Performance, QA, homologação técnica | In Test (QA) |
| US13 | [#12400](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12400) | Validação de negócio (Financeiro/Contábil/RH/Diretoria) + treinamento | Ready for Dev — bloqueio externo: agenda das 4 áreas |
| US14 | [#12401](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12401) | Go-live, pilotagem 1º fechamento, hypercare | Ready for Dev — bloqueio externo: ambiente prod, janela do fechamento, IT/Infra |

## 🚀 Status atual (31/08/2026) — módulo RH pronto, sobe pra produção hoje

Pacote completo de correções (#12808–#12811: parcela única auto-aprovada, CPF do gerente via responsável do caixa 99 na data de referência, envio ao RH só no fechamento com ciclo 20→19, prévia do ciclo aberto) passou por QA completo com o Danilo e foi **aceito em 31/08**. O card #12800 original (contexto no modal individual, filtro de data, export sem Referência) também foi ajustado e aceito no mesmo ciclo. **GMUD de hoje (31/08) sobe tudo pra produção**, junto com a Migração VarRet.

2 bugs pré-existentes (não causados por este projeto) achados durante a validação do #12810 viraram cards próprios, não bloqueiam a subida:
- [#12882](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12882) — `can-close` não valida o status da conciliação antes de liberar o botão de fechar.
- [#12884](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12884) — recusa de negócio no fechamento chega como erro genérico (500) em vez da mensagem real.

**Mecanismo técnico confirmado (Ozéias, comentário no #12809):** a identidade do gerente pra desconto em folha vem do **responsável pelo caixa 99 na data de referência da conciliação** (não a data do fechamento), sem consulta a Senior/Logix. Lojas que pagam quebra de caixa (descontam do próprio operador, não do gerente): **12, 14, 25, 69, 71, 80, 103, 144**.

## Status anterior (10/08/2026, via dashboard executivo)

> Implementação concluída bem mais rápido que o esperado; subiu para homologação em 10/08 e já começou a bateria de testes. **~90%.**

US8–US12 confirmadas em **In Test** no Azure em 12/08 — bate com o dashboard.

## O que falta antes do go-live

1. **US13 — validação com as áreas.** É o próximo passo depois da homologação técnica (US12). O fluxo é: apresentar ao responsável (⟵ **essa é a reunião com o Ozeias**) → aprovação → agendar sessão com cada área → validação → aceite formal → treinamento. Fluxograma completo do processo: [artifact](https://claude.ai/code/artifact/2b33340a-6d0a-415e-835c-87cfd64943ee).
2. **US14 — go-live.** Depende de US12+US13 concluídas, ambiente de produção, janela do 1º fechamento e suporte IT/Infra — nenhum confirmado ainda.

## Pontos técnicos em aberto (levantados no refinamento, confirmar status na homologação)

- **US8**: mecanismo/credenciais de envio (MTA) pendentes de definição por Spin/Taunay — confirmar se já resolvido, já que o card avançou pra QA.
- **US9**: autorização do tenant Microsoft (Mail.Read) pra ler webhooks — mesma observação, confirmar status.

## Bug novo levantado na reunião de planejamento (12/08) — resolvido

> Fonte: [`../dailies/2026-08-12-planejamento-sprint.md`](../dailies/2026-08-12-planejamento-sprint.md) e [`../dailies/2026-08-12-retaguarda.md`](../dailies/2026-08-12-retaguarda.md).

Ozéias sinalizou um bug relacionado às **linhas** (não detalhado na transcrição da reunião de planejamento). Na daily do mesmo dia (12/08), o Fernando relatou ter corrigido "um bug de uma contagem de linhas" — provável mesmo item (não há um segundo candidato nas dailies revisadas). Plano combinado: como o que resta da Conciliação Fase 2 tende a ser correção (não mais desenvolvimento novo), **Kauã volta pra Gamificação** e Diego segue sozinho nos ajustes finais da Fase 2.

## Bug de token quebrando permissionamento de rotas — NÃO é desta Fase 2

> Fonte: [`../dailies/2026-08-11-retaguarda.md`](../dailies/2026-08-11-retaguarda.md), [`../dailies/2026-08-12-retaguarda.md`](../dailies/2026-08-12-retaguarda.md).

Achado durante homologação da Conciliação Fase 2 (o usuário de teste do Danilo apresentava erro no meio do fluxo), mas é um **bug geral do portal**, não específico desta feature — Diego + Danilo confirmaram em devbox que o tamanho do token quebra o permissionamento de rotas pra qualquer usuário com muitos grupos, independente da tela.

**Reclassificado em 13/08:** virou **[Bug #12514](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12514)**, tipo Bug (era PBI), linkado ao épico **#6640 — Portal de Retaguarda (Sustentação)** (não mais ao #12387). Confirmado como o mesmo bug de "muitos grupos no usuário" que o Leonardo já corrigia em paralelo — ele é o owner. Segue só citado aqui como contexto de origem; acompanhamento formal fica em `projetos/dailies/` e no próprio card.

## Risco ativo (dashboard executivo, 10/08)

> **Job noturno da Conciliação segue instável no portal Retaguarda.** Duplicação de lojas no processamento voltou a ocorrer em pelo menos três ocasiões no período, exigindo correção manual repetida. Time já testando mover o processo para um worker dedicado.

Vale mencionar pro Ozeias — é um risco de produção que pode pesar na decisão de ir pra homologação de negócio antes de estabilizar.

## Reuniões

- [reuniao-ozeias-apresentacao-inicial.md](reuniao-ozeias-apresentacao-inicial.md) — apresentação da v1 pro Ozeias, antes de levar às áreas. **Realizada em 12/08 (18:32), ver resumo e transcrição completa em [transcricao-ozeias-2026-08-12.md](transcricao-ozeias-2026-08-12.md).** Aprovação **condicional**: virou uma sessão de teste exploratório ao vivo e achou 2 gaps reais — ver seção abaixo.
- [reuniao-wagner-2026-08-13.md](reuniao-wagner-2026-08-13.md) — ata da apresentação das 4 telas pro **Wagner** (dono original do projeto — mapeou os requisitos com a área e desenhou o desenho inicial antes de repassar pro time). **Realizada em 13/08 (17:10, 42min), ver ata e transcrição completa em [transcricao-wagner-2026-08-13.md](transcricao-wagner-2026-08-13.md).** Aprovação geral ("vocês estão de parabéns"), com 2 gaps reais novos e esclarecimentos — ver seção abaixo.

## Achados da demo com o Ozéias (12/08) — 2 gaps reais + 1 ponto de atenção

1. **Bug confirmado e corrigido (validado na reunião do Wagner em 13/08):** validação de parcelas na tela de Aprovação de Vales rejeitava valor negativo, mas "desconto em folha" é inerentemente negativo (débito do funcionário) — mensagem de erro "installment amount must be positive". Diego corrigiu e demonstrou ao vivo pro Wagner: agora o sistema **bloqueia valor positivo** no aprovar (alerta "sem valor a descontar") e aceita negativo normalmente — comportamento correto confirmado.
2. **Ambiguidade a resolver com o Wagner — AINDA NÃO TRATADA:** reverter uma aprovação **depois** que ela caiu na fila de Aprovação de Vales mas **antes** do RH agir deixa o item "aguardando" na fila em vez de sumir — Leonardo acha que deveria sumir, não tem certeza. Apesar de a reunião com o Wagner ter acontecido em 13/08, **esse ponto especificamente não veio à pauta** (Leonardo estava presente mas não conduziu a pergunta) — segue pendente pra próxima interação com o Wagner.
3. **Ponto de atenção, não bloqueante:** timing do cron de fechamento (23h do último dia do ciclo) pode deixar incompletas conciliações feitas no próprio dia de corte — Ozéias levantou a ideia de um botão manual de "fechar ciclo" em vez de horário fixo; não decidido, vai reconfirmar com as áreas. **A regra de fechamento em si foi confirmada como correta pelo Wagner em 13/08** (ver seção abaixo) — o que ficou em aberto é só a ideia do botão manual.

**Prazo combinado:** ajustar os pontos 1 e 2 até **sexta-feira (14/08)**. Depois disso, prévia informal do Ozéias com uma responsável (nome capturado como "Mídia" na transcrição — confirmar) + Adriana; só na semana seguinte a reunião formal com RH e as demais áreas. **Não sobe pra produção sem aprovação formal** (documento de aceite + e-mail + prints de teste — já pedido ao Danilo/QA pra começar a guardar evidência).

### Atualização 13/08 (via [`../dailies/2026-08-13-retaguarda.md`](../dailies/2026-08-13-retaguarda.md))

- Diego corrigiu os bugs achados na própria demo do Ozéias e subiu pra homologação hoje de manhã; ainda testando, "algumas coisas pendentes" (não especificado se são os pontos 1/2 acima ou itens novos — confirmar na próxima daily).
- Kauã está construindo uma forma do Danilo disparar o cron job pela UI/front (em vez de precisar ir direto pra Prod sem passar por DevBox) — infraestrutura de teste, não um bug novo.
- Existem cards em "Bloqueado" que podem deixar de ser necessários assim que a Fase 2 confirmar que não precisam mais ser aplicados; Igor vai comentar/fechar quando isso for confirmado — **decisão do Igor, não uma ação a tomar unilateralmente**.

## Achados da reunião com o Wagner (13/08) — 2 gaps novos + esclarecimentos

> Ata completa: [reuniao-wagner-2026-08-13.md](reuniao-wagner-2026-08-13.md).

**Aprovação geral das 4 telas** (Gerenciar Perdas ajustada, Dashboard, RH·Aprovação de Vales, RH·E-mail de Setores) — "vocês estão de parabéns", nada bloqueia a Fase 2.

**2 gaps reais encontrados — cards criados em 13/08, ambos já Verified/Homologação (confirmado 25/08):**
1. **[#12515](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12515) — Bug: "Consolidado" do mês corrente aparece disponível pra download antes do fechamento oficial do ciclo** (deveria só liberar depois de ~23h do último dia do mês). Confirmado ao vivo pelo Diego. Workaround já existe (filtro de range de data customizado funciona certo). **Verified.**
2. **[#12516](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12516) — Ranking export sem agregação por Regional e Tesouraria** — a planilha padrão anterior tinha essas 2 visões agregadas, além da flat que foi mostrada na demo. **Verified.**

**Esclarecimentos de negócio (documentar, não é bug):**
- "Reprovado" na fila de Aprovação de Vales = reprovação do **parcelamento**, não do desconto em si (o desconto segue pro RH normalmente).
- Planilha do Sênior (RH): todos os valores exportados são sempre **positivos** (formato fixo pedido pela área), com colunas obrigatórias rubrica + referência (coluna V) + CPF. Já implementado conforme.

**Sugestões de produto (não são ação agora):** unificar a lógica de sinal (positivo/negativo) desde a origem na tela de conciliação de caixa (vale reunir com o Ozéias pra decidir); ideia de "inteligência de dados consultiva" pra versões futuras (área do Taunay, backlog sem prazo).

## Achados da demo pra área — RH/Financeiro/Contábil (25/08) + alinhamento interno (26/08)

> Atas completas: [reuniao-area-rh-financeiro-2026-08-25.md](reuniao-area-rh-financeiro-2026-08-25.md), [alinhamento-interno-2026-08-26.md](alinhamento-interno-2026-08-26.md).

Demo do módulo de RH (Gerenciar Perdas → Aprovação de Vales) pro Gilson (RH — Folha), Midia (RH) e Adriana (Contábil). 4 correções levantadas, formalizadas em cards no dia seguinte:

1. **[#12808](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12808) — Parcela única deve ser aprovada automaticamente**, sem passar pela fila do RH. 3 pts (PO).
2. **[#12809](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12809) — CPF do gerente em lojas sem quebra de caixa.** ⚠️ Conflita com decisão D8 já documentada no código (CPF sempre do operador) — precisa alinhar com o time técnico antes de implementar. Sem estimativa ainda.
3. **[#12810](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12810) — Envio ao RH no fechamento da conciliação (não na aprovação), com ciclo do RH mudando de 26→25 pra 20→19**, e trava de edição pós-fechamento. 8 pts (PO) — maior das 5, muda o gatilho central do fluxo.
4. **[#12811](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12811) — Permitir prévia do ciclo RH ainda aberto**, sem duplicar no export oficial. 5 pts (PO).
5. **[#12812](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12812) — Planilha pro Contábil no layout de importação do Oracle.** 🔴 Bloqueado — Adriana ainda vai levantar o layout exato. Resolve a discrepância já apontada no item 7 do plano técnico original (seção abaixo).

Todos filhos do Epic #12387, Sprint 27, atribuídos ao Diego. **Atualização 31/08: #12808, #12809, #12810 e #12811 foram todos pra Accepted** (ver seção de status atual, topo do arquivo) — só o #12812 (planilha Oracle/Contábil) segue em Refinement, bloqueado pela Adriana.

**Achado técnico relevante:** o módulo de RH já está implementado, mas só na branch `epic/GAV-RTG-12387` (ambos os repos), ainda não mesclada em main/develop.

## Plano técnico original (VSCODE)

> Fonte: `Tarefas_Conciliacao_Fase2.md` (plano mestre, v1.0, 01/07/2026) e `user_stories_conciliacao_fase2.md` (reescrita em US) — documentos de planejamento técnico que antecederam a criação dos cards no Azure. Úteis como referência de arquitetura e para rastrear pendências que podem não ter sido carregadas para o board.

**Estrutura do plano mestre — 3 épicos, 14 tasks/US, 564h:**

| Épico (plano original) | Tasks/US | Horas | Mapeia para (Azure) |
|---|---|---|---|
| Épico 1 — Front mockado (as 4 telas: E-mails, Gerenciar Perdas, Aprovação de Vales, Dashboard) | T1–T5 / US1–US5 | 212h | Correspondem à base das telas hoje em In Test |
| Épico 2 — APIs e integração (fonte de dados, XLSX, envio, webhooks, reenvio/auditoria, tempo real) | T6–T11 / US6–US11 | 224h | US8–US12 no board atual |
| Épico 3 — Fechamento (QA/homologação técnica, validação de negócio, go-live) | T12–T14 / US12–US14 | 128h | US12 (homologação técnica), US13 (#12400 — validação de negócio), US14 (go-live) |

**Bloqueios/pendências abertos no plano original (8 itens na tabela de dependências gerais):**

1. **Fonte de Perdas da Fase 1 indefinida** — acesso/contrato à saída de Perdas (endpoint, evento ou view) da Fase 1 é hoje uma caixa-preta; nomes reais dos campos (`concId`, `loja`, `operador`, `valor`, `data`...) não confirmados. Bloqueante para virar o mock em dado real (T6/US6).
2. **Stack de backend indefinida** — linguagem/framework, engine de banco e storage de objetos não estavam definidos nos contextos disponíveis ao plano original; impacta T6/T7/T8/T10 (US6/US7/US8/US10).
3. Estrutura do front da Fase 1 (`ConciliaçãoCaixaFront`) — roteamento, gestão de estado e ponto de reuso do tempo real, a confirmar (T1/T11).
4. Mecanismo exato de tempo real da Fase 1 (WebSocket, SSE ou polling) — só havia a diretriz "reusar o padrão da Fase 1" (T11).
5. Autenticação e enforcement de papéis (Admin/Analista/RH) sem mecanismo definido no material disponível (T1/T4/T10).
6. **Credenciais/mecanismo de envio (MTA)** — pendente de definição por **Spin/Taunay**, com **contatos Santos/Abreu** citados no plano original para o mecanismo de envio/token (T8/US8). ⚠️ **Discrepância a reconciliar**: o card no Azure (US8, ver seção acima) registra o bloqueio apenas como "pendente de definição por Spin/Taunay" — sem menção a Santos/Abreu. Não está claro se Santos/Abreu são os contatos técnicos atuais do lado do fornecedor/área de e-mail ou se essa referência ficou desatualizada em relação ao que está no card. Vale confirmar com o time qual dupla de nomes é a válida hoje antes de cobrar retorno.
7. **Layout do Oracle (Contábil) vs. Sênior HCM (RH)** — divergência apontada entre o layout C1 da Consolidada Vale e a documentação do Sênior HCM, a reconciliar antes de fechar o gerador de XLSX (T7/US7).
8. Reconciliar "7 planilhas" mencionadas em reunião vs. os 3 destinos citados no brief original — pode alterar escopo de geração/envio (T7/T8).

**Pendências de área (não bloqueiam desenvolvimento, mas precisam resolver antes do go-live):** autorização do tenant Microsoft (`Mail.Read` delegada, para leitura de webhooks — US9); ambientes de dev/homolog/prod e storage de objetos definidos; confirmação dos KPIs e da política de retenção (jurídico/CTN); aval sobre exibir CPF completo na Consolidada Vale (LGPD); layouts confirmados do Oracle e do Sênior.

## Próxima atualização

Preencher aqui quando: (1) os cards #12515/#12516 (gaps novos da reunião do Wagner: Consolidado antes do fechamento, Ranking sem agregação Regional/Tesouraria) entrarem em andamento; (2) a ambiguidade da fila do RH pós-reversão (não tratada na reunião do Wagner) for finalmente esclarecida numa próxima interação; (3) a prévia informal com a responsável ("Mídia"/confirmar nome) + Adriana acontecer (prevista sexta 14/08); (4) a reunião formal com RH e demais áreas da semana seguinte for marcada e/ou realizada; (5) os bloqueios técnicos US8/US9 e o risco do job noturno instável forem finalmente discutidos com o Ozéias; (6) Igor decidir sobre os cards em "Bloqueado" que podem não ser mais necessários; (7) a reunião Ozéias↔time sobre validar valor positivo direto na conciliação de caixa acontecer. (Bug de token/permissionamento saiu do escopo deste projeto — virou Bug #12514, épico Portal de Retaguarda Sustentação #6640.)
