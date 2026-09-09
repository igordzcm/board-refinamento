# Minhas pendências (Igor)

> Reuniões a marcar, devolutivas que eu devo pra alguém, e coisas combinadas que alguém vai me entregar. Só isso — não é status de projeto (isso fica nos `contexto.md`). Atualizado sempre que surgir um combinado novo em daily/reunião/conversa. Consultar diariamente; ao resolver um item, apague a linha (ou mova pra "Resolvidos recentemente" se quiser manter rastro por um tempo).

## ✅ Checklist fixo (rotina)

> Recorrente — desmarque/remarque a cada dia, não risque de vez.

**Todo dia:**
- [ ] Checar o board (Azure DevOps + board de refinamento)
- [ ] Verificar cards e refinar o que for necessário
- [ ] Baixar transcrições do dia anterior

**Toda segunda-feira:**
- [ ] Avaliar o Danilo no Verzel RH
- [ ] Atualizar o dashboard executivo
- [ ] Verificar quantidade de horas da equipe

## 🗓️ Reuniões a marcar

- [x] **Call com Arthur** — realizada **02/09**. Bug de propagação confirmado corrigido; levantou pedidos de usabilidade + 1 dúvida técnica (SKU). Ata em [motor-descontos/2026-09-02-call-arthur.md](motor-descontos/2026-09-02-call-arthur.md), resumo executivo em [motor-descontos/2026-09-02-call-arthur-resumo-executivo.md](motor-descontos/2026-09-02-call-arthur-resumo-executivo.md).
- [x] **Reunião com Ana Carina e Marcos** — confirmada pra **quarta-feira, 02/09, 17h–18h**, sobre testes de Gamificação. Combinada na review/retro de 01/09 — Igor vai encaminhar o invite. Ver [reviews-retros-planning/2026-09-01-review-retro-retaguarda.md](reviews-retros-planning/2026-09-01-review-retro-retaguarda.md).
- [ ] **Alinhar com Sergio da Silva** — destrava o refino do card #12512 (Dashboard CDs, relatório WMS com nova data). Ver [dashboard-cds/contexto.md](dashboard-cds/contexto.md).
- [ ] **Reunião com o Ozéias** — decidir se vale validar/bloquear valor positivo direto na tela de conciliação de caixa (origem), em vez de só no aprovar do RH. Sugestão do Wagner, 13/08. Ver [conciliacao-fase-2/contexto.md](conciliacao-fase-2/contexto.md).
- [ ] **Próxima interação com o Wagner** — esclarecer a ambiguidade da fila do RH pós-reversão (não veio à pauta da reunião de 13/08). Dono provável: Leonardo.
- [ ] **Esclarecer "Arco" vs. planilha Oracle com Diego/Ozéias** — pro card #12812 (Conciliação Fase 2, planilha do Contábil). Diego citou "integração diretamente no Arco" numa daily (28/08); preciso saber se é o mesmo destino do card ou mudança de abordagem antes de reescrever.
- [x] **Reunião com o Fabio sobre Motor de Descontos** — marcada pra **terça-feira, 08/09, 15h**. Pauta: se corrigir o lado do VAR pra campanhas de departamento já está no planejamento; viabilidade de um cancelamento real de campanha (futura e ativa); viabilidade de editar lojas de uma campanha global ativa (puxar o Kauã junto). Ver [motor-descontos/2026-09-02-call-arthur.md](motor-descontos/2026-09-02-call-arthur.md).

## 📄 Material recebido, pra revisar

- [ ] **Ler o TAP + Especificação Funcional da "Ferramenta Pesquisas Colaboradores"** (recebidos, arquivados em [pesquisas-colaboradores/](pesquisas-colaboradores/) em 01/09, ainda não lidos). Pelo nome dos arquivos, parece ser um projeto novo (ferramenta de pesquisa com colaboradores) — **não confirmado se é a mesma TAP que o Spin tinha enviado sobre o Ciacon** ou um assunto totalmente separado. Confirmar ao ler.
- [ ] **Usar a transcrição da reunião de Gamificação** — ainda não processada/digerida.

## 🛠️ A fazer

