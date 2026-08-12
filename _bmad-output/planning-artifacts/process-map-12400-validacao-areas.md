# Process Map: Validação de Negócio com as Áreas (US13 · card #12400)

> Gerado com a skill `process-mapper` (método determinístico: `process_documenter.py` → `cycle_time_analyzer.py` → `bottleneck_detector.py`). Python não está instalado nesta máquina, então os três scripts foram computados manualmente seguindo exatamente as fórmulas do código-fonte (não são achismo) — se instalarem Python depois, `scripts/*.py --input us13-validacao-areas.json --profile services` reproduz os mesmos números.

**Fonte dos dados:** durações estimadas (não medidas) — primeira passada, conforme a própria skill recomenda para quem ainda não instrumentou o processo. Substituir por dados reais assim que houver histórico de 2-3 ciclos completos.

## Metadados do processo

- **Processo:** Validação de Negócio com as Áreas (US13)
- **Dono:** PO (Igor)
- **Frequência:** sob demanda, uma vez por área (Financeiro, Contábil, RH, Diretoria — roda 4x)
- **Gatilho:** US12 concluída (homologação técnica aprovada)
- **Estado final:** aceite formal registrado + treinamento/onboarding concluído por área
- **WIP:** 4 (as 4 áreas podem estar em estágios diferentes ao mesmo tempo)

## Estágios

| # | Estágio | Dono | Tipo | P50 | P90 |
|---|---------|------|------|-----|-----|
| 1 | Apresentar ao responsável da área | PO | value-add | 30 min | 45 min |
| 2 | Aguardar aprovação do responsável pra agendar | Responsável da área | **wait** | 1440 min (1 dia) | 4320 min (3 dias) |
| 3 | Agendar sessão de validação com a área | PO | **wait** | 1440 min (1 dia) | 2880 min (2 dias) |
| 4 | Sessão de validação (área revisa telas/arquivos) | Área | value-add | 60 min | 90 min |
| 5 | Coletar e priorizar feedback | PO | value-add | 60 min | 120 min |
| 6 | Implementar ajustes | Dev | value-add | 480 min (1 dia) | 1440 min (3 dias) |
| 7 | Reapresentar à área após ajustes | PO | **rework** | 45 min | 60 min |
| 8 | Registrar aceite formal | Área | value-add | 30 min | 60 min |
| 9 | Treinamento (Admins 1h) + onboarding (Contábil/RH 1 semana) | Área | value-add | 90 min | 10080 min (1 semana) |

**Swim lanes (por dono):**
- **PO** → #1 Apresentar → #3 Agendar → #5 Coletar feedback → #7 Reapresentar
- **Responsável da área** → #2 Aguardar aprovação ⚠️ *(estamos aqui hoje — apresentação às 15:30)*
- **Área** → #4 Sessão de validação → #8 Aceite formal → #9 Treinamento/onboarding
- **Dev** → #6 Implementar ajustes

## Análise de cycle time (perfil `services`)

| Métrica | Valor |
|---|---|
| Nº de estágios | 9 |
| Total P50 | 3675.0 min (~61h / ~2,6 dias corridos de fila+trabalho) |
| Total P90 | 19095.0 min (~318h / ~13,3 dias) |
| Minutos value-add (P50) | 750.0 |
| Minutos wait (P50) | 2880.0 |
| Minutos rework (P50) | 45.0 |
| **Value-add ratio (VA%)** | **20,4%** |
| Wait ratio | 78,4% |
| Rework ratio | 1,2% |
| **Veredito** | **HEALTHY** (bem no limite — perfil `services` exige ≥20%) |
| WIP | 4 |
| Throughput (Lei de Little) | 0,065 itens/hora (~1 área concluída a cada ~15h de capacidade dedicada) |

**Nota automática do modelo:** mais da metade do ciclo é tempo de espera → o throughput melhora mais removendo fila do que acelerando as etapas de valor.

## Bottlenecks detectados (perfil `services`)

**1. [CRITICAL] Estágio lento: Aguardar aprovação do responsável pra agendar**
- Regra: R1 — P50 de 1440 min vs. média das etapas value-add de 125 min (11,5x)
- Hipótese: aprovação em lote, aprovador único, ou critério de aceite não claro pro responsável decidir rápido
- Ação recomendada: decompor a etapa — dá pra paralelizar ou tornar condicional? Se é fila, aplicar limite de WIP ou remover o handoff

**2. [CRITICAL] Estágio lento: Agendar sessão de validação com a área**
- Regra: R1 — P50 de 1440 min vs. média de 125 min (11,5x)
- Mesma hipótese/ação do item 1 — este é o segundo maior ofensor

**3. [HIGH] Processo dominado por tempo de espera**
- Regra: R2 — etapas de espera são 78% do ciclo total, vs. 50% do limite do perfil `services`
- Hipótese: handoffs enfileiram trabalho atrás de um único papel/lote — por Teoria das Restrições, o throughput do sistema é definido pela fila mais longa, não pela velocidade das etapas
- Ação recomendada: identificar a fila mais longa (aqui, é a aprovação do responsável — item 1), puxá-la pra frente, eliminar via self-service, ou aplicar limite de WIP a montante

**4. [MEDIUM] Estágio lento: Implementar ajustes**
- Regra: R1 — P50 de 480 min vs. média de 125 min (3,8x)
- Hipótese/ação: mesma linha do R1, severidade menor

## Leitura pra apresentação de hoje (15:30)

O gargalo real do processo **não são as sessões de validação em si** (só 20% do ciclo é trabalho de valor) — **é a fila de aprovação/agendamento** (78% do ciclo, os dois achados CRITICAL). Isso é argumento pra pedir, na apresentação de hoje, uma decisão rápida do responsável (a etapa #2 é exatamente onde estamos agora) em vez de deixar entrar na fila padrão de agendamento — cada dia de atraso aqui atrasa o ciclo inteiro proporcionalmente, já que é o maior componente do tempo total.
