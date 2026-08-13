# Prioridades e Planejamento de Sprint

> Visão acionável — atrasado/bloqueado, o que está sendo feito agora, e o que entra na próxima sprint. Complementa o [dashboard executivo](dashboard-executivo.html) (mais voltado a status/stakeholder) e o [índice de projetos](README.md) (navegação). Atualizado a partir de dailies, reuniões e do dashboard executivo — mesma fonte, ângulo diferente: aqui o corte é por **urgência e alocação de time**, não por projeto.

**Última atualização:** 12/08/2026, via reunião de planejamento de sprint (Ozéias, Igor, Léo — [transcrição](dailies/2026-08-12-planejamento-sprint.md)) + reunião Dashboard CDs (Igor, Maria, JB, Léo — [transcrição](dashboard-cds/transcricao-reuniao-maria-2026-08-12.md)) + [dashboard executivo](dashboard-executivo.html) de 10/08.

---

## 🔴 Atrasado / Bloqueado

Itens onde o time está travado por algo que não controla, ou que já passou do prazo esperado sem decisão.

| Item | Há quanto tempo | Trava | Ação necessária |
|---|---|---|---|
| **SIGA · Indicadores** | Sem data — retomada adiada repetidamente | Sem fonte de dados confiável pra performance de indicadores | Kovalski assume assim que fechar SSO + Automação Fiscal — sem data definida ainda |
| **Overlimit (crédito na venda)** | Desde antes de 04/08 | Fornecedor RPE não respondeu sobre credencial de teste; sem ela não dá pra validar a solução pra limitação do Kong (não suporta 2 credenciais simultâneas) | Cobrar RPE de novo. Bloqueio **não avançou** mesmo com o escopo tendo sido destrinchado em 12/08 (ver Próxima Sprint) — escopo pronto não desbloqueia o fornecedor |
| **SmileGo (NeuroTech)** | +4 semanas sem retorno | Ambiente de teste do fornecedor não funciona, sem massa de dados válida | Escalar formalmente se não houver retorno até o fim da semana |
| **#11973 — FTP no Dashboard CDs** | Em aberto desde antes de 10/08 | Ninguém decidiu se ainda é necessário — a premissa de que a planilha corrigida eliminaria a necessidade do FTP **não se confirmou nem se descartou** na reunião de 12/08 (não entrou na pauta) | Agendar conversa específica sobre esse card entre JB e Maria/área — não misturar com a paridade de planilha |
| **Portal Gamificação sumindo de homolog** | Detectado 12/08 | Ozéias não consegue mais ver o ambiente em homolog | Investigar com o time técnico antes do Kauã retomar o projeto |

**Risco ativo (não bloqueia, mas pesa):** job noturno da Conciliação segue instável no portal Retaguarda — duplicação de lojas em pelo menos 3 ocasiões recentes, correção manual repetida. Time testando mover pra worker dedicado.

---

## 🔄 Em andamento agora

Por squad/dono, o que está sendo trabalhado nesta sprint.

### Retaguarda

| Frente | Dono | Status | Nota |
|---|---|---|---|
| Conciliação Fase 2 — correções finais | **Diego** | ~90%, US8-12 em homologação (In Test) | Bug novo na parte de "linhas" (achado 12/08) — Diego segue sozinho, Kauã libera pra Gamificação |
| Migração VARRet — lote 2 | **JB** | Concluído, em code review/QA | Ozéias vai marcar call com JB pra "subir tudo" |
| SSO / Keycloak | **Kovalski** | 97% | Só falta remover a regra de prazo mínimo de troca de senha |
| Dashboard CDs — replicar paridade de planilha | **JB** (após lote 2) | Escopo definido 12/08, dev ainda não iniciado | 8 mudanças da Maria a replicar (ver `dashboard-cds/contexto.md`) — prioridade sobre as melhorias novas |
| Indicadores de performance (SIGA) | **Danilo** (validação) | "Em tese" pronto, em homolog e Dev | Danilo precisa começar a validar o fluxo completo o quanto antes; validação de regra é em conjunto com o time |
| Automação Fiscal — triagem de backlog | **Ozéias** | Em andamento | Revisando ~40 cards do Kovalski, decidindo o que descarta vs. refina — prazo 14/08 |
| Onboarding Fernandes (Júnior) | **Fernandes**, com Léo acompanhando | Em sustentação | Corrigindo bugs pontuais achados pelo Danilo numa revisão geral do portal; hoje corrigindo bug no contador de conciliação (front) |

### VAR 3.0

