# Daily Retaguarda — 13/08/2026 (hoje)

> Resumo (não transcrição literal), convertido de `RETAGUARDA - Daily (2025)qq.docx` (raiz do workspace, movido pra cá). 9m24s.

**Participantes:** Igor (PO), Diego, Leonardo, Kauã, Fernando, Kovalski, JB, Danilo.

## Por pessoa

- **Diego** — Preparou branch pra merge da Conciliação Fase 2 ontem; depois teve a agenda com o **Ozéias** pra apresentar a tela da Fase 2 (ver [reuniao-ozeias-apresentacao-inicial.md](../conciliacao-fase-2/reuniao-ozeias-apresentacao-inicial.md)) — nessa agenda apareceram bugs não pegos nos testes dos dias anteriores. Já corrigiu e subiu pra homologação hoje de manhã, ainda testando, algumas coisas pendentes. **Reunião às 14h hoje com o Wagner** pra apresentar o fluxo e, se der, já testar as correções em HML com ele.
- **Kauã** — Reunião "GMou" de ontem não rolou. Trabalhando com o Diego nos testes pendentes — o ponto principal é permitir que o Danilo dispare o cron job pela UI/front (em vez de precisar ir direto pra Prod sem passar por DevBox), pra poder testar/quebrar com controle. Depois disso, provável retorno à Gamificação. Cards em "Bloqueado" que não serão mais aplicados: combinado com o Igor de deixar como estão por enquanto; quando a Conciliação Fase 2 confirmar que não são mais necessários, comentar e fechar.
- **Fernando** — Continuando correção de bug no card **#12505** (confirmado pelo Igor — a transcrição tinha derrubado o primeiro dígito). Quase terminando.
- **Igor** — Terminou de refinar um card hoje de manhã, deve passar pro Fernando em seguida. Combinou de alinhar com o Leonardo hoje o que ele queria repassar pro Fernando sobre testes. Maria (Dashboard CDs): respondeu hoje de manhã que ainda não mandou a planilha corrigida — está esperando alguém da área dela responder com informações; assim que tiver, ela envia.
- **Kovalski** — Seguindo com o Siga, meta de terminar amanhã (14/08). Sem impedimento além da própria máquina.
- **JB** — Seguindo Migração VarRet, respondendo rework do Danilo. Igor lembrou de um card que o Leonardo tinha pedido: **pegar o lote 1 e ajeitar os downloads pra enviar por e-mail via worker** — é exatamente o card **#12484**, já em Doing.
- **Danilo (QA)** — Analisou cards de QA; alguns de Migração VarRet estão em "QA Doing", bloqueados aguardando DASH (Dashboard CDs). Vai analisar mais. Aguardando o Kauã terminar antes de iniciar DevOps/testes dos cards de Conciliação. Confirmado com Diego/Kauã: **card #10562 não subiu pra prod ainda, segue em homologação.** Explica fluxo próprio: cards aprovados vão pra "Homologação DONE" pra não conflitar com o que já está em homologação; o que ainda não foi testado/aprovado fica em "Doing" (caso do Donato e do Kovalski). Alinhou shadowing mensal com o Gui da Verizon pra evoluir em teste.
- **Leonardo** — Thalison pediu documentação do motor de desconto e de RPA pra registrar no DW — entrou na fila. Seguindo na correção do bug de portal quando o usuário tem **muitos grupos** (mesma frente do "erro 400" mencionado em 12/08). Levantando mais débitos técnicos do portal. Precisa alinhar com o Igor hoje sobre as tasks/testes do Fernando.

## Pontos de atenção

- **Cards em Bloqueado que podem não ser mais necessários** — Igor vai comentar/fechar depois que a Conciliação Fase 2 confirmar. (Só documentado — nenhum card mexido sozinho.)
- **#10562** confirmado ainda em homologação (não subiu pra prod) — consistente com o motivo de já ter sido tirado do board de refinamento.
- **#12484** confirmado ativo — JB já trabalhando nele (Doing).
- **#12505** (Fernando) — confirmado pelo Igor, quase concluído.
- **Bug de token (permissionamento de rotas)** — virou card **#12514** (Refinement/Doing, 13/08), linkado ao épico #12387. Falta investigação técnica de onde exatamente é o fix.
