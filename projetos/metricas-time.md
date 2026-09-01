# Métricas do time

> Métricas operacionais do time (lead time, throughput etc.), calculadas sob demanda a partir do Azure DevOps. Não é status de projeto — isso fica nos `contexto.md` e no [README.md](README.md).

## Lead time médio de entrega

> ⚠️ **Definição mudou em 01/09/2026.** A partir desta data, lead time = **primeira transição pra `Doing` → primeira transição pra `Accepted`** (histórico de revisão do work item), não mais `ClosedDate − CreatedDate`. Motivo: a definição antiga contava tempo que o card passou parado no backlog antes de alguém pegar pra trabalhar, o que não é lead time de entrega de verdade. **O cálculo abaixo (31/08) usa a definição antiga e não é comparável a recálculos futuros** — mantido aqui só como registro histórico.

### Cálculo de 31/08/2026 (definição antiga — Created→Closed, não usar como comparação)

A partir de todos os itens do projeto "Var Retaguarda" com estado Done/Closed/Accepted/Verified e `Microsoft.VSTS.Common.ClosedDate` desde **01/08/2026** (122 itens). Lead time = `ClosedDate − CreatedDate`, em dias corridos.

| Métrica | Valor |
|---|---|
| Itens analisados | 122 |
| Média bruta | 29,4 dias |
| Mediana bruta | 11,6 dias |
| Média excluindo outliers (>60 dias) | **22,5 dias** |
| Mediana excluindo outliers | 10,3 dias |

**Por tipo de work item:**

| Tipo | Qtd | Média |
|---|---|---|
| Task | 66 | 8,2 dias |
| Product Backlog Item (história) | 39 | 59,1 dias |
| Bug | 8 | 35,8 dias |
| Nonfunctional Item | 5 | 55,9 dias |
| Technical Enabler | 4 | 43,2 dias |

**Outliers (>60 dias) — backlog antigo fechado em lote, não trabalho recente:**

| ID | Tipo | Lead time | Título |
|---|---|---|---|
| [#8311](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/8311) | PBI | 469,2 dias | Relatório sem operador (compromisso/filial) |
| [#10624](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/10624) | PBI | 192,8 dias | Keycloak not public |
| [#11568](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11568) | PBI | 90,0 dias | Backoffice - Configuração de Campanhas Chute ao Gol |
| [#11847](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11847) | PBI | 75,0 dias | [GESTÃO DE CAMPANHAS] Teste Regressivo (Roleta e Chutou Ganhou) |
| [#11854](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11854) | PBI | 74,8 dias | Configuração da Máquina de Vinhedo p/ Keycloak Not Public |
| [#11833](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11833) | Bug | 70,9 dias | [BUG] Corrigir upload, download e vínculo de anexos — Termo Assinado |

## ⚠️ Ressalva de qualidade do dado — importante ao reusar este número

Boa parte das `ClosedDate` está concentrada em **rajadas** — dezenas de itens fechados em segundos de diferença nos dias 05/08, 11/08 e 20-21/08. Isso tem cara de **fechamento em lote/retroativo** (alguém passando vários cards de uma vez pro estado final), não de conclusão item a item no momento real. Ou seja: **o número é uma aproximação razoável de ordem de grandeza, não uma métrica de precisão de engenharia** — não usar pra comparar sprints ou avaliar performance individual sem antes confirmar se o time está fechando cards no dia real da entrega.

## Como recalcular (definição atual — Doing → Accepted)

WIQL no projeto "Var Retaguarda" pra achar candidatos (itens que já passaram por Accepted em algum momento):
```
SELECT [System.Id], [System.Title], [System.WorkItemType], [System.State]
FROM WorkItems
WHERE [System.TeamProject] = 'Var Retaguarda'
AND [System.State] IN ('Accepted','Verified','Done','Closed')
AND [System.ChangedDate] >= '<data de corte>'
```
Depois, **por item** (não tem endpoint em lote pra histórico de revisão): `wit_work_item` `list_revisions`, achar a primeira revisão em que `System.State` vira `Doing` (início) e a primeira em que vira `Accepted` (fim), usar `System.ChangedDate` de cada uma. Isso é o que o agente `portfolio-report` (modo Métricas) já faz automaticamente.

## Próxima atualização

Recalcular periodicamente (sugestão: mensal) pra ter uma série histórica de verdade, em vez de um ponto isolado — agora comparável de fato, já que a definição não muda mais entre rodadas. Vale rodar uma vez logo já com a definição nova pra ter o primeiro ponto real da série.
