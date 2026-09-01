# Log da rotina diária (daily-digest + board-sync)

> Atualizado a cada execução da rotina automática (seg-sex, 8h). Entrada mais nova primeiro. Cada entrada documenta **o que rodou, o que mudou, por quê, e com base em qual fonte** — pra revisão rápida pela manhã sem precisar reconstruir o raciocínio.

---

## Formato de cada entrada (referência — apagar depois da primeira execução real)

```
## AAAA-MM-DD HH:MM (America/Sao_Paulo)

### daily-digest
- Transcrições novas encontradas: N (lista de arquivos)
- Já cobertas / puladas como duplicata: N (qual arquivo, qual digest já existente cobria)
- Digest(s) criado(s): [nome do arquivo](dailies/arquivo.md) — período/tema
- Achados principais, por projeto:
  - **<Projeto>**: <achado> — fonte: <trecho/data da transcrição>
- Arquivos sinalizados como desatualizados (NÃO editados por este agente):
  - `<arquivo>` — <o que especificamente parece defasado e por quê>

### board-sync
- Cards com estado/coluna mudados:
  | ID | De | Para | Motivo (fonte) |
  |---|---|---|---|
  | #NNNNN | Refinement (Quase pronto) | Refinement (Precisa refinar) | Comentário do Danilo em DD/MM: "<citação>" |
- Cards removidos do escopo do board (avançaram além de Ready for Dev):
  | ID | Estado atual | Motivo |
  |---|---|---|
- Cards novos descobertos (não rastreados antes):
  | ID | Score DoR (4 pontos) | Coluna onde entrou |
  |---|---|---|
- Checagem de paridade chip/modal: OK / FALHOU (detalhe se falhou)
- Artifact republicado: <URL> — <sim/não, e por quê se não>

### Pendências que ficaram para o Igor decidir
- <qualquer bloqueio externo real encontrado, não resolvido pelo agente>

### Erros/falhas nesta execução
- <qualquer chamada ADO que falhou, arquivo que não abriu, etc — nunca omitir silenciosamente>
```

---

*(entradas reais começam abaixo, mais recente no topo)*

---

## 2026-09-01 21:50 (execução manual, sob pedido do Igor — "atualize nosso dash de tarefas só com tarefas da sprint 28"; 6ª rodada do dia)

### board-refinamento.html — filtro de sprint, sem full sync
Confirmado a-a-a via `get_batch` que os 30 cards já rastreados no board tinham, todos, `IterationPath` = "Var Retaguarda\Sprint 28" (resultado das rodadas 4 e 5) — nenhum card precisou ser removido do board. Atualizado: breadcrumb (+ segmento "Sprint 28"), subtitle (nota explícita de filtro por sprint) e footer (parágrafo novo no topo explicando o filtro e o método de verificação). Nenhuma mudança de coluna/DoR/conteúdo dos cards.

**Não foi um board-sync completo** — não foram re-checados comentários novos, cards novos via WIQL, nem State/BoardColumn individual além do que já se sabia. Artifact republicado.

### Erros/falhas
Nenhum.

---

## 2026-09-01 21:43 (execução manual, sob pedido do Igor — mover todos os cards em "Refinement" pra Sprint 28; 5ª rodada do dia)

### Ação direta no ADO — `wit_work_item_write update_batch`
WIQL `System.State = 'Refinement'` no projeto Var Retaguarda retornou 20 cards; todos tiveram `System.IterationPath` alterado pra **"Var Retaguarda\Sprint 28"** — confirmado 20/20 com HTTP 200: #11813, #11818, #11840, #11935, #11938, #12115, #12178, #12182, #12284, #12403, #12437, #12509, #12510, #12511, #12512, #12513, #12514, #12793, #12812, #12813.

