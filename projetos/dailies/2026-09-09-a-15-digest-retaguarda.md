# Digest — Dailies Retaguarda, 09–15/09/2026

> Síntese das 5 dailies do squad Retaguarda nesse período (09, 10, 11, 14, 15/09 — sem daily nos dias 12–13/09, fim de semana). Fontes: `RETAGUARDA - Daily (2025)  (6).docx` (09/09, 10m30s), `(7).docx` (10/09, 9m6s), `(8).docx` (11/09, 9m30s), `(9).docx` (14/09, 18m0s — segunda-feira, recapitula "sexta" = 11/09), `(10).docx` (15/09, 8m0s, recapitula "ontem" = 14/09). Participantes ao longo do período: Igor, Diego, Kauã, Fernando, JB (João Bernardo), Kovalski, Danilo, Donato, Victor Moraes, Ozéias, Luiz Spineli ("Spin"), Francisco Sola, Leonardo ("Léo").

## 🔴 Léo (Leonardo) saiu da empresa — anúncio ao vivo na daily de 14/09

Na daily de 14/09, Igor recebe Léo de volta ("bem-vindo de volta, cara, quanto tempo") e Léo imediatamente anuncia que está saindo, com efeito **imediato no mesmo dia**: *"rapaziada, eu não, a partir de hoje, acho que não vou mais trabalhar com vocês... recebi uma proposta e acabei aceitando, então a partir de hoje o Leozinho não faz mais parte da versa[til]."* Motivo declarado: oportunidade nova, "não tinha muito mais o que aprender aqui dentro". Sem mais detalhe sobre a nova empresa (brincadeiras do time sobre "Vasco"/"gigante da colina" parecem só piada, não confirmação do destino real). Isso é tratado como fato consumado na Review/Retro do dia seguinte (15/09) — ver [`../reviews-retros-planning/2026-09-15-review-retro-retaguarda.md`](../reviews-retros-planning/2026-09-15-review-retro-retaguarda.md), onde Igor cita repetidamente o impacto da saída dele (fila de code review, relação com Ozéias na criação de cards).

**Cruzamento a verificar:** Léo era owner do bug #12514 (permissionamento/token) em [`../conciliacao-fase-2/contexto.md`](../conciliacao-fase-2/contexto.md) e aparece como quem desativou o job de duplicação de desconto em [`../motor-descontos/contexto.md`](../motor-descontos/contexto.md) ("Risco ativo") — ambos precisam de novo owner.

## Conciliação Fase 2 / "Gerenciar Perdas" (Diego)

- **09/09**: Diego relata devbox de 08/09 com Danilo e Ozéias — corrigiu caso em que uma divergência adicionada manualmente na tela de gerenciar perdas não trazia os operadores; agora o gerente do Financeiro pode inputar o CPF na hora de aprovar essa divergência específica (mantendo o comportamento padrão de retornar os dados do operador sênior). Preparou a branch da GMUD (seus cards + Fernando + Kauã), testes ok, GMUD rodou à noite "de certa forma tudo bem"; de manhã um problema "com o Anthony" foi resolvido por Kauã/JB — Kauã segue monitorando.
- **10/09**: card **#12624** (rework do Danilo, feito no "DevConexão", branch desalinhada) — Valdo (quem precisa subir de novo) está afastado essa semana, só consegue domingo; card movido pra Code Review aguardando ele. Nova demanda de 09/09: bug de layout no fluxo de perda das divergências aprovadas (dava a entender que informar CPF ia descontar do operador, mesmo sendo fluxo de perda/contato) — corrigido em força-tarefa, tentaram subir na GMUD mas não deu tempo; **pronto pra próximo deploy**. Diego fica sem task.
- **11/09**: Diego trata pontos pendentes de um sistema referido só como "Wally"/possível transcrição de outro nome (abertura de conta no ERP Oracle, taxonomia, campo de "subir como imediato" pra emissão de conta = mesma data do vencimento) — trabalho ligado ao card ali de retaguarda "que surgiu aquela urgência" que ficou indefinido se sobe na próxima GMUD ou como urgência (já em homologação). Publica ajustes, espera concluir pra mostrar segunda-feira.
- **14/09 (recapitulando sexta 11/09)**: identificado como **card #13013** — trabalhou nos pontos pendentes (taxonomia, campo imediato/vencimento), achou e corrigiu um bug novo no histórico de visualização; hoje (14/09) reunião interna pra revisar antes de reunião com a área de negócio.
- **15/09 (recapitulando ontem 14/09)**: devbox do #13013 com Danilo e Ozéias — validaram todos os fluxos, tudo corrigido, atende requisitos; PR aberta, aguardando aprovação do Valdo. Hoje revisando fila de PRs abertas no Retaguarda; sem task no momento.

