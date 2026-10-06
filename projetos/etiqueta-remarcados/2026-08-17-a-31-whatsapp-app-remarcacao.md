# App de remarcação de preço (coletor) — conversas WhatsApp Igor ↔ Donato, 17 a 31/08/2026

> Interpretado a partir de `chat.md` (exportação de WhatsApp, extraída pelo Ozéias em 04/09 a pedido do Igor — ver [`dailies/2026-09-08-digest-retaguarda.md`](../dailies/2026-09-08-digest-retaguarda.md)). O interlocutor não se identifica no texto, mas o conteúdo (builds do `app-remarcacao-preco`, firmware de impressora, coletor) bate exatamente com o que as dailies atribuem ao **Donato** — mesma pessoa citada em [`contexto.md`](contexto.md) como quem está "numa força-tarefa com o Ozéias no app de chão de loja". Não é reunião nem call — é o canal de trabalho diário entre os dois enquanto o app evoluía em ciclos de build→teste→fix, quase todo dia útil do período. Tom bem informal (mensagens picadas, "gato"/"mano"/"bb") — resumido aqui por tema, não por mensagem.

## Achado principal: isto já é o mesmo módulo do #12428/#12506

Em 24/08 o Donato mandou a URL de homolog **`portal-retaguarda-hml.avenida.com.br/etiqueta-remarcados/pendencias`** dizendo "aqui estão as telas para conferência, seu user já tem o grupo pra acessar". É a mesma rota do módulo de BI/Configurações do épico **#12428**, cujo card autoritativo é o **#12506** (já Verified). Isso **responde a pergunta que estava em aberto desde 28/08 no `contexto.md`** ("é a mesma frente do #12428 ou trabalho paralelo?") — pelo menos o lado de conferência/portal é a mesma tela. O que ainda não dá pra confirmar só com esta conversa: se o **app do coletor** em si (`app-remarcacao-preco`) é considerado dentro do escopo do #12428 ou é uma frente separada que só *alimenta* a mesma tela — a conversa é 100% sobre o app, nunca menciona o número do épico/card.

## Contexto técnico do app

App Android/Flutter que roda em coletores de loja (modelo "novo mestre", Android 13), usado pra bipar item, imprimir etiqueta de remarcação numa impressora térmica conectada por **Bluetooth**, com leitura de **RFID** na bobina de etiquetas. Builds trocados quase diariamente como APK direto pelo WhatsApp, sempre "homolog", nunca produção nessa janela.

## 1. Firmware da impressora (17–18/08)

- App/coletor esperava firmware baseado na versão 5.26; a impressora real já estava na 5.31 → incompatibilidade causava timeout mesmo forçando um valor mais alto (5.100).
- Causa: o patch de gravação de firmware era feito por uma lib nativa do Flutter, que **bloqueava** a gravação. Corrigido trocando pra um patch em código dentro do próprio app (não nativo) — passou a permitir gravar.
- **Resultado:** firmware atualizado com sucesso via app (18/08, confirmado por Igor "Acho que tá atualizando essa bomba" → funcionou).

## 2. Tamanho de etiqueta (17/08 e 19/08)

- Grande: 3 cm (A) × 5 cm (L). Pequena: 1,5 cm (A) × 5 cm (L).
- Igor sugeriu deixar configurável ("Mudar tipo de etiqueta: Grande/Pequena") em vez de fixo, oferecendo puxar a opinião do Bruno.
- **Decisão aplicada (19/08):** pequena como **default pra produção**, com **seletor disponível em homologação**.
- **Pendência não fechada:** Igor disse "vamos manter por hora" mas **não tinha repassado a decisão pro Bruno ainda** (21/08) e pediu pro Donato repassar com ele depois. Não há confirmação posterior na conversa de que isso foi feito.

## 3. Acúmulo de quantidade via múltiplos bipes (pedido do Igor, 17/08)

Especificação completa dada pelo Igor, não confirmada como implementada dentro da janela desta conversa:

- Hoje: bipar 1 item → espera 3s → imprime automaticamente com quantidade 1.
- **Novo comportamento pedido:**
  - 1º bipe do item: inicia contagem em 1, mantém os 3s antes da impressão automática.
  - Bipar o **mesmo** código de barras de novo dentro da janela: cancela/adia a impressão automática e incrementa (2, 3, 4...) — equivalente a apertar o "+" manual, só que via leitor.
  - Ao parar de bipar, o usuário imprime a quantidade total acumulada.
  - Bipar um código **diferente** no meio da sequência: não soma à contagem, exibe mensagem avisando que é item diferente do que está em acumulação.
  - Exemplo dado: 8 bipes do mesmo produto → acumula 8 → imprime 8 etiquetas.

## 4. Popup do Android sobrepondo a tela ("acesso à área de transferência") (20/08)

- Mensagem preta aparecendo por cima da tela a cada bipe — identificada como aviso **nativo do Android** (clipboard access), não algo que o app controla diretamente.
- Workaround encontrado por ambos em paralelo: `Configurações do coletor → Privacidade → Desativar "Mostrar acesso à área de transferência"` — Igor testou manualmente e confirmou que resolve.
- Como não dá pra desativar isso programaticamente pelo app, o Donato subiu builds sucessivos com **avisos on-boot** lembrando o usuário de desativar o parâmetro no aparelho (`...aviso-clipboard...`, `...aviso-desligar...`, `...aviso-desligar2...`) — não existe forma de o app **verificar** se a opção já está desativada (confirmado 20/08, "não senhor").
- **Risco operacional:** essa configuração é por aparelho, manual, sem checagem automática — em rollout pra múltiplas lojas isso pode ficar inconsistente coletor a coletor sem alguém validar um por um.

