# Incidente 2026-09-17 — API de HML em crash-loop após queda do Redis

**Ambiente:** Homologação · **Nó afetado:** `api-retaguarda-hml.admcuiaba.com` — **10.150.20.9** (Node 2 / Worker)
**Início:** 2026-09-17 19:32 UTC · **Restabelecido:** 22:16 UTC · **Duração total:** 2h44 de indisponibilidade
**Status:** ✅ resolvido · causa raiz confirmada empiricamente · correções estruturais pendentes (§7)

---

## 0. Topologia — em qual máquina rodar o quê

| Apelido | Hostname (`docker node ls`) | IP | Papel no Swarm | O que roda | Comandos que só funcionam aqui |
|---|---|---|---|---|---|
| **Node 1** | `portal-retaguarda-hml.admcuiaba.com` | **10.150.20.8** | **Manager (Leader)** | `nginx`, `app` (front) | `docker service *`, `docker node *`, `docker stack *` |
| **Node 2** | `api-retaguarda-hml.admcuiaba.com` | **10.150.20.9** | Worker | `api`, `worker`, `worker-excel`, `substitution-worker`, `redis`, `promtail` | `docker ps`, `docker logs`, `docker inspect` de container, `df`, `dmesg` |
| **Tools** | `tools-hml` | **10.150.20.111** | Worker | Harbor Registry, **Portainer (:9000)**, Semaphore | — |

Três armadilhas de navegação que custaram tempo nesta investigação:

1. **`docker service` / `docker node` não rodam no Node 2** — ele é worker. Para estado do Swarm é sempre o **Node 1 (10.150.20.8)**.
2. **Os logs de container só existem no Node 2 (10.150.20.9)**, onde os serviços da API rodam. Alternativa a partir do Node 1: `docker service logs <serviço>`, que o manager agrega de qualquer nó.
3. **`sudo` é necessário no Node 2 (10.150.20.9), não no Node 1 (10.150.20.8).** O usuário `admshell` está no grupo docker do manager, mas não no do worker.

> Os nós usam o domínio interno `.admcuiaba.com` (é o que aparece no `docker node ls` e nas constraints do compose). O domínio público `.avenida.com.br` é só do nginx/portal — não confunda ao procurar a máquina.

---

## 1. Resumo executivo

Um **estol de I/O de disco de 3min20s** no nó da API reprovou simultaneamente os healthchecks do Redis e da API. O Swarm encerrou as duas tasks. O Redis encerrou com **exit 0** (desligamento gracioso via SIGTERM) e, por causa da política `restart_policy: condition: on-failure`, **o Swarm nunca o recriou** — uma saída limpa não é considerada falha.

Sem Redis, a API passou a travar permanentemente no boot: o `setupBullBoard` roda **antes** do `app.listen()` e consulta as 15 filas do Bull com um `retryStrategy` que **nunca desiste**. O `await` nunca resolve, a porta nunca abre, o healthcheck reprova 3× e o container morre aos 93s. Todos os deploys subsequentes falharam nesse mesmo ponto.

**Não houve relação com nenhuma PR.** As três PRs mergeadas depois das 19:46 apenas tentaram deployar num ambiente já quebrado.

---

## 2. Linha do tempo

| Hora (UTC) | Evento |
|---|---|
| 19:11–19:17 | Build **20927** (`ed0e9fbd`) deployada. `verify: Service portal-retaguarda_api converged` às 19:17:08 — healthcheck passou, ambiente saudável |
| 19:28:45 → 19:32:04 | **Estol de I/O.** Redis loga `Asynchronous AOF fsync is taking too long (disk is busy?)` a cada ~10s, ininterruptamente |
| 19:32:10.8 | Redis: `Received SIGTERM scheduling shutdown...` |
| **19:32:11** | **API recebe SIGTERM** (1 segundo depois do Redis) |
| 19:32:13.3 | Redis: `Redis is now ready to exit, bye bye...` → **exit 0** |
| 19:32:14.8 | Container do Redis encerrado. Swarm marca `Complete`. **Nenhuma task substituta é criada** |
| 19:32:42 / 19:34:20 / 19:35:59 | 3 restarts da API (`max_attempts: 3`), 93s cada, todos falham |
| 19:46 / 20:23 / 20:34 | Builds **20937**, **20948**, **20951** — todas falham em `Atualizar servico API` |
| 20:43:00 | Último container encerrado. `UpdateStatus: paused`. Serviço em 0/1, sem tentativas |

