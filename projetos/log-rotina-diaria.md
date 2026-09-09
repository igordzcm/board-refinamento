# Log da rotina diária (daily-digest + board-sync)

> Atualizado a cada execução da rotina automática (seg-sex, 8h). Entrada mais nova primeiro. Cada entrada documenta **o que rodou, o que mudou, por quê, e com base em qual fonte** — pra revisão rápida pela manhã sem precisar reconstruir o raciocínio.

---

## Formato de cada entrada (referência — apagar depois da primeira execução real)

```
## AAAA-MM-DD HH:MM (America/Sao_Paulo)

### daily-digest
- Transcrições novas encontradas: N (lista de arquivos)
- Já cobertas / puladas como duplicata: N (qual arquivo, qual digest já existente cobria)
- Digest(s) criado(s): [nome do arquivo](dailies/arquivo.md) — período/tema
- Achados principais, por projeto:
  - **<Projeto>**: <achado> — fonte: <trecho/data da transcrição>
- Arquivos sinalizados como desatualizados (NÃO editados por este agente):
  - `<arquivo>` — <o que especificamente parece defasado e por quê>

### board-sync
- Cards com estado/coluna mudados:
  | ID | De | Para | Motivo (fonte) |
  |---|---|---|---|
  | #NNNNN | Refinement (Quase pronto) | Refinement (Precisa refinar) | Comentário do Danilo em DD/MM: "<citação>" |
- Cards removidos do escopo do board (avançaram além de Ready for Dev):
  | ID | Estado atual | Motivo |
  |---|---|---|
- Cards novos descobertos (não rastreados antes):
  | ID | Score DoR (4 pontos) | Coluna onde entrou |
  |---|---|---|
- Checagem de paridade chip/modal: OK / FALHOU (detalhe se falhou)
- Artifact republicado: <URL> — <sim/não, e por quê se não>

### Pendências que ficaram para o Igor decidir
- <qualquer bloqueio externo real encontrado, não resolvido pelo agente>

### Erros/falhas nesta execução
- <qualquer chamada ADO que falhou, arquivo que não abriu, etc — nunca omitir silenciosamente>
```

---

*(entradas reais começam abaixo, mais recente no topo)*

---

## 2026-09-08 16:13 (execução manual, sob pedido do Igor — daily-digest: 2 transcrições .docx novas de 08/09 + verificação dos loose .docx restantes na raiz do repo)

### daily-digest

- **Transcrições novas encontradas: 2 arquivos .docx**, ambos datados 08/09/2026 (confirmado pelo cabeçalho interno "8 de setembro de 2026, HH:MMPM"):
  - `RETAGUARDA - Daily (2025)  (5).docx` (13:49, 8m54s, transcrição iniciada por Igor Diniz Camargo)
  - `VAR 3.0 - Daily Proj_Sust (2).docx` (13:35, 11m6s, transcrição iniciada por Filipe de Lacerda Grangeiro)
- **Já cobertas / puladas como duplicata: 5 arquivos/temas** (confirmação repassada pelo Igor na invocação desta rodada, não reprocessados por já estarem digeridos):
  - `RETAGUARDA - Daily (2025)  (3).docx` (01/09) e `(4).docx` (03/09) → já cobertas por [dailies/2026-09-01-e-03-digest-retaguarda.md](dailies/2026-09-01-e-03-digest-retaguarda.md).
  - `VAR 3.0 - Daily Proj_Sust.docx` (01/09) e `(1).docx` (04/09) → já cobertas por [dailies/2026-09-01-e-04-digest-var3.md](dailies/2026-09-01-e-04-digest-var3.md).
  - `Sprint Planning  (1).docx` (02/09) → já coberta por [reviews-retros-planning/2026-09-02-planning-retaguarda.md](reviews-retros-planning/2026-09-02-planning-retaguarda.md).
  - `Motor de Descontos - Próximos passos.docx` (02/09) → já coberta por [motor-descontos/2026-09-02-call-arthur.md](motor-descontos/2026-09-02-call-arthur.md).
  - `GAMEFICAÇÃO.docx` (02/09) → já coberta por [gamificacao/2026-09-02-demo-crm-ana-marcos.md](gamificacao/2026-09-02-demo-crm-ana-marcos.md) (e o `contexto.md` de Gamificação já reflete essa demo).
- **Digest(s) criado(s):**
  - [dailies/2026-09-08-digest-retaguarda.md](dailies/2026-09-08-digest-retaguarda.md) — daily Retaguarda de 08/09 (arquivo único — squad estava presencial na sexta anterior, conteúdo curto o bastante pra não justificar split).
  - [dailies/2026-09-08-digest-var3.md](dailies/2026-09-08-digest-var3.md) — daily VAR 3.0 de 08/09.
- **Achados principais, por projeto:**
  - **Conciliação Fase 2**: card novo #12887 (Diego) — melhoria em "aprovar divergências"/"gerenciar perda" pra caso em que a analista adiciona divergência manualmente e cai como "operador vazio", não mapeado; GMUD prevista pra hoje (08/09) usa esse card como base de teste — fonte: `RETAGUARDA - Daily (2025)  (5).docx`, Diego: "já peguei esse caso, já coloquei junto com a minha tesk 12887... hoje pela manhã eu estou testando aqui esse card... para preparar para a GMUD de hoje que está prevista".
  - **Bug de permissionamento (usuário do Danilo)**: recorrência não fechada — travou o Danilo boa parte de sexta (04/09); Diego e Kauã confirmam que mesmo resetando/trocando grupo o permissionamento continua errado — fonte: mesma transcrição, Kauã: "mesmo que a gente apaga, reseta, troca grupo lá, fica permissionamento errado, ele fica admin alguma coisa e não fica admin e mostra a tela errada". Não confirmado se é o mesmo #12514 já reclassificado (owner Leonardo) ou recorrência nova.
  - **Engine — Doc Pendentes da Migrate**: Kovalski confirma que começa a trabalhar nisso hoje — resolve a ambiguidade deixada em aberto no digest de 01-03/09 (lá era só "talvez") — fonte: mesma transcrição, Kovalski: "hoje devo pegar as coisas doc pendentes para fazer da engine".
  - **Etiqueta Remarcados / app de remarcação (Donato)**: Ozéias respondeu na sexta e extraiu do WhatsApp toda a conversa sobre remarcação; Igor vai revisar para criar os cards — fonte: mesma transcrição, Igor: "ele extraiu do Whats, toda a conversa... da aí eu vou dar uma olhadinha para ele poder criar os cards".
  - **Dashboard CDs**: Maria segue sem resposta — padrão que se repete desde as dailies de 01-03/09 — fonte: mesma transcrição, JB: "tenho que falar com a Maria, não consegui mais falar com ela, sumiu".
  - **VAR 3.0 — urgência de piloto**: Gustavo reforça que o piloto começa semana que vem (confirma o prazo de 14/09 já rastreado) e lista o que precisa subir até lá: Overlimit, tratamento de erros (Wanderleia), consulta automática, Pix no TEF, item de "voucher" (nome garbled) — GeneXus→Java fica de fora dessa release — fonte: `VAR 3.0 - Daily Proj_Sust (2).docx`, Gustavo: "semana que vem a gente tem piloto... esses quatro dias... a gente precisa concluir tudo até segunda-feira que vem".
  - **VAR 3.0 — bug "537"**: reportado como recorrência no sábado (fim de semana), já ajustado segundo Filipe — sem causa raiz documentada nesta transcrição — fonte: mesma transcrição, Filipe: "só aquele problema do 537 no final de semana, no sábado... mas aí a gente ajustou, tudo certo".
  - **VAR 3.0 — tratamento de erros (Wanderleia)**: destravado — Felipe orientou passar 4 das 8 tasks pro Walter e 4 pro Wesley testarem antes do PR, resolvendo o pedido de apoio da daily de 04/09 — fonte: mesma transcrição, Wanderleia: "o Felipe me orientou a pedir para o Walter e para o Wesley testar... como são 8, aí eu passei 4 para cada".
  - **VAR 3.0 — novo dev Diogo**: Gustavo confirma que vai liberar acesso permanente pro Diogo no lugar do Matheus Martins (desligado); Diogo já está com o setup rodando e vai receber tarefas de otimização futura (não desta release) — fonte: mesma transcrição.
