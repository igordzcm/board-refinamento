# API Retaguarda — plano de ação pós-incidente (01/09/2026)

> Apuração feita em 01/09/2026 a partir do relato de que "a API caiu, aparentemente na busca do
> saldo do caixa na conciliação de lojas". Evidência tirada do Loki de produção (dashboard
> Api Logs - APIS PRT, `logging="retaguardaProd"`) e de inspeção somente-leitura no host da API.
> Nada foi alterado em produção durante a apuração.
>
> Este documento é o plano do que será feito e por quê. O diagnóstico está resumido em seguida,
> e a evidência completa de cada afirmação está no anexo, com as consultas para reconferir.

## O que será feito

| Pacote | Itens | Onde | Risco |
|---|---|---|---|
| **1. Contenção imediata** | Corrigir o healthcheck do nginx | repo `infra` | Baixo |
| **2. Thread pool e visibilidade** | `UV_THREADPOOL_SIZE` + log no boot + registrar o `VAR_POOL` no monitor + reverter o timeout de 25s | API + env de prod | Baixo/médio |
| **3. Foto fora do `/api/auth/me`** | Endpoint próprio para a imagem, com `ETag` | API + front | Médio |
| **4. Liveness separado do diagnóstico** | Rota de liveness sem dependência externa | API + `infra` | Baixo |
| **5. Batch fora da API** | Mover o `StoreJobProcessor` para o worker | API + deploy | Médio |

Os pacotes 1 e 2 são contenção e dão para fazer já. Os pacotes 3, 4 e 5 são card próprio.

O pacote 2 tem quatro itens de propósito. Não é conveniência: as quatro coisas são a mesma
investigação, e fazer só a primeira deixa o time sem como provar se funcionou. Está explicado
na seção do pacote.

### Aviso sobre horários

Três relógios diferentes nesta apuração, o que confunde quem for reconferir:

- O host de produção está em **-04**.
- Os containers (autoheal, por exemplo) logam em **UTC**.
- O Grafana mostra no fuso do navegador, ou seja **BRT (-03)**.

Todos os horários deste documento estão em **BRT**, que é o que aparece no Grafana.

---

# Diagnóstico

São **três problemas independentes**, e o mais barulhento não é o que estava sendo discutido.

## Achado 1 — o healthcheck do nginx reprova sempre

A sonda configurada é `curl -f http://localhost:80`, ou seja, a raiz. Não existe rota para `/`.
Sondei o container ao vivo:

```
/            -> 404
/api/health  -> 200
```

O nginx responde e proxia normalmente. Mas `curl -f` trata 404 como falha (exit 22), então o
healthcheck **nunca** passa. A última sonda registrada confirma:
`curl: (22) The requested URL returned error: 404`.

O `autoheal-retaguarda` (willfarrell/autoheal, `AUTOHEAL_CONTAINER_LABEL=all`) reinicia qualquer
container unhealthy. Contagem dos eventos dele nas últimas 26h:

```
583  /nginx_dev_container-retaguarda
  1  /api_dev_container-retaguarda
```

O ciclo de ~2min40s é exatamente o `interval 30s x retries 5` = 150s que o nginx leva para ser
declarado unhealthy de novo depois de cada restart. O loop começou em **31/08 11:27** e continua.
O `RestartCount` do container aparece zerado porque quem reinicia é o autoheal, não a restart
policy — por isso isso passou despercebido.

Cada reinício derruba as conexões em curso na porta de entrada da API, de dois em dois minutos e
meio, o dia inteiro. **Provavelmente é daqui que vem a maior parte da instabilidade que os
usuários relatam.** Tratado no pacote 1.

## Achado 2 — Oracle em thick mode com o thread pool padrão do Node

Aparecem no log de produção, em vários dias:

```
[ORACLE] listOpenCashRegisterCodesByStoreAndDate excedeu 4500ms aguardando conexao do pool RTG (possivel saturacao)
[ORACLE] findStoreOptionsWithDetails excedeu 25000ms aguardando conexao do pool RTG (possivel saturacao)
[TRANSACOES] [ORACLE] listAllNextDayDepositsOfDay excedeu 25000ms aguardando conexao do pool RTG (possivel saturacao)
[findUserInLogix] Query timeout após 5000ms
```