Após 20:43 o serviço parou de tentar. HTTP 502 em `/api/health` e `/api/health/live`.

> **Atenção a fusos.** O SO do nó está em **UTC-4**; os containers rodam `TZ=America/Sao_Paulo` (UTC-3); o Grafana exibe UTC-3. Três relógios diferentes na mesma investigação.

---

## 3. Cadeia causal

```
Estol de I/O no datastore (VMware)
        │
        ├─► healthcheck do Redis (redis-cli ping) reprova  ─► SIGTERM ─► exit 0
        │        └─► restart_policy: on-failure NÃO trata exit 0 como falha
        │                 └─► Swarm nunca recria o Redis            ❰CAUSA RAIZ❱
        │
        └─► healthcheck da API (curl /api/health) reprova  ─► SIGTERM ─► exit 1
                 └─► restart_policy religa (3×)
                          └─► boot trava em setupBullBoard (Redis ausente)
                                   └─► app.listen() nunca executa
                                            └─► healthcheck reprova 3× ─► morto aos 93s
                                                     └─► LOOP
```

### 3.1 Por que a API não consegue mais bootar

`src/main.ts:82` executa `await setupBullBoard(app)` **antes** do `await app.listen(port)` (`main.ts:85`).

`src/config/bull-board.config.ts:343` chama `logBootSnapshot`, que em `:240` percorre as **15 filas** do `QUEUE_NAMES` **sequencialmente**, cada uma com `await Promise.all([queue.getJobCounts(), queue.getWorkers()])`, **sem timeout**.

`src/app.module.ts:242` configura o Bull com:

```ts
retryStrategy: (times: number) => Math.min(times * 500, 30_000),
```

O comentário no código é explícito: *"Aqui fica tentando para sempre, com backoff até 30s."* Com o Redis ausente, o `getJobCounts()` da **primeira** fila **nunca resolve nem rejeita**. Não é lentidão — é deadlock permanente. A API é estruturalmente incapaz de subir sem Redis.

### 3.2 Por que não há nenhum log de erro

O `main.ts:33` usa `bufferLogs: true`. No NestJS 10.4.22, o `useLogger()` (`main.ts:38`) só descarrega o buffer se `flushLogsOnOverride()` tiver sido chamado — e **o `main.ts` não chama**. O único outro ponto de flush está no callback do `httpAdapter.listen()`:

```js
// node_modules/@nestjs/core/nest-application.js:185
this.httpAdapter.listen(port, ..., (...) => {
    if (this.appOptions?.autoFlushLogs ?? true) { this.flushLogs(); }
```

**Todo log do Nest do boot só aparece se a porta abrir.** Como ela nunca abre, o processo morre com o buffer cheio.

As 4 linhas visíveis no log escapam por não passarem pelo logger do Nest:

| Linha | Origem |
|---|---|
| `[AUTH-DIAG][feature-flag-eval]` | `console.log` cru em `src/config/feature-flag.ts` |
| `KafkaJS v2.0.0 switched default partitioner` | logger próprio do kafkajs |
| `NOTE: ... AWS SDK for JavaScript (v2)` | warning do AWS SDK |
| `[OfmClientService] / [GftClientService] axios instance created` | `Logger` do **`nestjs-pino`** injetado por DI (escreve direto no pino) |

Confirmado em `src/modules/ofm/services/ofm.client.service.ts:3,13`.

### 3.3 Por que o container morre sempre aos 93 segundos

`Infra.Docker/docker-compose.yml`, serviço `api`:

```yaml
healthcheck:
  test: ["CMD", "curl", "-fsS", "http://localhost:3000/api/health"]
  interval: 30s
  timeout: 5s
  retries: 3
  start_period: 30s
```

Confirmado no spec aplicado (`Interval: 30000000000`, `Timeout: 5000000000`, `StartPeriod: 30000000000`, `Retries: 3`). São 3 sondas reprovadas em 30/60/90s → `unhealthy` → SIGTERM. O Swarm reporta:

```
"task: non-zero exit (1): dockerexec: unhealthy container"
```

---

## 4. Evidências