**Cruzamento a verificar:** o "sistema Wally"/#13013 parece ser continuação do projeto de "mapeamento de termos pra integração com Oracle" que a Review/Retro de 01/09 registrou como já entrando em sustentação (ver ata linkada abaixo) — não há `contexto.md` dedicado a esse card; vale confirmar se é sustentação avulsa ou merece projeto próprio.

## Saldo Parcial de Caixa / Relatório de Saldos / Dashboard CDs (JB)

- **09/09**: corrigiu problema de API no "saldo parcial de caixa" — refatorou, criou endpoint específico pra checar se caixa está aberto, refatorou a modal pra só chamar quando abre de fato; subiu na GMUD. Agora tentando avançar no "relatório de saldos", buscando ajuda pra uma "engenharia reversa" — Adriana não consegue vir hoje, vai tentar falar com "João" (Oracle) que estava vendo esse assunto. **Segue sem contato com a Maria** (Dashboard CDs) — mandou mensagem de novo, sem resposta.
- **11/09**: revisou PRs (do Fernando e próprios), corrigiu erro que travava boot em Homolog; começou a analisar card **#12795** (passado por Ozéias/Igor) — mapeou cenários de teste.
- **14/09 (recap 11/09)**: enviou pra code review o "relatório de saldos"; ficou "meio perdido" na fila de code review por excesso de comentários pro Fernando. **Maria segue sem responder.** João Brito (Oracle) disse que ia falar com JB mas sumiu — mandou "bom dia" de novo, ainda sem resposta. Sem card no momento.
- **16/09 (Sprint Planning)**: confirma trabalhando em "envio para aprovação" (nome em inglês no card) — espera fechar código e testes essa semana, code review na semana seguinte. **Maria segue sem responder** (mesmo padrão desde 01/09). Novo item "**Conciliação de Depósitos**" — Ozéias vai falar direto com "João" sobre isso, não passou formalmente pro JB ainda.

**Continua sem resolução** o padrão "Maria sumida" já rastreado desde as dailies de 01-08/09 — sinalizar de novo em [`../minhas-pendencias.md`](../minhas-pendencias.md) / [`../dashboard-executivo.html`](../dashboard-executivo.html) se ainda estiverem tratando isso como pendência recente.

## Gamificação (Kauã, Danilo, Kovalski)

- **09/09**: Kauã limpou fila de "code review blocked"; implementou Google Tag Manager ("GoTags Manager") com uma dashboard no próprio perfil pra QA testar (precisa e-mail do Danilo pra dar acesso). Store não puxada de manhã = query sem dado no banco, não bug. Item "Anthony" = defasagem de conhecimento do usuário, não bug.
- **10/09**: Kauã ataca cards que o Leonardo devolveu pra rework (nem todos com fundamento — ex.: cor de botão); repassa Google Tag Manager pro Leonardo acompanhar/testar; precisa falar com Ozéias/Igor sobre seu card de fechamento contábil ("In do contábil").
- **11/09**: Kauã relata muito rework em Gamificação por ter começado tasks antes do AC fechar (AC mudou máscara de CPF de 3 pra 2/4 dígitos); maioria das voltas fazem sentido, corrigindo. Ainda não abriu revisão das PRs do Leonardo. Fala com Ozéias sobre task **#12892** (parte contábil de Conciliação Fase 2) — começou planejamento, criando tela nova; alinhamento com Ozéias à tarde.
- **Danilo** (10-11/09): fez devbox com Kauã sobre card **#12898...9** (ajuste de comportamento da "Silvaar" do portal); fez regressivo pedido pelo Kovalski no "gerar link de acesso" — achou bugs, enviou; testou toda a Gamificação, maioria passou pra homologação, algumas voltaram pra rework (nada muito sério).
- **14/09**: Kauã foca em fechamento contábil (ver seção abaixo); Danilo focou nas tasks de Gamificação de Kauã sexta, fez devbox com ele sobre a task "1289889" de ajuste de comportamento do portal; Kovalski pediu regressivo no SSO ("todo mundo vai resetar OTP na segunda").
- **15/09 (recap 14/09)**: Danilo validou 3 cards da fila do Kauã, mas precisa de resposta dele pra fechar; testou Gamificação de novo, tudo passou sem problema, "todos os ajustes já necessários o canal já resolveu"; em homologação.