O `findUserInLogix` da última linha vem do endpoint do Logix (`logix.controller.ts:68`), **não**
do `/api/auth/me` — vale registrar porque a semelhança dos nomes engana, e eu mesmo troquei os
dois na primeira leitura.

### "Saturação" é o nome errado

O pool RTG **nunca passou de 5 conexões em uso de 15** em 48 horas. Conferido faixa por faixa nos
`[SUMMARY]` do `OraclePoolMonitorService`, que sai a cada 10s:

| Conexões em uso no pool RTG | Ocorrências em 48h |
|---|---|
| 0 | 14.885 |
| 1 a 2 | 97 |
| 3 a 5 | 2 |
| 6 a 9 | 0 |
| 10 ou mais | 0 |

Ninguém estava esperando vaga no pool. O `getConnection()` estava esperando **outra coisa**.

### A causa

Inspeção do processo dentro do container (o PID 1 é o `npm`, a aplicação é o PID 18):

```
PID=18   libclntsh mapeada: 8   threads: 18
   5 libuv-worker      3 tokio-runtime-w      1 MainThread
   4 V8Worker          2 WorkerThread         1 futures-timer  ...

NODE_ENV=production
LD_LIBRARY_PATH=/opt/oracle/instantclient_19_24
UV_THREADPOOL_SIZE = undefined
nproc = 4          container limitado a 3 CPUs
```

A `libclntsh` (Oracle Instant Client) está mapeada no processo: o driver roda em **thick mode**.
Vem de `src/var.module.ts:26`:

```ts
thickMode: isProductionEnvironment() || isHomologationEnvironment(),
```

E não fica restrito ao TypeORM: o `OracleDriver` chama `initOracleClient()`
(`node_modules/typeorm/driver/oracle/OracleDriver.js:810`), que liga thick mode **no processo
inteiro** — inclusive no pool RTG do `DynamicOracleService`, que não tem relação nenhuma com o
TypeORM.

Em thick mode, toda ida ao Oracle ocupa uma thread do libuv pela duração inteira da chamada,
**incluindo a aquisição da conexão**. E o `UV_THREADPOOL_SIZE` não está definido em lugar nenhum
— nem no código, nem no `Dockerfile.prod`, nem no env do container. São 5 threads para:

- `VAR_POOL` (TypeORM), `poolMax: 50` — `src/var.module.ts:29`
- pool RTG (`DynamicOracleService`), `poolMax: 15` — `dynamic-oracle.service.ts:87`
- um pool de 15 por loja, criado sob demanda
- o `StoreJobProcessor`, que roda dentro do processo da API em produção

### Duas confirmações cruzadas

1. **O Oracle não caiu.** Nas janelas de falha, `var_service` seguiu com 2.000 a 7.000 linhas por
   minuto e taxa de erro normal, e `tesouraria_api` com zero erro. O problema é nosso.
2. **O que era Postgres continuou funcionando.** As `tokio-runtime-w` na lista de threads são do
   engine do Prisma, que tem runtime próprio em Rust e não usa o pool do libuv. No log, durante o
   apagão, as operações de Postgres continuaram saindo e as de Oracle pararam. É exatamente o
   corte que a explicação prevê.

### O elo com o saldo do caixa

A primeira exceção do apagão de hoje, às 11:59:51, é a tela do relato:

```
ServiceUnavailableException: Não foi possível ler o saldo parcial dos operadores no VAR Retaguarda
   at PartialOperatorBalanceService.fetchFromVar
   at StoreConciliationController.getPartialOperatorBalances
```

Custo acumulado por endpoint nos 21 minutos anteriores:

| Endpoint | Chamadas | Tempo total | Pico |
|---|---|---|---|
| `/api/auth/me` | 115 | 310.406 ms | 10.928 ms |
| `/api/health` | 95 | 190.204 ms | 2.004 ms |
| `/api/store-conciliation/:id/partial-operators` | 34 | 105.783 ms | 16.162 ms |

Cuidado ao ler essa tabela: **só a terceira linha é custo de Oracle.** O `/api/auth/me` gasta esse
tempo no Microsoft Graph (achado 3) e os 2 segundos fixos do `/api/health` são o timeout do check
da AWS, que falha sempre (pacote 4).

Entre os que tocam o Oracle, o `partial-operators` é o mais caro por chamada. Desde o merge
`16b01edfb` (31/08) ele dispara **duas** queries em paralelo por request — o `Promise.all` do
`fetchFromVar`, com o `listOpenCashRegisterCodesByStoreAndDate` que entrou junto. São duas das
cinco threads por usuário que abre a tela.

Não é que a tela seja a culpada. Ela é a maior consumidora por request num orçamento de threads
que já estava apertado, e por isso é onde a falha aparece primeiro.

Tratado no pacote 2.

## Achado 3 — o `/api/auth/me` baixa a foto do usuário a cada chamada

`AuthService.getMe` (`src/auth/auth.service.ts:1915`) faz três coisas por chamada:

```ts
const userDb    = await this.userService.findByEmail(...);                      // Postgres
const userPhoto = await this.microsoftGraphService.getUserPhotoByEmail(...);    // Azure AD
const inheritance = await this.inheritanceResolver.resolveInheritedGroups(...); // Postgres
```

E o `getUserPhotoByEmail` (`src/auth/microsoft-graph/microsoft-graph.service.ts:48`) faz, **toda
vez, sem cache nenhum**:

```ts
const client = await this.getGraphClient();                    // token MSAL
const photoResponse = await client.api(`/users/${email}/photo/$value`).get();
const base64Photo = Buffer.from(photoResponse).toString("base64");
return `data:image/jpeg;base64,${base64Photo}`;
```

Cada navegação do usuário baixa a foto de perfil dele do Microsoft Graph e devolve a imagem
inteira em base64 embutida no JSON. 115 chamadas em 21 minutos, média de 2,7 segundos, pico de
10,9 segundos. É a rota mais cara do sistema e está no caminho de toda navegação.

Não causou o incidente. Mas piora tudo em volta, e por dois caminhos: o payload (uma foto de
~30 KB vira ~40 KB em base64, trafegados em toda chamada) e a chamada HTTPS externa, que passa por
`dns.lookup()` — que no Node usa **o mesmo thread pool do libuv** que o Oracle está consumindo.
Ou seja, o `/me` não é só vítima da falta de threads, ele contribui para ela a cada requisição.

Tratado no pacote 3.

---

# Os pacotes

## Pacote 1 — corrigir o healthcheck do nginx

### O que muda

Criar um endpoint de saúde no próprio nginx e apontar a sonda para ele:

```nginx
location = /healthz { access_log off; return 200 "ok\n"; }
```

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:80/healthz"]
```

### Por quê assim

A alternativa óbvia é apontar a sonda para `http://localhost:80/api/health`, que também resolve o
loop em uma linha. Não é o que eu faria: isso acopla a saúde do nginx à da API, e aí uma
indisponibilidade da API passa a reiniciar o nginx junto — que é exatamente o efeito em cascata
que a gente quer evitar. O healthcheck do nginx deve dizer se o nginx está de pé, e mais nada.

### Onde mexer

O compose de produção vem pelo pipeline (`infra/docker-compose.prod.yml`), então a correção é no
repo `infra` e sobe por deploy. Editar o arquivo direto na máquina seria sobrescrito no próximo
release.

### Risco e validação

Risco baixo: é config de healthcheck, reversível, e o pior caso é voltar ao comportamento atual.

Para validar: `docker inspect nginx_dev_container-retaguarda` deve mostrar
`Health.Status=healthy`, e o log do autoheal deve parar de citar o nginx.

## Pacote 2 — thread pool e visibilidade