**Redis — saída limpa**
```
$ sudo docker inspect 0c8d91fd762a --format '... {{.State.ExitCode}} {{.State.OOMKilled}}'
start=2026-09-04T16:20:13Z finish=2026-09-17T19:32:14Z exit=0 oom=false err=
```

**Redis — o estol de disco e o SIGTERM**
```
19:28:45Z  * Asynchronous AOF fsync is taking too long (disk is busy?)...
   ... repetido a cada ~10s por 3min20s ...
19:32:04Z  * Asynchronous AOF fsync is taking too long (disk is busy?)...
19:32:10Z  1:signal-handler Received SIGTERM scheduling shutdown...
19:32:13Z  # Redis is now ready to exit, bye bye...
```

**Swarm — serviço abandonado**
```
$ docker service ls | grep -i portal
portal-retaguarda_api                  0/1   .../api:20951
portal-retaguarda_redis                0/1   redis:6.2-alpine
portal-retaguarda_substitution-worker  0/1   .../api:latest
portal-retaguarda_worker               1/1   .../api:20927
portal-retaguarda_worker-excel         1/1   .../api:20927

$ docker service ps portal-retaguarda_redis --no-trunc
...redis.1   Shutdown   Complete 2 hours ago     ← coluna ERROR vazia
...redis.1   Shutdown   Complete 13 days ago
```

Todos os serviços do **Node 2 (`api-retaguarda-hml.admcuiaba.com`, 10.150.20.9)** que têm healthcheck estão fora; todos **sem** healthcheck aparecem `1/1` (o que só indica processo vivo, não funcional).

**Log cru da API — blackout de 90s**
```
20:36:34.821Z  [OfmClientService] axios instance created ...
20:36:34.821Z  [GftClientService] axios instances created ...
        ← 90 segundos de silêncio absoluto
20:38:04.474Z  npm error signal SIGTERM
```
Idêntico ao Grafana — não há filtragem do promtail.

**Reincidência — `dmesg` de 4 de setembro**
```
[sex set 4 11:33:25] INFO: task bio_aof_fsync:332905 blocked for more than 122 seconds.
[sex set 4 11:33:25] INFO: task xfsaild/dm-0:581  blocked for more than 122 seconds.
[sex set 4 11:33:25] INFO: task promtail:261963   blocked for more than 122 seconds.
```
`bio_aof_fsync` é a thread de AOF do Redis. O container atual do Redis foi criado em **2026-09-04 12:20** — nasceu exatamente dessa ocorrência anterior.

---

## 5. Hipóteses descartadas

| Hipótese | Evidência que descarta |
|---|---|
| Disco cheio | `df -h`: 81% usado, 27G livres em `/var/lib/docker` |
| OOM | `State.OOMKilled = false` |
| Reboot do nó | `uptime`: up 222 days |
| Oracle inalcançável | Listener `172.16.10.2:1521` responde; API funcionou até 19:32 |
| Regressão de código (PR) | Build 20927 convergiu saudável às 19:17 e a **mesma imagem** parou de subir às 19:32, sem deploy no intervalo |
| Deploy de stack / CI | Nenhum run do `Infra.Docker` em 17/09. PR Validators rodam em `vmImage: ubuntu-22.04` (agente hospedado), não nos nós |

---

## 6. Defeitos identificados

