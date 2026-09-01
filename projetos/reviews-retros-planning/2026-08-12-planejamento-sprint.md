# Transcrição — Preparar próxima sprint (12/08/2026)

> Transcrição bruta, convertida de `Preparar próxima sprint .docx` (raiz do workspace) e limpa de ruído de reconhecimento de voz. Reunião de planejamento/triagem entre Ozéias (liderança, cross-squad Retaguarda + VAR 3.0) e Igor (PO), passando card a card pelo board para decidir prioridade da próxima sprint e fazer limpeza de backlog.

**Data:** 12 de agosto de 2026, 19:35 · **Duração:** 19m06s
**Participantes:** Ozéias Denis de A. Tavares (liderança), Igor Diniz Camargo (PO), Leonardo Henrique da Silva — Léo (dev)

---

**Ozéias** (0:03) — PPO não precisa se preocupar, vamos conseguir tratar direto pela Oracle. Um problema a menos. O que a gente precisa focar essa semana? *(abre o board)* Vamos lá: Conciliação Fase 2 — sexta-feira passada pegamos alguns pontos, mais um problema que o Léo não tinha passado porque o Diego estava focado nisso. Tem um bug na parte das linhas, precisamos ajustar.

**Igor** (1:17) — Beleza.

**Ozéias** (1:22) — Vindo pra cá: Portal Gamificação — preciso validar isso, porque não consigo olhar em homolog, nunca está lá. Será que tiraram de homolog?

**Igor** (1:31) — É um ponto — eu já estava pensando: agora que a Conciliação Fase 2, se surgir algo, vai ser mais correção, dá pra deixar o Diego focado nisso e voltar o Kauã pra Gamificação, que ele tem bastante coisa ainda pra fazer lá.

**Ozéias** (2:04) — Boa. Então o Diego arruma o problema que a gente identificou, deve ser rápido.

### Indicadores de performance (SIGA)

**Ozéias** (2:04) — Indicadores de performance voltou — mandei mensagem no grupo e o search pro Léo. Em tese está tudo desenvolvido, o Danilo precisa validar o fluxo inteiro. Está tudo em homolog e no Dev — ele já pode começar a validar, tipo hoje, o quanto antes. Em paralelo a gente valida se os dados batem — isso ele não vai conseguir validar sozinho, se a regra bate a gente valida em conjunto.

**Ozéias** (2:48) — GNRE, pelo que o Léo passou, está arrumado, certo Léo?

**Léo** (2:56) — Sim senhor, testamos ontem e passou.

### Conciliação de depósitos / Migração VARRet

**Ozéias** (2:57) — Conciliação de depósitos — tem aquela parada do número da loja, lembra que eu falei? Mas isso pode segurar por enquanto, enquanto terminamos as outras. O JB está terminando a Migração VARRet, não é? Como ficou?

**Igor** (3:35) — O lote 1 já está pronto. O lote 2 ele terminou esses dias, está em processo de code review e QA.

**Ozéias** (3:40) — Verdade? Ele queria falar comigo sexta, eu estava no dentista e não consegui. Vou marcar um papo com ele e a gente sobe tudo.

**Igor** (4:04) — Depois disso, o que ele está fazendo agora — combinamos com o Léo — é pegar tudo que já estava feito na fase 1 que ainda exporta Excel/PDF direto na tela e subir isso via worker + envio por e-mail, em vez de fazer na tela. É só essa correção que ele tem, de resto está meio pronto. Junto com isso tem umas coisinhas do Dashboard CDs pra ele corrigir, mas nada muito absurdo.

**Ozéias** (4:34) — Tô ligado, o Daniel tá enchendo o saco por causa disso também, né?

**Igor** (4:37) — Mas vai voltar a andar.

### Overlimit

**Ozéias** (4:42) — A gente também tem o Overlimit pra fazer, mano. Precisa entregar, é simples em tese — você lembra, Léo?

**Léo** (4:56) — Sim.

**Ozéias** (4:57) — Basicamente é uma telinha de import de Excel — já tem na documentação.

**Igor** (5:04) — O import é dos clientes que podem receber esse bônus do overlimit, né?

**Ozéias** (5:12) — Isso. Precisa criar uma tela pra fazer import de planilha, com leitura e [trecho inaudível]. E aí, pra mandar essa base pra loja — a gente já tem uma parada que faz isso, não tem lá no RPA? Tipo a blacklist?

**Igor** (5:39) — Mandar pra loja, tipo rodar na loja pra saber se o cliente pode receber?

**Ozéias** (5:52) — Isso — basicamente igual à blacklist, só muda que aqui vai ser outra base, e o VAR tem que consumir essa base. Precisamos subir isso na release de setembro do VAR, porque depois vem o freeze.

**Ozéias** (6:19) — Acho que até o Gui estava mexendo nisso, será que tem só um Gui lá também?

**Léo** (6:29) — Quem fez a blacklist também? Vai ser mais fácil de mexer partindo dela.

### Onboarding do Fernandes (novo dev Júnior)

**Ozéias** (6:39) — E aí, o pessoal que está chegando — a gente tem várias paradinhas de sustentação pra atacar, ir passando pra eles. Por exemplo, o novo menino — como é o nome dele?

**Igor** (7:16) — Fernandes.

**Ozéias** (7:17) — O que ele está fazendo agora?

**Igor** (7:21) — Quando ele chegou, o Danilo fez uma geral no portal, identificou uns bugzinhos e ele estava corrigindo. Hoje está corrigindo um bug no contador de conciliação, no front.

**Ozéias** (7:21) — Qual o nível dele?