- **Arquivos sinalizados como desatualizados (NÃO editados por este agente):**
  - `projetos/conciliacao-fase-2/contexto.md` — não menciona o card #12887 nem o novo caso de "operador vazio" em Gerenciar Perdas/aprovar divergências; também não reflete a GMUD prevista pra 08/09 (o contexto atual só cobre a GMUD de 31/08).
  - `projetos/engine-doc-pendentes-migrate/contexto.md` — seção "Reuniões" ainda diz "nenhuma reunião formal registrada" e trata o levantamento como sem dono de execução confirmado; hoje o Kovalski confirmou que começa a trabalhar nisso.
  - `projetos/etiqueta-remarcados/contexto.md` — a pergunta em aberto ("confirmar com o Donato se é frente nova dentro do mesmo épico ou trabalho paralelo") ganhou novo dado: Ozéias já passou o conteúdo completo da conversa sobre remarcação pro Igor, que vai revisar pra criar os cards.
  - `projetos/dashboard-cds/contexto.md` — segue sem refletir que o impasse com a Maria já dura pelo menos desde 01/09 até 08/09 sem novidade (não é informação nova, mas o contexto não documenta a persistência do bloqueio).
  - `projetos/overlimit/contexto.md` — segue registrado como "5% — bloqueado" desde 12/08 (RPE sem resposta), mas o PO (Gustavo) tratou o Overlimit hoje como item ativo de prioridade pra essa semana — o contexto do projeto em si não reflete o destravamento que `prioridades-sprint.md` já registrava desde 31/08.
  - `projetos/prioridades-sprint.md` — "última atualização" ainda datada 31/08; não reflete nada das dailies de 01, 03, 04 ou 08/09 (inclusive a recorrência do bug 537 e a reconfirmação do prazo de piloto em 14/09).
  - `projetos/minhas-pendencias.md` — item "Abrir as tarefas do Donato" já parece estar alinhado com o achado desta daily (Ozéias respondeu, conteúdo recebido) — não é uma defasagem nova, só uma confirmação; vale considerar consolidar esse item com "Criar card... pro app de remarcação do Donato" (mesma frente, dois itens separados na lista).

### Pendências que ficaram para o Igor decidir
- Confirmar se o bug de permissionamento do usuário do Danilo (recorrente em 04/09 e 08/09) é o mesmo #12514 (reclassificado, owner Leonardo) ou uma recorrência distinta.
- Confirmar o que mais compõe a GMUD de 08/09 além do card #12887 — a transcrição não detalha o pacote completo.
- Confirmar causa raiz da recorrência do bug "537" no fim de semana — a transcrição de hoje só confirma que "foi ajustado", sem detalhar o que causou a volta do problema.
- Identificar o item de "voucher" citado pelo Gustavo (VAR 3.0) como prioridade pré-piloto — nome saiu garbled na transcrição ("Voucher Cave"), não foi possível mapear pra um card/projeto específico.

### Erros/falhas nesta execução
- Nenhuma falha na extração via `docx2text.py` para os 2 arquivos novos — ambos processados com sucesso.
- Nota operacional: os 2 `.docx` novos (e todos os demais soltos na raiz) ficaram invisíveis para o Bash tool (mesmo com sandbox desabilitado) enquanto o cwd apontava pra `TAREFAS` (pasta-mãe, fora do repo) — o `git status` fornecido no início da sessão listava os arquivos com caminho relativo ao repo `board-refinamento`, o que inicialmente pareceu indicar que estariam na raiz de `TAREFAS`. Resolvido ao confirmar (via `ls` de dentro de `board-refinamento`) que os `.docx` estavam de fato na raiz do próprio repo, não da pasta-mãe.

---

## 2026-09-04 19:00 (execução manual, sob pedido do Igor — daily-digest: 6 transcrições .docx soltas na raiz do workspace + 1 fragmento de call colado na conversa)

### daily-digest

- **Transcrições novas encontradas: 6 arquivos .docx** na raiz do workspace + **1 fragmento de transcrição colado diretamente pelo Igor** na conversa (sem arquivo, sem timestamp):
  - `GAMEFICAÇÃO.docx` (02/09/2026, demo funcional pro CRM)
  - `RETAGUARDA - Daily (2025)  (3).docx` (01/09/2026)
  - `RETAGUARDA - Daily (2025)  (4).docx` (03/09/2026)
  - `Sprint Planning  (1).docx` (02/09/2026, planning Retaguarda)
  - `VAR 3.0 - Daily Proj_Sust (1).docx` (04/09/2026)
  - `VAR 3.0 - Daily Proj_Sust.docx` (01/09/2026)
  - Fragmento colado: call Vinicius ↔ Leonardo, GNRE + filtro CFOP, **data não confirmada**.
- **Já cobertas / puladas como duplicata: nenhuma.** Nenhum dos 6 arquivos batia com digest já existente (`dailies/2026-08-24-a-28-digest-retaguarda.md` e `-var3.md` cobrem só até 28/08) — confirmado pela data extraída de dentro de cada `.docx` (metadata "X de setembro de 2026, HH:MMAM/PM" no topo do texto extraído), não pelo nome do arquivo: os sufixos "(3)"/"(4)" e "(1)"/sem sufixo eram ambíguos e não seguiam ordem cronológica óbvia (ex.: `VAR 3.0 - Daily Proj_Sust.docx` sem sufixo é do dia 01/09, e a versão "(1)" é do dia 04/09 — mais recente, apesar do nome sem número parecer "original"/mais antigo).
- **Digest(s) criado(s):**
  - [dailies/2026-09-01-e-03-digest-retaguarda.md](dailies/2026-09-01-e-03-digest-retaguarda.md) — dailies Retaguarda de 01 e 03/09 (sem daily em 02/09 nesse squad — foi dia de planning).
  - [dailies/2026-09-01-e-04-digest-var3.md](dailies/2026-09-01-e-04-digest-var3.md) — dailies VAR 3.0 de 01 e 04/09.
  - [reviews-retros-planning/2026-09-02-planning-retaguarda.md](reviews-retros-planning/2026-09-02-planning-retaguarda.md) — planning Retaguarda de 02/09.
  - [gamificacao/2026-09-02-demo-crm-ana-marcos.md](gamificacao/2026-09-02-demo-crm-ana-marcos.md) — demo funcional do Portal de Gamificação pro CRM (Ana Carina/Marcos). Não é daily nem review/retro/planning de sprint — arquivada direto na pasta do projeto, mesmo padrão já usado em `conciliacao-fase-2/reuniao-ozeias-apresentacao-inicial.md` e `dashboard-cds/reuniao-maria-2026-08-12.md`.
  - [automacao-fiscal/call-vini-leonardo-gnre-cfop-data-incerta.md](automacao-fiscal/call-vini-leonardo-gnre-cfop-data-incerta.md) — fragmento colado pelo Igor, **data não confirmada** (nome do arquivo foge de propósito da convenção `AAAA-MM-DD-...` até a data ser esclarecida).
- **Achados principais, por projeto:**
  - **Retaguarda geral**: 36 cards acumulados na coluna Deploy em 01/09 — fonte: `RETAGUARDA - Daily (2025)  (3).docx`, Igor: "Os cards que estão aqui em Deploy, 36 cards. Eu posso jogar todos pra Donato ou vocês preferem revisar antes?".
  - **Conciliação Fase 2**: contorno aplicado pro bug de "token muito grande" — usuário com ADM no grupo passa a ter acesso irrestrito, em vez de precisar remover/trocar grupo manualmente — fonte: mesma transcrição, Kauã: "se tiver ADM no seu grupo, você consegue acesso a tudo irrestrito".
  - **Motor de Descontos — possível ressurgimento do bug "desconto duplicado" do lado VAR 3.0**, sem card aberto (Gustavo criou um novo ali mesmo) — fonte: `VAR 3.0 - Daily Proj_Sust.docx` (01/09), Guilherme Caixeta: "Tem outro problema aí que a gente estava resolvendo... era o lance do desconto duplicado, lembra?". **Não confirmado** se é a mesma frente do job de duplicação já rastreado em `motor-descontos/contexto.md` (risco ativo desde 24/08) ou um bug distinto do lado loja/PDV.
  - **Desconto de Gerente (Java) — regressão pós-deploy** 🆕: erro "537" em produção, causado por arredondamento incorreto do desconto residual entre itens quando o valor é ímpar; atribuído a uma subida equivocada das tasks do Donato nessa atualização — fonte: mesma transcrição, Gustavo: "a gente acabou subindo as suas tasks pra produção de forma equivocada... causou muitos 537". Donato contesta que a rotina que subiu é só mensagem/trava, não mexe em cálculo — **investigação não fechada na transcrição**.
  - **Tap on Phone / VAR 4G**: causa raiz do bug do "acordo" identificada — faltava o esquema do banco na config da IDE do GeneXus, gerando `.ar` compilado com esquema default incorreto pro usuário de caixa da loja — fix + deploy emergencial planejado pra noite de 01/09 — fonte: `VAR 3.0 - Daily Proj_Sust.docx`, falas do Walter e do Gustavo. Em 04/09, Nicolas/Gui confirmaram que um erro intermitente reportado não era bug novo (celular trocou de rede ao ser levado do escritório pra loja) e que o fix de NSU (backend não tratava `0` como erro) parece ter resolvido o crash-ao-abrir relatado antes — fonte: `VAR 3.0 - Daily Proj_Sust (1).docx`.
  - **Release VAR 3.0 confirmada**: 10 dias corridos a partir de 04/09 → **14/09, piloto inicia nesse dia** — fonte: `VAR 3.0 - Daily Proj_Sust (1).docx`, Gustavo: "nossa release... é dia 14, o piloto inicia dia 14".
  - **Novo dev no squad VAR 3.0**: Diogo (Ubiratã/PR) — fonte: mesma transcrição.
  - **Gamificação**: dois bugs achados ao vivo durante a demo pro CRM (acesso de homologação bloqueado temporariamente; edição de símbolo no cadastro do caça-níquel quebra a tela de configuração); discussão em aberto pra remover a validação de "campanha ativa por tipo" (permitir concorrência entre campanhas do mesmo jogo); meta informal de go-live até o final de setembro/2026, substituindo Chute ao Gol + Roleta atuais — fonte: `GAMEFICAÇÃO.docx`, ver digest dedicado pra citações completas.
  - **Automação Fiscal**: novo chamado envolvendo GNRE + bug de filtro CFOP bloqueando o processo do time do Vini (lado Migrate/fiscal) — fix de CFOP classificado como simples pelo Leonardo, deploy emergencial cogitado pra quarta ou quinta daquela semana — fonte: fragmento colado pelo Igor (**data não confirmada**, ver arquivo pra ressalvas completas).
