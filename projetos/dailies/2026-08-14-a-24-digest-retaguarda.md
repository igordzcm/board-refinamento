# Digest — Dailies Retaguarda, 14–24/08/2026

> Síntese das 7 dailies do squad Retaguarda nesse período (14, 17, 18, 19, 20, 21, 24/08). Transcrições brutas nos `.docx` datados nesta pasta. Não é transcrição literal — é o fato relevante extraído de cada fala, organizado por pessoa/tema pra alimentar o dashboard e o arquivo de pendências.

## Conciliação Fase 2 (Diego)

- **14/08**: reunião com o Wagner (13/08) revisou fluxos ponta a ponta — faltou cumprir poucos requisitos. Diego coletou feedback, Igor criou cards, correções já em code review → aplicadas → homolog, pronto pra novos testes.
- **17/08**: testes finais de sexta, nada novo além do que já subiu.
- **18/08**: Fase 2 estabilizada, Diego sem cards pendentes nela — volta 100% pro SIGA.
- **20/08**: aplicou ajustes pedidos pela área de negócio (contato "Mídia") — pronto pra homolog. **Pediu um card pra isso, ainda não tinha.**
- **21/08**: task dos ajustes da área finalizada, PRs abertos. Weekly com a área foi cancelada (não deu pra apresentar).
- **24/08**: DevBox com Danilo sexta explicando o fluxo (guards de aprovação de parcelas). Depois reunião com a área do Financeiro apresentando a Fase 2 pra "Mídia" — Ozéias mapeou pontos de correção/melhoria e passou pro Diego, que trabalhou nisso sexta à tarde e está concluindo hoje de manhã pra subir ao homolog. **De novo, sem card formal — "só não tenho o card disso, mas já estou executando."**

**Pendência clara:** pelo menos 2 rodadas de correção (20/08 e 24/08) foram feitas sem card no Azure — precisam ser retroativamente documentadas ou pelo menos linkadas a algo existente.

## SIGA — Performance de Indicadores (Diego)

- **14/08**: Igor confirma que a fonte de dados problemática foi resolvida (via Ozéias); projeto volta segunda 18/08.
- **17/08**: Diego volta a focar nisso. DevBox com Danilo não rolou — ambiente sem a branch configurada.
- **18/08**: rodando localmente, problema resolvido. Revisão do código desde a última implementação (compartilhada com Vitor). Retoma indicadores de absenteísmo, turnover, extras compensáveis. **Precisa alinhar com Léo/Igor/Ozéias sobre tratamento de dados sensíveis** que causaram problema da última vez (existe tabela específica? investigar?). Sem card em Ready for Dev ainda.

**Pendência:** card de SIGA Indicadores precisa ser criado/refinado, incluindo a decisão sobre dados sensíveis.

## Migração VarRet / Dashboard CDs (JB)

- **14/08**: foco segue Migração VarRet (exportações lote 1 → worker, em code review).
- **17/08**: revisou os "reworks" que o Danilo apontou — nenhum é erro do JB de fato (Função 79 é problema de token/backend, não do código dele). Falta massa de teste pra caixa aberta — deixado em blocked. Vai falar com a Maria hoje pra retomar CDs.
- **18/08**: Maria ainda não pôde passar a planilha — **JB bloqueado em CDs**, sem tarefa por conta disso.
- **19/08**: massa de teste em progresso; Função 79 com PR aberto; Migração VarRet travada em comentários do Léo, testes não rodando numa branch específica (investigando).
- **20/08**: **conseguiu reunião com a Maria e pegou a planilha!** Já começou a trabalhar em cima dela.
- **21/08**: Danilo testou o lote 1 e achou confusão: Cenário 1 (Demonstrativo de Caixa) não existe de fato — só a tela de "conciliação de loja" tinha export no lote 1. **Card ficou em blocked esperando Igor (de licença) refinar isso.** Bom progresso em CDs, mais pontos levantados pra confirmar com a Maria.
- **24/08**: trabalhando no "RPA CDs" — muito da planilha já batendo, ajustes visuais (gráficos) que a Maria pediu já feitos. Espera terminar amanhã/depois de amanhã. Reunião com "Mídia" à tarde pra validar visualmente.