| # | Defeito | Severidade | Local |
|---|---|---|---|
| **D1** | `restart_policy: condition: on-failure` em serviço cujo processo sai com 0 no SIGTERM. O Redis é **estruturalmente incapaz** de se recuperar de uma morte por healthcheck | 🔴 Crítica | `Infra.Docker/docker-compose.yml` |
| **D2** | `setupBullBoard` bloqueia o `app.listen()` varrendo 15 filas sem timeout, com `retryStrategy` infinito. Redis fora = API nunca sobe | 🔴 Crítica | `main.ts:82` · `bull-board.config.ts:240` · `app.module.ts:242` |
| **D3** | `bufferLogs: true` sem `flushLogsOnOverride()`: qualquer falha antes do `listen()` é **totalmente muda** | 🔴 Crítica (observabilidade) | `main.ts:33,38` |
| **D4** | Healthcheck sonda `/api/health` (verifica LDAP/AWS/Oracle) em vez de `/api/health/live`, criado em 09/09 exatamente para isso | 🟡 Média | `docker-compose.yml` · `healthCheck.controller.ts:32,45` |
| **D5** | `substitution-worker` fora do ar há **13 dias** pelo mesmo mecanismo do D1, sem nenhum alerta. Agravante: o serviço **não consta nos passos de deploy** do `deploy-develop.yml` (só API, Worker e Worker Excel) — nunca é atualizado por CI, o que explica ele estar preso em `:latest` e à deriva do restante da stack | 🟠 Alta | `docker-compose.yml` · `deploy-develop.yml` |
| **D6** | Sem alerta de serviço em 0/N. O incidente só foi notado pela falha da pipeline, ~30min depois | 🟠 Alta | Monitoramento |
| **D7** | Estol de I/O recorrente no datastore do **Node 2 — `api-retaguarda-hml.admcuiaba.com` (10.150.20.9)** (17/09 e 04/09) | 🟠 Alta | Infra VMware — VM VMware |
| **D8** | Deploy **não idempotente**: `docker service update --image <tag-já-vigente>` é no-op, não cria task nova, e a task da pipeline morre por `timeoutInMinutes: 3` com mensagem que parece erro de aplicação. Descoberto ao tentar o re-deploy — custou uma tentativa perdida | 🟠 Alta | `.azuredevops/templates/deploy-develop.yml` |
| **D9** | `vm.overcommit_memory` não definido. Redis loga `WARNING Memory overcommit must be enabled!` — é justamente a config que protege *background saves* sob pressão de memória | 🟡 Média | **Node 2 — `api-retaguarda-hml.admcuiaba.com` (10.150.20.9)**, `/etc/sysctl.conf` |
| **D10** | `RABBITMQ_URI` no grupo `HML_API` da Library é variável **não-secreta**, com usuário e senha em texto claro, visível a qualquer leitor do grupo | 🟠 Alta (segurança) | Azure DevOps Library |

---

## 7. Proposta de correção

### 7.1 Imediata — restabelecer o serviço

Ordem obrigatória: **Redis primeiro**, API depois. A API não sobe enquanto o Redis não estiver 1/1.

```bash
docker service update --force portal-retaguarda_redis
# aguardar 1/1, então:
docker service update --force portal-retaguarda_api
```

> **`--force` recria a task com o mesmo spec — inclusive o mesmo digest de imagem.** Serve para ressuscitar um serviço parado, não para atualizá-lo. Para trocar a versão é obrigatório `--image <tag>`, que re-resolve o digest. O `substitution-worker` ilustra a armadilha: seu spec é `api:latest@sha256:420131fa86…`, com o digest congelado há 13+ dias — um `--force` o traria de volta rodando código antigo. Nele use:
>
> ```bash
> docker service update --with-registry-auth \
>   --image $REGISTRY/portal-retaguarda/homolog/api:<TAG_ATUAL> portal-retaguarda_substitution-worker
> ```

Executar no **Node 1 — `portal-retaguarda-hml.admcuiaba.com` (10.150.20.8)**, o manager; `docker service` não funciona no Node 2. Sem linha de comando, o equivalente é o **Portainer** no servidor de tools (`tools-hml.avenida.com.br:9000`, **10.150.20.111**) → Services → *Update the service* / *Force redeploy*. Ver §8.

### 7.2 D1 — política de restart (uma linha, maior retorno)

Em `Infra.Docker/docker-compose.yml`, nos serviços `redis`, `api` e `substitution-worker`:

```yaml
restart_policy:
  condition: any      # era: on-failure
  delay: 5s
  max_attempts: 5
  window: 120s
```

`any` religa a task independentemente do código de saída. Elimina a classe inteira de falha: um processo que trata SIGTERM corretamente deixa de ser punido por isso.

### 7.3 D2 — tirar o Bull Board do caminho do boot

Duas opções, não excludentes:

1. **Mover o `logBootSnapshot` para depois do `app.listen()`.** É um log de diagnóstico; não pode decidir se a aplicação sobe.
2. **Envelopar cada fila com deadline** em `bull-board.config.ts:240`:
   ```ts
   const counts = await Promise.race([
     queue.getJobCounts(),
     new Promise((_, rej) => setTimeout(() => rej(new Error("snapshot timeout")), 2000)),
   ]);
   ```
   O `catch` por fila já existe em `:255`.

