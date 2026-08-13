# VAR 3.0 — Padronização de Retornos HTTP — contexto geral

> Arquivo de contexto do projeto. Atualizado a partir do PRD original e da lista de tasks. Ler antes de qualquer reunião sobre este projeto.

> ⚠️ **Sem card no Azure, sem menção em dailies até 10/08 — confirmar com o time se ainda é prioridade ou se foi descontinuado antes de agendar qualquer reunião sobre isso.**

## O que é

Padronização e blindagem dos retornos HTTP dos três serviços de backend do PDV VAR 3.0 (VendaMercantil, AvenueCustomerCard, VarService) e dos dois apps Flutter (Var3.App, Var_Mobile). Hoje erros de negócio sobem como `500`, recursos não encontrados retornam `400`, timeouts viram `500`, e vários endpoints retornam `200` com erro ou dado vazio no body (falha silenciosa) — sem interceptor HTTP central nos apps, com pontos de `jsonDecode` desprotegidos que travam o app diante de body vazio/não-JSON.

**Objetivos declarados no PRD:** zero falhas silenciosas (nenhum endpoint retorna `200` com erro), status semanticamente correto em 100% dos casos P1–P3 mapeados, zero crash de `jsonDecode`, e queda mensurável de chamados de SAC do tipo "erro genérico"/"falha na consulta" pós-deploy.

Criado em **09/06/2026**.

## Escopo técnico (5 fases, 9 tasks)

| Fase | Tasks | Paralelizável | Pré-requisito |
|---|---|---|---|
| 1 — Flutter blindagem | 1.0 (`decodeBodySeguro` + blindagem dos 6 pontos de `jsonDecode`) | — | nenhum |
| 2 — Flutter status | 2.0 (lógica de status de negócio: 404/400/422/408/504/502) | — | 1.0 |
| 3 — Backend P1 | 3.0 VendaMercantil, 4.0 AvenueCustomerCard (reativar handler comentado), 5.0 VarService | sim, por serviço | 2.0 + Q4 resolvida |
| 4 — Backend P2 | 6.0 VendaMercantil, 7.0 AvenueCustomerCard, 8.0 VarService | sim, por serviço | Fase 3 |
| 5 — Backend P3 + E2E | 9.0 (422/409/204 + validação E2E completa) | — | Fase 4 |

**Ordem não-negociável do PRD:** apps blindam (1.0) e reconhecem novos status (2.0) **antes** de qualquer troca de status no backend (3.0+) — backend não pode quebrar app em campo.

## Bloqueios / questões em aberto (do PRD original)

- **Q4 — bloqueia a Fase 3:** confirmar se existem consumidores além dos dois apps Flutter (outros PDVs/integrações) que dependam dos status HTTP atuais.
- **Q5:** baseline/fonte da métrica de SAC e janela de medição pós-deploy.
- Q2/Q3 já estavam resolvidas no PRD original (saldo insuficiente → 422; `deleteClienteBaseEmissora` ERRO → 502), mas o próprio documento pede reconfirmação com os consumidores de `/validaSaldo` antes do deploy da Fase 5.

**Dívida técnica registrada como fora de escopo:** handlers duplicados para `MethodArgumentNotValidException` (VM-10); divergência de `DEFAULT_TIMEOUT` (10 min vs 4s no `http_wrapper.dart`); interceptor HTTP central nos apps (mantém-se tratamento por repository).

## Status atual

Sem evidência de início de desenvolvimento. Nenhuma das 9 tasks tem indicação de progresso além de "pending" no documento original.

## Reuniões

Nenhuma reunião registrada ainda — e não deveria ser agendada nenhuma sem antes confirmar se o projeto segue vivo.

## Próxima atualização

Preencher aqui após confirmar com o time (Spin/Gustavo ou quem for dono do VAR 3.0) se este projeto ainda é prioridade. Se sim: abrir Epic no Azure e definir responsável. Se não: arquivar este contexto como referência técnica (mesmo padrão do Engine Fiscal CNPJ Alfanumérico).
