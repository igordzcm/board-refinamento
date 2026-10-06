# Motor de Descontos — contexto geral

> Arquivo de contexto do projeto. Atualizado a partir de pendências levantadas em reunião, das user stories técnicas e do dashboard executivo. Ler antes de qualquer reunião sobre este projeto.

## O que é

Motor de campanhas de desconto/combo por loja (Portal Nova Retaguarda), com cadastro de campanhas, validação de conflito de item entre campanhas, e-mails de criação/vigência e comparativo retaguarda x loja.

Épico: **[#6669 — Motor de Descontos](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/6669)** (Var Retaguarda). 2 itens ativos em Sprint23-26.

## Dono / stakeholders

Dev: **Kauã**. Stakeholder de negócio: **Arthur**. Ponto adicional levantado por **Taunay** (interface de destinatários de e-mail) e por **Igor** (comparativo retaguarda x loja).

## Status atual (via dashboard executivo)

A maior parte do escopo priorizado foi **entregue em 22/06/2026 sob responsabilidade do Kauã** — inclui edição de lojas em campanha ativa, resolução de conflito de item no modal, correção do bug de listagem (1 linha por campanha), filtro por regional/estado, melhorias no e-mail de criação e prorrogação de data (esta última seguiu para HML aguardando validação QA no momento do levantamento original).

## O que falta — Fase 2/3 (escopo a refinar)

**US5 — Notificação automática por e-mail para as lojas na entrada em vigência da campanha.** Disparo automático quando a campanha entra em vigor, com hierarquia de produtos no corpo do e-mail (para poucos itens) ou CSV/link (para campanhas grandes), log de envio com retry. **Bloqueio explícito no próprio documento fonte: escopo ainda a ser refinado em call entre Igor e Arthur** — falta sobretudo definir os destinatários por loja (gerente, e-mail de filial etc.).

Demais itens de backlog futuro (baixa prioridade, sem urgência confirmada por Arthur): combo entre departamentos inteiros, filtro por família na listagem de campanhas, relatórios de performance de campanhas, histórico consolidado com "duplicar campanha".

## 🔴 Risco ativo (atualizado 04/09) — job de duplicação segue sem reativação formal + possível segunda ocorrência não confirmada

**Leo desativou o envio pras lojas** depois de confirmar que o job estava duplicando descontos/cupons nas lojas — mitigação no ar desde a semana de 24/08. **A call de 02/09 com o Arthur NÃO tratou desse assunto** (conferido pela transcrição — pauta real da call foi outra, ver ata). O mapeamento completo (o que mais desativar, o que reativar — inclui uma tabela "03" que precisa voltar) segue sem decisão formal. Precisa de um alinhamento à parte com Thalison/Fabio, não estava (e não foi) coberto pela call com o Arthur.

**🆕 Cruzamento a verificar (01/09, digest VAR 3.0) — bug "desconto duplicado" redescoberto, sem card ainda.** Guilherme Caixeta trouxe de volta, na daily de VAR 3.0, um bug antigo de "desconto duplicado" do qual não achou task/card (Gustavo tampouco lembrava e decidiu abrir um card novo). **Não dá pra confirmar, só pelo conteúdo da transcrição, se é a mesma frente do job de duplicação acima ou um problema distinto**: pelo teor da conversa, o bug trazido pelo Caixeta parece ser do lado loja/PDV, enquanto o job desativado pelo Leo é do lado do job de propagação da Retaguarda — são pontos de falha diferentes na cadeia, então poderiam ser dois sintomas de uma mesma causa raiz (duplicação em algum ponto da propagação campanha→loja) ou dois bugs genuinamente independentes. Fonte: [`../dailies/2026-09-01-e-04-digest-var3.md`](../dailies/2026-09-01-e-04-digest-var3.md), seção "Bug 'desconto duplicado' redescoberto". **Ação:** checar isso assim que o novo card do Caixeta/Gustavo for criado, antes de tratar como a mesma coisa ou como problema novo.

## Bloqueios e pendências

- **Novo, 14/09** — filtro de estado na seleção de lojas (cadastro/edição de campanha) só permite escolher um estado por vez; precisa virar seleção múltipla. Ainda sem card no Azure DevOps.
- **Job de duplicação de desconto/cupom**: desativado por precaução (Leo), reativação/correção definitiva **ainda pendente** — não foi pauta da call de 02/09, precisa de alinhamento separado com Thalison/Fabio.
- **US5 (notificação às lojas) + escopo maior do épico**: também não foi assunto da call de 02/09 (que girou em torno de usabilidade + pedidos pontuais do Arthur, ver ata) — segue sem decisão sobre destinatários por loja e sem prioridade confirmada frente aos novos itens levantados na call.
- Destinatários do e-mail de criação de campanha (uso interno) — Arthur ainda precisa definir e passar a lista final (provisoriamente Igor + Arthur). Ligado ao item de e-mail levantado na call de 02/09 (assunto/conteúdo incorretos) — tratar junto.
- Interface de gerenciamento de destinatários no portal (evitar depender de deploy para alterar a lista) — pedido de Taunay, sem prioridade confirmada.
- **Novo, da call de 02/09** — retornos que o Igor deve ao Arthur por mensagem: se corrigir o lado do VAR pra campanhas de departamento já está no planejamento; viabilidade de um cancelamento real de campanha, futura e ativa (falar com Fabio); viabilidade de editar lojas de uma campanha global ativa (falar com Kauã/Fabio); e viabilidade de cadastro em nível SKU (falar com Spin/Diego — TAP já existe do lado do Arthur).

## Arquitetura de propagação (confirmado 02/09) — Retaguarda não propaga mais direto pra loja

A Retaguarda só grava campanha/desconto no banco da Retaguarda (card #12405, Leonardo — já Ready for Dev). Quem propaga pra loja, de acordo com a necessidade, é **Thalison (time de DB)** — não é mais responsabilidade da Retaguarda. Igor explicou a mudança pro Arthur na call de 02/09; Arthur confirmou que, nas últimas semanas, não viu mais o erro de "combo não passa" pra loja. **Ponto fechado.**

### 🆕 Plano de integração de lojas via PRO014_CONTROLE (15/09, call com Thalison)

Detalhe técnico novo de como essa propagação vai passar a funcionar na prática — relacionado às dependências D2/D3 do projeto "Cadastro por SKU/grade" abaixo, já que as tabelas citadas são as mesmas (`PRO014`/`PRO0141`/`PRO0144`):

- Campanhas continuam sendo gravadas em `PRO014`/`PRO0141`/`PRO0144`, mas agora sempre com **loja genérica "999"** na gravação inicial — não é mais a loja real.
- A loja de fato (a que efetivamente vai receber a campanha) fica registrada numa **tabela nova, `PRO014_CONTROLE`**, que tem uma coluna de status.
- Status nasce **F** (pendente); quando o **Thalison faz a integração** (propagação real pra loja), ele muda o status pra **T**.
- **Depois de virar T, a campanha não pode mais ser editada** — trava pra não mexer em algo que já foi propagado pra loja.
- `PRO014_CONTROLE` serve também como **tabela de controle**, pra listar/acompanhar quais campanhas já foram integradas em quais lojas.
- **Pendência nova:** essa lógica (gravar sempre como loja 999, ler `PRO014_CONTROLE`, bloquear edição quando status=T) **também precisa ser implementada do lado Portal Retaguarda**, não só no banco pelo time do Thalison. Ainda sem card criado.

## 🆕 Cadastro por SKU/grade (cor·tamanho) — de "TAP aberta" a plano técnico completo (10/09)

O item que aparecia como "direção futura, depende de TAP formal" (ver call de 02/09 e call com Fabio de 08/09, seção "Backlog novo") avançou muito além do esperado: chegaram **TAP, Especificação Funcional (rev.1, Ozéias Tavares, 08/09) e um plano de implementação técnico completo**, com o **DDL já aplicado e conferido em homologação em 09/09/2026 14:18**. Arquivos em [`desconto-sku/`](desconto-sku/):
- [`TAP - Motor de Descontos SKU.docx`](desconto-sku/TAP%20-%20Motor%20de%20Descontos%20SKU.docx) — Central Planning/Compras, 15/07.
- [`Especificação Funcional - Mecânica de Desconto nível SKU.docx`](desconto-sku/Especifica%C3%A7%C3%A3o%20Funcional%20-%20Mec%C3%A2nica%20de%20Desconto%20n%C3%ADvel%20SKU.docx) — Ozéias Tavares, rev.1, 08/09.
- [`PLANO-IMPLEMENTACAO-DESCONTO-SKU.md`](desconto-sku/PLANO-IMPLEMENTACAO-DESCONTO-SKU.md) — plano técnico datado 09/09, checado regra a regra contra a EF.

**O que o projeto faz:** permite que uma campanha de desconto (PRO014) mire uma grade específica (cor e/ou tamanho) dentro de um código de produto, em vez de aplicar automaticamente a todas as variações — ex.: descontar só a camiseta amarela tamanho M sem tocar nas demais cores/tamanhos. Não mexe em preço, fiscal ou estoque.

**Status por frente** (nomenclatura do plano):
- **F1 · DDL — ✅ feito e conferido em homologação** (`PRO0141.P14GRADE`, tabela nova `VAR.PRO0144`). Falta só a mesma conferência no servidor `10.150.10.126` (driver thin não alcança).
- F2/F3 (API leitura/escrita), F3b (conflito entre campanhas passa a considerar grade), F4 (front — wizard + tela de produtos), F5 (motor do PDV/Java) — **não iniciadas**, estimativa total **≈23-28 dias-homem, 5-6 semanas com 2 devs**.
- F6 (rollout) — sem flag nova necessária; a própria campanha cadastrada numa loja já serve de piloto.

**Dependências externas que o time não destrava sozinho** (nenhuma tem dono/data ainda):
- **D1** — DDL nas 200+ lojas (DBA/Infra).
- **D2** — Triggers `KAFKA_PRO0144`/`TG_PRO0144` (time que cria triggers, não é o nosso time) — **risco #1 do projeto**: sem a `TG_*`, a promoção não sai da central, sem nenhum erro (mesmo destino do `PRO017` hoje).
- **D3** — Quem consome o `OPERACAOLOG` e replica pra loja **não foi encontrado em nenhum repo** — "descobrir na semana 1" é a própria recomendação do plano.
- **D4** — Publicação do JAR nas lojas (TI/Infra).
- **D5** — Assinatura formal de paridade do motor E1 Java (hoje marcado "PARIDADE REAL PENDENTE" no `application.yml`) — sem isso a flag pode ser desligada e a grade não roda em loja mesmo pronta.

**Não existe ainda card/epic no Azure DevOps para isto** (confirmado por busca — nada sob o épico #6669 nem em qualquer WIQL por "SKU"/"grade" relacionado). Dado o volume de trabalho já investido (DDL em homologação) e a estimativa de 5-6 semanas, **precisa de uma conversa com Igor sobre como formalizar isso no board** — não criei nada em ADO sozinho por ser uma decisão de escopo grande.

## Backlog novo, levantado na call de 02/09

- **Pronto pra fila de dev, sem dependência externa:** permitir campanha/combo com 1 item só (hoje mínimo 2); corrigir e-mails de notificação (assunto/conteúdo/destinatários).
- **Direção futura, depende de TAP formal + aprovação do Diego:** criação de campanha por departamento + itens específicos (gatilho: Dia das Crianças); novos tipos de mecânica de campanha (desconto progressivo, cupom nominal — depende também do PDV/VAR). Cadastro em nível SKU **já não está mais nesse estágio** — ver seção própria acima, já tem TAP+EF+plano técnico e DDL em homologação.
- Detalhe completo na ata: [2026-09-02-call-arthur.md](2026-09-02-call-arthur.md).

## Atividade recente (11–13/08/2026, via dailies)

- **Leonardo (Retaguarda)** começou em 12/08 a **configurar e desenhar a arquitetura da sincronização nas lojas** (propagação de campanhas — a mesma frente descrita no card #12405, "gravação direta de campanhas no banco Retaguarda", cuja propagação pra loja passa a ser de outra equipe — ver nota acima, essa outra equipe é o Thalison/DB). Seguiu nisso em 13/08. Ver [`../dailies/2026-08-12-retaguarda.md`](../dailies/2026-08-12-retaguarda.md) e [`../dailies/2026-08-13-retaguarda.md`](../dailies/2026-08-13-retaguarda.md).
- **Time VAR 3.0** (squad diferente, ver [`../dailies/2026-08-11-var3-projsust.md`](../dailies/2026-08-11-var3-projsust.md) e [`../dailies/2026-08-12-var3-projsust.md`](../dailies/2026-08-12-var3-projsust.md)) está rodando, em paralelo, testes de integração da "rotina de desconto" pelo lado loja/PDV (Guilherme Caixeta) — caminho feliz passando, "primeira compra" é o cenário mais complicado, **nenhum gap de cenário identificado na história até 12/08**. É a contraparte de teste do lado loja pro que o Leonardo está desenhando do lado Retaguarda — vale cruzar antes de fechar o desenho de sincronização.

## Reuniões

- **02/09/2026 — Igor + Arthur. Realizada.** Cobriu: confirmação da correção de propagação, dificuldades de uso em campanhas grandes, pedido de combo com 1 item, e-mails de notificação incorretos, e uma dúvida técnica do Arthur sobre cadastro em nível SKU. **Não cobriu** US5 (notificação às lojas) nem a reativação do job de duplicação — ambos seguem em aberto. Ata completa em [2026-09-02-call-arthur.md](2026-09-02-call-arthur.md); resumo pra gestores em [2026-09-02-call-arthur-resumo-executivo.md](2026-09-02-call-arthur-resumo-executivo.md).

## Próxima atualização

- Igor confirmar com Fabio/Kauã/Spin os pontos em aberto da call de 02/09 (ver "Bloqueios e pendências") e criar os cards dos 2 itens já prontos pra dev.
- Agendar/alinhar separadamente a reativação do job de duplicação (Thalison/Fabio) e o escopo da US5 — nenhum dos dois tem data marcada.
