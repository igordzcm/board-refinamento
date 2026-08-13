# Tap on Phone + VAR 4G — contexto geral

> Arquivo de contexto do projeto. Atualizado a partir das transcrições de daily do VAR 3.0 (05/08 e 06/08) e do dashboard executivo. Ler antes de qualquer reunião sobre este projeto.

## O que é

Piloto conjunto de duas frentes de mobile do VAR 3.0, lançadas **juntas de propósito**:

- **Tap on Phone (GetNet)** — pagamento por aproximação usando o celular como maquininha, via app da GetNet integrado ao PDV.
- **VAR 4G — segurança** — piloto de segurança em celulares dedicados 4G para as lojas.

## Donos

**Gui Oliveira** (Tap on Phone) · **Gui Oliveira + Walter** (VAR 4G — segurança).

## Por que os dois pilotos andam juntos

Instrução explícita do **Spin (Luiz Spineli Lucchi Neto)** na daily de 06/08: *"a gente vai fazer esse tap on fone, a gente tá rolando o piloto do 4G (...) é importante a gente fazer o piloto do tap on fone junto com o do 4G (...) não faz sentido a gente rodar dois pilotos do mobile separados (...) ou vai tudo ou não vai."* Determinou que Gui Oliveira e Walter se articulem diretamente ("fica de mão dada com Walter") para manter os dois pilotos sincronizados.

## Status atual (10/08/2026, via dashboard executivo)

- **Tap on Phone:** 95% — piloto em loja ativo desde 10/08, junto com o VAR 4G.
- **VAR 4G — segurança:** 92% — piloto em andamento, integrado ao piloto do Tap on Phone (decisão técnica de não rodar os pilotos de mobile separadamente).

## Linha do tempo (via dailies)

- **05/08** — Gui Oliveira relata bug no app da GetNet identificado durante apresentação do Diego para a diretoria da GetNet; corrigido pela GetNet antes do início do piloto. GAV negociando compra de ~400 celulares dedicados para as lojas (conversa com a Vivo).
- **06/08** — Diego apresenta o Tap on Phone para a presidência da GetNet; bug aparece ao vivo na apresentação — aparentemente ligado a instabilidade de cache no app da GetNet (Tap on Phone), não no app da GAV. Comportamento: limpar o cache do app resolve, mas de forma inconsistente entre operadores/sessões. Gui Oliveira escala o ponto por e-mail para a GetNet. Compra dos ~400 celulares confirmada em conversa com a Vivo.
- **11/08 e 12/08** (via [`../dailies/2026-08-11-var3-projsust.md`](../dailies/2026-08-11-var3-projsust.md) e [`../dailies/2026-08-12-var3-projsust.md`](../dailies/2026-08-12-var3-projsust.md)) — Gui Oliveira segue unificando os testes 4G + Tap on Phone com o Walter (dia 11/08 com queda de energia/internet, contornado via 4G no celular). Nicolas/Felipe Pinheiro testando vendas no 4G, ainda falta validar localmente; **pendência de decisão se a correção da Danf sobe nessa release**. Dev box relacionado (do Moises) pronto, aguardando decisão se entra nessa sprint ou na seguinte. RPE/Rigolon (Overlimit) segue sem resposta em ambas as datas.

## Riscos e pontos de atenção

- **Instabilidade de cache do app da GetNet** — risco em aberto, causa exata desconhecida ("pode ser N fatores do lado deles"); mitigação atual é limpar o cache manualmente; escalado por e-mail à GetNet, sem resposta formal registrada nas fontes revisadas.
- App precisa de tela sempre visível durante a venda (Tap on Phone trava se a tela for monitorada/espelhada ou se houver outro app aberto em segundo plano) — celulares das lojas serão de uso exclusivo do VAR, sem outros apps instalados.
- Risco geral do VAR 3.0 (dashboard executivo): dependência recorrente de terceiros — GetNet (cache instável) é citada como um dos três fatores externos que mais atrasam projetos do VAR no momento (junto com RPE/Overlimit e o fornecedor do SmileGo).

## Reuniões

Nenhuma reunião registrada ainda.

## Próxima atualização

Preencher aqui após a GetNet responder sobre a causa da instabilidade de cache, e conforme o piloto avança para mais lojas: se os ~400 celulares já foram entregues e se a integração dos dois pilotos (Tap on Phone + VAR 4G) segue sem intercorrências.
