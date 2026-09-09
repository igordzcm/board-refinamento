# Motor de Descontos — Resumo executivo da call com Arthur (02/09/2026)

> Versão curta, sem detalhe técnico, pra quem só precisa da visão geral. Ata completa com os pontos técnicos em [2026-09-02-call-arthur.md](2026-09-02-call-arthur.md).

## Em uma frase

Reunião de acompanhamento de rotina com o Arthur (negócio). Confirmou que um problema antigo de estabilidade já foi corrigido, levantou algumas melhorias de usabilidade da ferramenta e uma dúvida técnica sobre um projeto próprio dele — nenhum bloqueio, nenhuma decisão de risco alto.

## O que já estava com problema e foi confirmado resolvido

- **Instabilidade no envio de campanhas pra loja** (campanha chegava errada, exigia correção manual) — já corrigida há algumas semanas; Arthur confirmou que não vê mais o erro.

## O que vai entrar direto na fila de desenvolvimento (sem custo de decisão)

- Permitir cadastrar uma promoção com um único item (hoje exige no mínimo dois).
- Corrigir os e-mails automáticos de aviso de campanha (hoje às vezes chegam com dado incorreto ou não chegam pro Arthur).

## A resolver com o Fabio — dependem de como funciona hoje do lado do VAR

Esses três pontos não são decisão só da Retaguarda: envolvem como a loja/PDV processa a campanha, então o Igor precisa alinhar com o Fabio antes de qualquer compromisso de prazo com o Arthur.

1. **Campanha por departamento + itens específicos** (motivada pelo Dia das Crianças, 17/09) — hoje o Fabio cadastra isso manualmente; confirmar se ajustar o lado do VAR pra automatizar já está no planejamento.
2. **Cancelamento real de uma campanha** (futura ou ativa) — hoje não existe, o contorno é antecipar a data de fim.
3. **Editar as lojas de uma campanha já ativa/global** (ex. tirar de todas as lojas menos uma regional) sem precisar recriar a campanha do zero.

## Ideias de novos tipos de campanha — tratar como projeto novo, não como ajuste incremental

Dois pedidos que surgiram na call não são "melhorias" na ferramenta atual — são funcionalidades novas, que mexem no PDV/loja e exigem processo formal (TAP) e aprovação do Diego antes de qualquer desenvolvimento:

- **Desconto por variação específica do produto (SKU: cor/tamanho), não só pelo código geral do item.** Projeto próprio do Arthur, já com TAP aberta do lado dele (Diego/Jaís/Ozéias). Avaliação inicial: a estrutura atual (Retaguarda e VAR) é toda baseada em código de item — viabilizar isso é comparável a construir uma funcionalidade nova dentro do motor de descontos, não um ajuste no que já existe.
- **Novas mecânicas de desconto** — desconto progressivo (1ª peça X%, 2ª peça Y%) e cupom de desconto nominal. Motivado por um pedido pontual de marketing (cupons para um evento). Depende do time de loja/caixa poder processar esse tipo de desconto no PDV, não é algo que a Retaguarda decide ou entrega sozinha.


**Clima geral:** feedback positivo sobre a ferramenta ("bem legal", "bem rápido"). Sem atrito, sem escalada necessária.