O `retryStrategy` infinito do `app.module.ts:242` **deve ser mantido** — ele existe por um motivo documentado (evitar fila zumbi). O defeito não é o retry infinito; é o boot depender dele.

### 7.4 D3 — devolver a visibilidade do boot

Em `src/main.ts`, logo após o `NestFactory.create`:

```ts
app.flushLogsOnOverride();
app.useLogger(app.get(Logger));
```

Uma linha. Elimina o blackout que tornou esta investigação inteiramente às cegas.

### 7.5 D4 — apontar o healthcheck para a rota certa

```yaml
test: ["CMD", "curl", "-fsS", "http://localhost:3000/api/health/live"]
```

`/api/health/live` (`healthCheck.controller.ts:32`) responde sem tocar em LDAP, AWS ou banco. A rota `/api/health` mantém o diagnóstico completo para consumo humano.

> Observação: o `HealthCheckService` injeta `@Inject("VarDataSource")` no construtor, acoplando a sonda de liveness ao pool Oracle. Vale desacoplar num segundo momento.

### 7.6 D6 — alerta de disponibilidade

Alerta no Grafana para `réplicas rodando < réplicas desejadas` por mais de 2 minutos, por serviço. Um serviço em 0/N por 13 dias sem ninguém notar é o defeito mais barato de corrigir e o de maior retorno operacional.

### 7.7 D7 — escalar para infra

Abrir chamado informando **a máquina e as janelas exatas**:

> **VM:** `api-retaguarda-hml.admcuiaba.com` — **10.150.20.9** (Node 2 do Swarm de HML).
> VM VMware, confirmado pelos módulos do kernel `vmw_pvscsi` e `vmw_balloon`. Sem reboot há 222 dias.
> Armazenamento: `/dev/mapper/ol-home` (XFS sobre LVM), servindo `/var/lib/docker` e `/home`.
>
> **Janelas com estol de I/O confirmado:**
> - **2026-09-17, 19:28–19:32 UTC** — `Asynchronous AOF fsync is taking too long (disk is busy?)` a cada ~10s nos logs do Redis, por 3min20s
> - **2026-09-04, ~15:33 UTC** — `bio_aof_fsync`, `xfsaild/dm-0`, `promtail` e `containerd-shim` bloqueados >122s no `dmesg`

Pedir verificação de latência do datastore do host ESXi nessas duas janelas. Não é falta de espaço (81% usado, 27G livres) nem de memória (9,2Gi disponíveis) — é latência.

O `sysstat`/`sar` **não está instalado** nessa VM: não há histórico de I/O para consultar depois do fato. Instalá-lo é pré-requisito para diagnosticar a próxima ocorrência sem depender do log do Redis como única testemunha.

---

## 8. Formas de executar a correção imediata

| Via | Avaliação |
|---|---|
| **Portainer** — `tools-hml.avenida.com.br:9000` (**10.150.20.111**) | ✅ UI de gestão já conectada ao Swarm. Services → `portal-retaguarda_redis` → *Update the service*. Sem linha de comando. ⚠️ Emite **a mesma chamada de API** que o `docker service update --force` — é a mesma operação com mouse, não uma mais segura |
| `docker service update --force` no **Node 1 — `portal-retaguarda-hml.admcuiaba.com` (10.150.20.8)** | ✅ **Foi o caminho usado.** Correto e cirúrgico; exige SSH ao manager. Não funciona a partir do Node 2 |
| Pipeline **Infra.Docker** (`pipelines/main.yml`) | ⚠️ **Não recomendada para este caso.** O job remove as redes overlay (`docker network rm app-network api-network redis-network monitoring`) e executa `docker stack deploy --prune`. Raio de impacto muito maior que o problema, e o `--prune` remove serviços ausentes do compose. Também trocaria a imagem da API de `:20951` para `:latest` (hoje o mesmo conteúdo — o build empurra as duas tags — mas desfaz o pin) |
| Pipeline **ConciliaçãoCaixaAPI** | ❌ Não resolve. Só faz `service update --image` na API e nos workers; não toca no Redis, e a API voltará a travar |

---

## 9. Lições