**Pendências claras:**
- Dashboard CDs **não está mais bloqueado por falta de planilha** — a partir de 20/08 JB já está com os dados. Os cards #12509–#12513 no board de refinamento precisam ter esse chip de bloqueio removido/atualizado.
- Card do lote 1 (#12484 ou #12437, a confirmar) tem uma ambiguidade no Cenário 1 que só o Igor pode resolver — está em blocked desde 21/08.

## Motor de Descontos (Fernando → depois Léo/Kauã)

- **14/08 (retro)**: Fernando corrigiu um bug de front (nomenclatura do campo "pague"/desconto). Igor decidiu **não mudar agora** — é uma correção maior, revisar o motor inteiro depois. Danilo já fez o dev do lado dele.
- Foco de Fernando a partir daí: sustentação do portal + projeto de automação de testes (8 fases). Progresso constante: 17/08 módulo Auth (com conflitos de PR), 18/08 seguindo Auth, 19/08 Auth+Person concluídos → Financeiro, 20/08 Financeiro concluído → Conciliação, 21/08 Fase 3 (Conciliação) e Fase 4 (loja/usuários) concluídas, começando CRM, 24/08 terminou as fases restantes sexta, agora trabalhando na parte Playwright (E2E automatizado).
- **24/08**: Léo quer falar com o Igor sobre o Motor de Descontos — **bug de duplicação de desconto/cupom nas lojas**, plano de desativar um job e trabalhar com o Kauã pra resolver (ligado ao mesmo esforço de mover o job de Conciliação pro worker). Menciona uma tabela desativada pro "03" que pode precisar reativar. Sugere reunião pra mapear o que está desativado/funcionando e criar cards.

**Pendência:** reunião de mapeamento de jobs desativados no Motor de Descontos + criação dos cards resultantes.

## Gamificação (Kauã)

- **14/08**: 100% foco liberado (Conciliação Fase 2 fechada). Todos os cards bloqueados movidos pra Ready for Dev.
- **17/08–24/08**: fechando fluxo de login (tela tipo formulário), depois UI dos jogos ("fui bem longe... queria deixar imersivo") — PR grande enviado ao Léo em 20/08, repassado formalmente em 24/08.
- **Job de Conciliação (recorrente)**: hotfix 17/08 funcionou 2 dias, quebrou de novo 20/08 e 21/08 (falha ao reconectar Oracle após queda de conexão, API reiniciava sem dar chance de reconectar). Fix aplicado 20/08 à noite; ainda instável — 24/08 Kauã rodou manualmente pra 3 dias por segurança, considerando **migrar de vez pro worker** junto com Léo.

**Risco recorrente:** o job noturno de Conciliação segue instável desde antes de 10/08 (já registrado no dashboard executivo) — 3+ recorrências nesse período de 10 dias, mitigação (mover pro worker) ainda em andamento, não fechada.

## SSO / SIGA Public / Ciacon (Kovalski)

- SigaPub (novo portal Siga em Nest, separado do resto): Kovalski fechando integração Keycloak, pipe, telas de ranking/comparativo públicas. Deploy aguardando volta de "Paulo/Pablo" de férias (~semana de 24/08).
- **Novo sistema "Ciacon"** entrou no escopo do Kovalski (24/08) — relacionado a remarcação de preço (Donato tem a documentação). Login/autenticação **diferentes** do Siga — vai exigir engenharia reversa. Arquitetura/documentação já levantada e enviada pro Spin/Filipe, aguardando decisão se avançam agora.
- Automação Fiscal: Kovalski vai corrigir uma quebra pontual do SSO se não avançar no Ciacon, depois provavelmente migração.

## QA / infraestrutura (Danilo, Léo)

- **VPN — problema recorrente**: Danilo ficou bloqueado por VPN em 14/08, de novo em 18/08 ("sem acesso ao Tim"), e de novo em 24/08. Cada vez trava testes de um dia inteiro ou parcial.
- **Léo**: cobertura de testes unitários da API chegando a ~80% (21/08) — PRs sem teste vão passar a ser bloqueados. Estrutura de testes movida pra raiz do projeto.

## Tesouraria (Sola/Filipe)

- **24/08**: rollout de Tesouraria começou — piloto em lojas 43 e 11 deu certo, hoje subiu pra 1/3 do parque de lojas.
