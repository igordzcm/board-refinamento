# Motor de Descontos — contexto geral

> Arquivo de contexto do projeto. Atualizado a partir de pendências levantadas em reunião, das user stories técnicas e do dashboard executivo. Ler antes de qualquer reunião sobre este projeto.

## O que é

Motor de campanhas de desconto/combo por loja (Portal Nova Retaguarda), com cadastro de campanhas, validação de conflito de item entre campanhas, e-mails de criação/vigência e comparativo retaguarda x loja.

Épico: **[#6669 — Motor de Descontos](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/6669)** (Var Retaguarda). 2 itens ativos em Sprint23-26.

## Dono / stakeholders

Dev: **Kauã**. Stakeholder de negócio: **Arthur**. Ponto adicional levantado por **Taunay** (interface de destinatários de e-mail) e por **Igor** (comparativo retaguarda x loja).

## Status atual (via dashboard executivo)

A maior parte do escopo priorizado foi **entregue em 22/06/2026 sob responsabilidade do Kauã** — inclui edição de lojas em campanha ativa, resolução de conflito de item no modal, correção do bug de listagem (1 linha por campanha), filtro por regional/estado, melhorias no e-mail de criação e prorrogação de data (esta última seguiu para HML aguardando validação QA no momento do levantamento original).

## O que falta — Fase 2/3 (escopo a refinar)

**US5 — Notificação automática por e-mail para as lojas na entrada em vigência da campanha.** Disparo automático quando a campanha entra em vigor, com hierarquia de produtos no corpo do e-mail (para poucos itens) ou CSV/link (para campanhas grandes), log de envio com retry. **Bloqueio explícito no próprio documento fonte: escopo ainda a ser refinado em call entre Igor e Arthur** — falta sobretudo definir os destinatários por loja (gerente, e-mail de filial etc.).

Demais itens de backlog futuro (baixa prioridade, sem urgência confirmada por Arthur): combo entre departamentos inteiros, filtro por família na listagem de campanhas, relatórios de performance de campanhas, histórico consolidado com "duplicar campanha".

## Bloqueios e pendências

- **US5 (notificação às lojas)**: escopo pendente de alinhamento Igor + Arthur — não iniciar desenvolvimento antes dessa call.
- Destinatários do e-mail de criação de campanha (uso interno) — Arthur ainda precisa definir e passar a lista final (provisoriamente Igor + Arthur).
- Interface de gerenciamento de destinatários no portal (evitar depender de deploy para alterar a lista) — pedido de Taunay, sem prioridade confirmada.

## Atividade recente (11–13/08/2026, via dailies)

- **Leonardo (Retaguarda)** começou em 12/08 a **configurar e desenhar a arquitetura da sincronização nas lojas** (propagação de campanhas — a mesma frente descrita no card #12405, "gravação direta de campanhas no banco Retaguarda", cuja propagação pra loja passa a ser de outra equipe). Seguiu nisso em 13/08. Ver [`../dailies/2026-08-12-retaguarda.md`](../dailies/2026-08-12-retaguarda.md) e [`../dailies/2026-08-13-retaguarda.md`](../dailies/2026-08-13-retaguarda.md).
- **Time VAR 3.0** (squad diferente, ver [`../dailies/2026-08-11-var3-projsust.md`](../dailies/2026-08-11-var3-projsust.md) e [`../dailies/2026-08-12-var3-projsust.md`](../dailies/2026-08-12-var3-projsust.md)) está rodando, em paralelo, testes de integração da "rotina de desconto" pelo lado loja/PDV (Guilherme Caixeta) — caminho feliz passando, "primeira compra" é o cenário mais complicado, **nenhum gap de cenário identificado na história até 12/08**. É a contraparte de teste do lado loja pro que o Leonardo está desenhando do lado Retaguarda — vale cruzar antes de fechar o desenho de sincronização.

## Reuniões

Nenhuma reunião registrada ainda.

## Próxima atualização

Preencher aqui depois da call entre Igor e Arthur sobre o escopo da US5 (notificação às lojas): quais destinatários por loja, se entra como Fase 2 ou Fase 3, e se algum item do backlog futuro (combo entre departamentos, relatórios de performance) ganhou prioridade.