1. **`Complete` ≠ `Failed` no Swarm.** Um processo que trata SIGTERM corretamente sai com 0, e `on-failure` o abandona. Comportamento correto do processo punido pela configuração.
2. **Falha transitória virou permanente** por política de restart. O estol de disco durou 3 minutos; a indisponibilidade durou mais de 5 horas.
3. **Dependência externa não pode bloquear o `listen()`.** Uma app que não abre a porta é indistinguível de uma app morta para qualquer orquestrador.
4. **Log em buffer sem flush garantido é pior que não ter log** — dá a falsa impressão de que a aplicação não chegou a executar nada.
5. **Correlação temporal não é causalidade.** As três PRs mergeadas após as 19:46 eram as suspeitas naturais e nenhuma tinha relação; a prova foi a mesma imagem ter subido saudável às 19:17 e falhado às 19:32 sem deploy no intervalo.

---

---

## 10. Resolução aplicada

Executado no **Node 1 — `portal-retaguarda-hml.admcuiaba.com` (10.150.20.8)**, o manager, em 2026-09-17 entre 22:01 e 22:16 UTC:

```bash
docker service update --force portal-retaguarda_redis          # 22:01 — converged, 1/1 healthy
docker service update --force portal-retaguarda_api            # 22:16 — converged, 1/1
docker service update --force portal-retaguarda_worker
docker service update --force portal-retaguarda_worker-excel
```

**Verificação pós-correção** (`/api/health`, 22:18 UTC):

```
HTTP 200 · ok=true · status=healthy · uptime=107s
ldap = up   (5ms)
aws  = up (525ms)
db   = up  (21ms)
pool: inUse=0 open=2 alias=VAR_POOL
```

### 10.1 A causa raiz foi confirmada empiricamente

O pool Oracle abriu em **21ms**, com `open=2` (exatamente o `poolMin`). Oracle nunca foi o impedimento em momento algum. Restaurado o Redis, a API subiu na primeira tentativa. Isso valida a cadeia causal da §3: o travamento era o deadlock do Bull no `setupBullBoard`, e não qualquer outra dependência.

### 10.2 Duas tentativas perdidas, ambas instrutivas

1. **Re-run da pipeline (22:06)** — falhou por timeout **sem criar container nenhum**. O serviço já estava em `api:20951`, então o `docker service update --image` foi no-op. A prova está no `docker service logs`: a entrada mais recente era de **20:43**, anterior ao próprio re-run. As ~180 linhas repetidas de `dockerexec: unhealthy container` no log da pipeline eram o CLI reimprimindo o estado de uma task morta, não novas falhas. → **D8**.
2. **Hipótese de rede descartada** — `docker service inspect` mostrou `api` e `redis` no mesmo overlay (`portal-retaguarda_default`, target `nudmllo4i208…`), com os aliases `api` e `redis`, batendo com `REDIS_HOST=redis`. DNS nunca foi o problema.

### 10.3 Reconciliação final — build 20953

A saída do D8 foi disparar uma **run nova** (não um re-run): `Build.BuildId` novo ⇒ tag nova ⇒ nenhum passo cai no no-op. Não exigiu PR — `develop` HEAD continuava em `cea32319`, o mesmo código já deployado, então a run trocou apenas a etiqueta.

```
build 20953 (20260917.10) · develop · cea32319 · succeeded
  Atualizar servico API            succeeded   43s
  Atualizar servico Worker         succeeded   12s
  Atualizar servico Worker Excel   succeeded   13s

/api/health → 200 · ok=true · status=healthy
  ldap=up · aws=up · db=up (22ms) · pool inUse=0 open=2 VAR_POOL
```

Os 43s de convergência da API reproduzem o perfil da build 20927 pré-incidente, confirmando retorno ao comportamento normal.

### 10.4 Pendência remanescente

`portal-retaguarda_substitution-worker` continua **0/1**, fora desde 04/09. A CI não o cobre (D5), então precisa de ação manual — e com `--image`, não `--force`, pelo digest congelado:

```bash
docker service update --with-registry-auth \
  --image tools-hml.avenida.com.br/portal-retaguarda/homolog/api:20953 \
  portal-retaguarda_substitution-worker
```

---

*Investigação conduzida em 2026-09-17. Serviço restabelecido às 22:16 UTC. As correções estruturais da §7 permanecem pendentes — sem elas, o próximo estol de disco reproduz o incidente integralmente.*
