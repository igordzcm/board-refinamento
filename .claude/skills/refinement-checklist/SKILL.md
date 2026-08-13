---
name: "refinement-checklist"
description: Var Retaguarda card-refinement standard — the fixed sequence and completeness gate applied to every backlog item before it's marked ready for dev. Covers user story + acceptance criteria format, reading Danilo's QA comments for changes, checking technical/infra context in the actual repo, formal Azure links, and the four-point Definition of Ready (Formato, Rótulo, Estimativa, Sem bloqueio). Use whenever refining, reviewing, or writing a card for the board-refinamento project — this is the default workflow, not an optional pass.
not_for: Generic user-story writing outside this project's Cenário+GWT convention (use agile-product-owner instead), architecture decisions with no card attached (use senior-architect directly), process/BPMN mapping (use process-mapper directly)
triggers:
  - refinar card
  - refine backlog item
  - dev-ready checklist
  - definition of ready
  - comentário do Danilo
  - cenário dado quando então
  - preparar card pro dev
  - atualizar board de refinamento
---

# Refinement Checklist — Var Retaguarda

The standard this workspace runs on every backlog item touched, so a card reaches a developer needing **zero extra planning conversations** before they can start coding. This is not a style guide — it's the sequence to run, in order, every time.

**Why this exists:** a card that's "written" but not "dev-ready" costs the developer a round trip (Slack the PO, wait, re-read, start). The whole point of refinement is to absorb that round trip during grooming, not leave it for pickup day.

---

## Table of Contents