- [ ] **Criar card(s) pro app de remarcação do Donato — ainda sem task/card formal.** Pedido repetido nas dailies de 01/09 e 03/09 e reforçado na planning de 02/09 (documentar o trabalho de melhorias que ele vem fazendo: firmware, velocidade de impressão, delay de telas). **08/09:** Igor conseguiu falar com o Ozéias na sexta (04/09), que extraiu do WhatsApp toda a conversa que tiveram sobre remarcação — Igor vai revisar esse conteúdo pra poder criar o(s) card(s); Donato "segue sem pendência formal", "tá tranquilo" enquanto espera. Ver [dailies/2026-09-01-e-03-digest-retaguarda.md](dailies/2026-09-01-e-03-digest-retaguarda.md), [reviews-retros-planning/2026-09-02-planning-retaguarda.md](reviews-retros-planning/2026-09-02-planning-retaguarda.md) e [dailies/2026-09-08-digest-retaguarda.md](dailies/2026-09-08-digest-retaguarda.md). Cruza com [etiqueta-remarcados/contexto.md](etiqueta-remarcados/contexto.md) — ainda em aberto se é a mesma frente do épico #12428 ou trabalho paralelo.
- [x] **Criar tarefa(s) do Kovalski para o Ciacon.** Criados 27/08: [#12813](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12813) (documentação) e [#12814](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12814) (implementação). **Atualização 28/08:** integração fechada, PR já aberto pro Spin — #12814 avançou pra Dev Review.
- [ ] **Cobrar Kovalski pra formalizar a documentação do Ciacon no ADO.** Ele diz que terminou (28/08), mas o #12813 segue com 0 comentários no Azure.
- [ ] **Definir apoio ao Kovalski pra assumir SigaPub/Siga.** Máquinas físicas chegam 31/08, viram responsabilidade direta da Retaguarda — ele já sinalizou que não dá conta sozinho.
- [ ] **Revisar cards em Homologação/Verified que precisam de reunião com alguma área.** Checado em 26/08: o épico Automação Planilha Fiscal (#11103) está inteiramente "Done", não "Verified" — a suposição inicial não bateu. Amostrei outros ~9 cards "Verified" (10562, 12001, 12430, 12431, 12506) sem achar um comentário do Danilo sugerindo especificamente "testar com a área" — precisa apontar os cards certos ou pedir pro Danilo indicar quais.
- [ ] **Endereçar "se tudo é urgente, nada é urgente"** — reclamação #1 do retro VAR 3.0 (28/08). Ver [reviews-retros-planning/2026-08-28-retro-var.md](reviews-retros-planning/2026-08-28-retro-var.md).
- [ ] **Enviar o resumo da review/retro de 01/09 pro Spin — prazo: amanhã, quarta-feira 02/09.** Inclui em especial o ponto da compressão de prazo da Conciliação Fase 2 (3 meses → 2 dias), que Igor sinalizou querer escalar. Resumo pronto em [reviews-retros-planning/2026-09-01-review-retro-retaguarda.md](reviews-retros-planning/2026-09-01-review-retro-retaguarda.md).
- [ ] **Decidir se o card de Motor de Descontos em "Verified" passa pra outra pessoa** — levantado na review de 01/09, sem decisão registrada ainda.
- [ ] **Checar sobreposição entre #12812 e #12892** (ambos sob o épico Conciliação Fase 2, ambos envolvendo layout/integração Oracle) antes de estimar os dois — #12892 foi movido pra Refinement e adicionado ao board em 01/09.
- [ ] **Criar os cards de Motor de Descontos levantados na call de 02/09 com o Arthur** — pelo menos os 2 já prontos pra dev sem dependência (combo com 1 item; correção dos e-mails de notificação). Ver [motor-descontos/2026-09-02-call-arthur.md](motor-descontos/2026-09-02-call-arthur.md).
- [ ] **Criar tarefa pra atualizar a UI do Motor de Descontos com base na UI da Gamificação.** Ver [motor-descontos/contexto.md](motor-descontos/contexto.md) e [gamificacao/contexto.md](gamificacao/contexto.md).
- [ ] **Validar o card do JB de Migração Var Ret.** Ver [migracao-varret/contexto.md](migracao-varret/contexto.md).
- [x] **Formalizar a ata da call com o Fabio (08/09, Motor de Descontos).** Ata completa em [motor-descontos/2026-09-08-call-fabio.md](motor-descontos/2026-09-08-call-fabio.md). **Ainda falta:** atualizar [motor-descontos/contexto.md](motor-descontos/contexto.md) com as respostas.
- [ ] **Criar as tarefas de Motor de Descontos combinadas na call de 08/09 com o Fabio** — 3 funcionalidades já definidas e sem bloqueio técnico: botão de "Encerrar campanha" (usabilidade, back-end já existe); duplicar campanha pra lojas específicas (a partir de uma campanha global); reativar a criação de campanha por departamento (PRO013) no portal — depende de confirmar com Caixeta/QAs primeiro. Ver [motor-descontos/2026-09-08-call-fabio.md](motor-descontos/2026-09-08-call-fabio.md).
- [ ] **Registrar o resultado da call com Ozéias/Diego (08/09, Ferramenta Pesquisas Colaboradores)** — pauta em [pesquisas-colaboradores/2026-09-08-call-ozeias-diego.md](pesquisas-colaboradores/2026-09-08-call-ozeias-diego.md). Cobre: custos/prazo ainda "em levantamento", status da aprovação formal, se o dev compete com a fila da Retaguarda, integração com Senior/DW, LGPD, e confirmar se é a mesma TAP do "Ciacon" citado pelo Spin. Atualizar essa pendência e o item "Ler o TAP + Especificação Funcional..." acima depois da call.
- [ ] **Revisar o card #12892 (Fechamento Contábil) com a conversa com o Alex, do Contábil.**
- [x] **Criar card pro bug de "Perda" entrando na fila de Aprovação de Vales (Conciliação Fase 2).** Criado 09/09: [#12912](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12912), Diego, Sprint 28, Ready for Dev. **Ainda falta:** investigação técnica de fato — se é regressão do pacote que subiu na GMUD de 31/08. Ver [conciliacao-fase-2/contexto.md](conciliacao-fase-2/contexto.md).

## 📤 Devo pra alguém

- [ ] **Cards em "Bloqueado" da Conciliação Fase 2** — comentar e fechar assim que a Fase 2 confirmar que não são mais necessários (combinado com o Kauã em 13/08). Ver [conciliacao-fase-2/contexto.md](conciliacao-fase-2/contexto.md).
- [ ] **Seguir cobrando a Maria** pela planilha corrigida do Dashboard CDs (ela disse em 13/08 que ainda está esperando resposta de alguém da área dela).
- [ ] **Alinhar com o Leonardo** o que ele queria repassar pro Fernando sobre testes (combinado na daily de 13/08, ainda não feito).

## 📥 Aguardando de alguém

- [ ] **Maria** → planilha corrigida do Dashboard CDs (destrava o refino de #12509, #12510, #12511, #12513).
- [ ] **Leonardo** → baixar e enviar a gravação/transcrição de uma reunião que pedi em 13/08 (eu não tenho permissão pra baixar diretamente).
- [ ] **Ozéias** → revisão completa da lista de ~40 cards de backlog de Automação Fiscal (Kovalski) — prazo combinado: sexta 14/08. Ver [automacao-fiscal/contexto.md](automacao-fiscal/contexto.md).
- [ ] **Leonardo** → identificar o módulo/arquivo exato do bug de token (#12514, já atribuído a ele) antes de dar estimativa.
- [ ] **Ozéias** → investigar por que não consegue mais ver o Portal Gamificação em homolog (sinalizado 12/08, sem dono confirmado ainda). Ver [gamificacao/contexto.md](gamificacao/contexto.md).

## Resolvidos recentemente

- [x] **Diego** → resultado da reunião com o Wagner sobre Conciliação Fase 2 — aconteceu 13/08 (17:10, 42min). Bug de parcela negativa confirmado corrigido; item órfão na fila do RH não veio à pauta (virou pendência nova, ver "Reuniões a marcar"). Ata em [conciliacao-fase-2/reuniao-wagner-2026-08-13.md](conciliacao-fase-2/reuniao-wagner-2026-08-13.md).
