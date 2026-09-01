# Ata — Alinhamento interno pós-reunião com a área (RH/Financeiro)

## Dados da reunião

- **Data/hora:** 26/08/2026, ~14:42 (16m25s)
- **Participantes:** Ozéias Denis de A. Tavares, Diego Oliveira Andrade Rafael, Danilo Santos Manzoli, Igor Diniz Camargo (PO)
- **Objetivo:** traduzir o feedback da reunião com a área (25/08, ver [reuniao-area-rh-financeiro-2026-08-25.md](reuniao-area-rh-financeiro-2026-08-25.md)) em correções concretas, formalizadas em cards.
- **Fonte:** transcrição completa em [alinhamento-interno-2026-08-26.docx](alinhamento-interno-2026-08-26.docx)

## Correções confirmadas (recapituladas pelo Ozéias como "as principais")

1. **Parcela única = aprovado automaticamente**, sem passar pela fila do RH — só entra na fila quando for parcelado.
2. **Regra de quebra de caixa** — bater na lista de lojas que não têm quebra de caixa; se não tiver, mandar o CPF do gerente (buscar em alguma tabela do Logix), não do operador.
3. **Momento e data do envio ao RH** — só enviar quando a **conciliação for fechada** (não na aprovação da perda), com a **data do fechamento**. Exemplo usado na reunião: diferença dia 10, aprovação dia 12, fechamento dia 13 → manda com data 13. Danilo perguntou se isso significa que a conciliação fechada fica bloqueada pra edição — Ozéias confirmou que sim, sem reabertura automatizada nesta fase.

## Item lembrado à parte (esqueceram de falar com o Spin na reunião de 25/08)

4. **Deixar puxar o mês/ciclo atual pra gerar prévias** — o Gilson processa a folha a partir do dia 20, mas o fechamento formal pode não bater com esse prazo. Sistema precisa permitir prévia do ciclo ainda aberto, sem duplicar quando o export oficial (carimbado) rodar depois.

## Último item (mais simples, segundo o Ozéias)

5. **Layout da planilha pro Contábil** — mudar pro formato de importação do Oracle. Ozéias não sabe o layout exato, vai levantar.

## Cards criados (26/08, por Igor)

| # | Título | Estimativa PO |
|---|---|---|
| [#12808](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12808) | Desconto em folha em parcela única deve ser aprovado automaticamente | 3 pts |
| [#12809](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12809) | Usar CPF do gerente em lojas sem quebra de caixa | sem estimativa — conflito com decisão D8, precisa alinhar antes |
| [#12810](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12810) | Envio ao RH no fechamento da conciliação, com ciclo 20→19 | 8 pts |
| [#12811](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12811) | Permitir prévia do ciclo RH ainda aberto, sem duplicar no fechamento oficial | 5 pts |
| [#12812](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12812) | Planilha pro Contábil no layout de importação do Oracle | sem estimativa — bloqueado até a Adriana trazer o layout |

Todos filhos do Epic #12387 (Conciliação Fase 2), Sprint 27, atribuídos ao Diego, estado Refinement.

## Achado técnico importante (não estava na transcrição, veio de investigação no código em 26/08)

O módulo de RH ("Aprovação de Vales RH", "Gerenciar Perdas" com escalonamento pro RH) já existe implementado, mas só na branch **`epic/GAV-RTG-12387`** (ConciliaçãoCaixaFront e ConciliaçãoCaixaAPI) — ainda não mesclada em main/develop. A regra de CPF do card #12809 conflita diretamente com uma decisão arquitetural já documentada no repo (decisão **D8**, `E3-S01-resolucao-do-cpf-do-operador.md`): "ninguém classifica por [CPF do gerente]" — precisa de alinhamento explícito antes de implementar.

## Fontes

- [reuniao-area-rh-financeiro-2026-08-25.md](reuniao-area-rh-financeiro-2026-08-25.md) — reunião original com a área.
- [transcricao completa (docx)](alinhamento-interno-2026-08-26.docx)
