# Etiqueta Remarcados — contexto geral

> Arquivo de contexto do projeto. Atualizado a partir do card vigente no Azure DevOps (#12506, reescrito 12/08/2026) e dos documentos técnicos de referência. Ler antes de qualquer reunião sobre este projeto.

## O que é

BI e Configurações para o módulo de **Etiqueta Remarcados** no Portal da Retaguarda — acompanha o app de chão de loja `app-remarcacao-preco`: telas de BI (produtividade por operador, justificativas/divergência, auditoria da etiqueta, aderência), tela de Configurações (parâmetros de operação e motivos de justificativa) e a tela de pendências que expõe quais lojas ainda não remarcaram.

**Não confundir com "Markdown / Remarcação de Preços"** (Victor + Hudá) — este projeto é sobre a **tela de pendências de etiquetas físicas em loja** (chão de loja); o outro é a ferramenta de **planejamento central** de desconto por família. Ver `projetos/markdown-precos/contexto.md`.

Épico: **[#12428 — BI e Configurações — Etiqueta Remarcados no Portal da Retaguarda](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12428)** (Var Retaguarda), status **To Do**.

## Card vigente e autoritativo: #12506

**[#12506 — Tela de pendências no módulo de etiqueta remarcados](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12506)** — status **Doing**, atribuído a **Matheus Gabriel Donato Alves**, Sprint 26, esforço 21 pts. Reescrito em 12/08/2026 com um plano técnico N1/N2/N3 detalhado — **este card é a fonte de verdade atual do projeto**, superior a qualquer planejamento anterior.

> **Como** Bruno (gestor que cobra as lojas) e encarregados de loja
> **Quero** uma tela que mostre quais lojas ainda não remarcaram os preços, com drill-down até o item quando eu precisar
> **Para que** eu saiba pra quem ligar sem precisar adivinhar qual loja olhar, e o encarregado saiba exatamente o que fazer na gôndola

**Protótipo navegável (rede → detalhe):** [claude.ai/code/artifact/be66e378-cf2a-497e-84f6-0c9ab2c8735a](https://claude.ai/code/artifact/be66e378-cf2a-497e-84f6-0c9ab2c8735a)

**Plano técnico completo:** `board-refinamento/referencias/12506-plano-pendencias-remarcacao.html` (arquitetura, SQLs medidos, taxonomias, armadilhas de dado).

### Arquitetura em 3 níveis (paga o custo só quando o usuário pede)

| Nível | Responde | Custo alvo | Quando executa |
|---|---|---|---|
| **N1 · Rede** | Quem não fez — uma linha por loja, as piores primeiro. Sem filtro obrigatório de loja | ≤ 1,5 s | A cada abertura da tela |
| **N2 · Lotes** | Quais lotes daquela loja estão parados | < 1 s | Ao expandir a linha de uma loja |
| **N3 · Detalhe** | Quais itens, quanto falta, ordem de trabalho (com preço vigente) | 6–16 s | Ao clicar na loja, com loading explícito |

O N1 nunca calcula preço vigente (é o que torna a rede inteira rápida); "itens no lote" é um **teto**, não uma meta — nunca deve virar denominador de %, exceto o caso zero (que é certeza).

**Situação da loja (N1):** Silenciosa (lote lançado, zero etiquetas) · Parada (lote intocado, N dias sem emitir) · Lote parado (lote intocado, emitiu recentemente) · Ativa (nenhum lote intocado).

**Situação do item (N3):** Não iniciado · Parcial · Falha de impressão (status ERR) · Justificado (linha em REM002) · Sem estoque · Concluído.

### Fica pendente (4 itens — paralelo à implementação, não bloqueiam o início do dev)

| Pendência | Dono |
|---|---|
| Índices em produção (`IX_REM001_ITEM`, `IX_REM001_DTMOV`, índice com `REMDTOCO` líder) | DBA · Thalison |
| Medir performance do N3 numa loja grande antes do piloto (margem contra timeout de 20s) | Antes do piloto |
| Limpeza das tabelas antigas `VAR.REM*` | DBA · Thalison |
| Definir "de quem é a cobrança" (destinatário por loja na lista de cobrança) | Negócio · a definir |

## Histórico — planejamento anterior (VSCODE, potencialmente desatualizado)

Antes da reescrita do #12506 em 12/08, o planejamento vivia em dois documentos no workspace VSCODE (`TASKS-BI-ETIQUETA-REMARCADOS-BOARD.md` e `TASK-BI-ETIQUETA-REMARCADOS.md`, gerados em 27/07/2026), organizados em **5 tasks (TF-01 a TF-05)**: TF-01 Fundação da API, TF-02 Tela de Configurações, TF-03 Telas de BI, TF-04 Snapshot e Aderência, TF-05 Endurecimento. Esse plano cobria o escopo mais amplo de BI/Configurações (não incluía ainda a tela de pendências, que só apareceu depois como #12506).

Pontos desse plano anterior que seguem relevantes como pano de fundo técnico (schema Oracle `APP_PRICETAG`, instância `DBCASELI` produção / `172.16.10.2:1521/teste` homologação):

- Pré-requisitos bloqueantes já identificados: confirmar que o `VarDataSource` do Portal aponta pra instância certa; grants ao Thalison em `REM001/REM002/REM004/REMPARAM`; índices no Oracle (mesmos citados no "Fica pendente" do #12506 atual); limpeza das tabelas legadas `VAR.REM001/REM002/REM004` (schema pré-migração de 23/07/2026).
- Observação operacional: **o BI nasce vazio** — o ledger só chega ao Oracle com `PUSH_HABILITADO` (app) e `SYNC_ESCRITA_HABILITADA` (API) ligados; na época do plano havia 148 linhas de apenas 2 lojas de teste.
- Armadilha central repetida em ambos os documentos: escrever `APP_PRICETAG.` explicitamente em toda query — o schema legado `VAR.REM*` ainda existe e é a armadilha mais provável da integração.

**Este histórico pode estar desatualizado** em relação ao plano vigente do #12506 — usar apenas como contexto de arquitetura de dados, não como fonte de escopo atual.

## Reuniões

Nenhuma reunião registrada ainda.

## Próxima atualização

Preencher aqui após o Passo 0 do card #12506 (medições antes de escrever código de produção): tempo real das duas consultas do N1 combinadas, fração de `REMDTMOV` nulos, folga do teto de "itens no lote", e resultado do SELECT em `VW_ESTOQUE` com o usuário do VarDataSource.