Quatro itens que sobem juntos.

### 2.1 Definir `UV_THREADPOOL_SIZE`

Colocar `UV_THREADPOOL_SIZE=32` no env de produção.

**Por quê 32:** a orientação do próprio driver é dimensionar o thread pool pelo número de conexões
Oracle simultâneas — o `oracledb` inclusive expõe `UV_THREADPOOL_SIZE` nas estatísticas de pool
(`node_modules/oracledb/lib/poolStatistics.js:83`), sinal de que trata isso como parâmetro de
primeira classe. Com os `poolMax` somando 65, cinco threads é ordem de grandeza errada. Igualar a
65 de cara também não faz sentido: thread custa memória e o container só tem 3 CPUs. Começar em 32
e observar.

### 2.2 Logar o valor no boot

Acrescentar o `UV_THREADPOOL_SIZE` na linha de configuração de pool que já é logada no boot
(`[ORACLE POOL] Configuration: poolMin=..., poolMax=..., queueTimeout=...`).

**Por quê:** hoje esse número não aparece em lugar nenhum — nem no log, nem no env, nem no
Dockerfile. É parte do motivo de isso ter passado tanto tempo despercebido. Sem ele registrado,
daqui a três meses ninguém vai saber com que valor a aplicação subiu.

### 2.3 Registrar o `VAR_POOL` no monitor de pools

O `OraclePoolMonitorService` só conhece o pool RTG e os de loja
(`dynamic-oracle.service.ts:463` e `:544`). O `VAR_POOL`, criado pelo TypeORM em
`var.module.ts:33`, **nunca é registrado** — não tem alerta, não tem histórico, não entra no
`[SUMMARY]` e não passa pela detecção de leak.

**Por quê junto com o resto:** ele é o maior dos três (`poolMax: 50`) e atende Logix, cash-balance
e tudo que herda de `BaseOracle`. Depois de mexer no thread pool, a forma de saber se resolveu é
olhar ocupação de pool. Se o maior pool é invisível, o time vai medir o efeito no lugar errado e
concluir o que não deve.

### 2.4 Reverter o `RTG_ACQUIRE_TIMEOUT_MS`

Em 31/08 às 22:05 o commit `1bbe311ba` subiu o `RTG_ACQUIRE_TIMEOUT_MS` de 4500 para 25000 e o
`QUEUE_TIMEOUT_MS` de 5000 para 30000, tentando resolver esse mesmo problema. Dá para ver a troca
no log de produção: até 22:05 os erros dizem "excedeu 4500ms", depois passam a dizer "excedeu
25000ms".

Não atacou a causa. Só fez cada requisição presa segurar recurso por 25 segundos em vez de 4,5 —
o que, com poucas threads, piora a fila em vez de aliviar.

**Por quê no mesmo pacote:** se corrigir o thread pool e deixar o paliativo, o paliativo continua
atrapalhando e ainda mascara o resultado da medição. Voltar para algo próximo do valor anterior,
com o thread pool corrigido, é o teste de que a causa era outra.

### Risco e validação do pacote

Risco baixo a médio. Mais threads consomem mais memória e mais troca de contexto, mas o container
tem 10 GB de limite e usa cerca de 450 MB.

Para validar: com o valor logado no boot e o `VAR_POOL` no `[SUMMARY]`, acompanhar um dia. Os
erros de "aguardando conexao do pool RTG" devem desaparecer. Se sumirem com os pools continuando
ociosos, a causa era essa.

## Pacote 3 — tirar a foto do `/api/auth/me`

### O que muda

1. `/me` devolve `photo_url: "/api/users/<id>/photo"` em vez do base64. O payload cai de dezenas
   de KB para algumas centenas de bytes.
2. Um endpoint próprio serve a imagem com `Cache-Control: private, max-age=86400` e `ETag`.
3. O navegador passa a cachear. Na segunda visita ele manda `If-None-Match` e recebe `304`, sem
   corpo.

### Por que não é cache

A primeira ideia é cachear a resposta do `me`. Não dá, por dois motivos independentes de escala:

