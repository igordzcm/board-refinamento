# Planning VAR 3.0 (31/08/2026)

> Planning quinzenal do squad VAR 3.0. Transcrição original já descartada após leitura. Participantes: Gustavo Do Estreito Deliberali (PO), Filipe de Lacerda Grangeiro, Guilherme Caixeta Rodrigues, Wesley Silva Alves, Nicolas Timoteu Cuerbas, Moises de Oliveira Santos Junior, Jeferson de Oliveira Guimarães, Matheus Gabriel Donato Alves, Gabriel Aparecido Kovalski Lopes.

## Overlimit — desbloqueado

RPE liberou as credenciais/webhooks. Testes de endpoint agora acontecem direto em produção, apontando pro Kong sem precisar de credencial — Gustavo passou as credenciais pro Caixeta.

## CNPJ Alfanumérico — maioria já em release

Caixeta confirmou que a grande maioria das correções já foi mesclada; um PR específico precisa ser localizado e revisado pra não perder a branch.

## Automação de testes — status geral

Kauã Cunha finalizou seus testes de "primeira compra"; Wesley entregando o fluxo de PIX/cobranças por dev review; Moises ainda buscando acesso próprio às máquinas de QA (usando o do Jeferson temporariamente); Jeferson trabalhando na documentação/migração GeneXus, com tarefa de FeatureFlag em andamento.

## Kovalski — dividindo tempo entre SSO e Engine

Ainda na engenharia reversa do SSO/SIGA em homologação, achando pontos não mapeados antes. Vai auxiliar o Donato numa força-tarefa na loja 208 (QA). Também vai pegar automação fiscal (correção pontual de SSO) e depois provavelmente migração.

## Tesouraria / Donato

Rotina de desconto de gerente no Java quase pronta, testes rodando com PDV. Também ajudando o Ozéias com melhorias na remarcação de preços.

## Novo processo — piloto não sobe mais sem estar mergeado na release

Gustavo formalizou com o Vini: nenhuma feature mais sobe direto pra loja no dia do piloto sem estar mergeada na release antes — já aconteceu 2 vezes de feature ficar destacada (não em release) no dia da atualização.

## Ponto de atenção — critério de aceite

Confirmado pelo time (Felipe/Nicolas): os próprios devs/QAs escrevem os critérios de aceite quando é bug; Gustavo só marca. Igor sinalizou que tem visto muito card sem critério de aceite, levou o ponto pra pauta do retro (28/08).
