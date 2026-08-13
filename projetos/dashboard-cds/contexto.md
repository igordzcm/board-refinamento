# Dashboard CDS — contexto geral

> Arquivo de contexto do projeto. Atualizado a partir de dailies, reuniões e do dashboard executivo. Ler antes de qualquer reunião sobre este projeto.

## O que é

Dashboard consolidando dados de **WMS** e **BI** dos Centros de Distribuição (CDs) no Portal da Retaguarda — visão unificada pra monitorar operações e tomar decisão com dado.

Épico: **[#10810 — Dashboard CD](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/10810)** (Var Retaguarda), status **Doing**.

## Dono

**JB (João Bernardo Ferreira Neto)** — depois de fechar a Migração VARRet (lote 2), volta pra esse projeto.

## Status atual (12/08/2026, via reunião com a Maria)

Reunião com a Maria (área de operação) realizada em 12/08 — ver `reuniao-maria-2026-08-12.md`. Principal descoberta: **a premissa que motivou a reunião não se confirmou.** Maria não trocou de fonte de dados nem parou de usar o WMS — o time dela identificou e contornou o problema original sem precisar migrar. Ou seja, **isso por si só não elimina a necessidade do FTP** (#11973); a questão do card segue em aberto porque **não foi discutida nesta rodada** (o foco foi 100% nas mudanças de cálculo/gráfico que a Maria já fez na planilha dela).

**Prioridade combinada com JB:** primeiro replicar no sistema as 8 mudanças que a Maria já fez na planilha (data de referência, tabela de lojas, gráfico novo, base de rotas unificada, PROCV de peças, fórmula de lead time ponderada, relatório WMS com data nova) — só depois entrar nos pedidos de melhoria novos (filtro, "último carregamento", "média da rota", números sempre visíveis). Detalhe completo em `reuniao-maria-2026-08-12.md`.

Confirmado também (reunião de planejamento de sprint, 12/08, `../dailies/2026-08-12-planejamento-sprint.md`): JB está fechando a Migração VARRet lote 2 (em code review/QA) antes de voltar full-time pro Dashboard CDs; "umas coisinhas" do Dashboard CDs já entraram na lista de correções dele, mas "nada tão absurdo".

**Cards criados em 13/08/2026** (ver tabela completa em `reuniao-maria-2026-08-12.md`): #12509 (data/tabela/gráfico Top 20), #12510 (peças via PROCV), #12511 (fórmula lead time), #12512 (relatório WMS, atribuído ao Igor), #12513 (melhorias pós-paridade, agrupadas). Todos em Refinement/Sprint 27, ainda pendentes da planilha atualizada da Maria pra fechar o refino.

## Código-fonte: onde o Dashboard CDs realmente vive

**Achado em 13/08/2026:** o backend do Dashboard CDs **não** fica nos repos do Portal Retaguarda (ConciliaçãoCaixaAPI/Front) — fica no repo **`rpa-service`**, projeto Azure DevOps **"Automação Dados Cartões"**, módulo `modules/cds/cds/`. Clonado localmente na raiz do workspace (ver README.md). Principais arquivos pra referência técnica em cards futuros:

| Área | Arquivo |
|---|---|
| Overview/KPIs gerais | `services/dashboard/overview_service.py`, `services/dashboard/kpi_service.py` |
| Lead time por rota | `services/dashboard/lead_time_service.py` |
| Lojas em destaque / Top N | `services/dashboard/featured_stores_service.py` |
| Cross-CD (Alagoas/Campo Grande) | `services/dashboard/cross_cd_service.py`, `strategies/cd80_strategy.py`, `strategies/cd83_strategy.py`, `strategies/registry.py` |
| ETL / ingestão WMS | `services/etl/extraction_service.py`, `services/etl/wms_csv_source.py`, `services/etl/wms_ftp_source.py`, `services/etl/mappers.py`, `services/etl/queries.py` |
| Workers | `workers/wms_refresh_worker.py`, `workers/etl_refresh_worker.py` |

**Achados que já foram incorporados nos cards (comentário + nota técnica em cada um):**
- **#12511** (fórmula lead time): bug confirmado em dois arquivos (`overview_service.py` e `kpi_service.py`), ambos com comentário no código citando a fórmula antiga do Excel — a correção é quase copy-paste do padrão já usado pra `pct_disponivel` nos mesmos arquivos.
- **#12510** (peças via PROCV): o lookup `ITEM → PECAS_PACK` já existe (`extraction_service.py`, tabela `CD_ITEM_PACK`) com fallback automático pra item sem pack conhecido — o Cenário 2 (que eu tinha deixado como pendência) já está coberto no código.
- **#12509** (Top 20 + rotas unificadas): `FeaturedStoresService`/`LeadTimeService` já existem mas precisam de ajuste de ordenação; `CrossCdService`/`strategies` já modelam rotas compartilhadas entre CDs — provável ponto de extensão.
- **#11973** (FTP vs PowerAutomate) — **não é um dos 5 cards novos, mas foi atualizado também**: o FTP **já está implementado e testado** (`wms_ftp_source.py`), atrás da flag `CDS_WMS_FTP_ENABLED` (default off). Falta só configurar host/porta/usuário/senha do ambiente, criar um job periódico, e decidir quando desligar o PowerAutomate — isso destrava a pendência que estava em aberto desde a reunião de 12/08 sobre se o card ainda fazia sentido.

## O que já foi entregue (épico #10810)

| Card | O que é | Status |
|---|---|---|
| [#10811](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/10811) | Coletar e tratar dados do WMS | Done |
| [#10812](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/10812) | Coletar e tratar dados de BI | Done |
| [#10813](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/10813) | Validar dados do Excel | Done |
| [#10814](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/10814) | Criação do Dashboard | Done (com histórico de QA — ver abaixo) |
| [#11370](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11370) | POC IA — CDS | Done |
| [#11973](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11973) | Trocar PowerAutomate por FTP | **To do** — pode ser descartado, ver acima |
| [#12509](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12509) | Data de referência, tabela de lojas e gráfico "Top 20 lojas + lead time" | **Refinement** — pendente da planilha da Maria |
| [#12510](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12510) | Corrigir cálculo de peças via PROCV | **Refinement** — pendente da planilha da Maria |
| [#12511](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12511) | Corrigir fórmula do lead time médio | **Refinement** — pendente da planilha da Maria |
| [#12512](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12512) | Atualizar relatório do WMS com nova data | **Refinement** — atribuído ao Igor (PO) |
| [#12513](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12513) | Melhorias pós-paridade | **Refinement** — bloqueado por esboço da Maria |

## Bloqueios e pendências

- **Dependência de dados "certinhos" pro cron job** — João Neto (06/04/2026): *"Falta os dados do WMS e BI certinho para fazer o cron job rodar corretamente. Assim que tiver o depara do BI pronto."* Como o WMS não mudou, essa dependência **segue de pé**; não foi endereçada na reunião de 12/08.
- **#11973 sem definição técnica, e sem decisão sobre necessidade** — QA (Danilo) já apontou duas vezes que falta host/protocolo/credenciais/formato do FTP. A reunião de 12/08 não resolveu se o card ainda é necessário — fica pendente de uma conversa específica sobre esse ponto (não rolou espaço na pauta, que virou toda sobre paridade de planilha).
- **#10814 — pendência de QA menor**: formatação de data após atualização (não trava, mas não confirmado como corrigido).
- **Planilha atualizada ainda não recebida** — status 13/08 (via [`../dailies/2026-08-13-retaguarda.md`](../dailies/2026-08-13-retaguarda.md)): Maria respondeu ao Igor hoje de manhã que **ainda não enviou** — está esperando alguém da área dela responder com informações antes de mandar. Igor segue acompanhando com ela diretamente.

## Reuniões

- [reuniao-maria-2026-08-12.md](reuniao-maria-2026-08-12.md) — realizada em 12/08. Maria confirmou que não trocou de fonte/não parou de usar WMS; levantou 8 mudanças de planilha a replicar e 4 pedidos de melhoria novos. Transcrição completa: [transcricao-reuniao-maria-2026-08-12.md](transcricao-reuniao-maria-2026-08-12.md).

## Próxima atualização

Preencher aqui quando: (1) a planilha atualizada da Maria chegar no grupo (destrava o refino final de #12509-#12511), (2) o esboço/protótipo da Maria chegar (destrava #12513), (3) o Igor alinhar com o Sergio da Silva (destrava #12512), (4) alguém decidir com a Maria/JB se o #11973 (FTP) ainda é necessário — ponto que ficou pendente após a reunião de 12/08.
