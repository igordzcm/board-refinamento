# Pauta + Ata — Call Igor + Arthur (quarta, 02/09/2026)

> Pauta preparada em 01/09, ajustada no mesmo dia pra refletir a pauta real do Igor (mais enxuta do que a primeira versão). Ata completa adicionada em 02/09 após a call, com base na transcrição + anotações do Igor. Versão resumida pra gestores em [2026-09-02-call-arthur-resumo-executivo.md](2026-09-02-call-arthur-resumo-executivo.md). Sincronizado com [contexto.md](contexto.md).

## Épico: [#6669 — Motor de Descontos](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/6669)

## 1. Explicar a mudança de arquitetura de propagação

A Retaguarda não propaga mais campanha/desconto direto pra loja. Fluxo atual: Retaguarda só grava no banco da Retaguarda (card [#12405](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12405), Leonardo — já Ready for Dev); **Thalison (DB)** propaga pra loja de acordo com a necessidade.

## 2. Melhorias no sistema e passos futuros — conversa aberta com Arthur

Sem pauta fechada — deixar o Arthur trazer prioridades. Se for útil puxar assunto, já existem 2 itens de backlog 100% refinados esperando só priorização:

| Card | Título | Estimativa |
|---|---|---|
| [#11813](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/11813) | Interface para gerenciar destinatários de e-mail | 3 pts |
| [#11818](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/11818) | Relatório de performance de campanhas | 13 pts |

## Ata da reunião (02/09/2026, 28m54s — Igor, Arthur, Kauã por parte da call)

### Como foi

Call de acompanhamento aberta, sem pauta fechada na parte 2 — Igor explicou a correção de propagação e o resto do tempo foi Arthur trazendo pontos de dificuldade de uso + uma dúvida técnica de um projeto próprio dele.

### 1. Propagação de campanha pra loja — resolvido

Bug antigo de propagação (campanha chegava errada na loja) foi corrigido pelo Léo: a Retaguarda só grava a campanha no banco da Retaguarda, e o time de DB (Thalison/Fabio) propaga pra loja. Arthur confirmou que não vê mais o erro.

### 2. Campanha por departamento + itens específicos (contexto: Dia das Crianças, 17/09)

Hoje esse tipo de campanha (departamento inteiro + itens avulsos de outros departamentos, ex. calçados infantil + itens de acessórios/lar) é feito manualmente pelo Fabio, e ele vai continuar subindo essa campanha assim quando chegar o momento. **Igor vai validar se corrigir o lado do VAR pra suportar esse tipo de criação de novo já está no planejamento**, com o objetivo de melhorar o sistema — sem compromisso de prazo.

### 3. Edição de campanhas grandes — maior ponto de dor do Arthur

Prorrogação/antecipação e o aviso de "item já em outro combo" funcionam bem.

**Problema:** em campanhas grandes (ex. leve 3 pague 2 de remarcados, ~8.000 itens), não dá pra reimportar uma lista de Excel na edição — só dá pra adicionar item por item na mão. Força o Fabio a atuar toda vez que sobra uma remarcação nova (última rodada: >1000 itens de calçados).

Esclarecido: remover item da lista não exclui de verdade, ele fica "inativo" (mantém histórico) e pode ser reativado — Arthur tinha ficado em dúvida se estava funcionando.

Erro de timeout ao subir listas muito grandes (~8000 códigos) é problema já conhecido — Léo já vem mexendo aos poucos, não é algo ignorado.

### 4. Cancelamento de campanha — precisa validar com o Fabio

Hoje não existe uma função real de cancelar/excluir uma campanha — nem futura, nem ativa. O workaround usado hoje é antecipar a data de fim. O mesmo vale pra tirar uma campanha de lojas específicas. **Igor vai validar com o Fabio** se/como dá pra implementar um cancelamento de verdade, cobrindo tanto campanha futura quanto campanha ativa.

### 5. Combo com 1 item só — vira item de backlog

Hoje o mínimo é 2 itens no combo; casos como o combo perene do travesseiro (3 pague 6) às vezes precisam ser recadastrados com 1 item só, e hoje isso força o Fabio a atuar porque a ferramenta não permite. **Decisão: permitir campanha/combo com apenas 1 item.**

### 6. Cadastro em nível SKU — pergunta técnica do Arthur, sem decisão fechada

Projeto do lado do Arthur (já com TAP aberta, Diego/Jaís/Ozéias): hoje tudo no motor de descontos é por código de item (6 dígitos); SKU seria mais granular (12 dígitos, + tamanho/cor). Caso de uso citado: toalha de banho com várias cores — querem promocionar só 2 cores de alto estoque sem sinalizar a promoção nas outras cores no PDV.
- Avaliação de Igor: a estrutura hoje (Retaguarda e VAR) é toda baseada em código de item, não SKU — mudar isso seria esforço grande. Visão dele: mais viável criar uma funcionalidade nova dentro do motor de descontos do que alterar a estrutura existente.
- **A resolver (Igor):** levantar o assunto com o Spin (mais próximo do Diego) e retornar. Assunto já está formalmente com o Diego pelo lado do Arthur.

### 7. Editar lojas de uma campanha já ativa/global — sem decisão fechada

Caso de uso: campanha ativa em todas as lojas, querer restringi-la depois a um subconjunto (ex. só regional Mato Grosso) sem recriar do zero. Hoje o sistema bloqueia edição de lojas numa campanha "global", e não ficou claro se é proposital (manutenção) ou não implementado.
- **A resolver (Igor):** avaliar com Kauã e Fabio antes de prometer qualquer coisa; entra na lista de retornos por mensagem.

### 8. E-mails de notificação (criação/prorrogação) — vira item de backlog

E-mails às vezes chegam com nome de remetente errado ("nome de teste", já veio com nome de uma colaboradora do financeiro) e o envio é inconsistente (Arthur nem sempre recebe, apesar de cadastrar ~1 combo/semana). Hoje quem recebe é a própria equipe de TI.
**Decisão:** corrigir o assunto do e-mail (tirar "teste"), simplificar o conteúdo pra só o essencial (campanha, tipo, período, quem criou/prorrogou) — tanto pra criação quanto pra prorrogação — revisar a lista de destinatários do projeto, e garantir que vá pro Arthur.

### 9. Relatório de performance de campanha e novos tipos de mecânica — direção futura

Relatório de performance (ideia antiga) não é mais prioridade pro Arthur no formato original — ele já tem uma solução própria funcionando pra acompanhar vendas por campanha.
Novo interesse: saber se a ferramenta é parametrizável pra novos tipos de mecânica — desconto progressivo (1ª peça X%, 2ª peça Y%) e cupom de desconto nominal (motivado por um pedido real: cupons pra um evento/corrida, que o PDV hoje não suporta).
Igor: a plataforma foi desenhada desde o início pra ser extensível a novos tipos (hoje só 2 dos 3 tipos originais funcionam) — mas qualquer tipo novo que toque o PDV/VAR exige TAP formal e trabalho simultâneo dos dois lados, não é só desenvolvimento do lado da Retaguarda. Sem decisão fechada — fica como direção, a formalizar via TAP se avançar.

### Resumo — pendências e próximos passos

**Igor vai resolver e responder por mensagem (sem nova reunião):**
- Validar se corrigir o lado do VAR pra campanhas de departamento já está no planejamento
- Com o Fabio: viabilidade de um cancelamento real de campanha (futura e ativa)
- Com Kauã/Fabio: viabilidade de editar lojas de uma campanha global já ativa
- Com o Spin/Diego: viabilidade de cadastro em nível SKU (TAP já existe do lado do Arthur)

**Já pode entrar na fila de desenvolvimento (Retaguarda, sem dependência externa):**
- Permitir campanha/combo com 1 item só (hoje mínimo 2)
- Corrigir e-mails de notificação — assunto, conteúdo essencial, lista de destinatários

**Em andamento, sem novidade além de confirmação:**
- Timeout ao subir listas muito grandes (~8.000 itens) — Léo já trabalhando aos poucos

**Direção futura / depende de TAP formal e aprovação (Diego):**
- Novo tipo de criação de campanha: departamento + itens específicos
- Cadastro em nível SKU
- Novos tipos de mecânica de campanha (progressivo, cupom nominal) — depende de suporte do PDV/VAR

---

## Anotações do Igor durante a call (brutas, mantidas para não perder nada)

17/09 começa de dia das crianças evento
leve 3 pague 2
fazem campanha de departamento

precisamos do de departamentos

conversar com Fabio


Começar a pensar em desenvolvimento de criaçaõ de campanha de departamentos + itens especificos
    na criação podemos fazer algo mais manual



dificuldade do arthur:
    - mexer em uma campanha ativa
        prorrogação funciona bem
        dificuldade em campanha grande
        ex: l3p2 com lista de 8 mil itens
        a cada prorrogação adiciona novos itens
        poder na edição subir uma lista de itens por excel

na edição salvar quando subiu cada lote


permitir campanha com 1 só item (hoje só funciona com 2 ou mais)


corrigir email
criação e prorrogação
enviar pro arthur

tudo é feito por codigo de item


na edição também
cadastrar combo pra todo mundo

criar combo pra todas as lojas
editar 


criação campanha
erro 502
ver o fluxo



cancelar campanha
falar com fabio tbm
tanto campanha futura e campanha ativa


tirar campanha das lojas
falar com fabio


começar a criar novos tipos de campanhas