(#11935, #11938 e #12793 já tinham sido movidos na rodada anterior — reaplicado sem efeito colateral, idempotente.)

Nenhum outro campo alterado. Board (`board-refinamento.html`) não tocado.

### Erros/falhas nesta execução
Nenhum.

---

## 2026-09-01 21:41 (execução manual, sob pedido do Igor — mover 16 cards pra Sprint 28; 4ª rodada do dia)

### Ação direta no ADO — `wit_work_item_write update_batch`
`System.IterationPath` alterado pra **"Var Retaguarda\Sprint 28"** (02/09–15/09) em 16 work items — confirmado 16/16 com HTTP 200. Escopo pedido pelo Igor: os 9 cards de uma lista anterior (#11933, #11935, #11938, #11941, #12190, #12793, #11407, #12795, #12797) + todos os que estavam em estado "Ready for Dev" no projeto (#12273, #12400, #12401, #12405, #12889, #12890, #12892 — união, sem duplicar os que já apareciam nos dois grupos).

**Confirmação explícita do Igor** antes de executar: 4 dos 16 (#11407, #12793, #12795, #12797) tinham reprovado o checklist de DoR (0/4 ou quase) — perguntei se ainda assim deveriam entrar na sprint; ele confirmou que sim, mover os 16 mesmo assim.

**Achado incidental durante a checagem:** #12892 tinha sido movido de novo no Azure — **pelo Ozéias**, não por mim — de "Refinement" pra "Ready for Dev" às 20:47 (depois da minha alteração anterior desta sessão que tinha colocado em "Refinement"). Não revertido; é atividade real dele. O board (`board-refinamento.html`) ainda mostra #12892 em "Refinement/Quase pronto" — **desatualizado, precisa de um board-sync pra refletir Ready for Dev**.

### O que NÃO foi feito nesta rodada
- Board (`board-refinamento.html`) não foi tocado — só o `IterationPath` no Azure. Sprint não é um campo que o board rastreia hoje.
- Nenhum outro campo alterado (State, BoardColumn, Effort etc. permaneceram como estavam).

### Pendências que ficaram para o Igor decidir
- #11407, #12793, #12795, #12797 entraram na Sprint 28 sem refino — se alguém for trabalhar neles, o refino ainda precisa acontecer (nenhum dos 4 tem Cenário/AC utilizável hoje).
- Sincronizar o board pra refletir #12892 = Ready for Dev (Ozéias já moveu, board desatualizado).

### Erros/falhas nesta execução
Nenhum — todas as 16 escritas retornaram 200 na primeira tentativa.

---

## 2026-09-01 20:XX (execução manual, sob pedido do Igor — mover #12892 pra Refinement e adicionar no board; 3ª rodada do dia)

### Ação direta (não board-sync — feita manualmente nesta sessão, com escrita no ADO)
- **#12892** ("Fechamento Contábil da Conciliação e Integração de Perdas e Vales com Oracle"): estado alterado no Azure de **"To do" → "Refinement"** via `wit_work_item_write` (System.BoardColumn é read-only e seguiu automaticamente o State). Card adicionado ao `board-refinamento.html` em **"Quase pronto"** (3/4 pendências — formato Dado/Quando/Então, rótulo, estimativa; sem bloqueio identificado). Total do board: 29 → **30 cards** (6 Precisa refinar + 11 Quase pronto + 13 100% pronto).
- Nota registrada no modal do card: possível sobreposição com #12812 (mesmo épico #12387, ambos envolvendo layout/integração Oracle) — não investigada a fundo, só sinalizada.
- Reorganização de arquivos: criada `projetos/reviews-retros-planning/` e movidos os 6 resumos de review/retro/planning que estavam em `projetos/dailies/` (que agora só guarda standups) — todos os links cruzados corrigidos (contexto.md de automacao-fiscal, conciliacao-fase-2, dashboard-cds, overlimit, migracao-varret; prioridades-sprint.md; minhas-pendencias.md; READMEs; agente `daily-digest.md`).
- Criada `projetos/pesquisas-colaboradores/` com TAP.doc + Especificação Funcional recebidos do Igor (não lidos, a pedido dele).
- `minhas-pendencias.md` atualizado: reunião Ana Carina/Marcos (02/09, Gamificação) adicionada; item do TAP do Spin reconciliado com os novos arquivos recebidos; itens novos — levar resumo da Conciliação Fase 2 pro Spin, decidir card de Motor de Descontos em Verified, checar sobreposição #12812/#12892.
- **Checagem de paridade chip/modal:** OK (30 chips = 30 modais, checado via grep antes de publicar)
- **Artifact republicado:** https://claude.ai/code/artifact/ced8aba8-8054-44d2-a8f9-a4b410264a96 (live version lida por completo — 1087 linhas — antes de publicar)

### Pendências que ficaram para o Igor decidir
- Confirmar se #12892 e #12812 são de fato itens distintos ou se um deles deveria absorver o outro antes de estimar.
- Decidir se move manualmente o card de Motor de Descontos em "Verified" pra outra pessoa (levantado na review de hoje).
- Confirmar se o TAP + Especificação Funcional recebidos são sobre um projeto novo ("Pesquisas Colaboradores") ou se têm relação com o Ciacon, como a pendência antiga supunha.

### Erros/falhas nesta execução
Nenhuma.

---

## 2026-09-01 15:XX (execução manual, sob pedido do Igor — checar #12892 e #12890, 2ª varredura do dia)

### board-sync
- **Cards com estado/coluna mudados:**
  | ID | De | Para | Motivo (fonte) |
  |---|---|---|---|
  | #11933 | 100% pronto (**Refinement**) | 100% pronto (**Ready for Dev**, label atualizado) | Estado ADO avançou de Refinement pra Ready for Dev entre a 1ª e a 2ª varredura de hoje (`ChangedDate` 2026-08-31T13:57:55, posterior ao batch update das 13:17:42) — sem mudança de conteúdo/DoR. Comentário único do card (Igor, 12/08, refinamento dos 14→8 cenários) não traz nada novo além do que já estava refletido. |
  | #11941 | Quase pronto | Quase pronto (sem mudança de coluna) | Título no Azure foi alterado pra "...usuários e operador..." — cosmético: os 3 comentários (Danilo 25/08 sobre Cenário 7, refinamento 12/08, mention 23/06) já cobriam operador vs. usuário no AC (Cenário 5/6). Título do board sincronizado, chip/bloqueador de QA mantido sem alteração. |

- **Cards removidos do escopo do board (avançaram além de Ready for Dev):**
  | ID | Estado atual | Motivo |
  |---|---|---|
  | *(nenhum nesta 2ª varredura)* | — | — |

- **Cards novos descobertos:**
  | ID | Score DoR (4 pontos) | Coluna onde entrou |
  |---|---|---|
  | #12889 (Bug — Ajustar expansão de menus e posicionamento do DTEF, Kauã Cunha) — **achado só pela consulta WIQL, não estava nos 2 IDs que o Igor sinalizou** | 1/4 — AC rico em prosa (7 critérios) mas sem formato Cenário/GWT, sem rótulo de verificação, sem estimativa; nota técnica (bug/sustentação) também ausente (0 comentários) | Precisa refinar |
  | #12890 (Nonfunctional Item — Engenharia Reversa, nº da loja na Conciliação de Depósitos) — um dos 2 IDs sinalizados pelo Igor | 0/4 — Description e AC são só o título repetido, 0 comentários, mesmo padrão do #11840 | Precisa refinar |
  | #12892 (PBI — Fechamento Contábil da Conciliação e Integração de Perdas/Vales com Oracle) — o outro ID sinalizado pelo Igor | **NÃO adicionado ao board** — está em estado "To do" no Azure, fora do escopo definido (Refinement/Ready for Dev). Conteúdo já é forte (Story completa + 16 Cenários Dado/Quando/Então), mas ainda não chegou em Refinement. |

- **Checagem de paridade chip/modal:** OK (29 chips = 29 modais, checado via grep antes de publicar)
- **Artifact republicado:** https://claude.ai/code/artifact/ced8aba8-8054-44d2-a8f9-a4b410264a96 (live version lida e confirmada idêntica à base de edição antes de publicar; primeira tentativa de publish foi recusada pelo guard anti-loop mesmo após leitura completa — resolvido re-fetchando a URL e publicando de novo)

### Pendências que ficaram para o Igor decidir
- **#12892**: bem refinado (Story + 16 Cenários) mas preso em "To do" no Azure — não entra no board até alguém mover pra Refinement. Vale mover manualmente se a intenção é que entre na fila de refino.
- Itens abertos herdados da 1ª varredura de hoje continuam válidos e não foram revisitados nesta rodada: #12812 (bloqueio externo real — Adriana/layout Oracle) e a correção pendente em `gamificacao/contexto.md`.

### Erros/falhas nesta execução
- `wit_work_item list_comments` falhou na 1ª tentativa para #11933 e #11941 por faltar o parâmetro `project` explícito ("Project selection cancelled") — resolvido reenviando a chamada com `project: "Var Retaguarda"`.
- O primeiro `Artifact` publish foi recusado por "conteúdo idêntico já recusado, reenviado sem alteração" mesmo após leitura completa da versão live salva localmente — resolvido re-fetchando a URL do artifact (nova leitura) e publicando em seguida, sem alterar o conteúdo.

---

## 2026-09-01 (execução manual, sob pedido do Igor — "atualize nosso board de cards")

### daily-digest
Não rodou nesta execução — o pedido foi só board-sync. Nenhuma transcrição nova foi verificada.

### board-sync
- **Cards com estado/coluna mudados:**
  | ID | De | Para | Motivo (fonte) |
  |---|---|---|---|
  | #11941 | 100% pronto (Ready for Dev) | **Quase pronto** (Ready for Dev) | QA (Danilo, comentário 25/08): Cenário 7 (auditoria) tem redação condicional "(se aplicável)" — precisa virar obrigatório ou ser removido antes de sair de Ready for Dev |
  | #12190 | 100% pronto (Refinement) | 100% pronto (**Ready for Dev**, label atualizado) | Estado ADO avançou de Refinement pra Ready for Dev — sem mudança de conteúdo/DoR |

- **Cards removidos do escopo do board (avançaram além de Ready for Dev):**
  | ID | Estado atual | Motivo |
  |---|---|---|
  | #12179 (T1 Gamificação) | In Test / QA | Avançou além de Ready for Dev |
  | #12181 (T2) | In Test / QA | idem |
  | #12183 (T4) | In Test / QA | idem |
  | #12184 (T5) | In Test / QA | idem |
  | #12185 (T6) | In Test / QA | idem |
  | #12186 (T7) | In Test / QA | idem |
  | #12187 (T8) | In Test / QA | idem |
  | #12189 (T10) | In Test / QA | idem |

  **Achado importante:** #12182 (T3 Gamificação) é a ÚNICA da leva T1-T10 que **não** avançou — segue em Refinement/Quase pronto com o bloqueador de QA de 25/08 (ordem do fluxo campanha/cadastro). Isso contradiz o que estava registrado em `gamificacao/contexto.md` ("todos os T1-T10 avançaram pra In Test/QA") — vale corrigir esse arquivo numa próxima rodada de `portfolio-report`.

- **Cards novos descobertos (via WIQL, não rastreados antes):**
  | ID | Score DoR (4 pontos) | Coluna onde entrou |
  |---|---|---|
  | #12813 (Ciacon — levantamento e documentação, Kovalski) | 0/4 — Description/AC vazios, 0 comentários | Precisa refinar |
  | #12812 (Conciliação F2 — planilha Contábil, Diego Rafael) | 0/4 — vazio + bloqueio externo real (Adriana/layout Oracle) | Precisa refinar |

- **Checagem de paridade chip/modal:** OK (27 chips = 27 modais, antes e depois das edições)
- **Artifact republicado:** https://claude.ai/code/artifact/ced8aba8-8054-44d2-a8f9-a4b410264a96 (a versão live estava desatualizada desde 25/08 — as edições anteriores desta sessão nunca tinham sido efetivamente publicadas nela)

### Pendências que ficaram para o Igor decidir
- #12812: bloqueio externo real (Adriana/layout Oracle) — não resolvido, só sinalizado.
- Corrigir `gamificacao/contexto.md`: a afirmação "todos T1-T10 avançaram" está incorreta (T3 não avançou).

### Achado de qualidade de dado
Quase todos os 33 cards consultados via `get_batch` compartilhavam o mesmíssimo `System.ChangedDate` (2026-08-31T13:17:42.557Z) — indício de uma atualização em lote no Azure (provavelmente campo administrativo), não de mudanças reais individuais naquele instante. O diff foi feito comparando `State`/`BoardColumn` atual contra o que o board mostrava, não usando `ChangedDate` como sinal de "mudou recentemente".

### Erros/falhas nesta execução
Nenhuma chamada ADO falhou. A primeira tentativa de publicar o Artifact foi recusada (exigia reconfirmar leitura da versão live antes de publicar) — resolvido reconfirmando a leitura e republicando.
