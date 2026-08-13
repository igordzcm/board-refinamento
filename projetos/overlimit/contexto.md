# Overlimit — contexto geral

> Arquivo de contexto do projeto. Atualizado a partir do dashboard executivo e das transcrições de daily do VAR 3.0 (05/08 e 06/08). Ler antes de qualquer reunião sobre este projeto.

## O que é

Funcionalidade de crédito na venda (Overlimit) no PDV VAR 3.0.

## Dono

**Gui Oliveira**.

## Status atual (12/08/2026, via reunião de planejamento de sprint)

**5% — bloqueado, mas escopo agora está mais claro e ganhou prazo-alvo.** Projeto seguia parado desde antes de 04/08 por falta de resposta do fornecedor RPE; a reunião de 12/08 não resolveu esse bloqueio, mas destrinchou o que precisa ser construído e definiu meta de entrega.

> Fonte: [`../dailies/2026-08-12-planejamento-sprint.md`](../dailies/2026-08-12-planejamento-sprint.md).

**Escopo confirmado por Ozéias (12/08):**
1. Tela de **import de planilha Excel** — lista de clientes elegíveis a receber o bônus/crédito do overlimit (leitura + [trecho da gravação inaudível, provavelmente "validação/aplicação" — confirmar]).
2. **Distribuição pra loja** — mecanismo pra levar essa base até o PDV VAR, igual ao que já existe pra **blacklist** (RPA): "muda só que aqui vai ser outra base, e o VAR tem que consumir essa base." Léo sugere partir do que já foi feito pra blacklist, deve ser mais rápido de adaptar.
3. **Prazo-alvo: release de setembro do VAR**, antes do code freeze — prazo definido nesta reunião, não confirmado se é compromisso firme ou meta de planejamento.

**Possível sobreposição:** Ozéias mencionou "acho que até o Gui estava mexendo nisso" — não confirmado se é retrabalho ou continuação do que Gui Oliveira (dono do projeto) já vinha fazendo antes do bloqueio da RPE. Vale confirmar com o Gui antes de iniciar.

## Bloqueio

**Fornecedor RPE sem resposta — segue sem atualização.** O bloqueio técnico de fundo é uma limitação do gateway Kong, que não suporta duas credenciais simultâneas — a validação da solução pra essa limitação depende da credencial de teste que a RPE prometeu enviar em 04/08 e não enviou. Não foi mencionado na reunião de 12/08 (que foi sobre planejamento/escopo, não sobre status do fornecedor) — **sem confirmação de que avançou**.

Citado no dashboard executivo (10/08) como um dos três fatores externos recorrentes que travam múltiplos projetos do VAR (junto com a instabilidade de cache da GetNet no Tap on Phone e o fornecedor do SmileGo, este sem retorno há mais de um mês).

## Reuniões

- [`../dailies/2026-08-12-planejamento-sprint.md`](../dailies/2026-08-12-planejamento-sprint.md) — reunião de planejamento de sprint (transversal, não específica deste projeto) onde o escopo foi destrinchado e o prazo de setembro definido.

## Próxima atualização

Preencher aqui: (1) se a RPE respondeu sobre a credencial de teste e se a limitação do Kong foi validada — bloqueio de fundo que independe do escopo definido em 12/08; (2) se confirmado com o Gui se ele já tem algo desenvolvido na tela de import; (3) se o prazo de release de setembro foi comunicado como compromisso ou é só meta de planejamento.