- **Arquivos sinalizados como desatualizados (NÃO editados por este agente):**
  - `projetos/gamificacao/contexto.md` — seção "Reuniões" ainda diz "Nenhuma reunião registrada ainda"; precisa linkar a demo de 02/09 e refletir os novos itens levantados (opção de validade "até o fim da campanha", possível remoção da trava de campanha por tipo, campo de nome pro cliente, decisão pendente de banner customizável, meta informal de go-live até o fim de setembro, 2 bugs achados ao vivo).
  - `projetos/motor-descontos/contexto.md` — a seção "Risco ativo — job de duplicação" pode precisar de uma nota cruzando com o bug "desconto duplicado" redescoberto pelo Caixeta em 01/09 (VAR 3.0) — não confirmado se é a mesma coisa, mas vale checar antes de tratar como duas frentes independentes sem necessidade.
  - `projetos/prioridades-sprint.md` — a linha "Tap on Phone / VAR 4G — bugs críticos novos" (🆕 desde o retro de 28/08) está desatualizada: causa raiz do bug do "acordo" já identificada e corrigida com deploy emergencial em 01/09; erro de NSU/crash intermitente parece resolvido conforme confirmação de 04/09. Vale também registrar o novo risco de regressão "537" (desconto de gerente) e a data confirmada de release/piloto (14/09).
  - `projetos/engine-doc-pendentes-migrate/contexto.md` — Kovalski mencionou (03/09, daily Retaguarda) que "talvez" vá começar a mexer em "Doc Pendentes" — se for confirmado que é este projeto (squad diferente do dele), atualizar quem está envolvido.
  - `projetos/automacao-fiscal/contexto.md` — não tem nenhuma seção citando o novo chamado de GNRE/CFOP; adicionar referência ao novo arquivo `call-vini-leonardo-gnre-cfop-data-incerta.md` e, se possível, confirmar a data com o Igor antes de formalizar.
  - `projetos/dashboard-executivo.html` — conferir se os itens de Tap on Phone (causa raiz resolvida), GNRE/CFOP (novo) e a regressão "537" já estão refletidos nos blocos de entrega/bloqueio/risco.
  - `projetos/README.md` — índice pode precisar de linha nova pra Gamificação (demo 02/09) e pro novo arquivo de Automação Fiscal.

### Pendências que ficaram para o Igor decidir
- Confirmar a **data real da call Vinicius↔Leonardo** (GNRE/CFOP) — fragmento colado não tem timestamp; arquivo ficou com nome fora do padrão (`call-vini-leonardo-gnre-cfop-data-incerta.md`) até isso ser resolvido, e a decisão de qual projeto ele pertence (ficou em `automacao-fiscal/` por ser o encaixe mais razoável, não confirmação).
- Confirmar se o bug **"desconto duplicado"** redescoberto por Caixeta (VAR 3.0, 01/09) é a mesma frente do job de duplicação já desativado pelo Leo (Retaguarda) ou um problema distinto do lado loja/PDV.
- Confirmar se a menção do Kovalski a **"Doc Pendentes"** (03/09) é sobre o projeto `engine-doc-pendentes-migrate` (squad VAR 3.0) ou outra coisa — ele é do squad Retaguarda, então a referência é ambígua.
- Confirmar a **causa raiz completa da regressão "537"** (desconto de gerente) — Donato disse que a rotina que subiu é só mensagem/trava, não cálculo, mas Gustavo não fechou a investigação dentro da transcrição.

### Erros/falhas nesta execução
- `python scripts/docx2text.py` extraiu os 6 arquivos sem erro de leitura de `.docx` — mas a primeira tentativa de rodar via Bash devolveu o texto com mojibake (cp1252 sobre conteúdo UTF-8) por causa do codepage padrão do console. Resolvido rodando de novo com `PYTHONIOENCODING=utf-8` e redirecionando a saída pra arquivo antes de ler.

---

## 2026-09-04 18:00 (execução manual, sob pedido do Igor — sweep obrigatório de 3 partes + limpeza completa da lista "O que falta" em todos os ~25 cards do board)

### board-sync

**Contexto do pedido:** rodar o sweep de 3 partes de novo (não pular por ser pedido de formatação) e, em cima dele, fazer uma passada de limpeza da `<ul class="gap-list">` em **todo** card do board — não só nos que mudaram de estado nesta rodada — aplicando a regra "gap-list só guarda pendência aberta" (refinada 04/09: prioridade+assunto, não whitelist rígida) já usada como exemplo em #12511/#12178.

