# Transcrição — Dashboard CDs · Mudanças na planilha (12/08/2026)

> Transcrição bruta (Zoom/Teams), convertida de `Dashboard CDs - Mudanças planilha.docx` (raiz do workspace) e limpa de ruído de reconhecimento de voz. Guardada aqui como registro completo; o resumo estruturado está em [reuniao-maria-2026-08-12.md](reuniao-maria-2026-08-12.md).

**Data:** 12 de agosto de 2026, 19:01 · **Duração:** 22m06s
**Participantes:** Igor Diniz Camargo (PO), Maria Leticia Souza Clavico (área de operação/CD), João Bernardo Ferreira Neto — JB (dev, dono do Dashboard CDs), Leonardo Henrique da Silva — Léo (dev)

---

**Igor** (0:03) — Reunião direto ao ponto: quando terminamos o Dashboard CDs, tiveram mais revisões e a Maria encontrou coisas para mudar na planilha do lado dela. Queremos entender tudo que ela mudou nesse processo pra gente poder refazer também na parte do sistema, e pegar uma planilha atualizada de hoje como base nova de comparação. Também tem a dúvida: o JB comentou que ela ia trocar a fonte de dados e sair do WMS — isso chegou a acontecer?

**Maria** (0:50) — Ainda não. A gente conseguiu identificar onde estava o problema e conseguiu contornar. Então não vamos precisar fazer essa mudança.

**Igor** (1:03) — Perfeito, então o foco aqui é entender o que mudou no processo de vocês e na planilha.

**Maria** (1:15) — Eu ia atualizar com vocês, mas meu BI não está funcionando. Deixa eu ver se mando mensagem no grupo de operação.

*(compartilhamento de tela — Maria mostra a planilha)*

**Maria** (2:32) — A gente só vai ter uma alteração na data: como o inventário foi no final de junho nos dois CDs, estou puxando a partir do dia 29. O resto continua igual, sempre a data de amanhã, embalagem normal, nada mudou.

**Maria** (3:17) — A única coisa que acrescentei foi essa tabelinha de loja, onde peguei todas as lojas que a gente tem no CD e fiz uma soma só para buscar as peças que estão há mais de 7 dias.

**Maria** (3:47) — Esse vai ser o gráfico novo: mostra a quantidade de peças, a loja e a quantidade de dias que ela está no CD.

**Igor** (4:02) — Confirma que esse gráfico é novo, a gente não tinha?

**Maria** (4:11) — Isso, é novo.

**JB** (4:11) — A gente substitui pelo que tinha antes, Maria, nos dois CDs?

**Maria** (4:15) — Nos dois CDs.

**Igor** (4:28) — Então vai ser nos dois CDs. Mantém o corte de Top 20 ou pode tirar?

**Maria** (4:31) — Pode manter o Top 20, porque senão fica muito extenso — é muita loja.

**Maria** (4:43) — Aqui não tem porque o CD ainda não deu 7 dias, mas é dos 2 CDs.

**Igor** (4:49) — Peças a mais de 7 dias e o lead time médio, certo?

**Maria** (4:55) — Isso. Loja, quantidade de peças e lead time. Às vezes a quantidade de peças por loja é maior mas o lead time é menor — por isso classifiquei pelo tempo do lead time, do maior para o menor.

**Igor** (5:51) — Então filtrar pelo filtro não é o mesmo que classificar pelo lead time, certo?

**Maria** (5:55) — Isso. Das rotas não mudou nada — continua mostrando CD 80 e CD 83 normal.

**Maria** (6:10) — No faturado eu não lembro se a gente tinha 2 guias quando te mandei antes, mas agora eu puxo os dois CDs junto — lá dá a opção de escolher os dois na hora de filtrar. Hoje incluo os dois porque não temos mais divisão de rotas — só um cubo para as rotas agora. O pessoal do transporte conseguiu unificar (do jeito que já carregávamos Alagoas). Então mantenho uma base só, separada por CD, e já consigo puxar o CD direto no PROCV.

**Igor** (7:12) — E antes eram 2 planilhas separadas, agora é uma só?

**Maria** (7:17) — Isso, era 2 bases, agora é uma só.

**JB** (7:20) — Então, Maria, agora não tem mais aquilo de ficar checando se a rota é da loja mesmo — sempre vai estar certo?

**Maria** (7:30) — Isso, agora já está certinho. Só se tiver alguma alteração de rota, aí a gente consegue modificar manualmente se precisar.

**JB** (7:46) — Mas você prefere que a gente também não separe mais por CD lá, deixa só uma igual está aí? Se precisar alterar uma rota, altera.

**Maria** (7:58) — Acho que vai ser mais trabalhoso se vocês tirarem. Pode manter como está — eu consigo olhar e alterar se tiver algo diferente, porque pode ter alguma loja que entra em outra rota e eu ainda não consegui ajustar lá.

**Maria** (8:30) — Na quantidade de peças eu faço um PROCV agora. Quando puxo do WMS, ele já me dá a quantidade certinha, que eu colo pra não mexer na minha base. Criei uma coluna auxiliar em cima do "pack" — porque estávamos com divergência de quantidade de peças, e agora consigo puxar a quantidade pelo pack no BI.

**Igor** (9:30) — Só confirmando: pack é quantas peças tem, é isso?

**Maria** (9:32) — Isso, exatamente.

