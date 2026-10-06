# API Retaguarda — Incidente de instabilidade (01/09) — contexto geral

> Arquivo de contexto do projeto. Apuração feita em 01/09/2026 a partir do relato de que "a API caiu, aparentemente na busca do saldo do caixa na conciliação de lojas". 5 cards criados em 04/09, todos em Refinement.

## O que é

Apuração de incidente de produção via Loki (dashboard Api Logs - APIS PRT) + inspeção somente-leitura do host. Achados três problemas independentes: um healthcheck do nginx mal configurado causando restart em loop (a maior fonte de instabilidade percebida), falta de threads no Node pro Oracle em thick mode (mascarada como "saturação de pool"), e a rota `/api/auth/me` baixando a foto do usuário sem cache a cada chamada. Apuração completa em [2026-09-01-plano-pos-incidente.md](2026-09-01-plano-pos-incidente.md).

## Cards criados (04/09, Var Retaguarda) — em Ready for Dev, Sprint 28, Fernando

| Card | Pacote | Risco | Estimativa (PO, Fibonacci) |
|---|---|---|---|
| [#12902](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12902) | Corrigir healthcheck do nginx (loop de restart do autoheal) | Baixo | 2 |
| [#12903](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12903) | Thread pool e visibilidade (UV_THREADPOOL_SIZE, registrar VAR_POOL no monitor, reverter timeout) | Baixo/médio | 3 |
| [#12904](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12904) | Tirar a foto do usuário do `/api/auth/me` | Médio | 5 |
| [#12905](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12905) | Separar liveness do diagnóstico completo | Baixo | 2 |
| [#12906](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/12906) | Mover o `StoreJobProcessor` da API pro worker | Médio | 5 |

Todos: linkados entre si como Related, filhos da Epic **#10542 (Infraestrutura)** — nota: essa Epic está com State=Done, ficando com filhos ativos novos, vale considerar reabrir; atribuídos a **Fernando Caetano de Lima**; Sprint atual (**Var Retaguarda\Sprint 28**); estimativas propostas pelo PO em Fibonacci, pendentes de confirmação técnica (comentário em cada card).

## Prioridade sugerida pelo próprio documento de apuração

Pacotes #12902 e #12903 são contenção e podem ser feitos já (baixo risco, resolvem a maior parte da instabilidade). #12904, #12905 e #12906 têm escopo/risco maior (contrato de API, deploy+fila) e podem seguir o fluxo normal de refinamento.

## O que a apuração deixa claro que NÃO prova

O log da API zerou completamente entre 11:59–12:17 (01/09) e 05:31–06:00 (31/08). É tentador ler como "a API parou de responder", mas não dá pra afirmar — o autoheal não marcou a API como unhealthy nessas janelas. Pode ter sido só o *logging* que morreu (mesmo pool de threads que o Oracle disputa). O card #12903 é o primeiro passo pra fechar essa dúvida; uma métrica de event loop lag fecharia de vez (não virou card ainda — considerar se o time achar valor).

## Pendências

- Confirmação técnica das 5 estimativas propostas pelo PO (Fernando/time técnico).
- Considerar reabrir a Epic #10542 (Infraestrutura), hoje Done, já que passou a ter 5 filhos ativos.
- Considerar card futuro pra métrica de event loop lag, se #12903 não for suficiente pra provar/descartar o congelamento total da API nas janelas de log zerado.

## Reuniões

Nenhuma — apuração feita unilateralmente pelo Igor via Loki/inspeção do host, sem reunião.

## Próxima atualização

Atualizar quando Fernando confirmar/ajustar as estimativas, ou quando #12902/#12903 subirem e o efeito puder ser confirmado em produção.

---

## Incidente 2 (17/09) — HML crash-loop após queda do Redis, causa diferente

API de HML ficou 2h44 indisponível depois que um estol de I/O de disco derrubou o Redis (saída limpa, `exit 0`, não recriado pela `restart_policy: on-failure`) e o boot da API travou tentando montar o Bull Board sem Redis disponível. Apuração completa em [2026-09-17-incidente-hml-crashloop-redis.md](2026-09-17-incidente-hml-crashloop-redis.md).

**Card criado (18/09, Var Retaguarda) — em Refinement, não Ready for Dev (pedido explícito do Igor)**

| Card | Pacote | Estimativa (PO, Fibonacci) |
|---|---|---|
| [#13117](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13117) | Resiliência do boot da API — dependência externa indisponível não pode impedir a aplicação de subir (defeito técnico: `setupBullBoard`/`logBootSnapshot` roda antes de `app.listen()` em `main.ts`, sem timeout por fila) | 3 |

Enquadramento do card (ajustado em 18/09): o sintoma real onde isso dói na prática é o **deploy de homologação preso em loop de falha** sempre que a dependência externa checada no boot (Redis, no caso) está fora do ar durante a janela de deploy — dá a falsa impressão de que a PR recém-publicada quebrou algo, quando na verdade é o boot travado. Story/Descrição do card foram escritas em cima desse sintoma, não só como "resiliência de boot" abstrata.

Linkado como Related aos cards #12902-#12906 (mesma família "API instável", causas diferentes) e como filho da Epic #10542 (Infraestrutura). Fica deliberadamente em Refinement — não é reprovação no gate de DoR, é decisão de timing do Igor.

**O que a apuração deixa como achado relacionado, mas fora do escopo do card:** `restart_policy: on-failure` do Redis (infra/compose) não recria o container quando ele sai com exit 0 — é o que multiplicou 3min20s de estol de disco em 2h44 de indisponibilidade. Não virou card ainda.

**Pendência:** confirmação técnica do card #13117 e da estimativa; decidir entre as duas opções de correção do defeito (mover o snapshot pra depois do `listen()` vs. timeout por fila — não excludentes).
