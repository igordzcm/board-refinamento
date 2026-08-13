# Guia do processo de refinamento

Como levar um card de "Refinement" ou "Ready for Dev" até um estado em que o **dev não precisa levantar nada** e o **QA consegue testar sem ambiguidade**. Construído e validado nos cards do projeto Var Retaguarda (Azure DevOps) — este documento existe pra não depender de reler o histórico de chat.

> Este processo também existe como skill invocável: [`refinement-checklist`](../.claude/skills/refinement-checklist/SKILL.md). Este documento é a referência de leitura/detalhamento; a skill é a versão que o Claude carrega automaticamente ao trabalhar em um card. Os dois devem dizer a mesma coisa — se um mudar, atualizar o outro.

## Checklist de prontidão (4 pontos)

Todo card é avaliado contra isto antes de ser considerado "100% pronto":

| # | Critério | O que significa |
|---|---|---|
| 1 | **Formato Cenário + Dado/Quando/Então** | Cada critério de aceite tem um título ("Cenário N — Título") e segue Dado/Quando/Então, não prosa solta. |
| 2 | **Rótulo de verificação** | Cada cenário diz *como* será verificado: backend/integração, UI/frontend, revisão/aprovação, ou "processo não-automatizado" (quando for investigação/comunicação, não teste). |
| 3 | **Estimativa preenchida** | Esforço (story points) no campo do work item, não deixado em branco. |
| 4 | **Sem bloqueio real em aberto** | Nenhuma dependência externa (credencial, autorização, agenda de terceiros), decisão de arquitetura, ou sequenciamento (depende de outro card não concluído) sem estar resolvido ou pelo menos isolado e rastreado numa task própria. |

Um card com os 4 pontos ✓ é **100% pronto**. Com 1–2 gaps pequenos é **quase pronto**. Caso contrário, **precisa refinar**.

## Formato da história

```
Como [persona],
Eu quero [ação/capacidade],
Para que [benefício/valor].
```

Persona real (ex: "operador de campanhas do Motor de Descontos"), nunca genérica tipo "usuário". O "para que" precisa articular o benefício — não basta repetir a ação.

## Formato de critério de aceite

```
**Cenário N — Título curto**
Dado que [pré-condição],
Quando [ação/gatilho],
Então [resultado esperado].
Verificável por [teste de backend/integração | UI/frontend | revisão/aprovação | processo não-automatizado].
```