## Fechamento Contábil / Oracle — parte de Conciliação Fase 2 (Kauã)

- **14/09**: fluxo completo do portal pronto (fechar, não enviar e-mails ainda), mas ainda não testado com Oracle — "um pouquinho de medo de fazer besteira", vai chamar o Diego pra acompanhar. De manhã, token de e-mail do portal expirou, causando problema — resolvido pelo Spin ("até 2028 a gente não se preocupa com isso"). **Spin pede a Igor uma task pra revisar segurança dos "envios"** — variáveis de ambiente/secrets não estão marcadas como segredo no pipeline (tentativa de privatizar quebrou o pipeline); Igor confirma que vai criar a task.
- **16/09 (Sprint Planning)**: "pronto, só testar algumas coisas a mais e fazer a devbox."

## SSO / Kong / Doc Pendentes / Ciacom / Apex Oracle (Kovalski)

- **11/09**: esqueceu de pedir pra Igor criar tasks. Danilo fez ótimo regressivo em "gerar link de acesso" achando bugs (achados durante apresentação, quando "acabou a bateria"); Kovalski complementou. Resolvendo os bugs sexta; deploy pro ambiente novo assim que o Danilo validar — pronto pra publicação semana seguinte. Precisa da máquina do Ciacom; vai chamar Ozéias sobre "Siga"; tem uma dúvida sobre "pessoal de Redes" — pediu ajuda de Ozéias/Spin. **Spin**: estará em Cuiabá essa semana, pode alinhar com Pablo/Luiz Henrique pessoalmente lá.
- **14/09 (recap)**: mesma pauta (bugs do "gerar link de acesso" já corrigidos, segue arrastando o Ciacom); segunda-feira (15/09) SSO muda de ambiente, "todo mundo vai ser obrigado a resetar os OTPs"; terminou o POP do Keycloak pra sustentação.
- **15/09**: SSO Ponta Avenida → SSO-hub (mesmo DNS), recadastro obrigatório a partir de segunda; achou erro no cálculo da tela de rankings do Siga (não é prioridade — prioridade é o SSO). **Pediu ajuda a Igor**: área de remarcação de preço pedindo acesso de HML (homologação) pra equipe inteira (8 usuários de uma vez, todo dia) — deveria ser só pra gerente/analista principal; Igor concorda em limitar e pede contato com o responsável.
- **16/09 (Sprint Planning)**: "perdido" nos cards do Siga — vão quebrar em várias tasks; descoberto: máquina não alcança IP do Valdo (componentização do Siga) — vai precisar de refatoração pra remover essa dependência; deploy quase pronto, falta front. 2 bugs pequenos do Siga já corrigidos (divergência de valores era timezone Cuiabá×São Paulo; e diferença real de nº de lojas entre ambientes, não bug). **Apex Oracle segue travado** — quem tinha acesso ao portal de admin não está mais na empresa, ninguém tem o acesso; Daniel foi a Cuiabá só pra tentar homologar isso — "não tem muito que a gente possa fazer" (mesmo achado relatado na Review/Retro).

## App de Remarcação / Motor de Descontos SKU (Donato)

