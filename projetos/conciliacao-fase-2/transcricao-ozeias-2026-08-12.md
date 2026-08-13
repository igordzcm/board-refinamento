# Transcrição — Conciliação Fase 2, apresentação pro Ozéias

> Fonte: `Conciliação Fase 2 - Apresentação.docx` (gravação/transcrição automática de reunião), extraída em 13/08/2026. Presentes: Diego Oliveira Andrade Rafael (dev, conduziu a demo), Ozéias Denis de A. Tavares, Leonardo Henrique da Silva, Kauã Miguel da Cunha, Igor Diniz Camargo (breve participação). 12/08/2026, 18:32–18:56 (24m24s). Transcrição automática — nomes/trechos podem ter ruído de reconhecimento de voz (marcados onde relevante).

Conciliação Fase 2 - Apresentação-20260812_153240-Meeting Recording
August 12, 2026, 6:32PM
24m 24s
Leonardo Henrique da Silva started transcription

**Diego** 0:10 — Bom, conseguem ver a tela?
**Ozéias** 0:13 — That.So.
**Leonardo** 0:16 — Teacher.
**Ozéias** 0:17 — Pegando, agora sim.
**Diego** 0:20 — Boa, vamos lá. [...] acho que o Ozéias não pegou muito o desenrolar dessas últimas semanas, então mostra rapidinho como ficou as telas.
**Ozéias** 0:38 — Pode me mostrar como se eu não soubesse de nada, tá?
**Diego** 0:42 — Tá, basicamente foram 4 novas telas e o fluxo vai partir do gerenciar perdas. [...] Aqui teve uma pequena mudança, que foi a adição dessa nova coluna, status RH, que vai persistir toda a interação que o analista do RH vai estar fazendo sobre os descontos em folha. [...] na tela do menu lateral a gente tem um novo grupo chamado RH, e dentro desse grupo temos recursos humanos e 2 telas novas: aprovação de vales e e-mails de setores. Aprovação de vales é onde vai cair de fato todas as divergências que o gerente do financeiro clicou em aprovar [...] fila de aprovação ou reprovação do RH. [...] E na outra tela, e-mails de setores, é gerenciado pelo RH, onde ele vai cadastrar os e-mails de quem vai receber as planilhas pelo cron job [...] a gente tem o setor dessa pessoa e o tipo do envio [...] planilha de perdas, planilha de rankings e e-mail RH [...] Voltando na parte administrativa do conciliação, a gente tem essa nova tela também, dashboard, que seria um resumo de tudo que está acontecendo com as divergências [...] histórico de envios, seria os casos que o cron job disparou os e-mails [...] ele se fecha no dia 25 do 8, e é quando o cron job pega todos os descontos de folha e perdas, gera os exports e dispara o e-mail.
**Ozéias** 4:40 — Uhum, pega uma conciliação lá, manda ela pra divergência, coloca ela como perda.
**Diego** 4:41 — Na própria conciliação mesmo, do zero, entendi.
**Ozéias** 4:50 — Marca desconto em folha, isso [...] está cortando muito minha voz.
**Igor** 5:00 — Tá tranquilo.
**Diego** 5:00 — [demo ao vivo] Aqui pode abrir qualquer uma, nesse caso aqui.
**Diego** 5:28 — Então a gente pegou a loja 1 do dia 15/04/2025. É marcar então um desconto em folha [...] a gente salva.
**Ozéias** 5:50 — Zero reais pra desconto em folha, não é?
**Diego** 5:52 — Nem me atentei nisso, pera aí que eu vou pegar então.
**Ozéias** 5:56 — Bota um 69 ali, 169.
**Diego** 5:59 — Melhor não dar um número negativo, né, também não é muito legal esse caso negativo.
**Ozéias** 6:06 — É negativo, se o cara tá devendo, vai pra desconto em folha.
**Diego** 6:10 — Cert[o].
**Ozéias** 6:11 — Tá certo.
**Diego** 6:13 — [...] recapitulando, na tela do RH a gente não tem nenhum em aguardando. E quando eu vim aqui no gerenciar perdas e aprovar esse caso, ele já persistiu como aguardando e quando voltar pra aprovação de vales...
**Ozéias** 7:06 — O aprovar em massa ainda existe, né?
**Diego** 7:08 — [...] tá aqui, caiu, a gente tem todas, né?
**Ozéias** 7:15 — Me volta lá rapidinho no [gerenciar perdas] pra ver o que vocês mudaram na tela.
**Diego** 7:20 — Gerencia perdas.
**Ozéias** 7:21 — Isso.
**Diego** 7:22 — [...] as ações, então a gente tem o botão de aprovar, reprovar e o histórico [...] agora, quando a gente aprovou um desconto em folha, a gente pode reverter essa ação. E também a gente tem um histórico dessa divergência.
**Ozéias** 7:45 — Mas a gente consegue reverter a qualquer momento ou só enquanto o status RH está aguardando?
**Diego** 7:45 — A gente pode reverter a qualquer momento.
**Ozéias** 7:53 — Mas aí, acho que a gente tem um gap, não?
**Diego** 7:56 — Aqui eu me lembro da regra de negócio que o Wagner passou, era isso.
**Ozéias** 8:01 — Porque pensa comigo: se essa [divergência] vai pra lá, eles baixam. Por exemplo, já está como aprovado no RH. Como que eles vão [reverter]?
**Diego** 8:12 — Ele pode fazer isso a qualquer momento, mas se tiver dentro do ciclo aberto, corrige no próprio ciclo. Mas se fechou o ciclo e iniciou outro, aí essa reversão vira um crédito pro próximo ciclo. É como se fosse um cartão de crédito, entendeu? Foi da forma que o Wagner tinha explicado pra mim.
**Ozéias** 8:49 — E aquele "reverter" é pra reverter a reversão, é isso?
**Diego** 8:53 — Esse reverter é pra reverter a aprovação.
**Ozéias** 8:56 — Não, tem um outro reverter ali agora — tem o aprovar, cancelar e reverter. Ah, tá.
**Diego** 9:03 — É só uma opção aqui.
**Ozéias** 9:03 — Achei que era pra reverter a reversão.
**Diego** 9:07 — Não. Aí o histórico persiste, né? Teve a decisão do gerente, a reversão, na aprovação de vales, a gente [...] tem esse caso aqui que ainda tá com a Rosineide aqui como aguardando, eu acho que deveria ter revertido aqui, mas...
**Ozéias** 9:31 — Oh.
**Diego** 9:32 — Aqui é uma dúvida agora, se era pra ter revertido ou não, se era pra ter saído daqui ou não. É nesse caso aqui que nem a gente estava no gerenciar perdas — a gente tinha aprovado, aí caiu pra fila dos vales...
**Diego** 9:50 — ...que seria isso aqui, que está aqui aguardando. Porém, o RH não interagiu em nada, nem aprovou nem reprovou. Só que aqui no gerenciar perdas, o próprio gerente do Financeiro reverteu a ação que ele acabou de aprovar.
**Diego** 10:07 — Aí a dúvida que ficou é: aqui deveria ter sumido, ou tá certo dele continuar aqui?
**Kauã** 10:07 — Boa pergunta, agora você vê, ficou de calças arriadas, Bernardo.
**Diego** 10:23 — É um caso que a gente pode ver com...
**Leonardo** 10:23 — Eu acho que ele some. Eu acho que ele some, tá? Mas a gente pode revisar depois. A gente pode até marcar uma reunião com o Wagner pra verificar essas coisas aí.
**Diego** 10:32 — Sim, sim, seria bom confirmar isso com ele.
**Diego** 10:37 — [...] vamos testar com esse aqui só pra ver o fluxo de cair lá pra aprovação dos vales [...] Aqui na aprovação dos vales, o aguardando agora tem 2. O RH tem a opção de aprovar, ele pode passar o número de parcelas, de 1 a 10 [...]
**Kauã** 11:33 — Você colocou como zero lá, ele foi...
**Diego** 11:36 — É, eu aprovei e foi.
**Kauã** 11:38 — Mas colocou as parcelas em zero, perdão, tava...
**Diego** 11:41 — Tava em um.
**Kauã** 11:43 — A outra tela deu um erro que eu me...
**Diego** 11:50 — Pior que eu passei batido, acho que troquei a lateral, não percebi.
**Kauã** 11:54 — Não, era o parcelamento em zero, tipo quando você coloca o valor em zero, tá ligado?
**Diego** 11:58 — Ah, entendi. Vou pegar outro caso, então [...] Vamos fazer do zero de novo [...] loja 2 no dia 15/04, salvar [...] desconto em folha [...] vamos aprovar [...] passa o número de parcelas [...] mas acho que ele está dando erro porque está com número negativo. Vamos confirmar pra ver o que vai dar. É "installment amount must be positive". É isso aí mesmo, tem que ser positivo.
**Ozéias** 13:35 — Como assim?
**Diego** 13:38 — Porque o número está negativo — a gente está passando uma parcela de número negativo, aí ele cai numa regrinha de que é número negativo.
**Kauã** 13:51 — Estamos com gap nessa lógica então — tem que aprovar ali e colocar um valor positivo.
**Diego** 13:53 — Yeah.
**Ozéias** 13:53 — Em tese.
**Diego** 14:05 — A soma também não bate, porque vai fazer a validação da soma das duas parcelas, tem que bater com o total do valor do desconto em folha.
**Diego** 15:02 — [...] a gente tem aqui esses casos de desconto em folha com valor positivo [...]
**Ozéias** 15:09 — Mas tem que ter desconto em folha com valor positivo?
**Diego** 15:17 — Isso eu já não sei te dizer, porque essa parte vem da conciliação da fase 1, então eu não teria muito o fluxo de como.
**Ozéias** 15:26 — Não, tipo assim, em tese acho que a gente não tem nenhuma trava lá, mas não acho que seja algo que aconteça.
**Kauã** 15:34 — Não deveria ter nenhum desconto em folha com valor positivo. Faz sentido, acho que faz sentido.
**Ozéias** 15:37 — Eu acredito que não [...]
**Kauã** 15:44 — Se tem sobra, não tem porque descontar da pessoa se sobrou alguma coisa.
**Ozéias** 15:46 — Exatamente [...] a gente precisaria colocar um bloqueio aí, não sei se faz sentido colocar ela agora, mas é algo que a gente tem que se preocupar, imagino eu, tá Diego?
**Ozéias** 16:39 — Porque, em tese, como é que eu vou descontar um valor positivo? Eu vou debitar um valor no cara?
**Diego** 16:45 — Entendi, só faz sentido se já nascer negativo lá da conciliação.
**Ozéias** 16:48 — Exatamente.
**Diego** 16:54 — Isso dá pra arrumar, é só aceitar valor negativo na hora do aprovar.
**Ozéias** 17:02 — Sim [...] pelo que eu me lembre do que o Wagner explicou, é isso.
**Ozéias** 17:11 — Aí o cron job roda todo final de mês, é isso?
**Diego** 17:15 — É no fechamento do ciclo [...]
**Ozéias** 17:17 — É o final do ciclo, que é 25 a 24 [...]
**Ozéias** 17:36 — Vamos pegar isso daí, vamos levar — a Mídia [nome capturado pela transcrição automática, possível ruído] tá viajando, eu vou dar um toque nela pra ver como ela prefere fazer. A gente apresenta primeiro pra ela e pra Adriana.
**Ozéias** 17:49 — Beleza, Léo — a gente apresenta essa primeira versão pra elas, vê o que elas falam, e aí, elas aprovando, a gente libera isso pro pessoal de RH.
**Diego** 18:01 — [...] é um cron que roda às 23h no último dia do ciclo.
**Ozéias** 18:09 — Okay, que ele faz?
**Diego** 18:09 — Aí ele gera o snapshot com o arquivo XLSX do relatório de Perdas.
**Ozéias** 18:22 — Vamos lá, eu vou questionar algumas dúvidas: elas têm até o dia 30 pra deixar ajustado, até o dia 25, pra iniciar o fechamento financeiro fiscal. Então como que elas conciliariam o dia 25, por exemplo, já que foi conciliado no dia seguinte e a gente fechou o ciclo no dia 23, às 23h?
**Diego** 18:52 — Essas 23h ele só roda no último dia do ciclo, no caso.
**Ozéias** 19:03 — Estamos no último dia do ciclo, que é dia 24, certo?
**Diego** 19:06 — [confirma]
**Ozéias** 19:07 — Ele pega tudo do dia 25 do mês [anterior] até dia 24 do mês atual e roda o cron, certo?
**Diego** 19:14 — Certo.
**Ozéias** 19:16 — Minha dúvida é: se ela só concilia no dia 24 [ou] no dia 25, vai estar incompleto.
**Diego** 19:25 — [...] essas 23h ele vai rodar, né?
**Ozéias** 19:31 — Eu não estou falando que vocês fizeram errado, tá? É que eu acredito que a regra em si já está falha.
**Kauã** 19:38 — Mas jogar pra frente não teria um problema, seria?
**Diego** 19:42 — Não, se ela for conciliar...
**Ozéias** 19:43 — Eu acho que o certo seria ter elas falarem quando tiver fechado o ciclo, quando elas tiverem finalizado — a gente criar um botãozinho tipo "finalizado", e aí se essa flag tiver fechada [dispara o cron].
**Ozéias** 20:10 — [...] pensando em questão de... não faz sentido, o João vai estar desatualizado. O canal das 8 da manhã eu vi o e-mail. Esse cron é o quê? Ele vai o quê?
**Diego** 20:33 — Esse aqui só fecha o período e gera o arquivo. Aí o das 8h do primeiro dia do mês faz o disparo dos e-mails. Isso pro fluxo de perda.
**Ozéias** 20:52 — Sim, acho que faz sentido. Entendi um pouquinho melhor. Como que seria essa parte, tá, Léo?
**Diego** 21:02 — Esse aqui é do de perda, tá? O desconto em folha já é outro fluxo.
**Diego** 21:11 — Ele exporta a planilha de desconto em folha na hora mesmo, e já está tudo compilado, com as movimentações que aprovou.
**Ozéias** 21:30 — Sim, vamos — acho que vale a gente reconfirmar com as meninas mesmo. Acho que não tem problema, é mais um ponto de atenção que a gente tem que confirmar. Mas beleza, fechou.
**Ozéias** 21:43 — É Léo, vamos — acho que eu não tenho mais o que comentar [...] Vamos marcar um dia aí, vou mandar mensagem pra Mídia pra ver se a gente consegue apresentar pra elas na sexta. Uma primeira apresentação só pra mostrar como está ficando, não uma entrega final, pra gente poder pegar o feedback delas — isso aqui falou, isso aqui não — a gente reajusta o que vai reajustar, libera pra elas testarem. E semana que vem a gente faz uma última reunião envolvendo o RH e as outras áreas, tá bom?
**Leonardo** 22:23 — Está bom — mas abre já pro Gustavo amanhã, que a gente já sobe desabilitado.
**Ozéias** 22:28 — Não podemos subir, não podemos [subir] até ter o approve delas.
**Ozéias** 22:35 — Infelizmente.
**Ozéias** 22:40 — Quando a gente finaliza, vou ter que gerar um documento de aceite. Elas vão ter que fazer o documento de aceite, mandar e-mail aprovando, tirar prints de teste — então já peço: se puder falar com o Danilo, já ir salvando e guardando print de teste de validação, de tudo.
**Leonardo** 23:03 — Tá bom, mas deixa eu deixar claro pra você e pro Higuinho: nosso cronograma de desenvolvimento foi 2 semanas, e a gente terminou.
**Ozéias** 23:12 — Perfeito. Sim.
**Leonardo** 23:20 — Se alguém perguntar, Diego — Spin, está finalizado — vou falar a mesma coisa pro Spin e pra quem mais perguntar.
**Ozéias** 23:23 — Perfeito. O que o Diego já tá ciente, a área também já tá ciente. Por isso a gente tem que fazer essa primeira agenda pra mostrar pras meninas, validar as regras, e abrir o processo de homologação.
**Leonardo** 23:30 — Então é isso, a gente terminou. [...] Esse processo tá à parte, tá? Eu falei 2 semanas de desenvolvimento.
**Ozéias** 23:52 — E a gente tem que botar em produção até o final do mês, resumidamente.
**Leonardo** 23:56 — Vou marcar uma reunião com o Wagner amanhã só pra mostrar pra ele e perguntar esses pontos que vocês mapearam. E aí a gente já vê se vai vir alguma coisa pra ajustar, e já ajusta.
**Ozéias** 24:04 — Fechou, beleza — combinado que a gente tem até sexta pra ajustar esses pontos.
**Ozéias** 24:14 — [...] Léo, e o Guilherme?
**Leonardo** 24:16 — Tem uma reunião agora, mas tô 4 minutinhos.
**Diego** 24:17 — Bye, galera.
**Ozéias** 24:18 — Eu também, falou.
Leonardo Henrique da Silva stopped transcription
