# Digest — Dailies Retaguarda, 24–25/09/2026

> Síntese das 2 dailies do squad Retaguarda: 24/09 (quinta, 8m18s) e 25/09 (sexta, 13m22s). Fontes: `RETAGUARDA - Daily (2025)  (16).docx` (cabeçalho interno confirma 24 de setembro de 2026), `RETAGUARDA - Daily (2025)  (17).docx` (cabeçalho interno confirma 25 de setembro de 2026) — nesse par a numeração de arquivo bateu com a ordem cronológica, mas confirmado pelo cabeçalho de data dentro do docx, não presumido pelo sufixo. Participantes: Igor, João Bernardo (JB), Kauã, Kovalski, Diego, Fernando, Matheus Gabriel Donato (Donato), Danilo, Filipe de Lacerda, Francisco Sola e, só em 25/09, Luiz Spineli Lucchi Neto ("Spin"), que entrou com pauta própria.

## Siga — card de rework do "Siga público" reatribuído ao Kovalski; Ciacom segue travado; deploy de 11 itens previsto pra domingo

**25/09:** Igor identifica que o card de rework aberto pelo teste de comparação do Danilo (achado do digest anterior, 17–23/09) está no nome do Danilo e pede pra passar pro Kovalski: **"esse aqui, ah, ele jogou pra rework, legal, eu vou botar no seu nome então, tá?"**. Kovalski confirma o escopo: **"é do siga público que tá errado"** — cálculo de ranking incorreto — e diz **"eu acho que eu consigo terminar tudo hoje"** (25/09).

**24/09:** Kovalski, sobre o **Ciacom ("CIA")**: **"conseguimos travados, fui dar uma cobrada ontem do pessoal ver se conseguia resolver alguma coisa e não dá, vai ter que aguardar mesmo"** — segue sem solução, sem novo prazo.

**25/09:** Diego conversou com Ozéias — **domingo (27/09) vai subir "11 do siga"**, que já está "meio que certo"; vai revisar o que sobe pra deixar pronto.

**Ação:** [`../siga/contexto.md`](../siga/contexto.md) precisa registrar (1) o bug de cálculo de ranking no Siga público — achado por Danilo em teste de comparação (digest 17–23/09), reatribuído ao Kovalski em 25/09, previsão "hoje"; (2) Ciacom (seção 1.1) segue travado por terceiros, sem prazo novo, desde pelo menos 23/09; (3) deploy de 11 itens do Siga previsto pra domingo 27/09 (Diego/Ozéias) — não confundir com o retry de migração do SSO mencionado no digest anterior para 28/09, que não foi citado em nenhuma das duas dailies deste período (sem confirmação se segue de pé).

## Pipeline de certificado digital / nova arquitetura (Kovalski) — frente nova, sem contexto.md próprio

**24/09:** Kovalski pede a Igor pra criar uma task sobre **"pipeline certificado digital"** — explica: **"a ideia é rodar uma pipeline e atualizar todas as máquinas de uma vez, inclusive as lojas"** — é o início de uma "POC de nova arquitetura".

**25/09:** Já está **"basicamente tudo pronto, com todos os inscritos"**, mas travou no devbox por falta de permissões. Conversou com **Luiz Pinheiro** e vai levantar exatamente quais permissões precisa, **"pra não ter acesso a mais coisas do que deve"**.

