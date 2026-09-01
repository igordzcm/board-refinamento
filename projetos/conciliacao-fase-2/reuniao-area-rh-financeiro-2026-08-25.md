# Ata — Demo do módulo de RH pra área (Financeiro/RH)

## Dados da reunião

- **Data/hora:** 25/08/2026, ~18:03 (50m28s)
- **Participantes:** Ozéias Denis de A. Tavares (apresentação/dev), Diego Oliveira Andrade Rafael, Kauã Miguel da Cunha, Danilo Santos Manzoli (devs/QA), **Gilson Valerio Dos Santos** (Gerente — Folha de Pagamento, Trabalhista, Remuneração e Benefícios), **Midia Negrao Do Espirito Santo Lima** (time de RH), **Adriana Cristina Lopes Ressineti** (contábil)
- **Objetivo:** apresentar pra área (RH/Financeiro/Contábil) o novo módulo de RH da Conciliação Fase 2 (tela "Gerenciar Perdas" + "Aprovação de Vales"), coletar feedback.
- **Fonte:** transcrição completa em [reuniao-area-rh-financeiro-2026-08-25.docx](reuniao-area-rh-financeiro-2026-08-25.docx)

## Fluxo apresentado

Analista financeiro concilia loja → marca divergência como "desconto em folha" → cai na tela "Gerenciar Perdas" (filtros por operador/loja/status) → Midia (RH) aprova/reprova, com opção de parcelamento → aprovado, cai no módulo RH "Aprovação de Vales" pro Gilson → Gilson aprova/recusa o parcelamento → export de planilha por período ou consolidado mensal (carimbado, sem duplicar) no formato pro Senior.

## Gaps encontrados (viraram cards)

1. **Aprovação automática em parcela única** — Gilson: aprovar cada vale individualmente é trabalho desnecessário; Midia esclareceu que só devia ser preciso aprovar quando for parcelado. → **card #12808**
2. **CPF do gerente em lojas sem quebra de caixa** — Midia: hoje sempre puxa CPF do operador; em lojas sem quebra de caixa isso desconta de quem não recebe quebra de caixa, tem que usar o CPF do gerente (lista já enviada por ela). → **card #12809** (⚠️ conflita com decisão D8 já documentada no código — ver nota técnica do card)
3. **Envio ao RH no fechamento, não na aprovação, com ciclo 20→19** — discussão longa entre Adriana/Ozéias sobre datas: RH precisa da data de **fechamento** da conciliação (não a da diferença/aprovação), e o ciclo do RH muda de 26→25 pra **20→19** (contábil continua 26→25, baseado na data da diferença). → **card #12810**
4. **Planilha pro Contábil no layout de importação do Oracle** — Adriana: o export atual é só o comparativo que já manda por e-mail hoje, sem conta contábil/centro de custo; precisa vir pronto pra importar no Oracle. **Adriana ainda vai levantar o layout exato.** → **card #12812**

## Esclarecimentos de negócio (não é bug)

- CPF vem hoje do cadastro de operador do Portal Retaguarda (não direto do Senior) — inconsistências de maiúscula/minúscula nos nomes são por causa de dados de homologação criados manualmente.
- Reabertura de conciliação já fechada: **não é fluxo automatizado nesta fase**, tratado manualmente por e-mail com autorização da Midia — confirmado como decisão consciente, não pendência.

## Fontes

- [transcricao completa (docx)](reuniao-area-rh-financeiro-2026-08-25.docx)
- Ver também [alinhamento-interno-2026-08-26.md](alinhamento-interno-2026-08-26.md) — reunião interna do dia seguinte que formalizou essas correções em cards.
