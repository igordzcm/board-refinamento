# Daily VAR 3.0 — Proj/Sust — 11/08/2026

> Resumo (não transcrição literal), convertido de `VAR 3.0 - Daily Proj_Sust.docx` (raiz do workspace, movido pra cá). 18m18s. Time diferente do Retaguarda (squad VAR 3.0, liderado pelo Gustavo Do Estreito Deliberali) — mantido aqui como referência cruzada porque compartilha pessoas (Kovalski, Matheus Donato) e toca frentes já rastreadas no índice de projetos ([tap-on-phone-var4g](../tap-on-phone-var4g/contexto.md), [motor-descontos](../motor-descontos/contexto.md), [automacao-fiscal](../automacao-fiscal/contexto.md)).

**Participantes:** Gustavo (lead), Franklin, Kevin, Nicolas, Guilherme Oliveira, Wanderleia, Moises, Kovalski, Matheus Donato, Guilherme Caixeta, Felipe Pinheiro, Filipe de Lacerda (audita ao final), Spin.

## Por pessoa

- **Guilherme Oliveira** — Unificando os pilotos de Tap on Phone + VAR 4G com o Walter, rodando testes. "Overlimit não está travado" — RPE/Rigolon ainda não respondeu.
- **Wanderleia** — Tratando casos de erro no retorno de CNPJ; aplicou correção pedida, teve que recriar a branch (problemas de compilação) a partir de uma mais nova.
- **Moises** — Trabalhou em bug (card citado como "12237"), enviou pra revisão do Felipe. Dois bugs no nome dele já foram pra DevBox — ficou sem task nova até o Gustavo realocar.
- **Kovalski** — Seguindo SSO; entrando na integração do Siga (projeto compartilhado com o Retaguarda — ver [daily 11/08 Retaguarda](2026-08-11-retaguarda.md)). Foco total no Siga até sexta; só volta pra Automação Fiscal se "acontecer alguma bomba".
- **Matheus Donato** — Tocando o projeto de etiqueta remarcada (Spin/Jonas/Bruno) — não está mexendo em nada do VAR/Engine.
- **Guilherme Caixeta** — Testes de integração do **Motor de Descontos** ("rotina de desconto") lado loja/PDV — caminho feliz primeiro, depois cenários tristes. Sem gap percebido na história até aqui.
- **Nicolas / Felipe Pinheiro** — Testes de venda no 4G, correção da Danf a decidir se sobe nessa release, dev boxes na fila.

## Pontos de atenção

- Testes de integração do Motor de Descontos (lado loja) rodando em paralelo ao trabalho de arquitetura de sincronização que o Leonardo (Retaguarda) começou em 12/08 — ver [motor-descontos/contexto.md](../motor-descontos/contexto.md).
- Kovalski e Matheus Donato aparecem nos dois times (Retaguarda e VAR 3.0) no mesmo período — cross-squad confirmado, não duplicidade de dados.
