# Gamificação (Roleta 3.0) — contexto geral

> Arquivo de contexto do projeto. Atualizado a partir dos planos técnicos (v9.3 e EP1/EP2/EP3), de dailies e do dashboard executivo. Ler antes de qualquer reunião sobre este projeto.

## O que é

Portal de Gamificação Avenida (Roleta 3.0): cliente identifica-se por CPF, é elegível a campanhas com diferentes mecânicas de jogo (Roleta, Raspadinha, Caça-Níquel, Gol Premiado) e recebe voucher de desconto gerado pela lógica de voucher já existente no VAR (campo PRO015). Inclui backoffice step-by-step para cadastro de campanhas, antifraude/auditoria de cadastro e analytics (CRM/BI + pixel).

Épico: **[#11950 — Gameficação](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11950)** (Var Retaguarda). Cards ativos: **T1–T10** (#12179, #12181–#12189), todos em **Ready for Dev** desde 13/08.

## Dono

Dev: **Kauã**. Dono de negócio: **Ozéias Tavares**.

## Status atual (31/08/2026)

**Todos os T1-T10 avançaram pra "In Test"/QA no board** (confirmado via ADO). Painel administrativo já subiu no portal (28/08), com bugs de auto-increment em ajuste (Kauã investigando). Plano é testar tudo de ponta a ponta na semana de 01/09. Verificar se as pendências da rodada de 13/08 (rework de T1-T3, bloqueio de CRM/BI em T8, assets visuais em T9, visibilidade em homolog) já foram endereçadas nessa fase de teste — não confirmado nas dailies desse período.

## Status anterior (13/08/2026 — decisão do Igor no refinamento do board)

**Deixou de ser "perpetuamente despriorizado".** Igor decidiu (13/08) mover os 10 cards T1-T10 (#12179, #12181-12189) de "Refinement" pra **"Ready for Dev"**, considerados prontos no board de refinamento — justificativa: o planejamento (docs v9.3 e EP1/EP2/EP3) é anterior ao processo de refinamento deste workspace e já é completo (Story/AC/estimativa desde a criação), não precisa da reescrita em Cenário/GWT. **Kauã volta a ter Gamificação como prioridade.** Todos os 10 cards foram atribuídos a ele.

**Achado técnico grande (13/08, durante o refinamento do T7/#12186):** já existe um módulo `campaign-roulette` em produção no `ConciliaçãoCaixaAPI` (`src/modules/campaign-roulette/`) — cria campanhas, grava direto na tabela `VAR.PRO015`, sobe banners, configura lojas e probabilidades. Tipos suportados hoje: `ROULETTE` e `WORLD_CUP` (não as 4 mecânicas do Gamificação — Roleta, Raspadinha, Caça-Níquel, Gol Premiado). **Vale o Kauã avaliar se dá pra estender esse módulo em vez de construir do zero em T5-T10** — pode mudar dimensionamento. Detalhe: os campos de validade do voucher (`P15DIASINI`/`P15VALID`/`P15DIASVAL`) são gravados hoje com valores fixos (`PRO015_DEFAULTS`), não configuráveis por campanha — precisaria de extensão se o Gamificação exigir validade configurável. Registrado como comentário no card #12186.

**Pendências que seguem valendo, mesmo com os cards em Ready for Dev** (não bloqueiam o board, mas bloqueiam a execução real):
- **T1/T2/T3 (#12179/12181/12182):** reprovados pelo QA (Danilo) em rodadas anteriores — rework real pendente (cor de marca, validação de CPF, telas de confirmação/antifraude caindo em tela genérica, escopo vazado pra Fase 3). Ver comentários dos cards.
- **T8 (#12187):** bloqueio externo de CRM/BI/marketing (destino/formato de exportação, IDs de tags) segue sem resposta da área.
- **T9 (#12188):** assets visuais das 4 mecânicas (arte/sprites/sons) ainda não entregues pelo design.
- **Alerta de visibilidade em homolog** (Ozéias, 12/08): não consegue mais ver o Portal Gamificação em homolog — ainda não investigado.

Padrão histórico anterior a 13/08 (mantido como contexto): o projeto foi **repetidamente despriorizado** sempre que a Conciliação Fase 2 precisava do Kauã — não era um bloqueio pontual. Via daily de 04/08 (info anterior): ajustes no mockup de front-end ainda estavam sendo feitos a pedido do Ozéias.

## Mapeamento entre a numeração original (T1–T10) e os cards T7–T10 do Azure

O plano técnico completo (`us_gamificacao_v2_completo.md`, v9.3, 19/06/2026) organiza o projeto em **4 épicos e 10 tasks (T1–T10, 528h)**:

| Épico do plano original | Tasks | Horas |
|---|---|---|
| Épico 1 — Front mockado | T1–T4 | 208h |
| Épico 2 — APIs e integração | T5–T8 | 204h |
| Épico 3 — Jogos e animações | T9 | 64h |
| Épico 4 — Fechamento (QA e go-live) | T10 | 52h |

Isso **confirma diretamente** a leitura de que os cards atuais no Azure (T7, T8, T9, T10 = #12186–#12189) são a cauda final deste mesmo projeto: T7 e T8 caem dentro do Épico 2 (APIs e integração), T9 é o Épico 3 inteiro (jogos e animações) e T10 é o Épico 4 inteiro (performance, QA, go-live). O mapeamento não precisou ser tratado como incerto — a numeração T1–T10 do plano bate exatamente com a numeração dos cards no board.

**Atenção para não confundir:** existe um segundo documento fonte na mesma pasta, `us_gamificacao_ep1_ep2_ep3-v2.md` (responsável Ozéias Tavares, revisor Diego Aoki), que reorganiza o mesmo escopo em **EP1/EP2/EP3 com códigos A01–A02, B01–B03, C01–C06** (consolidação de 18 → 11 cards). Essa numeração **não corresponde 1:1** à numeração T1–T10 — são dois recortes diferentes do mesmo projeto, feitos em momentos distintos. Ao usar qualquer um dos dois documentos como referência técnica, confirmar qual dos dois é o vigente antes de citar um código de card para o time.

## Bloqueios (cards T8/T9/T10, via card Azure)

- **T8** — depende de dados de CRM/BI + pixel vindos da área de Marketing.
- **T9** — depende de assets de design (arte, sprites das 4 mecânicas de jogo) ainda não entregues.
- **T10** — depende de ambiente de produção e disponibilidade de stakeholders de negócio para a sessão de homologação.

Todos são bloqueios externos reais, não just falta de capacidade de dev — mas a falta de capacidade (Kauã sendo puxado para Conciliação Fase 2) segue sendo o fator que mais atrasa o avanço mesmo quando os bloqueios externos se resolvem.

## Reuniões

- **Data não informada (resumo recebido em 02/10/2026): apresentação do Portal + revisão de UX.** Resumo em [2026-10-02-resumo-apresentacao-portal-gamificacao.md](2026-10-02-resumo-apresentacao-portal-gamificacao.md).
  - **Situação geral:** as regras de negócio estão aprovadas, mas a experiência não está fechada.
  - **5 grandes temas:**
    1. landing page antes do cadastro, com página e QR Code por campanha;
    2. gamificação dentro do domínio Avenida, com integração ao site (conversar com o Marcos/time do site);
    3. revisão de design + Mobile First;
    4. analytics do funil inteiro;
    5. elegibilidade regional clara antes de jogar.
  - **Decisões do CRM pendentes:**
    - quais campos do cadastro são obrigatórios;
    - como campanhas segmentadas por CPF aparecem (ou não) no site aberto.
  - **Jonas:** a homologação precisa chegar praticamente pronta pra produção.
  - **Cards (02/10, Kauã, Sprint 30, Ready for Dev):**
    - #13464 landing page;
    - #13465 QR Code;
    - #13466 domínio Avenida (bloqueado);
    - #13467 funil de analytics;
    - #13468 não pedir identificação de novo;
    - #13469 elegibilidade regional (bloqueado).

- **02/09/2026 — Demo/homologação pro CRM (Ana Carina Araujo Souza e Marcos Eidi Yonamine), conduzida por Ozéias com apoio do Kauã.** Ata completa em [2026-09-02-demo-crm-ana-marcos.md](2026-09-02-demo-crm-ana-marcos.md). Mostrou o fluxo completo (cadastro de campanha + experiência do cliente final). Pontos levantados:
  - **2 bugs achados ao vivo:** (1) acesso de homologação ao banco bloqueado — travou a demo por ~5-10min até o Alisson (infra) resolver; (2) editar rótulo/valor de símbolo no cadastro do caça-níquel quebra a tela de configuração (reproduzido ao vivo, não investigado a fundo ainda).
  - **Discussão sobre remover a validação de "campanha ativa por tipo"** — hoje só permite 1 campanha ativa por jogo; CRM validou a ideia de permitir várias campanhas simultâneas segmentadas por CPF/loja/valor, mas **não é decisão 100% fechada tecnicamente** (Ozéias anotou pra validar depois).
  - **Decisões pendentes:** banner customizável por campanha (Ana se inclinou a favor, não fechado) e um novo campo "nome da campanha pro cliente" (separar nome interno do nome exibido ao cliente — a implementar).
  - **Meta informal de go-live: até o final de setembro/2026** — no lançamento, este portal substitui tanto o "Chute ao Gol" quanto a "Roleta" atuais (link da roleta atual ganha redirect; chute ao gol é descontinuado). Destacada como mais simples por não depender de nenhuma mudança no VAR.

## Próxima atualização

Preencher aqui quando: (1) o Kauã avaliar se o módulo `campaign-roulette` existente pode ser estendido em vez de construir T5-T10 do zero; (2) o rework de QA em T1-T3 for endereçado; (3) os bloqueios externos de T8 (CRM/BI+pixel) e T9 (assets de design) forem resolvidos; (4) o sumiço do portal em homolog (flagado por Ozéias em 12/08) for investigado e explicado.