- [The sequence (run every time)](#the-sequence-run-every-time)
- [1. Read the card as it stands](#1-read-the-card-as-it-stands)
- [2. Read every comment — Danilo's especially](#2-read-every-comment--danilos-especially)
- [3. Check the technical/infra context](#3-check-the-technicalinfra-context)
- [4. Write Story + Cenários in the house format](#4-write-story--cenários-in-the-house-format)
- [5. Label verification per scenario](#5-label-verification-per-scenario)
- [6. Link formally — don't just mention](#6-link-formally--dont-just-mention)
- [7. Estimate, or name who does](#7-estimate-or-name-who-does)
- [8. Flowchart or mock — only when it earns its place](#8-flowchart-or-mock--only-when-it-earns-its-place)
- [The Definition of Ready (4-point gate)](#the-definition-of-ready-4-point-gate)
- [What "minimizing dev steps" means concretely](#what-minimizing-dev-steps-means-concretely)
- [Board columns map to this gate](#board-columns-map-to-this-gate)

---

## The sequence (run every time)

1. Read the card as it stands (title, description, AC, current state/column).
2. Read every comment on the card — **Danilo's comments are QA feedback and almost always mean "the AC needs to change," not "note for later."**
3. Check technical/infra context: is there an existing pattern in the codebase this should reuse? Search it — don't assume.
4. Write the Story (Como/Quero/Para que) + Cenários (Dado/Quando/Então) in the house format.
5. Label how each scenario is verified.
6. Link formally in Azure DevOps: parent epic, related screens/cards, prior bug references.
7. Fill the estimate, or name explicitly who needs to and why it's not you.
8. Decide whether a flowchart or mock earns its place — add it if yes, skip it deliberately if no. **For any card whose deliverable is a new/changed screen, this decision is mandatory and must be recorded, not silently skipped** (see step 8 below).

Steps 2 and 3 are the ones most often skipped under time pressure — they're also the ones that most directly reduce what the developer has to figure out alone. Do not skip them because the card "looks done" from the description alone.

---

## 1. Read the card as it stands

Standard read: Title, Description, AcceptanceCriteria, State, Assignee, StoryPoints/Effort, Parent. Note the `multilineFieldsFormat` returned by the API — never assume Markdown; check whether Description/AC render as HTML and write real `<p>`/`<strong>`/`<ul><li>` markup accordingly. A field written in the wrong format renders literal asterisks on the real board — verify, don't guess.

---

## 2. Read every comment — Danilo's especially

Danilo is QA. His comments on a card are signal, not noise — they flag real defects, edge cases the AC missed, or regressions tied to specific bugs (e.g. a header/cookie-size failure mode seen before in one card and cited defensively in another). Treat a Danilo comment as **required input to the AC rewrite**, not an FYI to leave unaddressed:

- If he names a concrete risk (a bug class, a data edge case, a regression), add a Cenário that covers it explicitly, and reference the originating card/bug by ID.
- If he asks a question, answer it in a reply comment *and* fold the answer into the AC — don't let the resolution live only in the comment thread where the next reader won't see it.
- If the card has no comments yet, still check — don't skip the API call because the description looks complete. Silence is not the same as "no QA input exists yet."

This applies to any QA/tech-lead commenter, not literally only Danilo — but on this board it's almost always Danilo, so his name is the trigger to remember the step.

---

## 3. Check the technical/infra context

Before writing AC that assumes a mechanism exists ("processed via worker," "reuses the existing queue," "same pattern as X"), verify it against the real source, not just the work-item text. Two outcomes, both useful, and only one requires care:

- **Found it:** cite the exact file/class/service/queue name in the card's Description as a technical note. This is the single highest-leverage thing you can do for the next developer — it turns "figure out how this pattern works" into "extend this specific file."
- **Not found:** say so explicitly in the card, and say what you searched (repos, keywords). Never invent a plausible-sounding file path or service name to fill the gap — a fabricated reference is worse than no reference, because it sends the developer hunting for something that doesn't exist. Flag it as a pendency for the tech lead to point to the real one.

**Mandatory for bug fixes and sustentação cards (added 2026-08-13, gap found on #12507):** any card whose deliverable is a correction to existing behavior — bug fix, data-correction, sustentação — must get the technical suggestion written to the card in **two places, both required, every time:**
1. A comment on the work item (`mcp__azure-devops__wit_work_item_comment_write`) with the full finding — file paths, what was checked, the reasoning.
2. A **leaner** version folded into the card's Description itself (`mcp__azure-devops__wit_work_item_write`, a short "Nota técnica" section) — a couple of sentences naming the file(s)/screen and the likely fix point, not the full investigation narrative. The Description is what a developer opens first; a finding that only lives in a comment thread is easy to miss.

A local board/session note alone is never enough — both of the above must land on the actual Azure DevOps card. At minimum, both must name **where the fix will happen** — the exact file (backend) or screen/component (frontend) — even if you can't pin down the precise root cause. Grep the local repo clones for the field/table/function named in the bug report (e.g. a PRO0xx column, a service method) before concluding "not found." When you can trace the actual data path (e.g. confirming a value is passed through unchanged with no transformation, across create/update/persist), say so — that's more valuable to the dev than a guess at the fix, and often reframes the bug (see #12507: not a wrong formula, but a missing one, across three call sites). Skip this only when there's truly no plausible codebase to search (e.g. a pure content/business-rule card).

**Where to actually look (found 2026-08-12 — check this list is still current before trusting it blindly):**

- **`mcp__ado__search_code` against the "Var Retaguarda" Azure DevOps project searches the wrong code.** That project's repos (`report-project`, `Infra.*`, `roleta_premiada_api`, etc.) are auxiliary tooling, not the portal. Confirmed empty result chasing a pattern that turned out to live elsewhere — don't repeat that search.
- **The real Portal Retaguarda backend/frontend lives in a different Azure DevOps project**, "Projeto - Conciliação de Caixa", repos `ConciliaçãoCaixaAPI` / `ConciliaçãoCaixaFront`. **Confirmed path as of 2026-08-13**: `C:\Users\igor.diniz\Documents\ConciliacaoCaixa\ConciliacaoCaixaAPI` and `...\ConciliacaoCaixaFront` — two levels above this workspace (`Documents/ConciliacaoCaixa/`, not `Documents/BMAD/`). **The earlier note about `TAREFAS/...` was wrong/stale — the clones were missing (empty parent folder) when checked on 2026-08-13 and had to be re-cloned.** Verify with a quick `ls`/`Glob` before trusting either path blindly; re-clone (commands in root `README.md`) if empty. Use `Glob`/`Grep`/`Read` directly on these local paths — faster and more reliable than the ADO code-search API, and this is where Motor de Descontos, Migração Var Ret, Automação Fiscal, Gamificação/campaign-roulette, and the rest of the Retaguarda modules actually live (`src/modules/<domain>`).
- Known reusable infrastructure already confirmed in `ConciliaçãoCaixaAPI`: an async **worker + e-mail** export pipeline — `ExcelGenerationQueue` port (`src/modules/tax-closing/ports/excel-generation-queue.port.ts`) implemented by `BullExcelGenerationQueue` (Bull/Redis), and `ExcelNotifier` port (`ports/excel-notifier.port.ts`) implemented by `GraphExcelNotifier` (sends via Microsoft Graph, `EmailService.sendEmail`, file attached as base64). Reference processor: `TaxClosingExcelProcessor`. As of 2026-08-12 this is used **only** by the Automação Planilha Fiscal (`tax-closing`) module — no Migração Var Ret screen (Lote 1 or Lote 2) uses it yet, despite that being the assumption going into card #12484. Don't assume it's already wired up elsewhere just because the infrastructure exists — check the specific controller (grep for `@Res() response: Response` vs. a queue/notifier call) before claiming a screen already uses it.
- **`src/modules/campaign-roulette/`** (found 2026-08-13, refining card #12186/T7 of Gamificação): a full existing campaign-management module already in production — controller `/campaign-roulette`, `CampaignRouletteService`/`Repository`, DTOs, banner upload, store config, probabilities, direct writes to Oracle table `VAR.PRO015`. Types today: `ROULETTE` and `WORLD_CUP` only (not the 4 Gamificação mechanics). **Before assuming any Gamificação card (T5-T10) needs to be built from scratch, check whether it should extend this module instead** — it may substantially change scope/estimate. Specific gap found: campaign start/end dates (`P15DTINI`/`P15DTFIM`) are written per-campaign from the DTO, but voucher-validity fields (`P15DIASINI`/`P15VALID`/`P15DIASVAL`) are hardcoded from `PRO015_DEFAULTS`, not configurable per campaign — would need extending if Gamificação requires per-campaign voucher validity.

Also worth a look, when relevant to the story: which repo/module owns this screen, whether there's an existing ADR or architecture note for the area (`senior-architect` skill / `_bmad-output/planning-artifacts/`), and whether the change touches a documented integration point (Kong/Keycloak, MTA, BI feeds, etc.) that has known failure modes from past cards.

---

## 4. Write Story + Cenários in the house format

This project uses **Cenário + Dado/Quando/Então** (Portuguese Given-When-Then), not the English GWT template from `agile-product-owner` — match the existing convention on the board, don't introduce a second format.

```html
<p><strong>Como</strong> [persona]<br>
<strong>Quero</strong> [ação/capacidade]<br>
<strong>Para que</strong> [benefício/valor]</p>
<h3>Descrição</h3>
<p>[contexto, motivação, referências a cards relacionados]</p>
```

```html
<div>
<p><strong>Cenário 1 — [título curto]</strong><br>
Dado que [pré-condição], quando [ação/gatilho], então [resultado esperado]. Verificável por [rótulo].</p>
<p><strong>Cenário 2 — [título curto]</strong><br>
...</p>
</div>
```

See `references/card-standard-template.md` for the ready-to-paste HTML skeleton (this exact block, no placeholders to hunt for).

Minimum scenario count scales with size, same as `agile-product-owner`'s table (3-4 for 1-2 pts, up to 8 for large items) — but on this board, a bug-fix card with a single confirmed rule (like a data-correction card) can be complete with 2-3 tightly-scoped scenarios; don't pad for the sake of a count.

---

## 5. Label verification per scenario

Every scenario ends with **"Verificável por [rótulo]"** — this is not decoration, it tells the developer and QA what kind of check closes the item:

| Rótulo | When to use |
|---|---|
| `teste de backend` | Pure API/data logic, no UI involved |
| `teste de frontend` / `e2e` | UI behavior, user-visible state |
| `teste de integração` | Crosses a boundary — worker+email, API+DB, service-to-service |
| `revisão do time técnico` / `aprovação formal` | Not testable by assertion — documentation, architecture sign-off |

If a scenario is **required** for the story to be complete, the label is not optional — leave a scenario unlabeled and a developer or QA has to guess what "done" means for it.

---

## 6. Link formally — don't just mention

Mentioning a related card by `#ID` in prose is not the same as linking it. Use `mcp__ado__wit_work_item_link_write`:

- **Parent**: every card should resolve to its Epic. If it doesn't, link it — don't leave it orphaned even if the Epic is obvious from context.
- **Related**: link every screen/card a change touches, every prior bug a new scenario defends against, every dependency (`Depends on [BE] Função X`).

**Known gotcha (hit 2026-08-12):** the `link` action can silently strip trailing content from `System.Description` as a side effect. Always re-fetch the card after a `link` call and confirm the Description is intact before moving on — don't assume the write-then-link sequence is safe.

**Known gotcha (hit 2026-08-12):** Azure DevOps boards split a column into a Doing/Done sub-state (visible in the UI as a divider inside e.g. "Refinement"). This state is readable via `System.BoardColumnDone` (bool) on any work item, but that field is **read-only** — writing to it fails with `TF401326: Invalid field status 'ReadOnly'`. To actually toggle it, write the team-specific mirror field instead: `WEF_CA2D2CCF39524B8CBBEA41E6E670BF7C_Kanban.Column.Done` (this project's team GUID; confirm it hasn't changed if writes start failing). Writing that field updates `System.BoardColumnDone` as a side effect. There's no dedicated "get board config" MCP tool in this workspace's ADO server — the split state only shows up per-item via these fields, not via a board/column listing call.

**Value polarity (corrected 2026-08-13, got this backwards once — caught by the user after cards #12509-#12513 landed in the wrong sub-lane):** `Kanban.Column.Done = false` → **Doing** sub-lane (still being worked). `Kanban.Column.Done = true` → **Done** sub-lane (finished within that column, ready to move on). When a card should sit in "Refinement — Doing," write `false`, not `true` — the field name reads like a completion flag for the whole item, but it's scoped to the sub-lane within the current column.

---

## 7. Estimate, or name who does

Never invent a story-point number to make a card look complete — an estimate is the technical team's call, not the PO's. If it's missing:

- Note explicitly in the card who needs to size it (usually the tech lead/dev who'll pick it up) and why it's pending (e.g. "escopo pequeno, mas fica a critério do time técnico").
- A card with everything else done and only the estimate outstanding still belongs in "Quase pronto," not "100% pronto" — the board is honest about this, keep it that way.

---

## 8. Flowchart or mock — only when it earns its place

Three artifact types, three chips, three trigger conditions. None of them are part of the 4-point gate below — a card can be 100% pronto with zero diagrams. Add one only when it removes a real question the developer would otherwise have to reconstruct from prose, per the `artifact-diagramming` rule: *if a sentence says it faster, write the sentence.* Defaulting to "add a diagram" on every technical card is decorative noise, not refinement — it's the same failure mode as padding scenario counts.

| Chip | Color | Skill to invoke | Add it when... |
|---|---|---|---|
| 🧭 Técnico | purple `flow-tech` `#6A4FA3` | `senior-architect` | The change crosses multiple components/services and the sequence isn't obvious from the AC alone (auth flows like browser→Kong→Keycloak→callback; a worker+email pipeline; gravação direta + soft delete + reprocessamento). Also add one whenever the card is really an **architecture decision** worth an ADR — record it under `_bmad-output/planning-artifacts/adr-<id>-<slug>.md` and link the artifact from the card. |
| 🧭 Processo | teal `flow-proc` `#0E7C77` | `process-mapper` | The card's real content is a **business process** with human handoffs/approvals across roles or areas (validação de negócio com múltiplas áreas, runbook operacional, onboarding). Especially valuable when a real external blocker is *itself* about an unclear multi-step approval chain — the flowchart is what lets the PO point at exactly which step is stuck. |
| 🏷️ Mock | pink `mock` `#B23A6B` | Artifact (interactive HTML prototype) | The card introduces or meaningfully changes a **screen** where a written description leaves layout/interaction genuinely ambiguous, or where multiple stakeholders need to react to something concrete before dev starts (business-area review, design sign-off). |

**Decision test, in order:**
1. Would a cold-read developer have to draw this flow themselves on a whiteboard to understand it? → technical flowchart.
2. Is the ambiguity really "who does what, in what order, across which teams" rather than "how does the code work"? → process flowchart.
3. Is the ambiguity about what something *looks like* rather than how it *flows*? → mock.
4. None of the above — two or three AC scenarios already make the sequence obvious? → skip it. Leave it as a non-blocking suggestion in the "O que falta" list at most ("Sugestão (não bloqueia): ...") rather than actually building one.

**Mandatory check for interface-generation cards (added 2026-08-12, gap found on #11813):** if the card's deliverable is a new or meaningfully-changed **screen** — title/description says "gerar/criar/implementar interface," "tela de gerenciamento," "tela de configuração," a new CRUD view, or similar — test #3 above must be run and its outcome **explicitly recorded**, the same way a skipped flowchart gets a recorded "não é necessário porque X" instead of just silently not appearing. Do not let this fall out through option 4's catch-all by default; option 4 requires actively confirming the layout has no genuine ambiguity (e.g. a single trivial label swap), not just "the AC scenarios exist." A list+add+remove management screen (#11813 is the case that surfaced this) almost always clears the bar for #3 — there's a real layout question (where does the list live, what does the add form look like, where does the validation error show) that prose alone leaves to the developer to invent. Record the decision in the card's Description/AC or a comment, and reflect it on the board (`board-refinamento.html`) either as a 🏷️ Mock chip + link, or as an explicit "Sugestão (não bloqueia): mock não necessário — [razão]" note — never as silence.

**Mechanics once you decide to build one:**
- Invoke the matching skill (`senior-architect` or `process-mapper`), or build the mock as a self-contained Artifact per `artifact-design`.
- Publish via the `Artifact` tool, then link it in **both** places: the Azure DevOps card (as an external link in the Description or a comment) and the board (`board-refinamento.html` — add the chip to the `.chips` row and an `<a class="ext">` link in the modal).
- Don't touch a card's existing flowchart/mock decision when re-syncing the board unless the underlying card content changed — re-litigating "should this have a diagram" on every sync is wasted motion.

---

## The Definition of Ready (4-point gate)

A card is dev-ready when all four are true. This is the exact checklist already rendered on the board (`board-refinamento.html` `.checkgrid`) — this skill is what produces the inputs to that grid, not a separate standard:

1. **Formato Cenário + GWT** — Story + scenarios in the house format, no prose-only AC.
2. **Rótulo de verificação** — every scenario says how it's checked.
3. **Estimativa preenchida** — a number, or an explicit named-owner pendency.
4. **Sem bloqueio real** — no unresolved external dependency (stakeholder approval, vendor response, infra not provisioned). A real external blocker is not something to resolve unilaterally — per standing project rule, ask the user before deciding how to handle it (column placement, whether to proceed). Internal pendencies (scope to confirm with a teammate, estimate to fill) are *not* the same thing as external blockers — don't conflate them, and don't hold a card in "Precisa refinar" for an internal pendency that format/label work has already resolved.

**5th item, conditional (added 2026-08-13):** for bug-fix/sustentação cards only, the board also renders a 5th `.check-item` row — "Nota técnica no card" — reflecting the mandatory technical-suggestion requirement from step 3. Yes (`mark yes`) when both the comment and the Description note are posted; No (`mark no`) when the card qualifies but neither/only one is done yet; "não se aplica" (`mark na`) with a recorded reason when the card explicitly reserves investigation to the dev (e.g. a timeboxed bug AC). This row does **not** appear on feature/non-correction cards — don't add it everywhere, only where step 3's mandatory rule actually applies. It's additive to the 4-point gate, not a 5th gate condition for column placement (Precisa refinar/Quase pronto/Pronto still runs off the 4 points above).

---

## What "minimizing dev steps" means concretely

The test for "is this card dev-ready" is not "does it have Cenários" — it's **"if a developer picked this up cold, what's the first question they'd have to ask someone?"** Answer that question in the card before it leaves refinement:

- If the answer is "which existing screens does this touch" → link them (step 6).
- If the answer is "does this already exist somewhere I should copy" → search and cite it, or flag honestly that you searched and didn't find it (step 3).
- If the answer is "did QA already flag something about this" → check comments (step 2).
- If the answer is "what does the output need to look like" → pull the concrete formatting/behavior requirements from sibling cards or existing screens into the AC, don't leave it implicit (e.g. "segue o padrão do portal" is weaker than naming the actual fields: logo, timestamp, filters, user).
- If the answer is "how big is this" → estimate or name the owner (step 7).

A card that still requires the developer to open Slack before writing code has not finished refinement, regardless of how well-formatted the Cenários are.

---

## Board columns map to this gate

| Board column | Meaning |
|---|---|
| **Precisa refinar** | Content itself is insufficient (empty/one-line AC) or format is genuinely missing — needs to be written from scratch with the technical team. |
| **Quase pronto** | Format + label done; blocked only by estimate, an internal pendency with a named owner, or a real external blocker already surfaced to the user. |
| **100% pronto** | All four gate points pass. Nothing left for the developer to ask before starting. |

Run this checklist, and the column a card lands in should never need a second look to justify.

## Related Skills

- **agile-product-owner** — general INVEST/story-splitting theory this project's format specializes.
- **senior-architect** — pull in for ADRs or when a card's technical note needs a fuller architecture writeup, not just a file citation.
- **process-mapper** — pull in when the card's blocker or scope is really a business-process question (who approves what, in what order), not a coding question.

## See also

- [`docs/processo-de-refinamento.md`](../../../docs/processo-de-refinamento.md) — the longer-form reference version of this same standard (worked examples, INVEST table, Definition of Done). Keep both in sync if either changes.
- [`README.md`](../../../README.md) — full list of all 22 skills in this workspace and when each applies, not just the ones directly related to card refinement.
