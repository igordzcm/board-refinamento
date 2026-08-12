# board-refinamento

Workspace pessoal de trabalho como PO no projeto **Var Retaguarda** (Azure DevOps, Grupo Avenida): skills do Claude Code, board de refinamento de cards e artefatos de planejamento produzidos ao longo do processo.

## Documentação

- **[`docs/processo-de-refinamento.md`](docs/processo-de-refinamento.md)** — guia do checklist e do passo a passo usado pra refinar cards: formato de história e AC, INVEST, Definition of Done, quando investigar código, quando usar fluxograma, e a lista de skills.

## Boards

- **[`boards/board-refinamento.html`](boards/board-refinamento.html)** — board estilo Trello com os 25 cards de "Ready for Dev" + "Refinement" do Var Retaguarda, agrupados por status de prontidão (Precisa refinar / Quase pronto / 100% pronto) contra um checklist de refinamento: formato Cenário + Dado/Quando/Então, rótulo de nível de verificação (backend, UI, revisão), estimativa preenchida e ausência de bloqueio real. Clique num card pra abrir o detalhe do que falta. Também publicado como [Artifact](https://claude.ai/code/artifact/ced8aba8-8054-44d2-a8f9-a4b410264a96).
- **[`boards/breakdown-ready-for-dev.html`](boards/breakdown-ready-for-dev.html)** — dashboard anterior com a lista de trabalho por card e o veredito de necessidade de fluxograma (técnico via `senior-architect` ou de processo via `process-mapper`) para cada um.

Abra qualquer um dos dois arquivos direto no navegador — são HTML autocontidos, sem dependência externa.

## Skills (`.claude/skills/`)

21 skills selecionadas para uso como PO, vindas de [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills):

`agile-product-owner`, `apple-hig-expert`, `code-to-prd`, `competitive-teardown`, `experiment-designer`,
`landing-page-generator`, `process-mapper`, `product-analytics`, `product-discovery`, `product-manager-toolkit`,
`product-skills`, `product-strategist`, `research-summarizer`, `roadmap-communicator`, `saas-scaffolder`,
`scrum-master`, `senior-architect`, `senior-pm`, `spec-to-repo`, `ui-design-system`, `ux-researcher-designer`.

## Planejamento (`_bmad-output/planning-artifacts/`)

Backups de versões originais de cards e o ADR-1 (decisão de arquitetura do redesenho do Motor de Descontos) produzidos durante o refinamento do card #12405 e outros.

## Referências (`referencias/`)

Material bruto recebido de terceiros (planos técnicos, protótipos navegáveis, specs) usado como insumo pra refinar um card — diferente de `_bmad-output/planning-artifacts/`, que guarda o que *o Claude produz* durante o refinamento. Nomeado `<card-id>-<slug>.html`. Quando cair um arquivo novo desses na raiz do workspace, ele é movido pra cá.

## O que NÃO está aqui (e como restaurar numa máquina nova)

Estas pastas ficam de fora (`.gitignore`) porque são código-fonte de terceiros ou da empresa, cada uma já com seu próprio repositório remoto. Depois de clonar este repositório, rode:

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