| Frente | Dono | Status |
|---|---|---|
| Tap on Phone (GetNet) + VAR 4G — piloto | Gui Oliveira · Walter | 95% / 92%, pilotos rodando juntos desde 10/08 |
| Release fiscal — Engine + Portal Automação | Donato | 95%, piloto desde 03/08 |
| Pix pelo Pinpad | Time VAR | 15%, entrou no meio da sprint |

### Tesouraria

| Frente | Dono | Status |
|---|---|---|
| Migração pra novo sistema | Walter | 55%, sem atualização — depende de decisão sobre incluir o GSX |

---

## 🎯 Planejamento — próxima sprint

Decisões e prioridades saídas da reunião de planejamento de 12/08 (Ozéias + Igor + Léo).

### Realocação de time

- **Kauã**: sai da Conciliação Fase 2 (que agora é só correção com Diego) e volta pra **Gamificação** — mas só depois de confirmado o sumiço do portal em homolog.
- **Diego**: segue sozinho nas correções finais da Conciliação Fase 2 (bug de linhas).
- **JB**: fecha o lote 2 da Migração VARRet (code review/QA) → migra as exportações Excel/PDF do lote 1 pro padrão worker+e-mail (**card #12484**, já refinado) → volta pro Dashboard CDs pra replicar a paridade de planilha com a Maria.
- **Fernandes** (novo Júnior): fica em sustentação por enquanto — tarefas pequenas e variadas de propósito, pra ganhar familiaridade com o sistema e ajudar a esvaziar o backlog de itens pequenos.

### Escopo novo confirmado

- **Overlimit** — escopo destrinchado: tela de import de planilha Excel (clientes elegíveis ao bônus) + mecanismo de distribuição pra loja igual ao da **blacklist** (RPA). Meta: **release de setembro do VAR**, antes do code freeze. Confirmar com o Gui se ele já tinha algo desenvolvido antes de começar do zero.
- **Migração VARRet — lote 1 → worker+e-mail** — pegar tudo que no lote 1 ainda exporta Excel/PDF direto na tela e migrar pro padrão assíncrono (mesmo usado na Automação Planilha Fiscal). Já existe como card **#12484** no board de refinamento (Var Retaguarda), refinado, faltando só a estimativa do time técnico.
- **Dashboard CDs** — replicar as 8 mudanças de cálculo/gráfico que a Maria já fez na planilha dela (prioridade), só depois entrar nos pedidos de melhoria novos (filtro, "último carregamento", "média da rota", números sempre visíveis no gráfico). Detalhe completo em [dashboard-cds/reuniao-maria-2026-08-12.md](dashboard-cds/reuniao-maria-2026-08-12.md).

### Backlog — triagem em andamento

Ozéias está revisando ao vivo a coluna **Backlog** do board, card a card:

- Itens sem contexto claro, parados há +1 ano → **descartar**.
- Itens do Kovalski pra Automação Fiscal (~40 cards) → Ozéias revisa até **sexta (14/08)**.
- SPPO → **morto**, não vai ser feito.
- Itens pequenos e "legais de fazer" → candidatos naturais pro **Fernandes**.
- Tudo que sobreviver à triagem e estiver "mínimo pra desenvolver" → mover pra coluna **Refinement**, separado do que ainda não foi decidido.
- Igor já tinha limpado as colunas **To Do** e **Refinement** antes desta reunião — ficaram vazias, por isso a necessidade da triagem agora.

### Pendências a confirmar antes de fechar o planejamento

- [ ] Card/sintoma exato do bug de "linhas" na Conciliação Fase 2 (Diego) — não detalhado na transcrição.
- [ ] Se o Gui já tem algo desenvolvido pro Overlimit antes de iniciar do zero.
- [ ] Se o sumiço do Portal Gamificação em homolog foi investigado.
- [ ] Se a planilha atualizada da Maria (Dashboard CDs) chegou no grupo.
- [ ] Decisão sobre o card #11973 (FTP) — ainda necessário ou obsoleto?
- [ ] Resultado da triagem de backlog do Ozéias (prazo 14/08).

---

## Fontes

- [dailies/2026-08-12-planejamento-sprint.md](dailies/2026-08-12-planejamento-sprint.md) — transcrição completa da reunião de planejamento.
- [dashboard-cds/reuniao-maria-2026-08-12.md](dashboard-cds/reuniao-maria-2026-08-12.md) — resumo estruturado da reunião com a Maria.
- [dashboard-executivo.html](dashboard-executivo.html) — dashboard de status, 10/08/2026.
- [README.md](README.md) — índice de todos os projetos com `contexto.md` próprio.
