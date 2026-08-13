# Automação Planilha Fiscal — contexto geral

> Arquivo de contexto do projeto. Atualizado a partir da análise técnica original, do fluxo detalhado de cálculos e do padrão de bugs reportados. Ler antes de qualquer reunião sobre este projeto.

## O que é

Funcionalidade no Portal da Retaguarda que automatiza o fechamento fiscal mensal: o analista seleciona lojas + mês/ano e recebe uma planilha `.xlsx` pronta com 4 abas (Conferência GFT, MODELO X CFOP X CST, DINÂMICA VS LIVRO, VAR), eliminando o processo manual de exportar GFT e VAR, colar em Excel e montar fórmulas/dinâmicas na mão. Inclui gate de liberação de mês pelo TI (`controle_meses_fiscais`) e cruzamento GFT x VAR por chave de acesso (44 caracteres) com cálculo de NOVA BASE ICMS, NOVO ICMS e DIFERENÇA (arredondamento `ROUND_HALF_UP` obrigatório — regra fiscal, diferente do padrão Python).

Épico: **[#11103 — Automação Planilha Fiscal](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11103)** (Var Retaguarda). 9 itens em Sprint23-26, **todos Done**.

## Dono

Entregue em **22/06/2026 sob responsabilidade do Kauã**. Via daily de 06/08: **Kovalski** está assumindo a reorganização do projeto após fechar o SSO — "mexer na automação Fiscal só pra ver o que tem ali que precisa ser feito, que precisa ser organizado já pra gente destravar as homologações". Até então, sem responsável fixo — a Retaguarda absorvia bugs à medida que apareciam (ver Sprint 23 sem responsável).

## Status atual

Funcionalidade **entregue e em uso**, mas gera bugs e retrabalho recorrentes desde o lançamento — não é mais projeto de desenvolvimento inicial, é sustentação ativa de um recurso já em produção.

## Padrão de bugs recorrentes (via histórias de bug e board de sustentação)

- **Loja marcada como "Pendente" mesmo após extração concluída** — o sistema notifica (tela + e-mail) que a extração terminou, mas o mês correspondente não reflete isso e a loja continua "Pendente", como se a extração nunca tivesse ocorrido. Divergência entre o que o sistema informa e o que é de fato persistido/exibido.
- **Campo Isentas/Não Tributadas ausente** — falta esse campo na seção de soma da nova base de cálculo (bug aberto, referência a prints anexados no card original).
- **"Loja 01 não está batendo" / "Loja 13 não bate"** — divergências recorrentes entre os dados do sistema e a referência dos analistas, tratadas como Technical Enabler de investigação (não como bug único) — cada ocorrência exige nova investigação de causa raiz.
- Outros temas do mesmo board de sustentação: notas sem match no GFT, cupons com diferença na aba VAR, notas canceladas sem chave de acesso na integração, erro no download do Excel, filtro de "situação do documento" para trazer só documentos autorizados.

## Pontos técnicos de risco conhecidos (da análise técnica original)

- Mapeamento de colunas do GFT (posições Excel AH/AK/Y/Z etc.) para os nomes reais de campo no banco — apontado como o maior risco de erro na implementação original.
- Arredondamento: `ROUND_HALF_UP` é obrigatório para bater com o Excel/fiscal; o padrão do Python (`ROUND_HALF_EVEN`) gera diferenças reais de centavos — já validado com casos reais na amostragem original.
- Notas com chave de acesso presente em um sistema (GFT ou VAR) e ausente no outro — comportamento esperado (zero, vazio ou `#N/D`) precisa estar alinhado com o time fiscal.

## Triagem de backlog em andamento (12/08, reunião de planejamento de sprint)

> Fonte: [`../dailies/2026-08-12-planejamento-sprint.md`](../dailies/2026-08-12-planejamento-sprint.md).

Ozéias está revisando ao vivo a lista de ~40 cards que o **Kovalski** mandou criar pro backlog de Automação Fiscal (provider service da GNRE, repositório, migrations, modelagem de tabela de UF, correção de caracteres UTF-8 no portal, etc.) — boa parte sem contexto claro nem para o próprio Ozéias ("não sei nem o que é a maioria"). Decisão combinada: **descartar tudo que não fizer mais sentido**, e mover pra coluna **Refinement** tudo que ainda vale a pena trabalhar, pra separar do que é lixo de backlog antigo.

**Prazo combinado:** Ozéias revisa a lista completa até **sexta-feira** (14/08) e confirma com Kovalski/Kauã/Léo o que segue válido em "Automação de Fluxo Fiscal".

## Reuniões

- [`../dailies/2026-08-12-planejamento-sprint.md`](../dailies/2026-08-12-planejamento-sprint.md) — reunião de planejamento de sprint (transversal) onde a triagem do backlog começou.

## Próxima atualização

Preencher aqui: (1) se a triagem de Ozéias (prazo 14/08) terminou e quantos cards sobreviveram vs. foram descartados; (2) quando houver uma rodada de triagem dos bugs recorrentes (Pendente/isentas/Loja 01-13) com o time fiscal — se algum padrão comum foi identificado na causa raiz (ex.: mapeamento de coluna incorreto) e se o projeto volta a ter responsável fixo.