**Maria** (9:40) — Às vezes aparece "nada" embaixo porque recebemos muitos códigos e o pack muda sempre. Eu filtro pelo "nada", copio, tiro formatação e duplicadas, pego essa lista de packs inteira e jogo no BI — se ele estivesse funcionando, ajudaria.

**JB** (10:19) — Acho que eu já faço isso, consigo pegar os packs. Posso fazer uma tabela nova no front pra mostrar esses packs e você poder alterar a quantidade de peças também.

**Maria** (10:29) — Acho que foi só essas duas alterações mesmo. Do mapa a gente não precisa mexer ainda, porque ainda estamos em mudanças ali — não está sendo usado, pode manter como está. Quando eu tiver uma atualização eu passo.

**Maria** (11:13) — Deixa eu ver uma coisa — acho que mudei um cálculo. Eu estava fazendo média sobre média nessa de baixo, que é o lead time geral, e estava errado. Fiz uma média ponderada, porque cada rota tem uma quantidade x de lojas e x de peças. Fiz isso nos dois CDs.

**Igor** (12:15) — Certo. Já que mantivemos o WMS, o relatório do WMS mudou alguma coisa?

**JB** (12:25) — Mudou a data, ela falou.

**Maria** (12:26) — Só a data. Provavelmente se a gente for puxar do ano passado não vai encontrar nada, porque mudamos de ano. Seria mais interessante puxar a partir do último inventário.

**Igor** (12:28) — Então tem que falar com o Serginho da Silva pra atualizar o relatório que chega pra gente.

**Maria** (12:57) — Acho que foi só isso — vou atualizar agora e mando pra vocês no grupo.

---

### Segunda parte — pedidos de melhoria (filtros no gráfico)

**Igor** (13:08) — Maria, além disso, você quer entrar já no assunto de filtro no gráfico — possibilidade de filtragem no dashboard — ou prefere deixar pra depois?

**Maria** (13:26) — Pode falar.

**JB** (13:38) — Vocês tinham comentado (ela e o Laurysson, acho) sobre alterar o gráfico — "quero ver tal coisa, ordenado por tal coisa". Não lembro direito, ela deve saber melhor.

**Maria** (14:01) — O que eu queria: pega essa rota aqui — está disponível, mas na verdade pode estar carregando, então não tem os 12.000 disponíveis pra carregar de fato. Queria um campo auxiliar, nem que fosse manual, tipo "último carregamento da rota" — data de quando essa rota foi carregada pela última vez. Isso já evitaria mostrar como "disponível" uma rota que na prática já sumiu do relatório porque carregou ontem.

**Igor** (15:23) — Isso a gente consegue. Só não peguei se dá pra puxar de algum lugar ou se seria você preenchendo.

**Maria** (15:32) — Se for pra preencher, não tem problema. Só queria ver se dá pra ter essa informação ali.

**Igor** (15:45) — Então é um campo mesmo que seja você preenchendo manualmente todo dia, pra facilitar depois, tá bom.

**Maria** (15:54) — Acho que dava pra cruzar com o SIACON depois, não sei se tem como. Mas inicialmente, se der pra fazer manual, já está bom.

**Maria** (16:13) — Outro pedido, do Francisco: colocar a média de carregamento por rota. Por exemplo a rota 100 tem 4.000 disponível, mas a média dela é 15.000 — então ela está com uns 90% da rota completa. Ele queria essa visão de "quanto é a média de carregamento por rota" ao lado do disponível atual (ex.: rota 100 = 15.000 de média, 4.000 disponível = ~38% da rota).

**Igor** (17:26) — Essa média por rota já existe?

**Maria** (17:28) — Já existe, está na planilha de estoque. Seria só trazer essa informação pro gráfico — nem que fosse em cima, tipo "rota 100 = 15.000, rota 101 = 10.000" — e embaixo o último carregamento dela.

**Igor** (18:15) — Anotado. De cara, a prioridade vai ser bater as mudanças que você já fez, pra ficar tudo compatível e igual. Depois que isso estiver feito, a gente parte pras melhorias novas (filtro, último carregamento, média da rota).

**Maria** (18:33) — Combinado. Qualquer coisa, desenha um esboço antes de jogar no programa, aí a gente conversa certinho antes.

**Igor** (18:50) — Concordo, é bom fazer um protótipo pra garantir que estamos falando a mesma coisa.

*(Léo entra na conversa)*

**Maria** (19:40) — Outra coisa: dá pra deixar os números sempre visíveis no gráfico, sem precisar passar o mouse em cima? A ideia é deixar isso numa TV — quem vier de fora não vai saber que precisa passar o mouse.

**Léo** (20:07) — Ah, é, tem que colocar mesmo, isso hoje não aparece.

**Maria** (20:36) — Da minha parte acho que é isso. Deve ter mais coisa que o Porteiro falou, mas não lembro agora — vamos começar por esses pontos e ir desenvolvendo se precisar de mais.

**Maria** (20:53) — Esse painel é mais operacional, pro pessoal de carregamento visualizar o que dá e o que não dá pra carregar. Não é tanto sobre tempo de entrega — isso já foge do escopo do CD.

**Maria** (21:36) — Vou colocar na minha agenda pra entrar e atualizar as rotas, provavelmente ainda hoje. Quando vocês tiverem algo pronto, a gente marca e conversa de novo.

**Igor** (21:56) — Fechado, combinado, valeu.

---
*Transcrição encerrada em 22:05.*
