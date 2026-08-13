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

## Status atual (10/08/2026, via dashboard executivo)

> Implementação concluída bem mais rápido que o esperado; subiu para homologação em 10/08 e já começou a bateria de testes. **~90%.**

US8–US12 confirmadas em **In Test** no Azure em 12/08 — bate com o dashboard.

## O que falta antes do go-live

1. **US13 — validação com as áreas.** É o próximo passo depois da homologação técnica (US12). O fluxo é: apresentar ao responsável (⟵ **essa é a reunião com o Ozeias**) → aprovação → agendar sessão com cada área → validação → aceite formal → treinamento. Fluxograma completo do processo: [artifact](https://claude.ai/code/artifact/2b33340a-6d0a-415e-835c-87cfd64943ee).
2. **US14 — go-live.** Depende de US12+US13 concluídas, ambiente de produção, janela do 1º fechamento e suporte IT/Infra — nenhum confirmado ainda.

## Pontos técnicos em aberto (levantados no refinamento, confirmar status na homologação)

- **US8**: mecanismo/credenciais de envio (MTA) pendentes de definição por Spin/Taunay — confirmar se já resolvido, já que o card avançou pra QA.
- **US9**: autorização do tenant Microsoft (Mail.Read) pra ler webhooks — mesma observação, confirmar status.

## Bug novo levantado na reunião de planejamento (12/08)

> Fonte: [`../dailies/2026-08-12-planejamento-sprint.md`](../dailies/2026-08-12-planejamento-sprint.md).

Ozéias sinalizou um bug relacionado às **linhas** (não detalhado na transcrição — precisa confirmar com o Diego o card/sintoma exato). Diego está focado em corrigir. Plano combinado: como o que resta da Conciliação Fase 2 tende a ser correção (não mais desenvolvimento novo), **Kauã volta pra Gamificação** e Diego segue sozinho nos ajustes finais da Fase 2.

## Risco ativo (dashboard executivo, 10/08)

> **Job noturno da Conciliação segue instável no portal Retaguarda.** Duplicação de lojas no processamento voltou a ocorrer em pelo menos três ocasiões no período, exigindo correção manual repetida. Time já testando mover o processo para um worker dedicado.

Vale mencionar pro Ozeias — é um risco de produção que pode pesar na decisão de ir pra homologação de negócio antes de estabilizar.

## Reuniões

- [reuniao-ozeias-apresentacao-inicial.md](reuniao-ozeias-apresentacao-inicial.md) — apresentação da v1 pro Ozeias, antes de levar às áreas.

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

Preencher aqui depois da reunião: o que o Ozeias aprovou/pediu de ajuste, e se a agenda de validação com as áreas foi liberada.
