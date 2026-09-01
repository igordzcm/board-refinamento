# Prioridades e Planejamento de Sprint

> Visão acionável — atrasado/bloqueado, o que está sendo feito agora, e o que precisa virar reunião, card novo ou card refinado. Complementa o [dashboard executivo](dashboard-executivo.html) (status/stakeholder) e o [índice de projetos](README.md) (navegação).

**Última atualização:** 31/08/2026, a partir de 13 transcrições novas (5 dailies Retaguarda, 5 dailies VAR 3.0, 1 Tesouraria, 1 Planning VAR, 1 Review/Retro VAR) cobrindo 24–31/08, mais o desfecho da validação QA da Conciliação Fase 2 no ADO. Ver digests em [dailies/2026-08-24-a-28-digest-retaguarda.md](dailies/2026-08-24-a-28-digest-retaguarda.md) e [dailies/2026-08-24-a-28-digest-var3.md](dailies/2026-08-24-a-28-digest-var3.md).

---

## ✅ Resolvido desde a última atualização (24/08)

- **Conciliação Fase 2 (módulo RH) — pronta, sobe pra produção na GMUD de hoje (31/08).** Pacote completo (#12800, #12808–#12811) aceito após QA com o Danilo. 2 bugs pré-existentes achados na validação viraram cards próprios (#12882, #12884), não bloqueiam.
- **Migração VarRet — testada, aprovada, sobe pra produção na mesma GMUD de hoje.**
- **Tesouraria — rollout 100% do parque concluído** (25/08 à noite).
- **Overlimit — RPE liberou credenciais/webhooks.** Testes de endpoint em produção já começaram, direto no Kong, sem precisar de credencial. Sai da lista de bloqueios críticos.
- **Motor de Descontos — job de duplicação desativado** pelo Leo (mitigação), como combinado com Thalison/Fábio.
- **Reunião com o Arthur confirmada para quarta-feira (02/09)** — escopo ampliado além da US5, cobre os próximos passos do épico inteiro.
- **Ciacon — integração fechada, PR aberto pro Spin.** Cards #12813/#12814 criados e linkados ao Epic SSO (#11853).
- **Gamificação T1–T10** — avançaram todos pra QA/In Test no board; painel administrativo já subiu no portal.

---

## 🔴 Atrasado / Bloqueado

| Item | Desde quando | Trava | Status/ação |
|---|---|---|---|
| **NFe — rejeição em massa pela Migrate (VAR 3.0)** | 21/08 | Documentos antigos travando o DocPay identificados; pedido de limpeza feito ao Vini pra liberar notas represadas | Sem confirmação de resolução total até 28/08 — checar direto com Franklin/Donato antes do fechamento fiscal do mês |
| **SmileGo (NeuroTech)** | +5 semanas sem retorno | Ambiente de teste do fornecedor não funciona | Sem qualquer menção desde 10/08 — confirmar se segue parado ou foi abandonado silenciosamente |
| **Tap on Phone / VAR 4G — bugs críticos novos** 🆕 | Achado no retro de 28/08 | Transações sendo canceladas com pagamento ainda ativo (fatura, acordo) | Squad inteiro dedicado a estabilizar antes do rollout pras lojas (meta: semana de 01/09) |
| **SSO SIGA — deploy bloqueado** | 28/08 | Pablo (deploy) de férias + WAF bloqueando acessos por questão de contrato | Implementação pronta (Dev Review), só falta destravar o deploy |
| **Ciacon — self-review sem segunda pessoa** 🆕 | 28/08 | Kovalski descreveu o fluxo como "eu faço, eu valido e eu aprovo" | Vale pedir revisão de outro dev antes de mesclar definitivamente |

---

## 📅 Reuniões a ter / agendar

- [x] **Igor + Arthur — Motor de Descontos, novas etapas.** Confirmada pra **quarta-feira, 02/09**. Escopo ampliado além da US5 — define os próximos passos do épico inteiro, incluindo o que fazer com o job desativado pelo Leo.
- [ ] **Cobrar formalização da documentação do Ciacon no ADO** — Kovalski diz que terminou (28/08), mas o card #12813 segue com 0 comentários no Azure.
- [ ] **Definir apoio ao Kovalski pras máquinas do Siga** — a partir de 31/08 SigaPub + resto do Siga viram responsabilidade direta da Retaguarda; Kovalski já sinalizou que não dá conta sozinho, precisa de Diego/Kauã.
- [ ] **Endereçar "se tudo é urgente, nada é urgente"** — reclamação #1 do retro VAR 3.0 (28/08). Cards sem critério de aceite criados tarde demais; Gustavo (PO) sobrecarregado cobrindo 2 projetos + infra à noite.

---

## 🃏 Cards a criar

- [x] **Conciliação Fase 2 — 2 bugs pré-existentes achados na validação do #12810.** Criados 31/08: [#12882](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12882) (can-close sem validar status) e [#12884](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12884) (erro genérico em vez da mensagem real).
- [x] **Ciacon — Kovalski, documentação e implementação.** Criados 27/08: [#12813](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12813) e [#12814](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12814), linkados ao Epic SSO (#11853).
- [ ] **VAR 3.0 — Epic de migração GeneXus → Java.** Ainda sem Epic formal. Jeferson já começou a 1ª tarefa (tabela de Feature Flag) a pedido do Walter — Igor pediu card formal pra não perder rastreio.
- [ ] **Tesouraria — regra de NSU padronizada em 8 dígitos.** Pedido do Financeiro (4 dígitos loja + 4 dígitos comprovante GVT); vai numa release separada (3.0.1→3.0.2) por ser mudança de risco assumido — Sola: "provavelmente vai dar rollback depois".
- [ ] **SIGA — Indicadores de Performance, em Ready for Dev.** Segue sem dono/card formal confirmado.

---

## 🔍 Cards a refinar / decisões do PO pendentes

- [ ] **Conciliação Fase 2 #12812 (planilha Contábil).** Bloqueado até a Adriana levantar o layout exato — ⚠️ ainda em aberto se "Arco" (citado por Diego em 28/08 como destino da integração) é o mesmo que o layout Oracle original ou uma mudança de abordagem (integração direta em vez de planilha exportável). Precisa esclarecer com o Diego/Ozéias antes de reescrever o card.
- [ ] **Dashboard CDs — validação final com a Maria.** JB diz que já fez quase tudo, só falta agendar a conferência final.

---

## 🔄 Em andamento agora (por pessoa)

### Retaguarda

| Pessoa | Frente | Status em 31/08 |
|---|---|---|
| **Diego** | Conciliação Fase 2 (produção hoje) + SIGA Indicadores | Fase 2 pronta e aceita, indo pra GMUD; SIGA Indicadores em segundo plano, ~30% |
| **Kauã** | Gamificação (todos os T1-T10 em QA) | Painel administrativo no ar, bugs de auto-increment em ajuste; teste ponta a ponta previsto pra semana de 01/09 |
| **JB** | Dashboard CDs + Migração VarRet (produção hoje) | CDs quase pronto, falta validação final com a Maria; Migração VarRet aprovada, sobe hoje |
| **Fernando** | Automação de testes do portal (8 fases) | Todas as 8 fases concluídas, Playwright (E2E) quase pronto |
| **Kovalski** | SigaPub/SSO, Ciacon (integração fechada) | SSO bloqueado por deploy (Pablo férias + WAF); Ciacon com PR aberto; chegada das máquinas físicas do Siga aumenta a carga |
| **Danilo (QA)** | Testes cruzados — foco intenso em Conciliação Fase 2 essa semana | Validou o pacote completo da Fase 2 até aceitar em 31/08; segue revisando cards de Automação Fiscal pra "teste com área" |
| **Léo** | Motor de Descontos (job desativado) | Aguardando reunião de 02/09 com o Arthur pra formalizar o resto do mapeamento |

### VAR 3.0

| Pessoa | Frente | Status em 31/08 |
|---|---|---|
| **Caixeta** | Overlimit (agora liberado) | Testando endpoints direto no Kong, sem credencial |
| **Donato** | Desconto de Gerente (Java) + apoio Ozéias/Kovalski | Desenvolvimento terminado, aguardando aprovação de review; ajudando na engenharia reversa do Ciacon/loja 208 |
| **Moises + Jeferson** | Testes automatizados mobile + migração GeneXus | POC de teste entregue ao Lacerda; Jeferson iniciou tarefa de Feature Flag da migração |
| **Walter** | Migração GeneXus (documentação) | Documentação atualizada, 1ª tarefa (Feature Flag) já delegada ao Jeferson |
| **Wesley** | Pix pelo Pinpad (TEF) | Bug de truncamento de ID de transação achado, em correção |
| **Nicolas / Felipe** | Tap on Phone / 4G | Bugs críticos novos de fatura/acordo — foco total em estabilizar |
| **Gustavo (PO)** | Cobrindo 2 projetos + infra à noite | Sinal de sobrecarga real — retro de 28/08 votou isso como problema #1 |

---

## ⚠️ Riscos ativos (resumo)

1. **NFe/Migrate** — segue sem confirmação total de resolução, prazo do fechamento fiscal se aproximando.
2. **Tap on Phone/4G** — bugs críticos novos, achados no retro de 28/08.
3. **Sobrecarga da equipe VAR 3.0** — "se tudo é urgente, nada é urgente" foi a reclamação #1 do retro; PO cobrindo demais.
4. **Ciacon sem segunda revisão** — Kovalski aprovando o próprio trabalho, somado à chegada das máquinas do Siga (mais carga pra ele).
5. **NSU 8 dígitos (Tesouraria)** — mudança que o próprio time já espera precisar de rollback; mitigada por ir em release separada.
6. **Motor de Descontos** — job desativado é mitigação, não solução definitiva; depende da reunião de 02/09.

---

## Fontes

- [dailies/2026-08-24-a-28-digest-retaguarda.md](dailies/2026-08-24-a-28-digest-retaguarda.md) — digest das 5 dailies Retaguarda.
- [dailies/2026-08-24-a-28-digest-var3.md](dailies/2026-08-24-a-28-digest-var3.md) — digest das 5 dailies VAR 3.0.
- [dailies/2026-08-25-tesouraria-daily.md](dailies/2026-08-25-tesouraria-daily.md) — daily Tesouraria (regra de NSU + rollout 100%).
- [dailies/2026-08-31-planning-var.md](dailies/2026-08-31-planning-var.md) — planning VAR 3.0.
- [dailies/2026-08-28-retro-var.md](dailies/2026-08-28-retro-var.md) — retro VAR 3.0 (sobrecarga, critério de aceite).
- [dashboard-executivo.html](dashboard-executivo.html) — dashboard de status.
- [README.md](README.md) — índice de todos os projetos com `contexto.md` próprio.
