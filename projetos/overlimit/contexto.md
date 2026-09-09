# Overlimit — contexto geral

> Arquivo de contexto do projeto. Atualizado a partir do dashboard executivo e das transcrições de daily do VAR 3.0 (05/08 e 06/08). Ler antes de qualquer reunião sobre este projeto.

## O que é

Funcionalidade de crédito na venda (Overlimit) no PDV VAR 3.0.

## Dono

**Gui Oliveira**.

## Status atual (08/09/2026) — não mais bloqueado, tratado como prioridade semanal ativa

> Fontes: [`../dailies/2026-09-08-digest-var3.md`](../dailies/2026-09-08-digest-var3.md), [`../prioridades-sprint.md`](../prioridades-sprint.md) (seção "Resolvido desde a última atualização", 31/08).

**A trava de fundo (fornecedor RPE) já foi resolvida.** Per o `prioridades-sprint.md`: a RPE liberou credenciais/webhooks em 31/08; testes de endpoint em produção já começaram, direto no Kong, sem precisar de credencial de teste — Overlimit saiu da lista de bloqueios críticos. Isso bate com o digest VAR 3.0 de 01/09 ("RPE liberou as credenciais de produção pra uso direto") e de 04/09 (Gui Oliveira retomou o projeto, backend com endpoint adicional já pronto, trabalhando no front de validação de elegibilidade).

**Confirmado como prioridade ativa em 08/09:** na daily VAR 3.0, o PO Gustavo listou Overlimit entre os itens que precisam subir antes do piloto de 14/09 (junto com tratamento de erros, consulta automática, Pix no TEF). Não é mais tratado como bloqueado — é tratado como trabalho corrente da semana.

**O "5% — bloqueado" de 12/08 abaixo está desatualizado e não deve mais ser citado como status atual.** Não há, nas fontes revisadas (dailies de 01, 04 e 08/09), um número de progresso atualizado — a estimativa de percentual precisa ser levantada separadamente com o Gui antes de voltar a aparecer neste arquivo. (O dashboard executivo traz um progress-item de "45%" pro Overlimit, mas atribuído ao Caixeta como owner — este arquivo registra Gui Oliveira como dono; não está claro se são a mesma pessoa/frente ou papéis diferentes (dev vs. teste), então não uso o "45%" aqui sem confirmar isso primeiro.)

## Status anterior (12/08/2026, via reunião de planejamento de sprint)

**5% — bloqueado, mas escopo agora está mais claro e ganhou prazo-alvo.** Projeto seguia parado desde antes de 04/08 por falta de resposta do fornecedor RPE; a reunião de 12/08 não resolveu esse bloqueio, mas destrinchou o que precisa ser construído e definiu meta de entrega.

> Fonte: [`../reviews-retros-planning/2026-08-12-planejamento-sprint.md`](../reviews-retros-planning/2026-08-12-planejamento-sprint.md).

**Escopo confirmado por Ozéias (12/08):**
1. Tela de **import de planilha Excel** — lista de clientes elegíveis a receber o bônus/crédito do overlimit (leitura + [trecho da gravação inaudível, provavelmente "validação/aplicação" — confirmar]).
2. **Distribuição pra loja** — mecanismo pra levar essa base até o PDV VAR, igual ao que já existe pra **blacklist** (RPA): "muda só que aqui vai ser outra base, e o VAR tem que consumir essa base." Léo sugere partir do que já foi feito pra blacklist, deve ser mais rápido de adaptar.
3. **Prazo-alvo: release de setembro do VAR**, antes do code freeze — prazo definido nesta reunião, não confirmado se é compromisso firme ou meta de planejamento.

**Possível sobreposição:** Ozéias mencionou "acho que até o Gui estava mexendo nisso" — não confirmado se é retrabalho ou continuação do que Gui Oliveira (dono do projeto) já vinha fazendo antes do bloqueio da RPE. Vale confirmar com o Gui antes de iniciar.

## Bloqueio — RESOLVIDO em 31/08

> Ver Status atual (08/09) no topo do arquivo pra fonte e detalhe.

**Fornecedor RPE respondeu e liberou credenciais/webhooks em 31/08** — o bloqueio abaixo (histórico, até 12/08) não reflete mais a situação atual, mantido só como registro de como o bloqueio evoluiu.

~~**Fornecedor RPE sem resposta — segue sem atualização.** O bloqueio técnico de fundo é uma limitação do gateway Kong, que não suporta duas credenciais simultâneas — a validação da solução pra essa limitação depende da credencial de teste que a RPE prometeu enviar em 04/08 e não enviou. Não foi mencionado na reunião de 12/08 (que foi sobre planejamento/escopo, não sobre status do fornecedor) — sem confirmação de que avançou.~~

Citado no dashboard executivo (10/08) como um dos três fatores externos recorrentes que travavam múltiplos projetos do VAR (junto com a instabilidade de cache da GetNet no Tap on Phone e o fornecedor do SmileGo, este último ainda sem retorno — não confirmado se segue parado, ver [`../prioridades-sprint.md`](../prioridades-sprint.md)).

## Reuniões

- [`../reviews-retros-planning/2026-08-12-planejamento-sprint.md`](../reviews-retros-planning/2026-08-12-planejamento-sprint.md) — reunião de planejamento de sprint (transversal, não específica deste projeto) onde o escopo foi destrinchado e o prazo de setembro definido.

## Próxima atualização

Preencher aqui: (1) uma estimativa de percentual de progresso atualizada (levantar com o Gui — nenhuma fonte revisada até 08/09 traz um número confiável pra este projeto especificamente; o dashboard executivo tem um progress-item de "45%" mas atribuído a "Caixeta" como owner, enquanto este arquivo registra Gui Oliveira como dono — não uso o número sem antes confirmar se são a mesma frente ou papéis diferentes, ex. Gui no dev e Caixeta em teste); (2) se o item "voucher" citado pelo PO em 08/09 (nome incompleto/garbled na transcrição) é parte deste projeto ou outra coisa; (3) status do teste com os 3 CPFs controlados pela área de negócio mencionado em 04/09.
