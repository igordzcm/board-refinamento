# Daily Tesouraria (25/08/2026)

> Transcrição original já descartada após leitura. Participantes: Francisco Sola Herrero Fernandes Neto, Matheus Gabriel Donato Alves, Walter Pereira da Silva Lira, Filipe de Lacerda Grangeiro.

## Nova regra — padronização de NSU em 8 dígitos

Pedido do Financeiro: todo tipo de depósito passa a ter NSU de 8 dígitos — os 4 primeiros identificam a loja (número da loja), os 4 últimos vêm do comprovante GVT (cofre eletrônico), com zero à esquerda se vier incompleto. Validação de NSU já cadastrada passa a olhar só os 4 últimos dígitos.

**Risco assumido conscientemente** — Sola: "não é algo que eu concordo muito, mas o financeiro quer assim... provavelmente a gente vai dar rollback depois". Por isso vai numa release separada (front 3.0.1 → 3.0.2), isolada do que já está no piloto, pra minimizar o impacto de um rollback se precisar.

Donato: front já quase pronto (começou quando a regra subiu a 1ª vez), só falta validação do Walter.

## Rollout — 100% do parque concluído

"Já estamos com a tesouraria em quase todas as lojas em produção. Hoje viramos o segundo terço, falta só mais um terço que será feito hoje à noite. Até o momento não tivemos problemas... e já sem GeneXus."