**Ação:** não há projeto/`contexto.md` existente que cubra essa frente — recomendo confirmar com Igor se é uma extensão do épico de SSO (#11853, mesmo Kovalski) ou se merece registro próprio; hoje só existe menção dispersa nas dailies.

## Overlimit / Cartão Avenida (Luiz Spineli) — escopo novo, prazo curto "até segunda/terça" (28-29/09)

**25/09:** Luiz Spineli traz pauta própria: **"a gente precisa fazer uma parada para o overlimiting, uma função lá de crédito emergencial que a gente vai ter no Cartão Avenida"** — precisa **"criar uma tela lá no portal do RPA de cartões"**, **"a mesma ideia do blacklist, só que pra poder fornecer um produto"**: upload de uma tabela com os CPFs elegíveis; **"posteriormente"** também o valor, e no futuro isso será automatizado via um projeto chamado **"Behavior"**. Pede que, saindo da daily, **JB e "Higuinho" conversem com o Gui e com o Gustavo** pra pegar os detalhes. Prazo dado por Spineli: **"dá pra fazer até segunda, terça-feira, e a gente precisa disso rápido, ok?"** (ou seja, 28-29/09). Igor confirma que já tinha conversado bastante com "eles" e que o **Léo participou também**, então "a gente meio que já sabe o que tem que ser feito" — combinam de confirmar com o Gui que dá pra iniciar.

**Ação:** [`../overlimit/contexto.md`](../overlimit/contexto.md) — o arquivo hoje descreve o escopo (import de planilha Excel + distribuição pra loja igual blacklist) como definido em 12/08 sem prazo firme confirmado; agora há um **prazo explícito e apertado (segunda/terça, 28-29/09)**, um dono operacional novo mencionado para a conversa de detalhamento (**JB + "Higuinho"**, falar com **Gui e Gustavo**), e a menção a um projeto futuro de automação chamado **"Behavior"** que não consta no arquivo.

## Motor de Descontos — reestruturação do esquema de banco vai bloquear cards (Donato/Fábio/Thalison)

**24/09:** Donato avisa que o motor de desconto **"vai ter alterações"** porque **Thalison e Fábio "tinham alinhado um ponto lá entre eles e não tinham passado pra gente"** — precisa incluir isso antes de seguir. Ainda em 24/09, Diego agrupou os 3 cards de motor de desconto numa única branch (nome do épico), estava **"só uns ajustes"** e já passou pra devbox com Danilo.

**25/09:** Donato confirma o que se desenhava: **"ontem a gente teve a call com o pessoal sobre o motor de descontos e vamos ter uma reestruturação no esquema do banco"** — está aguardando o Fábio passar os detalhes, vai mandar a transcrição da call e a reestruturação pro Igor **"pra gente poder subir as novas testes"**. Pra não travar o Danilo e deixar visível, Donato vai **mover o que está [em teste] pra um bloco de "não deve ir pra frente antes disso"**. Igor pede que, se algo for movido, deixem comentário no card explicando o motivo.

**Ação:** [`../motor-descontos/contexto.md`](../motor-descontos/contexto.md), seção "Bloqueios e pendências" — precisa de uma entrada nova: reestruturação do esquema de banco decidida em call de 24/09 entre Thalison/Fábio (sem a Retaguarda na mesa originalmente), Donato aguardando detalhes do Fábio antes de liberar os testes já feitos por Danilo, cards sendo movidos pra bloco de bloqueio até isso resolver.

## Gamificação / Fechamento Contábil (Kauã) — reunião de negócio marcada, teste de roleta e cenário extra

**24/09:** Kauã resolveu a "Dep Stream" (nome garbled, confirmar), falta devbox; avisa que amanhã (25/09) **Ozéias tem reunião com "as meninas" e também com "o chefão do negócio" (nome não citado)** sobre gamificação.

**25/09:** Kauã fez devbox da **"roleta"** com Danilo, mas sem VPN foi difícil testar em homologação — testou local; segue testando em HML. Também recebeu de alguém identificado só como **"Filme"** (nome garbled) um pedido de **roteiro de testes pra sábado**, já entregou um.

Danilo (25/09) confirma que ficou faltando devbox do "Kauãzinho" ontem por impedimento de VPN (bate com o relato do Kauã) e que hoje está olhando duas tasks pra testar: **gamificação e fechamento contábil** — alguém pediu pra **incrementar o teste de gamificação com mais um cenário**.

**Ação:** [`../gamificacao/contexto.md`](../gamificacao/contexto.md) — sem contradição de escopo, mas vale registrar a reunião de negócio de 25/09 (Ozéias + "chefão do negócio" não identificado) e o pedido de cenário extra de teste, ainda sem detalhe do que mudou.

## Reenvio para Aprovação / "Revisão" (JB) — segue sem fechar, erro 500 novo

**24/09:** JB acredita ter finalizado o card de reenvio; combinou devbox pra amanhã (25/09) com "Zé" (estava offline), Danilo e ACS.

**25/09:** JB está esperando o Ozéias pra mostrar o teste; no rework, identifica que falta um e-mail que **"deu errado no teste do Danilo"** e que outro ponto é só reprocessar a conciliação — mas ao tentar testar, **"deu um 500 no portal"**; suspeita que **"está faltando uma migration"** e já estava alinhando isso de manhã com alguém identificado só como **"a mão"** (nome garbled, não dá pra confirmar).

Nenhuma menção à "Maria" nas duas dailies deste período — a ambiguidade levantada no digest 17–23/09 (se a "Maria" de 18/09 era sobre este card ou sobre o Dashboard CDs) **segue sem esclarecimento**.

**Ação:** nenhum arquivo específico de projeto rastreia esse card hoje (não há `contexto.md` próprio para "Reenvio para Aprovação"); registrar como pendência aberta se/quando o dono decidir criar um.

## Concessão de Depósitos (JB / Ozéias / João) — reunião marcada pra 25/09 15h

**25/09:** JB explica a Luiz Spineli o pendente: **"tem uma tarefa agora que é realmente saber cada depósito ali de qual loja que é"** — os valores já estão prontos, mas falta identificar a loja; tentou falar com "João" que estava "meio fora" na sala. **Ozéias vai falar com JB hoje (25/09) às 15h sobre concessão de depósitos** — JB não sabe se Ozéias e João já resolveram entre eles.

**Ação:** sem `contexto.md` dedicado identificado; se essa frente ganhar prazo/escopo formal na reunião de 15h de hoje, vale decidir se cria projeto próprio ou entra em algum já existente.

## Conciliação — bug de processamento que "sumia" uma loja (Kauã/Danilo)

**24/09:** Kauã relata ter pegado uma tarefa (nome garbled — soa como "Ready for Dev") e começado a resolver um bug notado durante demo: **"quando a gente estava em de Mood [demo], eu percebi que estava com alguns bugs"**. Danilo detalha: **"aquela paradinha que ele chegava faltando uma loja e travava, é realmente um bug (...) ele estava só sumindo, então às vezes ele meio que trava na última loja e não processa ela (...) isso é um problema bem grande, eu percebi que estava rolando faz uns dias de conciliação já"**.

**Cruzamento a verificar:** [`../conciliacao-fase-2/contexto.md`](../conciliacao-fase-2/contexto.md) já registra instabilidade recorrente do "job noturno da conciliação" (duplicação de lojas no processamento, múltiplas ocorrências). O sintoma descrito aqui (loja "sumindo"/não processada) é diferente de duplicação — **não dá pra confirmar pela transcrição se é a mesma instabilidade de fundo ou um bug novo** no mesmo job. Vale confirmar com Kauã/Danilo antes de tratar como o mesmo item.

## Automação de contas de energia dos portais (Luiz Spineli / Diego / "José") — retomada pedida, sem contexto.md próprio

**25/09:** Luiz Spineli pergunta pelo andamento da **"automação das contas de energia lá dos portais"**. Diego esclarece que hoje o fluxo (o mesmo "sistema de conexão" já citado em digests anteriores) está só na etapa de **"a loja envia a conta e faz a extração"** — a automação direta com portais de fornecedores de energia (ex.: Enel) **ainda não começou**. Spineli: **"eu estava na reunião de um projeto ontem e esse é um ponto pendente (...) a gente precisa retomar essa automação, seria um próximo passo natural"**. Diego confirma que **"José"** já comentou informalmente sobre isso, mas **"ainda não foi nada definido e nem nada escopado"**. Igor sinaliza que vai conversar pra levantar mais detalhes antes de ir atrás de desenvolver.

**Ação:** não existe `contexto.md` dedicado a esse "sistema de conexão"/automação de contas — está disperso em dailies anteriores (referenciado no digest 17–23/09 na seção "Dev Conexão / Homolog"). Com um pedido explícito de retomada por Spineli, vale decidir se cria projeto próprio.

## Diego — fila de devbox limpa, 3 cards de motor de desconto agrupados, code review em aberto

**24/09:** Completou o card **13112** (reorganização do menu lateral do módulo de conciliação); o card **12793** que estava pendente foi pra devbox; agrupou 3 cards de motor de desconto numa única branch nomeada pelo épico, trabalhou nos 3 juntos, ficaram só ajustes finais, já marcou devbox com Danilo. Igor confirma que um card enviado por ele deveria estar com o nome do Diego — Diego confirma que acabou de mover.

**25/09:** Revisou PRs do Kauã pela manhã, fez devbox com Danilo de toda a fila pendente, abriu as PRs restantes pra code review (pede apoio de quem puder revisar). Ficou sem card novo hoje — avisou que se continuar sem nada, avisa o Igor.

**Ação:** [`../conciliacao-fase-2/contexto.md`](../conciliacao-fase-2/contexto.md) pode registrar a conclusão do #13112 (reorganização do menu lateral) se ainda não estiver marcado como entregue.

## Automação Fiscal / Engine (Donato) — segue corrigindo trabalho do Kovalski, novo problema com devoluções

**24/09:** Donato corrigiu partes do "portal de automação" que Kovalski havia feito; checou a pipe da "vivo" pra garantir que a subida ocorra OK; hoje ia olhar de novo o portal de automação porque **"o Fábio pegou um probleminha lá com as devoluções"**.

**Ação:** [`../automacao-fiscal/contexto.md`](../automacao-fiscal/contexto.md) — vale registrar que quem está corrigindo agora é o **Donato** (não mais só o Kovalski) e o novo problema de devoluções reportado por Fábio, ainda sem detalhe técnico na transcrição.

## Sem menção neste período

- **Sola / Conciliador de Tesouraria** — pendência sem dono, aberta desde 09/09 (ver digest 17-23/09), não foi mencionada; Sola só confirma "tudo certo" em 25/09.
- **App de Remarcação (Donato/Victor/Ozéias/Thalison)** — bloqueio de GMUD/AD do digest anterior não foi retomado diretamente; único toque foi Kovalski (24/09) dizendo que pegou "a questão do Spin pra ver sobre o app de remarcação, sistema de login" e que "tava certinho", "o Diego deve ter confundido" — pediu uma validação. Não esclarece se o bloqueio de AD já foi resolvido.
- **Dashboard CDs / Maria** — sem menção; ambiguidade do digest anterior segue aberta.

## Cruzamentos a verificar

- **Siga público**: bug de ranking (achado por Danilo) reatribuído ao Kovalski em 25/09, previsão "hoje" — conferir se realmente fechou.
- **Ciacom**: segue travado por terceiros sem prazo, há pelo menos 2 dailies seguidas sem novidade.
- **Overlimit**: prazo apertado (28-29/09) dado por Spineli, sem confirmação ainda de que Gui/Gustavo validaram início — Igor e JB combinaram de confirmar.
- **Motor de Descontos**: reestruturação de banco pode bloquear cards já testados por Danilo — aguardando detalhes do Fábio via Donato.
- **Conciliação**: bug de loja "sumindo"/não processada (Kauã/Danilo, 24/09) — confirmar se é o mesmo job instável já registrado em `conciliacao-fase-2/contexto.md` (lá o sintoma registrado é duplicação, não omissão).
- **Automação de contas de energia**: pedido de retomada por Spineli sem projeto/contexto.md próprio — decidir se formaliza.
- **Pipeline de certificado digital (Kovalski)**: frente nova sem projeto/contexto.md próprio.