- **11/09**: testou tela no portal sobre a nova frente do Motor de Descontos — item cadastrado com SKU completo (visão macro do produto em vez de só os 6 primeiros dígitos do código); indo bem; hoje olha integração com "venda mercantil".
- **14/09 (recap sexta)**: finalizou atualizações do motor de desconto no portal retaguarda sexta; hoje inicia parte de venda mercantil; confirma com Ozéias/Spin que prioridade não mudou; tabela já criada nos bancos 126 e 72 (Thalison); reunião marcada com Thalison (15h) pra alinhar propagação pra loja via "Earthflow".
- **15/09 (recap 14/09)**: devbox de campanhas do processo SKU completo com Jesus/Spin/Thalison — decidiram implementar **tabela de controle nova** pra facilitar a passagem de dados retaguarda→loja pro Thalison. **Isso já está refletido em [`../motor-descontos/contexto.md`](../motor-descontos/contexto.md)** (seção "🆕 Plano de integração de lojas via PRO014_CONTROLE, 15/09") — não é achado novo, só confirma a fonte.
- **16/09 (Sprint Planning)**: parte SKU em review concluída, subiu ontem. Sem mais pendência de motor de desconto por ora; pegando task de "engine" pedida pelo Filipe (Fio); aguardando retorno pro app de marcação.

## App de Remarcação de Preços — Victor Moraes (Markdown, 11/09) — atualização grande, contexto.md desatualizado

> **Não confundir com o app de chão de loja do Donato/Ozéias** (Etiqueta Remarcados) — Victor Moraes é o dono do projeto **Markdown/Remarcação de Preços** ([`../markdown-precos/contexto.md`](../markdown-precos/contexto.md)), que roda fora do board Azure do Retaguarda.

Victor: terminou o desenvolvimento de uma bateria de melhorias que a área tem testado; PRs abertas aguardando deploy/revisão; *"a gente tá praticamente o mês todo fazendo esses testes com a área e eu acredito que dessa semana a gente fecha todas as melhorias mesmo. Arthur não tem nem mais o que sugerir ali."* Depois dessa bateria, **começa a Fase 3** — implementação da branch de "remarcação incrementada".

**`markdown-precos/contexto.md` está parado em "55% — sem atualização desde 12/08/2026" e prazo revisado de 15/08 "já vencido sem confirmação"** — esse achado de 11/09 mostra progresso real (fase praticamente fechada, indo pra Fase 3), mas o arquivo de contexto não reflete nada disso.

## Sola / Conciliador de Tesouraria (09/09)

Francisco Sola perguntou sobre uma correção pedida ao Ozéias pra que o conciliador não duplique saldos da tesouraria — Igor confirma que **JB está desenvolvendo isso** (a mesma linha de "saldo parcial de caixa" acima); Sola pergunta previsão de subida, Igor vai confirmar com "Vitor"(Victor?)/pessoa que não entrou na call.

## Pesquisas Colaboradores — menção breve na daily de 14/09 (sem achado novo)

No início da daily de 14/09 (antes do standup formal), Spineli pergunta a Igor sobre o andamento do projeto Pesquisas Colaboradores; Igor resume o que já foi levantado na call de 11/09 (envio via e-mail/número pessoal do Senior, pesquisa "anônima, só que depende", confirmação de que **ninguém tem acesso a AD** — por isso o modelo atual via Forms segue sendo referência de baseline) e confirma que será **um portal novo, apartado do que existe hoje**. Não traz informação além do que já está em [`../pesquisas-colaboradores/contexto.md`](../pesquisas-colaboradores/contexto.md) e na ata de [`2026-09-11-call-thais-francisco.md`](../pesquisas-colaboradores/2026-09-11-call-thais-francisco.md) — registrado aqui só como confirmação, não como achado novo.

## Cruzamentos a verificar

- **Léo saiu da empresa (14/09)** — precisa de novo owner pro bug #12514 (conciliação-fase-2) e pro job de duplicação de desconto (motor-descontos); impacta rotina de code review do time inteiro (ver Review/Retro de 15/09).
- Card **#13013** ("sistema Wally"/nome garbled) sem `contexto.md` próprio — confirmar se é sustentação do projeto de mapeamento Oracle já fechado em 01/09 ou frente nova.
- **Markdown/Remarcação de Preços (Victor)** — `contexto.md` desatualizado desde 12/08; achado de 11/09 indica que a fase atual está prestes a fechar e a Fase 3 começa.
- Área de remarcação de preço pedindo acesso HML em excesso (Kovalski, 15/09) — sem responsável identificado ainda pra alinhar.