- O payload carrega `user_permission_group` e `substitution`. Cachear permissão significa que
  revogar o acesso de alguém só passa a valer depois do TTL. Isso é problema de segurança, não de
  performance.
- A parte cara é a foto, que quase nunca muda. Não faz sentido amarrar ela ao resto.

E cachear só a foto no servidor esbarra em memória. O cache é dimensionado pelos usuários **ativos
na janela do TTL**, não pelo total cadastrado — quem não fez request não ocupa espaço. Mas o valor
é grande:

| Usuários ativos na janela | Memória aproximada |
|---|---|
| 500 | ~20 MB |
| 5.000 | ~200 MB |
| 50.000 | ~2 GB |

Na escala de hoje é tranquilo. Numa base grande, não fecha. E, principalmente: mesmo com cache,
cada request continuaria carregando 40 KB de base64 no corpo. O cache mudaria de onde a foto vem,
não o fato de ela ser enviada de novo toda vez.

Com o endpoint separado, a memória do servidor fica **constante**, não importa quantos usuários
existam. Quem guarda é o navegador de cada um, que é onde esse dado deveria estar.

Se ainda quiserem cache no servidor, ele entra **no endpoint novo**, com teto fixo — LRU de 1000
entradas e TTL de uma hora, por exemplo. Aí o limite é por construção (1000 x 40 KB = 40 MB) e não
cresce com a base. É a diferença entre um cache com teto e um vazamento lento.

### Alternativa mais barata, se o contrato não puder mudar agora

Manter o campo devolvendo o base64 e colocar um LRU com teto no serviço. Resolve o tempo de
resposta, não resolve o payload. É meio caminho, e vale se o front não puder acompanhar no mesmo
release.

### Risco e validação

Risco médio: mexe em contrato de API, o front precisa sair junto.

Para validar: o `/api/auth/me` cai de ~2,7s para dezenas de milissegundos, e o tamanho da resposta
cai de dezenas de KB para centenas de bytes.

## Pacote 4 — separar liveness do diagnóstico

### O problema

O healthcheck do container da API é `curl -f http://localhost:3000/api/health` com `timeout 5s`,
`interval 10s` e `retries 3`. E a rota leva 2002 ms fixos, sempre.

O motivo está no `healthCheck.service.ts:152`: os três checks rodam em `Promise.allSettled`, então
o tempo total é o do mais lento. O mais lento é o `checkAWS` (`healthCheck.service.ts:345`), que
bate em `https://s3.us-east-1.amazonaws.com` e **falha sempre**, estourando o deadline de 2
segundos:

```
AWS (us-east-1) health check: DOWN - Request timeout after 2000ms
Health degraded (aws=down database=saturated) - reported only, container stays up
```

Duas consequências. A primeira: sobram 3 segundos de margem no healthcheck, e agora que sabemos do
autoheal, qualquer lentidão que empurre a rota além dos 5s faz o container ser reiniciado. A
segunda: existe um alarme permanente de `aws=down` que ninguém consegue acionar e que todo mundo
já aprendeu a ignorar — que é a pior coisa que um alarme pode virar.

### O que muda

Separar as duas responsabilidades:

- `/api/health/live` — responde 200 sem tocar em nada externo. É o que o container sonda.
- `/api/health` — continua com o diagnóstico completo (LDAP, AWS, banco), para uso humano e de
  monitoração.

E decidir o que fazer com o check da AWS: ou libera a saída para o S3 e ele volta a ser
informativo, ou tira ele do payload. Do jeito que está, ele só produz ruído.

### Risco e validação

Risco baixo: rota nova, e a mudança no compose é de uma linha.

Para validar: o healthcheck do container passa a responder em milissegundos, e o `/api/health`
continua mostrando o estado real dos três serviços para quem for olhar.

## Pacote 5 — tirar o `StoreJobProcessor` da API

O batch de lojas roda hoje dentro do mesmo processo que atende usuário — confirmado pelos 367
registros de `StoreJobProcessor` no log do container da API. Existe worker para isso.

