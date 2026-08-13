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

## O que já foi entregue (épico #10810)

| Card | O que é | Status |
|---|---|---|
| [#10811](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/10811) | Coletar e tratar dados do WMS | Done |
| [#10812](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/10812) | Coletar e tratar dados de BI | Done |
| [#10813](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/10813) | Validar dados do Excel | Done |
| [#10814](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/10814) | Criação do Dashboard | Done (com histórico de QA — ver abaixo) |
| [#11370](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11370) | POC IA — CDS | Done |
| [#11973](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11973) | Trocar PowerAutomate por FTP | **To do** — pode ser descartado, ver acima |

## Bloqueios e pendências

- **Dependência de dados "certinhos" pro cron job** — João Neto (06/04/2026): *"Falta os dados do WMS e BI certinho para fazer o cron job rodar corretamente. Assim que tiver o depara do BI pronto."* Como o WMS não mudou, essa dependência **segue de pé**; não foi endereçada na reunião de 12/08.
- **#11973 sem definição técnica, e sem decisão sobre necessidade** — QA (Danilo) já apontou duas vezes que falta host/protocolo/credenciais/formato do FTP. A reunião de 12/08 não resolveu se o card ainda é necessário — fica pendente de uma conversa específica sobre esse ponto (não rolou espaço na pauta, que virou toda sobre paridade de planilha).
- **#10814 — pendência de QA menor**: formatação de data após atualização (não trava, mas não confirmado como corrigido).
- **Planilha atualizada ainda não recebida** — Maria disse que ia enviar no grupo em 12/08; confirmar se chegou antes de começar a replicar as mudanças.

## Reuniões

- [reuniao-maria-2026-08-12.md](reuniao-maria-2026-08-12.md) — realizada em 12/08. Maria confirmou que não trocou de fonte/não parou de usar WMS; levantou 8 mudanças de planilha a replicar e 4 pedidos de melhoria novos. Transcrição completa: [transcricao-reuniao-maria-2026-08-12.md](transcricao-reuniao-maria-2026-08-12.md).

## Próxima atualização

Preencher aqui quando: (1) a planilha atualizada da Maria chegar no grupo, (2) as 8 mudanças de paridade forem replicadas no sistema, (3) alguém decidir com a Maria/JB se o #11973 (FTP) ainda é necessário — ponto que ficou pendente após a reunião de 12/08.
