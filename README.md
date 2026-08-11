# BMAD — Workspace de PO (Grupo Avenida / Var Retaguarda)

Workspace pessoal de trabalho como PO: skills do Claude Code e artefatos de planejamento gerados ao longo do refinamento dos cards do projeto **Var Retaguarda** no Azure DevOps.

## O que está neste repositório

- **`.claude/skills/`** — 21 skills instaladas para uso como PO (vindas de [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)):
  `agile-product-owner`, `apple-hig-expert`, `code-to-prd`, `competitive-teardown`, `experiment-designer`,
  `landing-page-generator`, `process-mapper`, `product-analytics`, `product-discovery`, `product-manager-toolkit`,
  `product-skills`, `product-strategist`, `research-summarizer`, `roadmap-communicator`, `saas-scaffolder`,
  `scrum-master`, `senior-architect`, `senior-pm`, `spec-to-repo`, `ui-design-system`, `ux-researcher-designer`.
- **`_bmad-output/planning-artifacts/`** — backups de versões originais de cards e o ADR-1 (decisão de arquitetura do Motor de Descontos) produzidos durante o refinamento do card #12405 e outros.

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

Este workspace nasceu de um processo de refinamento de cards "Ready for Dev" e "Refinement" no board do Azure DevOps (projeto **Var Retaguarda**), usando primeiro o framework BMAD-METHOD e depois migrando para skills avulsas do `claude-skills` (INVEST, Definition of Done, formato Cenário + Dado/Quando/Então). O BMAD-METHOD em si foi removido deste workspace — só os artefatos de trabalho (`_bmad-output/`) ficaram.
