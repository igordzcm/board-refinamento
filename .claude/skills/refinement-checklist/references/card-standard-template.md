# Card standard — ready-to-paste HTML

Paste these into `mcp__ado__wit_work_item_write` (`format: "Html"`) and fill the brackets. Keep the exact tag structure — it's what renders cleanly on the real Azure board, not just in previews.

## Description

```html
<p><strong>Eu, enquanto</strong> [persona]<br><strong>poderia/gostaria/devo</strong> [necessidade — a capacidade que a persona precisa, nunca a solução/tela já decidida]<br><strong>para/tal que/por que</strong> [benefício/valor]</p>
<h3>Descrição</h3>
<p>[o que existe hoje, o que motiva a mudança, e o que o card entrega — em linguagem direta, sem contar a história de como o card nasceu]</p>
<p><strong>Nota técnica:</strong> [se houver padrão existente no código, cite arquivo/serviço exato — se buscou e não achou, diga isso explicitamente e onde procurou, sem inventar]</p>
```

Pick whichever of poderia/gostaria/devo and para/tal que/por que fits **this sentence** — judge each card on its own, don't default to the same verb across a batch (poderia = capacidade opcional, gostaria = desejo, devo = obrigação funcional; um ator de sistema/motor quase sempre pede "devo", não "poderia"). Test before closing the "want" clause: does it name a capability (good) or a UI element like "um modal"/"uma tela" (rewrite it — that's the solution, not the need).

**Description tells what the card is, never how it was found.** Cut, always: dates ("pedido em 17/08", "confirmado em 20/08"), attribution ("Pedido por Fulano", "Fulano respondeu que ia aplicar segunda"), and narration of the source conversation's outcome ("a conversa termina sem confirmação", "essa é a pendência mais arriscada da call"). None of that is the card's context — it's the card's origin story, and it belongs in a **comment**, not in Description. If a source needs to be traceable (a call, a doc, a thread), cite it once in a comment; don't re-tell it in Description. A Description with a date or a person's name in it is a signal to go back and cut.

If part of the scope is explicitly out, say so in its own line — don't let it live only in your head:

```html
<p>[X] não tem [Y] e fica fora do escopo deste card.</p>
```

## Acceptance Criteria

```html
<div>
<p><strong>Cenário 1 — [título curto]</strong><br>Dado que [pré-condição], quando [ação/gatilho], então [resultado esperado]. Verificável por [rótulo].</p>
<p><strong>Cenário 2 — [título curto]</strong><br>Dado que [pré-condição], quando [ação/gatilho], então [resultado esperado]. Verificável por [rótulo].</p>
<p><strong>Cenário N — Falha / caso de borda</strong><br>Dado que [algo dá errado], quando [o erro ocorre], então [comportamento esperado — mensagem clara, sem estado corrompido]. Verificável por [rótulo].</p>
</div>
```

Always close with a failure/edge-case scenario when the story involves any async, external, or error-prone step (worker, API call, file generation, third-party integration) — "o que acontece quando falha" is the single most common gap in cards that otherwise look complete.

## Rótulo de verificação — pick the closest fit

- `teste de backend`
- `teste de frontend` / `e2e`
- `teste de integração` (crosses a boundary: worker+email, API+DB, service-to-service)
- `revisão do time técnico` / `aprovação formal` (not assertion-testable — docs, architecture sign-off)

## Checklist to literally paste into your own working notes before closing a card

```
[ ] Li o card e confirmei o formato do campo (HTML vs Markdown) via multilineFieldsFormat
[ ] Li todos os comentários — Danilo (QA) em particular — e incorporei o que for relevante na AC
[ ] Busquei padrão técnico existente no repo (search_code / repo_file) antes de citar "já existe" — cito arquivo real ou registro busca sem resultado
[ ] Story em Eu-enquanto-poderia/gostaria/devo-para/tal/por que + Cenários em Dado/Quando/Então
[ ] Escolhi o verbo (poderia/gostaria/devo) pelo sentido desta frase, não copiei do card anterior
[ ] O "quero" da story é uma necessidade (capacidade), não uma solução/tela já decidida
[ ] Description sem data, sem nome de quem pediu, sem narrar a conversa/fonte de onde o card saiu — isso é comentário, não Description
[ ] Cada cenário tem "Verificável por [rótulo]"
[ ] Vinculei formalmente: parent epic + related (telas, bugs, dependências) — não só menção em texto
[ ] Re-busquei o card depois de qualquer link_write pra confirmar que Description não foi truncada
[ ] Estimativa preenchida, OU pendência com dono nomeado explicitamente
[ ] Bloqueio real externo? Se sim, perguntei ao usuário antes de decidir — não movi coluna sozinho
[ ] Avaliei fluxograma/mock pelo teste de decisão (técnico / processo / mock / nenhum) — não adicionei por padrão
[ ] Card atualizado no board-refinamento.html com chips/modal correspondentes
```

## Fluxograma ou mock — teste de decisão rápido

1. Dev teria que desenhar esse fluxo num quadro pra entender? → **Técnico** (🧭 roxo, skill `senior-architect`)
2. A ambiguidade é "quem faz o quê, em que ordem, entre quais áreas" e não "como o código funciona"? → **Processo** (🧭 verde-água, skill `process-mapper`)
3. A ambiguidade é sobre aparência/interação de tela, não sobre fluxo? → **Mock** (🏷️ rosa, Artifact)
4. Nenhum dos casos, 2-3 cenários já deixam claro? → **Não construir.** No máximo, sugestão não-bloqueante no "O que falta".