## 5. Dados somem após reinstalar o app (31/08)

- Reinstalar o APK apaga dados persistidos localmente; como a "janela" de sincronização era de 21 dias, o app pareceu "vazio"/sem dado recente até resincronizar. Causa raiz coincidiu com a API do backend também ter caído momentaneamente no mesmo dia.
- Não é bug do app em si, mas um comportamento que confunde quem estiver testando/trocando de APK com frequência — vale documentar isso pra quem for validar em campo.

## 6. Velocidade de impressão (31/08)

- Igor reportou lentidão ao imprimir várias etiquetas em sequência (pedido formal em 21/08, ver lista abaixo).
- Causa raiz encontrada pelo Donato: passos desnecessários na negociação **Bluetooth** com a impressora que eram simplesmente ignorados no final, mais o cálculo do bitmap da etiqueta sendo repassado pra impressora fazer contas por conta própria.
- Fix: removidos os passos ignorados. **Confirmado por Igor como "genuinamente mais rápido"** depois do teste.
- Bug colateral relacionado (11:38, 31/08): tela pula direto a etapa de bipagem do SKU e vai pra tela de impressão — suspeita de ser o teclado abrindo/fechando sozinho introduzindo delay. Igor não conseguiu reproduzir de propósito depois, mas "parece legal agora".

## 7. Lista de bugs/melhorias formalizada pelo Igor (21/08)

1. **Justificativa editável depois de colocada pra imprimir** — precisa ficar oculta/travada, não deixar mexer depois de setada.
2. **Conferência fora do coletor** — perguntou onde dá pra conferir isso fora do aparelho. Resposta do Donato: **pelo Portal Retaguarda** (ver "Achado principal" acima — é a mesma tela do #12506).
3. **Impressão lenta em sequência** — endereçado e confirmado corrigido em 31/08 (ver item 6 acima).
4. **Editar quantidade clicando no número** — pedido pra manter os botões "+"/"−" mas também permitir clicar direto no número pra editar o valor.

Donato respondeu que aplicaria "na segunda" (a lista é de sexta 21/08) — não há confirmação later na conversa de que os itens 1 e 4 foram de fato entregues (só o item 3, impressão lenta, tem confirmação explícita em 31/08).

## 8. Bug de justificativa "fantasma" ao reduzir quantidade (31/08)

Relato do Igor: bipa um item → aumenta manualmente a quantidade acima do limite do lote (aparece campo de justificativa) → sem preencher nada, reduz a quantidade de volta pra uma faixa aceitável → clica em IMPRIMIR → **o campo de justificativa aparece de novo mesmo assim**. Donato reconheceu como comportamento "meio bugado", pediu mais casos se o Igor encontrar. **Sem confirmação de correção na janela desta conversa.**

## 9. Erro 20 / suspeita de RFID vs. Bluetooth (31/08, última mensagem)

Erro ao imprimir lote de 60 etiquetas. Como o app fala diretamente com o firmware da impressora, a hipótese é falta do RFID na bobina de etiquetas. Donato propôs testar "burlar" a checagem de RFID, com um plano de diagnóstico explícito:

- Rodar o lote de 60 duas vezes.
- **Sempre trava no mesmo número aproximado** → confirma que é contador/RFID.
- **Trava em etiqueta aleatória** → suspeita volta pro BLE, e nesse caso reverte o "link rápido" (uma linha só, sem perder as outras otimizações de velocidade do item 6).

**Esta é a pendência mais recente e, pelo teor, a mais arriscada tecnicamente — a conversa termina aqui sem resolução.**

## Pendências que esta conversa deixa (nenhuma tinha card formal até 10/09)

1. Confirmar se o app do coletor entra no escopo do épico #12428 ou é frente separada que alimenta a mesma tela do portal.
2. Fechar com o Bruno a decisão de tamanho de etiqueta (pequena default / grande via seletor) — Igor nunca confirmou ter repassado.
3. Confirmar status de implementação da funcionalidade de acúmulo de quantidade via múltiplos bipes (item 3) — pedida, sem confirmação de entrega na conversa.
4. Justificativa editável depois de setada pra impressão (item 7.1) — sem confirmação de correção.
5. Edição de quantidade clicando no número (item 7.4) — sem confirmação de correção.
6. Bug da justificativa reaparecendo ao reduzir quantidade abaixo do limite (item 8) — sem confirmação de correção.
7. **Erro 20 (RFID vs. BLE) no lote de 60 etiquetas** — diagnóstico em aberto, sem dono de próximo passo definido além do próprio Donato.
8. Risco de rollout: dependência de configuração manual por aparelho (desativar aviso de clipboard) sem forma de o app verificar/forçar isso — pensar em processo de setup de coletor novo antes de escalar pra mais lojas.

Nenhum destes tinha card formal em Azure DevOps até 10/09/2026 — é exatamente o material que a pendência "Criar card(s) pro app de remarcação do Donato" (`minhas-pendencias.md`) estava esperando o Igor revisar.
