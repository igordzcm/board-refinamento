# board-refinamento

Workspace pessoal de trabalho como PO no projeto **Var Retaguarda** (Azure DevOps, Grupo Avenida): skills do Claude Code, board de refinamento de cards e artefatos de planejamento produzidos ao longo do processo.

## Documentação

- **[`docs/processo-de-refinamento.md`](docs/processo-de-refinamento.md)** — guia do checklist e do passo a passo usado pra refinar cards: formato de história e AC, INVEST, Definition of Done, quando investigar código, quando usar fluxograma, e a lista de skills.

## Boards

- **[`boards/board-refinamento.html`](boards/board-refinamento.html)** — board estilo Trello com os 25 cards de "Ready for Dev" + "Refinement" do Var Retaguarda, agrupados por status de prontidão (Precisa refinar / Quase pronto / 100% pronto) contra um checklist de refinamento: formato Cenário + Dado/Quando/Então, rótulo de nível de verificação (backend, UI, revisão), estimativa preenchida e ausência de bloqueio real. Clique num card pra abrir o detalhe do que falta. Também publicado como [Artifact](https://claude.ai/code/artifact/ced8aba8-8054-44d2-a8f9-a4b410264a96).
- **[`boards/breakdown-ready-for-dev.html`](boards/breakdown-ready-for-dev.html)** — dashboard anterior com a lista de trabalho por card e o veredito de necessidade de fluxograma (técnico via `senior-architect` ou de processo via `process-mapper`) para cada um.

Abra qualquer um dos dois arquivos direto no navegador — são HTML autocontidos, sem dependência externa.

## Skills (`.claude/skills/`)

22 skills — 21 selecionadas de [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) pra uso como PO, mais 1 própria (`refinement-checklist`) construída neste workspace. **Regra do workspace: sempre invocar a skill que combina com a tarefa, em vez de fazer a mesma análise "à mão".** Não são referência passiva — são o fluxo de trabalho padrão.

### Refinamento de card (o dia a dia deste workspace)

| Skill | Quando usar |
|---|---|
| `refinement-checklist` | **Ponto de entrada padrão** pra qualquer trabalho em card do Var Retaguarda — refinar, reescrever, revisar. Define a sequência (ler comentários do Danilo, checar padrão técnico no repo, escrever Story+Cenário, rotular verificação, linkar formalmente, estimar, decidir fluxograma/mock) e o gate de 4 pontos. Orquestra quando chamar as demais abaixo. Ver também [`docs/processo-de-refinamento.md`](docs/processo-de-refinamento.md). |
| `agile-product-owner` | Escrever/validar user story e AC fora do card em si, INVEST, quebra de epic, planejamento e capacidade de sprint |
| `senior-architect` | Fluxograma técnico (🧭 roxo), ADR, decisão de stack/dependência, revisão de arquitetura |
| `process-mapper` | Fluxograma de processo de negócio (🧭 verde-água), BPMN, gargalo e tempo de ciclo — quando o card é sobre handoff entre áreas/pessoas |
| `senior-pm` | Priorização de portfólio (WSJF, EMV), análise de risco quantitativa, relatório executivo multi-frente |
| `scrum-master` | Forecast de velocidade (Monte Carlo), health score de sprint, análise de retro |

### Pesquisa, descoberta e estratégia

| Skill | Quando usar |
|---|---|
| `product-discovery` | Validar oportunidade/hipótese antes de comprometer capacidade de dev |
| `product-manager-toolkit` | RICE, síntese de entrevista de usuário, templates de PRD, go-to-market |
| `product-strategist` | Cascata de OKR, planejamento trimestral, visão de produto, proposta de estrutura de time |
| `competitive-teardown` | Análise de concorrente — matriz de features, SWOT, mapa de posicionamento |
| `experiment-designer` | Planejar experimento/A-B test, hipótese testável, tamanho de amostra |
| `product-analytics` | KPIs, dashboard de métricas, análise de coorte/retenção |
| `research-summarizer` | Resumir paper/artigo/relatório, análise comparativa, citações |
| `roadmap-communicator` | Release notes, changelog, narrativa de roadmap pra stakeholder |

### Código, arquitetura e scaffolding

| Skill | Quando usar |
|---|---|
| `code-to-prd` | Fazer engenharia reversa de um PRD a partir de código existente |
| `spec-to-repo` | Gerar repositório novo e completo a partir de uma spec em linguagem natural |
| `saas-scaffolder` | Boilerplate de SaaS (Next.js, auth, billing, dashboard) |

### UX e design

| Skill | Quando usar |
|---|---|
| `ux-researcher-designer` | Persona, jornada de usuário, plano de teste de usabilidade, síntese de pesquisa |
| `ui-design-system` | Design tokens, documentação de componente, handoff pra dev |
| `apple-hig-expert` | Auditar/desenhar UI de plataforma Apple contra a Human Interface Guidelines |
| `landing-page-generator` | Gerar landing page (Next.js/React/Tailwind) com copy orientada a conversão |

### Orquestração

| Skill | Quando usar |
|---|---|
| `product-skills` | Coordenar trabalho que cruza várias das skills de produto acima, ou rodar o loop contínuo de discovery |

## Planejamento (`_bmad-output/planning-artifacts/`)

Backups de versões originais de cards e o ADR-1 (decisão de arquitetura do redesenho do Motor de Descontos) produzidos durante o refinamento do card #12405 e outros.

## Referências (`referencias/`)

Material bruto recebido de terceiros (planos técnicos, protótipos navegáveis, specs) usado como insumo pra refinar um card — diferente de `_bmad-output/planning-artifacts/`, que guarda o que *o Claude produz* durante o refinamento. Nomeado `<card-id>-<slug>.html`. Quando cair um arquivo novo desses na raiz do workspace, ele é movido pra cá.

## O que NÃO está aqui (e como restaurar numa máquina nova)

Estas pastas ficam de fora (`.gitignore`) porque são código-fonte de terceiros ou da empresa, cada uma já com seu próprio repositório remoto. **Já estão clonadas nesta máquina, mas um nível acima** (`TAREFAS/ConciliaçãoCaixaAPI` e `TAREFAS/ConciliaçãoCaixaFront`, irmãs de `board-refinamento/`, não dentro dela) — é lá que fica o código real do Portal Retaguarda (Motor de Descontos, Automação Fiscal, Migração Var Ret etc.), útil pra citar arquivo/classe exatos ao refinar um card técnico. Numa máquina nova sem elas, clone a partir da raiz do workspace (`TAREFAS/`, não de dentro de `board-refinamento/`):

```bash
# Código proprietário do Grupo Avenida (projeto "Conciliação de Caixa" no Azure DevOps —
# é onde vive o back-end/front-end do Motor de Descontos, Portal de Retaguarda etc.)
git clone "https://dev.azure.com/GrupoAvenida/Projeto%20-%20Concilia%C3%A7%C3%A3o%20de%20Caixa/_git/Concilia%C3%A7%C3%A3oCaixaAPI" "Concilia%C3%A7%C3%A3oCaixaAPI"
git clone "https://dev.azure.com/GrupoAvenida/Projeto%20-%20Concilia%C3%A7%C3%A3o%20de%20Caixa/_git/Concilia%C3%A7%C3%A3oCaixaFront" "Concilia%C3%A7%C3%A3oCaixaFront"

# Biblioteca completa de skills de terceiros (só precisa se for instalar mais skills)
git clone https://github.com/alirezarezvani/claude-skills.git
```

Requer acesso ao Azure DevOps do Grupo Avenida (`az` CLI autenticado ou credencial de git configurada) para os dois primeiros clones.

## Contexto

Este workspace nasceu de um processo de refinamento de cards "Ready for Dev" e "Refinement" no board do Azure DevOps (projeto **Var Retaguarda**), usando primeiro o framework BMAD-METHOD e depois migrando para skills avulsas do `claude-skills` (INVEST, Definition of Done, formato Cenário + Dado/Quando/Então). O BMAD-METHOD em si foi removido deste workspace — só os artefatos de trabalho (`_bmad-output/`) ficaram. Todos os cards de "Ready for Dev" e "Refinement" no Azure DevOps foram marcados com uma tag `Refinamento: Pronto` / `Refinamento: Quase Pronto` / `Refinamento: Precisa Refinar` refletindo o status do board.