**Igor** (7:36) — Júnior.

**Igor** (7:39) — O Léo pode descrever melhor o perfil dele.

**Ozéias** (7:48) — Ótimo, temos bastante coisinha aqui — depois eu vou pegar tudo isso no nosso Excel, revisar e reabrir os testes que faltam, porque a maioria é besteira, mas tem coisa que a gente precisa implementar mesmo.

**Igor** (8:11) — A gente pode aproveitar que ele está chegando agora, precisa se acostumar com o sistema — é até bom passar bastante besteira de lugares diferentes pra ele mexer em várias partes. A gente tira da fila e entrega um monte de coisa, a galera fica feliz.

**Ozéias** (8:24) — Exatamente. A gente volta a entregar coisa, porque não lembro a última vez que entregamos algo — só ficamos apagando incêndio e fazendo projeto grande.

**Léo** (8:40) — Acho que a ideia é o Fernandes ficar em sustentação mesmo por enquanto, essas paradinhas.

**Igor** (8:47) — Se você quiser priorizar o que já tem controle pra criar à vontade, lembrando: no board, na coluna de backlog tem bastante coisa que você criou faz tempo — eu nem cheguei a mexer porque não sei se algumas ainda precisam ser feitas. Imagino que tenha coisa lá que já não precisa mais.

### Triagem ao vivo do backlog (coluna Backlog)

**Ozéias** (9:42) — *(abrindo a coluna Backlog no board)* Fase 4... NF cancelada... Automação Fiscal — essa aqui tem umas paradas, aquelas que o Kovalski mandou criar, que ele ia precisar fazer. Agora eu não sei mais, sinceramente — lembra que ele falou que tinha uns 40 cards? Tudo isso está em Automação Fiscal, não sei nem o que é a maioria — provider service da GNRE pra usar em banco, não sei o que é; repositório, não sei; criar migration; modelar tabela de configuração de UF; corrigir caracteres UTF-8 no portal — tem card criado há muito tempo, não faço ideia do que é isso daqui pra cima.

**Igor** (11:05) — Nossa.

**Ozéias** (11:23) — Posso descartar? *(seguindo)* Tudo que você achar que não faz mais sentido, pode descartar.

**Igor** (11:27) — Pode.

**Ozéias** (11:43) — Vou revisar tudo isso pra ver o que ainda serve.

**Igor** (11:51) — É o que eu deixei explicando lá atrás: tudo que era de projetos que meio que pararam e não estavam mais andando. Tem muita coisa de SIGA que dá pra reaproveitar se for usar o card de novo. Tem bastante coisa de SPPO também.

**Ozéias** (12:06) — SPPO pode morrer, não vamos fazer.

**Ozéias** (12:34) — *(revendo cards antigos, ~1 ano parados)* Se está com bug há um ano e ninguém reclamou mais... tem uns comentários aqui, esse é da nova empresa, vou deixar por enquanto.

**Igor** (13:09) — Esse não tem comentário nem calor nenhum, foi feito refinamento e depois nada.

**Ozéias** (14:15) — Esse aqui o Léo gosta, o Léo pode atuar.

**Léo** (14:20) — Nem lembro pra que fizemos isso, faz tempo.

**Ozéias** (15:16) — A unificação da base pode fechar esse aqui.

**Igor** (15:31) — Não lembro desse card, não sei se foi feito ou se ainda precisa.

**Ozéias** (15:34) — Cara, tudo que está aqui há mais de um ano já foi, mano — está parado há um ano.

**Igor** (15:44) — Sempre penso: se ficou parado um ano, teoricamente não era tão importante — mas se for legal de fazer, bota pro Fernandes.

**Ozéias** (15:58) — Esse é recente, uns 4 meses.

**Ozéias** (16:46) — Esse aqui sim, vou colocar.

**Igor** (16:51) — Sem que bloqueie os usuários.

**Ozéias** (16:58) — A [área] falou disso comigo outro dia, lembra?

**Ozéias** (17:04) — Você já limpou as outras filas e jogou tudo pra cá?

**Igor** (17:16) — Limpei o To Do e o Refinement. Alguns eu joguei pra lá porque achei interessante refinar depois, mas agora está tipo vazio de novo.

**Ozéias** (17:25) — Motor de Descontos?

**Igor** (17:31) — É a melhoria do Motor de Descontos que não chegamos a fazer, dá pra pensar com o Arthur. Pode deixar.

**Igor** (17:39) — Motor de Descontos é a mesma ideia — a gente não levou pra frente, mas é legalzinha, pode subir com ele.

**Ozéias** (17:48) — Certo. O que precisamos fazer agora: você consegue ver com o Kovalski, o Kauã ou o Léo essas que estão em Automação de Fluxo Fiscal? É a lista que o Cove [Kovalski] mandou eu abrir — não sei o que já foi feito, o que não foi, se avançou ou recuou.

**Igor** (18:24) — Beleza.

**Ozéias** (18:24) — Acho que até sexta eu finalizo essa daqui, tá bom?

**Igor** (18:32) — Perfeito. Se quiser, joga todas que a gente tem pra trabalhar/refinar mesmo na coluna de Refinement, só pra ter separado e saber o que precisa refinar.

**Ozéias** (18:39) — Tá bom — todas que estão ficando, que já estão mínimas pra desenvolver, eu já jogo pra cá, deixo em Refinamento.

**Igor** (18:51) — Beleza.

**Ozéias** (18:54) — Fechado então. Valeu, Léo.

**Igor** (18:59) — Valeu, gente.

---
*Transcrição encerrada em 19:00.*
