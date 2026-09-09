# Digest — Dailies Retaguarda, 01 e 03/09/2026

> Duas dailies do squad Retaguarda (não há transcrição de daily pra 02/09 — nesse dia o squad teve a [Sprint Planning](../reviews-retros-planning/2026-09-02-planning-retaguarda.md) em vez de standup). A daily de 01/09 aconteceu **antes** da Review+Retro do mesmo dia (ver [../reviews-retros-planning/2026-09-01-review-retro-retaguarda.md](../reviews-retros-planning/2026-09-01-review-retro-retaguarda.md)) — o próprio Igor comenta na daily "hoje a gente já tem a review e a reto". Fontes: `RETAGUARDA - Daily (2025)  (3).docx` (01/09, participantes: Igor, Kauã, Danilo, Diego, Filipe de Lacerda, JB, Fernando, Kovalski, Donato) e `RETAGUARDA - Daily (2025)  (4).docx` (03/09, curta — 3m30s —, participantes: Igor, Donato, Fernando, Kovalski, Sola).

## Deploy / GMUD (01/09)

- GMUD do dia anterior (31/08) passou bem, sem reclamação de cliente ("mídia chorando").
- 36 cards parados na coluna Deploy — Igor perguntou se pode empurrar tudo pro Donato revisar ou se o time prefere dar uma passada antes; Kauã: prefere dar uma vista por cima primeiro.
- Diego: preparou a branch da GMUD de Conciliação Fase 2, ajudou Fernando a preparar a dele, testou e subiu a autorização. Card #12800 (bug de tela) corrigido e subiu junto.

## Conciliação Fase 2 (01/09)

- Kauã confirmou correção do bug de "token muito grande" ainda não fechada definitivamente à noite — contorno aplicado: usuário com ADM no grupo passa a ter acesso irrestrito, sem precisar mais remover/trocar grupo manualmente.
- Danilo: manhã de 01/09 focada em revisar todas as tasks de Conciliação Fase 2 com o Diego pra validar o fluxo antes da GMUD — acharam gaps que já foram corrigidos na hora (é o mesmo card citado como "rework" na review/retro do mesmo dia).
- Igor perguntou a Kauã sobre os cards em rework/blocked de Conciliação Fase 2 — Kauã vai revisar se o que o Danilo apontou já está contemplado.

## Dashboard CDs (JB)

- 01/09: JB terminou o que tinha pra Dashboard CDs, mas não conseguiu falar com a Maria de novo — segue tentando. Um card em blocked (Ozéias já teria alinhado com o Léo, JB vai confirmar).
- Padrão se repete de dailies anteriores — ainda sem resposta da Maria.

## Portal / Infra (Kovalski)

- 01/09: subiu o portal de aprovações (pedido urgente do Spin) e refatorou um módulo que estava em Python; entregue, aguardando o pessoal usar pra validar a regra. Começou o deploy da máquina do Siga.
- 03/09: reclamou de estar uma semana inteira sem card formal (trabalhando direto pra prioridades do Spin); fechou o deploy do Siga + SigaPublic ontem (02/09). Segue precisando fazer engenharia reversa de "Campos" (sem acesso ainda). Resolveu um bug de grupos que impedia o Gaspar de acessar. LDAP muito lento (deveria sincronizar de 2 em 2 min, mas não está enviando). Vai começar o Ciacon, mas está atolado — **sinalizou que talvez comece a mexer em "Doc Pendentes" em breve** (ver nota abaixo, é o projeto VAR 3.0 [`engine-doc-pendentes-migrate`](../engine-doc-pendentes-migrate/contexto.md) — squad diferente do dele; confirmar se é engano ou se ele está mesmo entrando nessa frente).

## App de remarcação (Donato)

- 01/09: atualizações no firmware da impressora (resolvendo atraso na emissão de cupons), novo APK passado pro Ozéias, aguardando retorno. Sem task/card — Igor: vai criar um card mesmo que simplificado, só pra ter documentado.
- 03/09: seguiu com ajustes "mais cosméticos" (velocidade de impressão, delay de telas) — usando um firmware não-original da impressora que perde informação, tentando contornar isso.

## Portal — testes de front / pipeline (Fernando)

- 01/09: resolvendo conflitos de merge nos testes automatizados de front; ficou sem novo trabalho no fim do dia, Igor disse que ia procurar algo fácil pra ocupar o dia dele, já que a semana tinha review+retro (01/09) e planning (02/09) chegando.
- 03/09: seguiu em devbox com o Danilo, começou a trabalhar num novo card.

## Outras notas (01/09)

- Filipe de Lacerda: sem pontos a reportar (motor de desconto tem um item aguardando retorno).
- 03/09: Sola (presente na daily de Retaguarda dessa vez, não em daily separada) — "tudo certo", sem detalhes.

## Cruzamentos a verificar

- A menção do Kovalski (03/09) sobre "talvez eu comece a mexer na Doc pendentes" cruza com o projeto VAR 3.0 de Migrate/DocPay ([`engine-doc-pendentes-migrate/contexto.md`](../engine-doc-pendentes-migrate/contexto.md)) — vale confirmar se é isso mesmo ou se ele quis dizer outra coisa (o termo é ambíguo na transcrição).
