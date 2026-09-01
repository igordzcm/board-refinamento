# Planning VAR 3.0 (18/08/2026)

> Planning quinzenal do squad VAR 3.0. Transcrição bruta em `2026-08-18-planning-var.docx`. Participantes: Filipe de Lacerda Grangeiro (lead), Gustavo Do Estreito Deliberali, Guilherme Oliveira de Souza, Guilherme Caixeta Rodrigues, Felipe Pinheiro Santos, Wanderleia Candida da Cruz Santos, Nicolas Timoteu Cuerbas, Moises de Oliveira Santos Junior, Jeferson de Oliveira Guimarães, Wesley Silva Alves.

## Novo escopo — Desconto de Gerente (pedido da área de negócio)

Hoje o desconto de gerente é calculado **diariamente por quantidade**: venda histórica do mesmo dia no ano anterior ÷ 0,25 = quantidade de descontos disponíveis pra loja hoje. Área de negócio reportou que lojas de venda alta chegam a 8-10 descontos/dia — não é abuso, é o próprio cálculo permitindo demais.

**Mudança solicitada:** substituir por um **limite mensal em valor (R$)**, com possibilidade de também ter um limite diário combinado com o teto mensal. Atribuído a **Guilherme Caixeta Rodrigues**, que já estava em bugs de desconto e queria algo mais direto.

## GeneXus → Java — falta o Epic

Filipe identificou que a migração completa do GeneXus pro VAR 3.0 (Java) não tem Epic no board — é grande demais pra ser só uma tarefa. Walter já tem o mapeamento do que precisa ser feito (estava ocupado terminando o 4G antes). Gustavo pediu o mapeamento do Filipe pra abrir as tarefas granulares.

Trabalho de descoberta já em andamento com Moises e Jeferson (documentação de endpoints), mais Kovalski auxiliando com arquitetura/documentação quando sobra tempo do SIGA.

## Automação de testes — divisão do trabalho

- **Caixeta**: testes fiscal (desktop) praticamente prontos, vai replicar pro mobile.
- **Moises + Jeferson**: ainda em fase de descoberta/estudo dos endpoints da migração — não começaram a escrever testes ainda.
- Pendência de administração: tarefas de teste automatizado precisam ser marcadas "Done" quando passarem (senão carregam de sprint em sprint), e o épico das tarefas de "rotina fiscal"/"desconto" precisa trocar de "melhoria" pra "automação de testes".
- Acesso automatizado do mobile: ainda não revisado.

## Visão SAC — novo endpoint

Tela "Visão SAC" (consulta cartão do cliente) vai ganhar novos campos: valor de fatura atual, valor de fatura a vencer, parcelas futuras — reaproveitando endpoints existentes de consulta de fatura, mas **renomeando o endpoint** pra essa tela específica, pra não confundir análise de logs entre telas diferentes que reusam o mesmo endpoint.

## Limpeza administrativa do board

- Bug "erro de troca de para" marcado erroneamente como resolvido numa release antiga — corrigido sprint (Sprint 65) e movido pro board certo.

## Fontes

Ver também os digests diários 14–24/08 em `2026-08-14-a-24-digest-var3.md`.