Enquanto estiverem juntos, o job da madrugada e a tela do analista dividem as mesmas threads e as
mesmas 3 CPUs. Não à toa, uma das duas janelas de apagão (31/08, 05:31 às 06:00) coincide com o
horário do batch.

Fica por último porque exige cuidado com deploy e com a fila, e porque o pacote 2 já deve reduzir
bastante o sintoma. Mas enquanto não for feito, o risco continua estruturalmente presente.

Para validar: `[STORE]` some do log do container da API e passa a aparecer no do worker.

---

# O que este documento não prova

Sendo honesto sobre os limites da apuração, porque isso muda a gravidade.

O log da API zerou completamente entre **11:59 e 12:17** de hoje, e também entre **05:31 e 06:00**
de 31/08. É tentador ler isso como "a API parou de responder", mas **não dá para afirmar**. O
autoheal não marcou a API como unhealthy nessa janela — o único restart automático da API foi às
07:33. O reinício das 12:16 foi manual, feito por uma pessoa.

Se o healthcheck interno continuou passando, então a API estava servindo e o que morreu foi o
**logging**. Isso também é explicado pela mesma causa: o transport do pino usa worker thread e
escreve pelo mesmo pool do libuv.

Ou seja: **o apagão de log é fato, o congelamento total não é.** Separar os dois exige
instrumentação que hoje não existe. O pacote 2 é o primeiro passo nisso; uma métrica de event loop
lag fecharia a questão de vez, e vale considerar como item futuro.

Vale notar também que o `OraclePoolMonitorService` some justamente quando é mais necessário: o
`[SUMMARY]` de 10 em 10 segundos parou junto com o resto do log.

---

# Anexo — como reconferir

### No Grafana (dashboard Api Logs - APIS PRT, Loja `retaguardaProd`, Serviço `api_dev_container-retaguarda`)

```logql
# requisições concluídas por minuto — o apagão aparece como buraco
sum(count_over_time({logging="retaguardaProd", service_name="api_dev_container-retaguarda"} |= "request completed" [1m]))

# timeouts de aquisição de conexão
{logging="retaguardaProd", service_name="api_dev_container-retaguarda"} |~ "satura|aguardando conexao"

# ocupação do pool RTG (o terceiro número é o poolMax)
{logging="retaguardaProd", service_name="api_dev_container-retaguarda"} |= "[SUMMARY]" |~ "RTG\\([6-9]/"

# reinícios
{logging="retaguardaProd", service_name="api_dev_container-retaguarda"} |= "Starting Nest application"
```

### No host (tudo somente leitura)

```bash
# quem o autoheal está reiniciando
docker logs autoheal-retaguarda --since 26h 2>&1 \
  | grep -oE '/[a-z_0-9-]+_?container-retaguarda' | sort | uniq -c

# a sonda do nginx contra o que existe de verdade
docker exec nginx_dev_container-retaguarda curl -s -o /dev/null -w '%{http_code}\n' http://localhost:80/
docker exec nginx_dev_container-retaguarda curl -s -o /dev/null -w '%{http_code}\n' http://localhost:80/api/health

# thick mode e threads do processo da aplicação (PID 1 é o npm, não serve)
docker exec api_dev_container-retaguarda sh -c \
  'for p in /proc/[0-9]*; do if grep -qa "dist/main.js" $p/cmdline 2>/dev/null; then
     echo "PID=${p#/proc/}"; grep -c libclntsh $p/maps; ls $p/task | wc -l; fi; done'

# env do container
docker inspect api_dev_container-retaguarda \
  --format '{{range .Config.Env}}{{println .}}{{end}}' | grep -Ei 'UV_THREAD|NODE_ENV|LD_LIBRARY'

# healthcheck configurado (API e nginx)
docker inspect api_dev_container-retaguarda   --format '{{json .Config.Healthcheck}}'
docker inspect nginx_dev_container-retaguarda --format '{{json .Config.Healthcheck}}'
```