**Sweep de 3 partes rodado:** (1) `get_batch` nos 25 IDs então rastreados (`System.State`, `System.BoardColumn`, `System.BoardColumnDone`, `System.ChangedDate`, `System.CommentCount`, `System.AssignedTo`, `Microsoft.VSTS.Scheduling.Effort`); (2) `list_comments` em todo card cujo `ChangedDate`/`CommentCount` indicava atividade após a varredura anterior (#12178, #12902, #11941, #12514, #12793, #12892); (3) WIQL em Refinement/Ready for Dev/New no projeto Var Retaguarda.

- Cards com estado/coluna mudados:
  | ID | De | Para | Motivo (fonte) |
  |---|---|---|---|
  | *(nenhuma mudança de coluna no board)* | — | — | #12178 permanece em "100% pronto" (onde já estava fisicamente posicionado) — mas a última pendência real (arquitetura listar fluxos afetados pro Cenário 4) foi fechada por comentário do próprio Igor às 17:33: "os principais casos recentes de upstream error... foram no Motor de Descontos, ao tentar criar uma campanha" — citando `createAtomic`/`ASYNC_CAMPAIGN_CREATION_ROW_THRESHOLD` (`campaign-validation.constant.ts:9`) e, com menos evidência, a Automação Planilha Fiscal. A narrativa do rodapé da rodada anterior (que ainda descrevia #12178 como bloqueado) foi corrigida para refletir isso — a gap-list do card em si já estava correta (só a pendência de estimativa) e não precisou de edição. |

- Cards removidos do escopo do board (avançaram além de Ready for Dev):
  | ID | Estado atual | Motivo |
  |---|---|---|
  | #12902 — Infra · Corrigir healthcheck do nginx | **Doing** | Avançou de "Ready for Dev" pra "Doing" (17:09) — dev já começou (Fernando). Nenhum comentário de QA associado; graduação limpa. Removido do board (chip + modal). |

- Cards novos descobertos (não rastreados antes):
  | ID | Score DoR (4 pontos) | Coluna onde entrou |
  |---|---|---|
  | *(nenhum)* | — | WIQL em Refinement/Ready for Dev/New retornou 24 IDs — exatamente os 25 já rastreados menos o #12902 (agora em Doing). Nenhum ID fora da lista. |

- **Limpeza de gap-list (pedido específico desta rodada, aplicada a todos os cards, mudados ou não):**
  - Removida narração de transição de estado/sprint: #12513 ("avançou de Refinement pra Ready for Dev / Sprint 27 pra 28 — sem comentário novo").
  - Removidas confirmações de bookkeeping de varredura já resolvidas ("Atualização da varredura de 02/09 (tarde): Assigned To agora preenchido..."): #12509, #12510, #12513. O fato relevante que essas notas carregavam — a conta `joao.neto@grupoavenida.com.br` responder tanto por "João Bernardo (JB)" quanto por "João Neto (JN)" — foi dobrado pra dentro da linha `meta` do #12509 (`João Bernardo (JB) — mesma conta usada como "João Neto (JN)" em #11941/#12437`) em vez de ficar espalhado como item datado em 3 cards.
  - Removida a justificativa/comparação por trás de cada estimativa já preenchida e só pendente de confirmação técnica (regra: manter a pendência de confirmação, cortar o "por sizing relativo, comparável a #X" — isso já está no comentário do próprio card no Azure): #12190, #12437, #12509, #12510, #12514, #12793, #12892, #12903, #12904, #12905, #12906. Em #12892 mantive a única parte da rationale que é risco técnico real (falta de integração Oracle GL pronta pra copiar), não só número.
  - Cards já conferidos limpos nas rodadas anteriores (#12511, #11813, #11818, #11935, #12403, #11840, #12115, #12812, #12889, #12890) — revisados de novo nesta passada, sem necessidade de edição.
  - Nenhuma pendência real foi removida de nenhum card — só narrativa de processo/sync/rationale, nunca conteúdo do card. Corrigido também um mismatch pré-existente no cabeçalho "O que falta trabalhar" (dizia "8 cards", lista somava 7) — agora "7 cards".

- **Checagem de paridade chip/modal:** OK — 24 botões `.kcard` = 24 `<dialog>` (grep antes de publicar). Board caiu de 25 pra 24 cards (5 Precisa refinar + 2 Quase pronto + 17 100% pronto).
- **Artifact republicado:** https://claude.ai/code/artifact/ced8aba8-8054-44d2-a8f9-a4b410264a96 (live version lida por completo — 993 linhas do HTML servido — antes de editar/publicar, confirmada idêntica ao arquivo local no início desta rodada, sem edição concorrente).

### Pendências que ficaram para o Igor decidir
- Nenhum bloqueio externo novo encontrado nesta rodada. Seguem em aberto, sem novidade: bloqueio real do #12812 (Adriana/layout Oracle) e do #12513 (esboço da Maria) — não resolvidos unilateralmente, como manda a regra do projeto; #12284/#12813 fechados como Done sem documentação formal do gap de QA (sinalizado em rodadas anteriores, sem ação adicional pedida); confirmar `AssignedTo` de #11813/#11818/#12812 (segue vazio na API).

### Erros/falhas nesta execução
- Nenhuma. Todas as chamadas ADO (`get_batch`, `list_comments` ×6, `wiql`) retornaram na primeira tentativa.

---

## 2026-09-04 16:00 (execução manual, sob pedido do Igor — sweep obrigatório de 3 partes + adicionar 5 cards novos de Infraestrutura #12902-#12906)

### board-sync

**Contexto do pedido:** 5 PBIs novos criados direto no Azure (#12902-#12906, Epic Infraestrutura #10542, Sprint 28, "Ready for Dev", atribuídos a Fernando Caetano de Lima, estimativas PO 2/3/5/2/5) precisavam entrar no board pela primeira vez. Pedido explícito pra rodar o sweep completo de 3 partes em cima disso, não só adicionar os 5 e pular o resto.

**Sweep de 3 partes rodado:** (1) `get_batch` nos 20 IDs já rastreados + os 5 novos (`System.State`, `System.BoardColumn`, `System.ChangedDate`, `System.CommentCount`, `System.AssignedTo`, `Microsoft.VSTS.Scheduling.Effort`); (2) `get`/`list_comments` completo nos 5 novos (Description, AC, comentários) pra confirmar conteúdo e nota técnica antes de pontuar contra o gate de 4 pontos; (3) WIQL em Refinement/Ready for Dev/New no projeto Var Retaguarda.

- Cards com estado/coluna mudados (dos 20 já rastreados):
  | ID | De | Para | Motivo (fonte) |
  |---|---|---|---|
  | *(nenhum)* | — | — | Todos os 20 cards já rastreados na varredura anterior desta mesma manhã (04/09) seguem com State/BoardColumn/CommentCount idênticos — nenhuma mudança de conteúdo, nenhuma regressão, nenhum avanço além de Ready for Dev. |

- Cards removidos do escopo do board (avançaram além de Ready for Dev):
  | ID | Estado atual | Motivo |
  |---|---|---|
  | *(nenhum nesta rodada)* | — | — |

- Cards novos descobertos (não rastreados antes):
  | ID | Score DoR (4 pontos) | Coluna onde entrou |
  |---|---|---|
  | #12902 — Corrigir healthcheck do nginx (autoheal em loop) | 4/4 — Story+4 Cenários GWT rotulados, nota técnica (comentário 15:46 + Descrição, citando `infra/docker-compose.prod.yml`), estimativa PO 2 pts (comentário 15:52, pendente confirmação Fernando), sem bloqueio | 100% pronto |
  | #12903 — Thread pool Node insuficiente pros pools Oracle | 4/4 — nota técnica citando `src/var.module.ts:26/29`, `dynamic-oracle.service.ts:87/463/544`, commit `1bbe311ba` a reverter; estimativa PO 3 pts | 100% pronto |
  | #12904 — Foto do usuário fora do `/api/auth/me` | 4/4 — nota técnica citando `auth.service.ts:1915`, `microsoft-graph.service.ts:48`; estimativa PO 5 pts (muda contrato de API) | 100% pronto |
  | #12905 — Separar liveness do diagnóstico completo | 4/4 — nota técnica citando `healthCheck.service.ts:152/345`; estimativa PO 2 pts | 100% pronto |
  | #12906 — Mover StoreJobProcessor pro worker | 4/4 — nota técnica citando reuso de `ExcelGenerationQueue`/`TaxClosingExcelProcessor`; estimativa PO 5 pts (mexe em deploy/fila) | 100% pronto |

  Todos os 5 já vieram do Igor no formato Story "Eu-enquanto-poderia-para-que" + 4 Cenários Dado/Quando/Então rotulados + nota técnica dupla (comentário completo às 15:46-15:48 e versão enxuta na Descrição) + estimativa Fibonacci proposta pelo PO (comentário separado às 15:52, pendente de confirmação do Fernando) — sem gap a registrar. Nenhum introduz tela nova (mudanças de infra/backend), então não se aplica chip de flowchart/mock. WIQL confirmou 25 IDs totais (20 já rastreados + os 5 acima) — nenhum ID fora dessa lista, ou seja, não há mais nenhum card não-triado além desses 5.

- **Achado à parte, não tratado como drift desta rodada:** `System.AssignedTo` veio vazio na API pra #11813, #11818 e #12812, embora o board mostre "Kauã Cunha" (11813/11818) e "Diego Rafael" (12812). `list_revisions` falhou ("Project selection cancelled") ao tentar confirmar se é desatribuição recente ou imprecisão já presente em rodadas anteriores — não investigado a fundo por limite de tempo desta rodada. Sinalizado pro Igor conferir; não afeta score DoR (assignee não é um dos 4 pontos do gate).

- **Checagem de paridade chip/modal:** OK — 25 botões `.kcard` = 25 `<dialog>` (grep antes de publicar, IDs conferidos um a um). Board subiu de 20 pra 25 cards (5 Precisa refinar + 7 Quase pronto + 13 100% pronto).
- **Artifact republicado:** https://claude.ai/code/artifact/ced8aba8-8054-44d2-a8f9-a4b410264a96 (live version lida por completo — 837 linhas do HTML servido — antes de publicar; confirmada idêntica ao arquivo local no início desta rodada, sem edição concorrente).

### Pendências que ficaram para o Igor decidir
- **Confirmar `AssignedTo` de #11813, #11818 e #12812** — API retornou vazio hoje; board ainda mostra Kauã Cunha/Diego Rafael. Não foi possível checar o histórico de revisões nesta sessão (`list_revisions` falhou).
- Seguem em aberto, sem novidade nesta rodada: #12284/#12813 fechados como Done sem documentação formal do gap de QA (usuário já pediu pra deixar como estão, sem ação); confirmar se #12512 foi excluído de propósito; padronizar apelido "João Bernardo (JB)" vs "João Neto (JN)".

### Erros/falhas nesta execução
- `wit_work_item list_revisions` retornou "Project selection cancelled" ao tentar consultar o histórico de #11813 (a action não aceita parâmetro `project` no schema desta sessão) — não contornado, registrado como pendência acima em vez de prosseguir sem a informação.

---

## 2026-09-04 (execução manual, sob pedido do Igor — sweep obrigatório de 3 partes + re-checagem específica dos achados de 02/09)

### board-sync

**Contexto do pedido:** repetir o sweep obrigatório de 3 partes contra o Azure, re-checando explicitamente os 5 pontos deixados em aberto na varredura de 02/09 (tarde) — #12509/#12510/#12511/#12513 (Assigned To/apelido JB-JN), #12182 (Gamificação T3, Rework), #12512 (não encontrado) — mais o sweep completo dos 24 IDs então rastreados, e checar qualquer coisa datada 03/09-04/09 ainda não varrida.

**Sweep de 3 partes rodado:** (1) `get_batch` nos 24 IDs rastreados + #12182/#12512/#11938 (re-checagem específica) — #12512 causou `null` no batch inteiro (confirmado: card não existe/inacessível, mesmo padrão de 02/09); (2) `list_comments` em todo card cujo State/BoardColumn mudou (#11933, #12273, #12284, #12813) e no #11938 (ChangedDate de hoje); (3) WIQL em Refinement/Ready for Dev/New no projeto Var Retaguarda.

- Cards com estado/coluna mudados: nenhum dos 20 cards que permaneceram no board teve State/BoardColumn/CommentCount diferente do que o board já registrava — todos conferem com a varredura de 02/09 (tarde). Nenhuma linha nesta tabela nesta rodada.

- Cards removidos do escopo do board (avançaram além de Ready for Dev):
  | ID | Estado atual | Motivo (fonte) |
  |---|---|---|
  | #11933 (Sangria/saídas/suprimento, estava "100% pronto") | **Dev Box** | Avançou de "Ready for Dev" (03/09) — dev pegou o card. Único comentário é o de refinamento de 12/08 (Igor), sem achado de QA. Graduação limpa. |
  | #12273 (Admin permanente Keycloak, estava "100% pronto") | **Doing** | Avançou de "Ready for Dev" (03/09) — dev pegou o card. Pendência não bloqueante do Danilo sobre o vault (11/08) segue sem novo comentário. Graduação limpa. |
  | #12284 (Runbook SSO Hub, estava "Quase pronto", bloqueado por QA) | **Done** | Foi direto de "Refinement" pra "Done" (03/09) — **sem nenhum comentário novo** documentando a resolução do bloqueador do Danilo (25/08: "a lista de erros mais comuns está incompleta... sugestão: levantar com quem opera o SSO Hub a lista real"). 3 comentários totais no card, o mais recente ainda é o de 25/08. **Não resolvido por este agente — sinalizado pro Igor.** |
  | #12813 (Ciacon — Levantamento e documentação, estava "Precisa refinar", conteúdo vazio) | **Done** | Foi direto de "Refinement" pra "Done" (03/09), **0 comentários no work item** (mesmo 0 de antes). Card nunca teve Description/AC reais registrados — só relato verbal do Kovalski (28/08). Fechado sem qualquer documentação formal do que foi entregue. **Mesma preocupação do #12284 — sinalizado pro Igor, não resolvido por este agente.** |

- Itens específicos re-checados (pedido do Igor): #11938 segue em Dev Box, sem mudança de estágio (só update de campo hoje 04/09 14:52, sem comentário novo) — corretamente fora do board. #12182 (Gamificação T3) segue em Rework, `ChangedDate` idêntico a 02/09 (14:47) — sem mudança, fora do board. #12512 (Dashboard CDs · relatório WMS) segue **não encontrado** no Azure (`get` e `get_batch`, com/sem `fields`, retornam nulo) — indício de exclusão upstream persiste, ainda sem confirmação do Igor. Assigned To dos 4 cards #12509/#12510/#12511/#12513 segue preenchido e estável, mesma conta/apelido JB-JN já sinalizado — padronização ainda pendente.

- Cards novos descobertos (não rastreados antes):
  | ID | Score DoR (4 pontos) | Coluna onde entrou |
  |---|---|---|
  | *(nenhum)* | — | WIQL em Refinement/Ready for Dev/New retornou 20 IDs — exatamente os 20 que sobram dos 24 rastreados depois das 4 saídas de escopo acima. Nenhum ID fora da lista. |

- **Checagem de paridade chip/modal:** OK — 20 botões `.kcard` = 20 `<dialog>`, checado via grep antes de publicar. Board caiu de 24 pra 20 cards (5 Precisa refinar + 7 Quase pronto + 8 100% pronto).
- **Artifact republicado:** https://claude.ai/code/artifact/ced8aba8-8054-44d2-a8f9-a4b410264a96 (live version lida por completo — 948 linhas — antes de publicar; confirmada idêntica ao ponto de partida desta rodada, sem edição concorrente; 1ª tentativa de publish recusada por "conteúdo idêntico já recusado" — resolvido re-executando `action: "read"` na URL antes de tentar de novo).

### Pendências que ficaram para o Igor decidir
- **#12284 e #12813 foram fechados (Done) sem nenhum registro de como o gate de refinamento foi satisfeito** — #12284 tinha um bloqueador de QA documentado (Danilo, 25/08) que nunca recebeu resposta em comentário antes do card virar Done; #12813 nunca teve Description/AC formalizados no Azure e foi fechado com 0 comentários. Nenhum dos dois foi investigado além do que a API expõe (State/comentários) — decisão do Igor se cabe uma checagem retroativa (`refinement-gate`) ou uma conversa direta com quem fechou os cards.
- **Confirmar se #12512 foi excluído/removido de propósito** — segue não aparecendo em nenhuma consulta ao Azure, agora confirmado numa terceira rodada consecutiva.
- **Padronizar o apelido "João Bernardo (JB)" vs "João Neto (JN)"** no board — segue pendente desde 02/09, sem mudança nesta rodada.

### Erros/falhas nesta execução
- `wit_work_item get_batch` com 27 IDs (incluindo #12512) retornou `null` — resolvido removendo #12512 do lote e consultando-o isoladamente via `get` e `get_batch` (ambos retornaram `null`, consistente com não existir/inacessível).
- Publish do Artifact foi recusado 1x por "conteúdo idêntico já recusado" mesmo após ter lido o arquivo salvo por completo — resolvido re-executando `action: "read"` na URL dentro do mesmo turno antes de tentar publicar de novo (mesmo padrão de falha já visto em 02/09).

---

## 2026-09-02 15:00 (execução manual, sob pedido do Igor — segunda varredura completa da tarde, re-checar os 5 achados da manhã + sweep obrigatório de 3 partes)

### board-sync

**Contexto do pedido:** repetir a varredura obrigatória de 3 partes contra o Azure, re-checando explicitamente os 5 pontos da rodada das 12:44 (Done de #12400/#12401/#12405, #12182 em In Test, #12512 não encontrado, Assigned To vazio em #12509/#12510/#12511/#12513) em vez de assumir que nada mudou, mais o sweep completo dos 25 IDs então rastreados.

**Sweep de 3 partes rodado:** (1) `get_batch` nos 25 IDs rastreados + os 4 fora de escopo re-checados (#12400/#12401/#12405/#12182), mais `get` isolado em #12512; (2) `list_comments` em todo card cujo State/BoardColumn mudou ou cujo `ChangedDate` sugeria atividade nova (#12182, #11938, #12509/#12510/#12511/#12513, #12437, #12812); (3) WIQL em Refinement/Ready for Dev/New no projeto Var Retaguarda.

- Cards com estado/coluna mudados:
  | ID | De | Para | Motivo (fonte) |
  |---|---|---|---|
  | #12509 | Ready for Dev, Assigned To vazio (100% pronto) | Ready for Dev, Assigned To preenchido (100% pronto, sem mudança de coluna) | `Assigned To` passou a `joao.neto@grupoavenida.com.br` ("João Bernardo Ferreira Neto") — sem comentário associado; ChangedDate ~14:04. Resolve a pendência da manhã. |
  | #12510 | idem | idem | Mesmo padrão, mesma conta. |
  | #12511 | idem | idem | Mesmo padrão, mesma conta; card seguiu em "Quase pronto" (bloqueio parcial do mapa de estoque CD 83 continua). |
  | #12513 | idem | idem | Mesmo padrão, mesma conta; card seguiu em "Quase pronto" (bloqueio externo da Maria continua). |
  | #12514 | Sprint 27 (texto do modal desatualizado) | Sprint 28 | Azure já tinha movido; só o texto do modal estava atrasado — corrigido. |
  | #12793 | Sprint 27 (texto do modal desatualizado) | Sprint 28 | Mesmo caso. |

- **Achado novo — #11938 saiu de escopo nesta rodada:** avançou de "Ready for Dev" pra **Dev Box** (`System.BoardColumn` = "Devbox") — dev pegou o card pra implementar. Único comentário no work item é o de refinamento de 12/08, sem achado de QA associado a essa transição. **Removido do board** (estava em "100% pronto", 11→10 cards nessa coluna).

- **Achado sobre a identidade JB/JN (#12509/#12510/#12511/#12513):** a conta que ficou atribuída (`joao.neto@grupoavenida.com.br`, nome de exibição "João Bernardo Ferreira Neto") é a **mesma conta** já usada em #11941 e #12437, onde o board rotula a pessoa "João Neto (JN)". Nome completo é composto ("João Bernardo" + sobrenome "Ferreira Neto") — os dois apelidos no board batem pra mesma pessoa, não são duas pessoas diferentes nem erro de atribuição. Mantido "João Bernardo (JB)" nos 4 cards por ser o apelido que o Igor usou ao pedir a reatribuição; sinalizado no board pra padronizar numa próxima passada.

- Cards removidos do escopo do board (avançaram além de Ready for Dev):
  | ID | Estado atual | Motivo |
  |---|---|---|
  | #11938 (Nomenclatura "Ativo"→"Trabalhando") | **Dev Box** | Novo nesta rodada — ver achado acima. |
  | #12400/#12401/#12405 | **Done** (re-checado) | Sem mudança desde a manhã — confirmado novamente, nenhum comentário novo. |
  | #12182 (T3 Gamificação) | **Rework** (não mais In Test) | **Atualização real:** Danilo rodou teste manual formal às 14:47 de hoje e reprovou o card — comentário cita que o AC "regras e lojas elegíveis acessíveis antes do jogo (R32)" não atende (só aparece depois do resgate) e que dois AC de concorrência não puderam ser testados por limitação do ambiente de HML. Segue fora do board (mais avançado que Ready for Dev), mas confirma na prática o padrão de risco já sinalizado pro `refinement-gate`: o bloqueador de negócio do Danilo (25/08, ordem do fluxo campanha/cadastro) nunca foi fechado antes do card avançar, e agora falhou justamente numa área adjacente. |
  | #12512 (Dashboard CDs · relatório WMS) | **Não encontrado** (re-checado) | `get` sem `fields` também retorna vazio — mantém indício de exclusão upstream, ainda sem confirmação do Igor. |

- Cards novos descobertos (não rastreados antes):
  | ID | Score DoR (4 pontos) | Coluna onde entrou |
  |---|---|---|
  | *(nenhum)* | — | WIQL em Refinement/Ready for Dev/New retornou 24 IDs — exatamente os 25 já rastreados menos #11938 (saiu de escopo). Nenhum ID fora da lista. |

- **Checagem de paridade chip/modal:** OK — 24 botões `.kcard` = 24 `<dialog>`, checado via grep antes de publicar. Board caiu de 25 pra 24 cards (6 Precisa refinar + 8 Quase pronto + 10 100% pronto).
- **Artifact republicado:** https://claude.ai/code/artifact/ced8aba8-8054-44d2-a8f9-a4b410264a96 (live version lida por completo — 973 linhas — antes de publicar; confirmado idêntica ao ponto de partida desta rodada, sem edição concorrente).

### Pendências que ficaram para o Igor decidir
- **Confirmar se #12512 foi excluído/removido de propósito** — segue não aparecendo em nenhuma consulta ao Azure, agora confirmado numa segunda rodada.
- **#12182 (T3 Gamificação) reprovado por QA (14:47 de hoje) e voltou pra Rework** — mesmo bloqueador de negócio da rodada de 25/08 nunca foi fechado antes do card avançar; decisão do Igor se cabe um `refinement-gate` retroativo nessa frente de Gamificação.
- **Padronizar o apelido "João Bernardo (JB)" vs "João Neto (JN)"** no board — são a mesma conta/pessoa (`joao.neto@grupoavenida.com.br`), usada com dois apelidos diferentes em grupos diferentes de cards.

### Erros/falhas nesta execução
- `wit_work_item get_batch`/`get`/`list_comments` sem `project` retornaram "Project selection cancelled" nas primeiras chamadas desta rodada — resolvido reenviando com `project: "Var Retaguarda"` em todas.
- `wit_work_item get_batch` com 30 IDs (incluindo #12512) retornou `null` — resolvido removendo #12512 do lote e consultando-o isoladamente (também retornou vazio, consistente com não existir mais).
- Publish do Artifact foi recusado 2x antes de ir: 1ª vez por rótulo (`label`) acima do limite de 60 caracteres; 2ª vez por "conteúdo idêntico já recusado" mesmo após ter lido o arquivo salvo por completo — resolvido re-executando `action: "read"` na URL dentro do mesmo turno antes de tentar publicar de novo.

---

## 2026-09-02 12:44 (execução manual, sob pedido do Igor — verificar reatribuição de #12509/#12510/#12511/#12513 ao JB + sweep completo)

### board-sync

**Contexto do pedido:** Igor reatribuiu manualmente #12509, #12510, #12511 e #12513 a João Bernardo (JB) no Azure e já tinha patchado localmente o texto "Sem atribuição" de #12511/#12513 pra "João Bernardo (JB)" como stopgap (12509/12510 já mostravam JB). Pedido explícito: verificar os 4 direto no Azure (não confiar no patch) + sweep completo, não só os 4 cards.

**Sweep de 3 partes rodado:** (1) diff dos 30 IDs rastreados via `get_batch`/`get` (`System.State`, `System.BoardColumn`, `System.AssignedTo`, `System.ChangedDate`, `System.CommentCount`, `System.IterationPath`); (2) `list_comments` em todo card cujo estado/coluna mudou; (3) WIQL em Refinement/Ready for Dev/New pra achar cards não rastreados.

- Cards com estado/coluna mudados:
  | ID | De | Para | Motivo (fonte) |
  |---|---|---|---|
  | #12509 | Refinement · Sprint 27 (100% pronto) | Ready for Dev · Sprint 28 (100% pronto, sem mudança de coluna) | Promoção administrativa no Azure hoje (~12:40); 3 comentários lidos (estimativa PO, notas técnicas) — nenhum novo, nenhuma mudança de conteúdo/DoR. |
  | #12510 | Refinement · Sprint 27 (100% pronto) | Ready for Dev · Sprint 28 (100% pronto, sem mudança de coluna) | Mesmo padrão — 2 comentários lidos, nada novo. |
  | #12511 | Refinement · Sprint 27 (Quase pronto) | Ready for Dev · Sprint 28 (Quase pronto, sem mudança de coluna) | Mesmo padrão — 2 comentários lidos, nada novo; Cenário 2 continua dependente do "mapa do estoque" do CD 83. |
  | #12513 | Refinement · Sprint 27 (Quase pronto) | Ready for Dev · Sprint 28 (Quase pronto, sem mudança de coluna) | Mesmo padrão — 1 comentário lido, nada novo; bloqueio externo (esboço da Maria) segue aberto. |
  | #12437 | Refinement · Sprint 23 (100% pronto) | Ready for Dev · Sprint 28 (100% pronto, sem mudança de coluna) | Mesma promoção administrativa; 1 comentário lido (estimativa PO), nada novo. Sprint no modal estava desatualizado (Sprint 23) — corrigido pra 28. |
  | #11938 | Refinement (100% pronto) | Ready for Dev (100% pronto, sem mudança de coluna) | Mesma promoção; 1 comentário lido (refinamento antigo, 12/08), nada novo. |
  | #12892 | Refinement · Sprint 27 (Quase pronto) | Ready for Dev · Sprint 28 (Quase pronto, sem mudança de coluna) | 0 comentários no card — sem conteúdo novo; DoR continua 1/4 (só "sem bloqueio" passa), mantido em Quase pronto pela mesma lógica já registrada (conteúdo rico, só falta forma). |

- **Verificação dos 4 cards da JB (pedido explícito do Igor):** State/BoardColumn confirmados "Ready for Dev" nos 4. **Achado importante:** o campo formal `System.AssignedTo` está **vazio nos 4** (#12509/#12510/#12511/#12513) — confirmado direto na API (`get`/`get_batch` com o campo explícito) e, pro #12509, no **histórico completo de revisões desde a criação** (nunca foi populado em nenhuma rev). A reatribuição a JB que o Igor fez no Azure **não aparece no campo oficial**. Board mantém "João Bernardo (JB)" nos 4 (inclusive corrigindo o avatar de #12511/#12513, que ainda mostravam "—" no card apesar do texto do modal já ter JB) por instrução explícita do Igor nesta rodada — **não confirmado no Azure, sinalizado no rodapé e nos 2 modais afetados.**

- Cards removidos do escopo do board (avançaram além de Ready for Dev):
  | ID | Estado atual | Motivo |
  |---|---|---|
  | #12400 (US13 · Validação de negócio) | **Done** | Avançou direto pra Done hoje (~12:37) — Conciliação Fase 2 encerrou essa frente. Nenhum comentário novo documentando o fechamento. |
  | #12401 (US14 · Go-live/hypercare) | **Done** | Mesma janela (~12:37), mesmo padrão — sem comentário novo. |
  | #12405 (Motor de Descontos — gravação direta) | **Done** | Mesma janela (~12:37) — sem comentário novo. |
  | #12182 (T3 Gamificação) | **In Test** (fila de QA) | Avançou sem que o bloqueador do Danilo (25/08 — ordem do fluxo campanha/cadastro nunca fechada com o negócio) tivesse sido resolvido no card. Mesmo padrão de risco dos outros 8 cards de Gamificação que já saíram do board antes — `refinement-gate` nunca rodou nele antes de avançar. |
  | #12512 (Dashboard CDs · relatório WMS) | **Não encontrado** | WIQL por ID retorna vazio; `get`/`get_batch` retornam `null` de forma persistente (3 tentativas). Indício de exclusão/remoção upstream — **não confirmado, fica pra o Igor verificar**, não assumi silenciosamente. |

- Cards novos descobertos (não rastreados antes):
  | ID | Score DoR (4 pontos) | Coluna onde entrou |
  |---|---|---|
  | *(nenhum)* | — | WIQL em Refinement/Ready for Dev/New retornou exatamente os 25 IDs já rastreados (30 originais menos os 5 que saíram de escopo acima) — nenhum ID fora da lista. |

- **Checagem de paridade chip/modal:** OK — 25 botões `.kcard` = 25 `<dialog>`, checado via grep antes de publicar. Board caiu de 30 pra 25 cards (6 Precisa refinar + 8 Quase pronto + 11 100% pronto).
- **Artifact republicado:** https://claude.ai/code/artifact/ced8aba8-8054-44d2-a8f9-a4b410264a96 (live version lida por completo — 1121 linhas — antes de publicar; 1ª tentativa de publish recusada porque a linha 1121 não tinha sido lida, resolvido lendo o trecho final e publicando de novo).

### Pendências que ficaram para o Igor decidir
- **Confirmar no Azure se a reatribuição a JB de #12509/#12510/#12511/#12513 realmente salvou** — o campo `Assigned To` está vazio nos 4 apesar da ação manual relatada. Pode ser problema de identity-picker ou a ação não ter sido salva.
- **Confirmar se #12512 foi excluído/removido de propósito** — não aparece mais em nenhuma consulta ao Azure (WIQL vazio, `get`/`get_batch` falhando persistentemente).
- **#12182 (T3 Gamificação) avançou pra In Test sem o bloqueador de QA (25/08) ter sido fechado** — mesmo padrão de risco das outras 8 Gamificação; se cabe um `refinement-gate` retroativo ou só seguir observando, é decisão do Igor.
- #12400/#12401/#12405 foram pra Done sem comentário de fechamento — se há algo do go-live/hypercare/Motor de Descontos que precisa de acompanhamento fora do board, não foi capturado aqui (fora do escopo deste agente).

### Erros/falhas nesta execução
- `wit_work_item get_batch` falhou repetidamente com lotes maiores (`null`, sem mensagem de erro) — contornado usando lotes de até 5 IDs; a causa raiz não foi identificada (não parece ser um ID específico, já que os mesmos IDs funcionaram em lotes menores).
- `wit_work_item get`/`get_batch` para #12512 falhou de forma persistente (`null`) mesmo isolado e mesmo com retry — consistente com o card não existir mais (ver acima).
- `wit_work_item list_revisions` sem `project` retornou "Project selection cancelled" — resolvido reenviando com `project: "Var Retaguarda"`; o resultado ainda assim excedeu o limite de tokens e precisou ser lido via grep no arquivo salvo.

---

## 2026-09-01 21:50 (execução manual, sob pedido do Igor — "atualize nosso dash de tarefas só com tarefas da sprint 28"; 6ª rodada do dia)

### board-refinamento.html — filtro de sprint, sem full sync
Confirmado a-a-a via `get_batch` que os 30 cards já rastreados no board tinham, todos, `IterationPath` = "Var Retaguarda\Sprint 28" (resultado das rodadas 4 e 5) — nenhum card precisou ser removido do board. Atualizado: breadcrumb (+ segmento "Sprint 28"), subtitle (nota explícita de filtro por sprint) e footer (parágrafo novo no topo explicando o filtro e o método de verificação). Nenhuma mudança de coluna/DoR/conteúdo dos cards.

**Não foi um board-sync completo** — não foram re-checados comentários novos, cards novos via WIQL, nem State/BoardColumn individual além do que já se sabia. Artifact republicado.

### Erros/falhas
Nenhum.

---

## 2026-09-01 21:43 (execução manual, sob pedido do Igor — mover todos os cards em "Refinement" pra Sprint 28; 5ª rodada do dia)

### Ação direta no ADO — `wit_work_item_write update_batch`
WIQL `System.State = 'Refinement'` no projeto Var Retaguarda retornou 20 cards; todos tiveram `System.IterationPath` alterado pra **"Var Retaguarda\Sprint 28"** — confirmado 20/20 com HTTP 200: #11813, #11818, #11840, #11935, #11938, #12115, #12178, #12182, #12284, #12403, #12437, #12509, #12510, #12511, #12512, #12513, #12514, #12793, #12812, #12813.

(#11935, #11938 e #12793 já tinham sido movidos na rodada anterior — reaplicado sem efeito colateral, idempotente.)

Nenhum outro campo alterado. Board (`board-refinamento.html`) não tocado.

### Erros/falhas nesta execução
Nenhum.

---

## 2026-09-01 21:41 (execução manual, sob pedido do Igor — mover 16 cards pra Sprint 28; 4ª rodada do dia)

### Ação direta no ADO — `wit_work_item_write update_batch`
`System.IterationPath` alterado pra **"Var Retaguarda\Sprint 28"** (02/09–15/09) em 16 work items — confirmado 16/16 com HTTP 200. Escopo pedido pelo Igor: os 9 cards de uma lista anterior (#11933, #11935, #11938, #11941, #12190, #12793, #11407, #12795, #12797) + todos os que estavam em estado "Ready for Dev" no projeto (#12273, #12400, #12401, #12405, #12889, #12890, #12892 — união, sem duplicar os que já apareciam nos dois grupos).

**Confirmação explícita do Igor** antes de executar: 4 dos 16 (#11407, #12793, #12795, #12797) tinham reprovado o checklist de DoR (0/4 ou quase) — perguntei se ainda assim deveriam entrar na sprint; ele confirmou que sim, mover os 16 mesmo assim.

**Achado incidental durante a checagem:** #12892 tinha sido movido de novo no Azure — **pelo Ozéias**, não por mim — de "Refinement" pra "Ready for Dev" às 20:47 (depois da minha alteração anterior desta sessão que tinha colocado em "Refinement"). Não revertido; é atividade real dele. O board (`board-refinamento.html`) ainda mostra #12892 em "Refinement/Quase pronto" — **desatualizado, precisa de um board-sync pra refletir Ready for Dev**.

### O que NÃO foi feito nesta rodada
- Board (`board-refinamento.html`) não foi tocado — só o `IterationPath` no Azure. Sprint não é um campo que o board rastreia hoje.
- Nenhum outro campo alterado (State, BoardColumn, Effort etc. permaneceram como estavam).

### Pendências que ficaram para o Igor decidir
- #11407, #12793, #12795, #12797 entraram na Sprint 28 sem refino — se alguém for trabalhar neles, o refino ainda precisa acontecer (nenhum dos 4 tem Cenário/AC utilizável hoje).
- Sincronizar o board pra refletir #12892 = Ready for Dev (Ozéias já moveu, board desatualizado).

### Erros/falhas nesta execução
Nenhum — todas as 16 escritas retornaram 200 na primeira tentativa.

---

## 2026-09-01 20:XX (execução manual, sob pedido do Igor — mover #12892 pra Refinement e adicionar no board; 3ª rodada do dia)

### Ação direta (não board-sync — feita manualmente nesta sessão, com escrita no ADO)
- **#12892** ("Fechamento Contábil da Conciliação e Integração de Perdas e Vales com Oracle"): estado alterado no Azure de **"To do" → "Refinement"** via `wit_work_item_write` (System.BoardColumn é read-only e seguiu automaticamente o State). Card adicionado ao `board-refinamento.html` em **"Quase pronto"** (3/4 pendências — formato Dado/Quando/Então, rótulo, estimativa; sem bloqueio identificado). Total do board: 29 → **30 cards** (6 Precisa refinar + 11 Quase pronto + 13 100% pronto).
- Nota registrada no modal do card: possível sobreposição com #12812 (mesmo épico #12387, ambos envolvendo layout/integração Oracle) — não investigada a fundo, só sinalizada.
- Reorganização de arquivos: criada `projetos/reviews-retros-planning/` e movidos os 6 resumos de review/retro/planning que estavam em `projetos/dailies/` (que agora só guarda standups) — todos os links cruzados corrigidos (contexto.md de automacao-fiscal, conciliacao-fase-2, dashboard-cds, overlimit, migracao-varret; prioridades-sprint.md; minhas-pendencias.md; READMEs; agente `daily-digest.md`).
- Criada `projetos/pesquisas-colaboradores/` com TAP.doc + Especificação Funcional recebidos do Igor (não lidos, a pedido dele).
- `minhas-pendencias.md` atualizado: reunião Ana Carina/Marcos (02/09, Gamificação) adicionada; item do TAP do Spin reconciliado com os novos arquivos recebidos; itens novos — levar resumo da Conciliação Fase 2 pro Spin, decidir card de Motor de Descontos em Verified, checar sobreposição #12812/#12892.
- **Checagem de paridade chip/modal:** OK (30 chips = 30 modais, checado via grep antes de publicar)
- **Artifact republicado:** https://claude.ai/code/artifact/ced8aba8-8054-44d2-a8f9-a4b410264a96 (live version lida por completo — 1087 linhas — antes de publicar)

### Pendências que ficaram para o Igor decidir
- Confirmar se #12892 e #12812 são de fato itens distintos ou se um deles deveria absorver o outro antes de estimar.
- Decidir se move manualmente o card de Motor de Descontos em "Verified" pra outra pessoa (levantado na review de hoje).
- Confirmar se o TAP + Especificação Funcional recebidos são sobre um projeto novo ("Pesquisas Colaboradores") ou se têm relação com o Ciacon, como a pendência antiga supunha.

### Erros/falhas nesta execução
Nenhuma.

---

## 2026-09-01 15:XX (execução manual, sob pedido do Igor — checar #12892 e #12890, 2ª varredura do dia)

### board-sync
- **Cards com estado/coluna mudados:**
  | ID | De | Para | Motivo (fonte) |
  |---|---|---|---|
  | #11933 | 100% pronto (**Refinement**) | 100% pronto (**Ready for Dev**, label atualizado) | Estado ADO avançou de Refinement pra Ready for Dev entre a 1ª e a 2ª varredura de hoje (`ChangedDate` 2026-08-31T13:57:55, posterior ao batch update das 13:17:42) — sem mudança de conteúdo/DoR. Comentário único do card (Igor, 12/08, refinamento dos 14→8 cenários) não traz nada novo além do que já estava refletido. |
  | #11941 | Quase pronto | Quase pronto (sem mudança de coluna) | Título no Azure foi alterado pra "...usuários e operador..." — cosmético: os 3 comentários (Danilo 25/08 sobre Cenário 7, refinamento 12/08, mention 23/06) já cobriam operador vs. usuário no AC (Cenário 5/6). Título do board sincronizado, chip/bloqueador de QA mantido sem alteração. |

- **Cards removidos do escopo do board (avançaram além de Ready for Dev):**
  | ID | Estado atual | Motivo |
  |---|---|---|
  | *(nenhum nesta 2ª varredura)* | — | — |

- **Cards novos descobertos:**
  | ID | Score DoR (4 pontos) | Coluna onde entrou |
  |---|---|---|
  | #12889 (Bug — Ajustar expansão de menus e posicionamento do DTEF, Kauã Cunha) — **achado só pela consulta WIQL, não estava nos 2 IDs que o Igor sinalizou** | 1/4 — AC rico em prosa (7 critérios) mas sem formato Cenário/GWT, sem rótulo de verificação, sem estimativa; nota técnica (bug/sustentação) também ausente (0 comentários) | Precisa refinar |
  | #12890 (Nonfunctional Item — Engenharia Reversa, nº da loja na Conciliação de Depósitos) — um dos 2 IDs sinalizados pelo Igor | 0/4 — Description e AC são só o título repetido, 0 comentários, mesmo padrão do #11840 | Precisa refinar |
  | #12892 (PBI — Fechamento Contábil da Conciliação e Integração de Perdas/Vales com Oracle) — o outro ID sinalizado pelo Igor | **NÃO adicionado ao board** — está em estado "To do" no Azure, fora do escopo definido (Refinement/Ready for Dev). Conteúdo já é forte (Story completa + 16 Cenários Dado/Quando/Então), mas ainda não chegou em Refinement. |

- **Checagem de paridade chip/modal:** OK (29 chips = 29 modais, checado via grep antes de publicar)
- **Artifact republicado:** https://claude.ai/code/artifact/ced8aba8-8054-44d2-a8f9-a4b410264a96 (live version lida e confirmada idêntica à base de edição antes de publicar; primeira tentativa de publish foi recusada pelo guard anti-loop mesmo após leitura completa — resolvido re-fetchando a URL e publicando de novo)

### Pendências que ficaram para o Igor decidir
- **#12892**: bem refinado (Story + 16 Cenários) mas preso em "To do" no Azure — não entra no board até alguém mover pra Refinement. Vale mover manualmente se a intenção é que entre na fila de refino.
- Itens abertos herdados da 1ª varredura de hoje continuam válidos e não foram revisitados nesta rodada: #12812 (bloqueio externo real — Adriana/layout Oracle) e a correção pendente em `gamificacao/contexto.md`.

### Erros/falhas nesta execução
- `wit_work_item list_comments` falhou na 1ª tentativa para #11933 e #11941 por faltar o parâmetro `project` explícito ("Project selection cancelled") — resolvido reenviando a chamada com `project: "Var Retaguarda"`.
- O primeiro `Artifact` publish foi recusado por "conteúdo idêntico já recusado, reenviado sem alteração" mesmo após leitura completa da versão live salva localmente — resolvido re-fetchando a URL do artifact (nova leitura) e publicando em seguida, sem alterar o conteúdo.

---

## 2026-09-01 (execução manual, sob pedido do Igor — "atualize nosso board de cards")

### daily-digest
Não rodou nesta execução — o pedido foi só board-sync. Nenhuma transcrição nova foi verificada.

### board-sync
- **Cards com estado/coluna mudados:**
  | ID | De | Para | Motivo (fonte) |
  |---|---|---|---|
  | #11941 | 100% pronto (Ready for Dev) | **Quase pronto** (Ready for Dev) | QA (Danilo, comentário 25/08): Cenário 7 (auditoria) tem redação condicional "(se aplicável)" — precisa virar obrigatório ou ser removido antes de sair de Ready for Dev |
  | #12190 | 100% pronto (Refinement) | 100% pronto (**Ready for Dev**, label atualizado) | Estado ADO avançou de Refinement pra Ready for Dev — sem mudança de conteúdo/DoR |

- **Cards removidos do escopo do board (avançaram além de Ready for Dev):**
  | ID | Estado atual | Motivo |
  |---|---|---|
  | #12179 (T1 Gamificação) | In Test / QA | Avançou além de Ready for Dev |
  | #12181 (T2) | In Test / QA | idem |
  | #12183 (T4) | In Test / QA | idem |
  | #12184 (T5) | In Test / QA | idem |
  | #12185 (T6) | In Test / QA | idem |
  | #12186 (T7) | In Test / QA | idem |
  | #12187 (T8) | In Test / QA | idem |
  | #12189 (T10) | In Test / QA | idem |

  **Achado importante:** #12182 (T3 Gamificação) é a ÚNICA da leva T1-T10 que **não** avançou — segue em Refinement/Quase pronto com o bloqueador de QA de 25/08 (ordem do fluxo campanha/cadastro). Isso contradiz o que estava registrado em `gamificacao/contexto.md` ("todos os T1-T10 avançaram pra In Test/QA") — vale corrigir esse arquivo numa próxima rodada de `portfolio-report`.

- **Cards novos descobertos (via WIQL, não rastreados antes):**
  | ID | Score DoR (4 pontos) | Coluna onde entrou |
  |---|---|---|
  | #12813 (Ciacon — levantamento e documentação, Kovalski) | 0/4 — Description/AC vazios, 0 comentários | Precisa refinar |
  | #12812 (Conciliação F2 — planilha Contábil, Diego Rafael) | 0/4 — vazio + bloqueio externo real (Adriana/layout Oracle) | Precisa refinar |

- **Checagem de paridade chip/modal:** OK (27 chips = 27 modais, antes e depois das edições)
- **Artifact republicado:** https://claude.ai/code/artifact/ced8aba8-8054-44d2-a8f9-a4b410264a96 (a versão live estava desatualizada desde 25/08 — as edições anteriores desta sessão nunca tinham sido efetivamente publicadas nela)

### Pendências que ficaram para o Igor decidir
- #12812: bloqueio externo real (Adriana/layout Oracle) — não resolvido, só sinalizado.
- Corrigir `gamificacao/contexto.md`: a afirmação "todos T1-T10 avançaram" está incorreta (T3 não avançou).

### Achado de qualidade de dado
Quase todos os 33 cards consultados via `get_batch` compartilhavam o mesmíssimo `System.ChangedDate` (2026-08-31T13:17:42.557Z) — indício de uma atualização em lote no Azure (provavelmente campo administrativo), não de mudanças reais individuais naquele instante. O diff foi feito comparando `State`/`BoardColumn` atual contra o que o board mostrava, não usando `ChangedDate` como sinal de "mudou recentemente".

### Erros/falhas nesta execução
Nenhuma chamada ADO falhou. A primeira tentativa de publicar o Artifact foi recusada (exigia reconfirmar leitura da versão live antes de publicar) — resolvido reconfirmando a leitura e republicando.