Exemplo real (card #12405):

> **Cenário 3 — Exclusão é soft delete**
> Dado que uma campanha é excluída,
> Quando a exclusão é confirmada,
> Então o registro é marcado como inativo (soft delete) no banco da Retaguarda, sem remoção física.
> Verificável por teste de backend/integração consultando o registro após a operação.

### Regra de ouro: AC pode exigir teste de backend, mas não deve prescrever a técnica

Um critério de aceite **pode e deve** dizer que algo precisa ser verificado por teste de backend/integração (isso é comportamento observável, testável). O que **não** entra no AC é a técnica de implementação (qual arquivo mexer, qual propriedade CSS usar, qual biblioteca). Achados de investigação de código viram uma seção separada na descrição:

```
**Levantamento técnico (sugestão para o desenvolvedor — não é regra fechada, vale confirmar):**
[achado, com referência a arquivo:linha quando aplicável]
```

Isso mantém o AC no nível de comportamento e deixa a decisão de implementação com quem vai codar.

## INVEST

Antes de considerar um card pronto, valide contra os 6 critérios:

| Critério | Pergunta | Passa se... |
|---|---|---|
| **I**ndependent | Dá pra desenvolver sem depender de outra story não commitada? | Sem dependência bloqueante |
| **N**egotiable | A implementação é flexível? | Mais de uma abordagem possível |
| **V**aluable | Entrega valor de usuário/negócio? | Benefício claro no "para que" |
| **E**stimable | O time consegue estimar? | Compreendida o suficiente pra dimensionar |
| **S**mall | Cabe em uma sprint? | ≤8 pontos |
| **T**estable | Dá pra verificar que está pronta? | Critérios de aceite claros |

**Nº mínimo de critérios por tamanho:** 1–2 pts → 3–4 critérios · 3–5 pts → 4–6 · 8 pts → 5–8 · 13+ pts → quebrar a story.

**Técnicas de quebra** quando uma story está grande demais: por etapa do fluxo, por persona, por tipo de dado, por operação (CRUD), ou happy-path-primeiro.

## Definition of Done

```
- [ ] Código completo e revisado por par
- [ ] Testes unitários escritos e passando
- [ ] Critérios de aceite verificados
- [ ] Documentação atualizada
- [ ] Deployado em staging
- [ ] Aprovado pelo Product Owner
- [ ] Sem bugs críticos remanescentes
```

## Quando investigar o código

Se o repositório do sistema estiver disponível localmente, vale ler o código antes de reescrever um card — isso já achou causa raiz real (contrato de API quebrado, coluna com nome errado, `overflow` duplicado) que uma leitura só do card não revelaria. Regras:

- **Sim, investigue** quando o objetivo é descrever com precisão o comportamento esperado, corrigir um fato errado no card (ex: nome de campo/coluna), ou fechar uma lacuna de "o que falta" que o QA já apontou.
- **Não pré-resolva a investigação** quando o próprio card já reserva isso como escopo do desenvolvedor (ex: um bug com timebox de investigação). Achar a causa raiz de antemão tira do dev o trabalho que é dele — nesse caso, pare e pergunte antes de aprofundar.
- Achados técnicos sempre entram como "levantamento — sugestão", nunca como determinação do PO.

## Quando usar fluxograma

- **Técnico** (skill `senior-architect`, Mermaid/PlantUML/ASCII) — quando há múltiplos branches de sistema (sucesso/falha/retry), uma sequência com ordem crítica (ex: validar antes de remover), ou quando o próprio critério de aceite exige um diagrama de arquitetura.
- **De negócio/processo** (skill `process-mapper`, BPMN) — quando é um processo operacional com etapas e tempo de ciclo (ex: runbook de backup/restore, homologação com múltiplas áreas).
- **Nenhum** — fixes pontuais, bugs de dado (contador dessincronizado, CSS), ou cards que herdam o diagrama de um card irmão.

## Quando usar mock/protótipo (checagem obrigatória em card de interface)

Sempre que o entregável do card for uma **tela nova ou alterada de forma relevante** — "gerar/criar/implementar interface", "tela de gerenciamento", "tela de configuração", uma view de CRUD — essa checagem é **obrigatória e o resultado precisa ficar registrado**, mesmo quando a resposta for "não precisa". Não deixar cair por omissão: um card de tela sem essa decisão anotada é um card mal refinado, do mesmo jeito que um card sem rótulo de verificação.

- **Sim, construir mock** (Artifact, protótipo HTML autocontido, guiado por `artifact-design`) — quando a ambiguidade é sobre **aparência/interação** (onde a lista fica na tela, como é o formulário de adicionar, onde aparece o erro de validação) e não sobre fluxo. Uma tela de listar+adicionar+remover quase sempre cai aqui — foi o caso do #11813, que passou pelo refino sem essa checagem (gap identificado em 12/08/2026).
- **Não, registrar a razão** — quando a mudança é trivial o suficiente pra não sobrar ambiguidade real (ex: troca de rótulo de um campo existente, reordenação simples de uma lista). Anotar como "Sugestão (não bloqueia): mock não necessário — [razão]" no card e no board, não deixar em silêncio.
- Publicar o mock via `Artifact`, linkar no card do Azure (Description ou comentário) **e** no board (`boards/board-refinamento.html` — chip 🏷️ Mock + link no modal).

## Comentários de QA (ex: Danilo)

Antes de reescrever um card, liste os comentários existentes. Um comentário tipo *"a descrição e os critérios precisam de mais detalhamento... para definir os cenários de teste e validar com maior assertividade"* é o sinal de que o AC está genérico demais — geralmente resolvido tornando os critérios objetivos e testáveis (não "sem erro", e sim "o dado X existe de fato depois da operação"). Depois de corrigir, responda o comentário no card explicando o que mudou.

## Fluxo passo a passo

1. Ler a descrição, AC e comentários atuais do card.
2. Rodar o checklist de 4 pontos.
3. Se algo depende de decisão de negócio (teto de retry, política de erro, prioridade), perguntar ao PO — nunca inventar.
4. Se algo depende de fato técnico verificável, e o código estiver disponível, investigar (respeitando a regra acima).
5. Reescrever descrição (Como/Quero/Para que) e AC (Cenário + Dado/Quando/Então + rótulo de verificação).
6. Decidir e registrar a necessidade de fluxograma/mock (ver seções acima) — obrigatório checar e anotar quando o card entrega uma tela, mesmo se a decisão for "não precisa".
7. Separar achados técnicos como "levantamento — sugestão", nunca misturados no AC.
8. Registrar decisões e pendências como comentário no card (rastro auditável).
9. Marcar a tag `Refinamento: Pronto` / `Refinamento: Quase Pronto` / `Refinamento: Precisa Refinar` no work item.
10. Atualizar o board (`boards/board-refinamento.html`) se o status mudou.

## Skills usadas (`.claude/skills/`)

| Skill | Quando usar |
|---|---|
| `refinement-checklist` | Sempre que for refinar/reescrever/revisar um card deste projeto — é o ponto de entrada, orquestra o uso das demais |
| `agile-product-owner` | Escrever/validar story, AC, INVEST, quebra de epic, planejamento de sprint |
| `senior-architect` | Fluxograma técnico, ADR, decisão de stack/dependências |
| `process-mapper` | Fluxograma de processo de negócio, BPMN, gargalo/tempo de ciclo |
| `senior-pm` | Priorização de portfólio (WSJF, EMV), risco quantitativo |
| `scrum-master` | Forecasting de velocidade, health score de sprint, retro |
| `code-to-prd` | Reverse-engineer um PRD a partir de código existente |
| `product-discovery` | Validar oportunidade antes de comprometer recursos de dev |
| `spec-to-repo` / `saas-scaffolder` | Scaffolding de projeto novo a partir de spec |
| `product-manager-toolkit` | RICE, síntese de pesquisa de usuário, templates de PRD |
| `roadmap-communicator` | Release notes, changelog, comunicação de roadmap |
| `research-summarizer`, `competitive-teardown`, `experiment-designer`, `product-analytics`, `product-strategist`, `ux-researcher-designer`, `ui-design-system`, `apple-hig-expert`, `landing-page-generator`, `product-skills` | Pesquisa, estratégia, UX e conteúdo — usar conforme a necessidade específica |
