# Ferramenta Pesquisas Colaboradores — call com RH (Thaís/Francisco), 11/09/2026

> Transcrição "Projeto Ferramenta Pesquisas com Colaboradores", 1h0m32s. Participantes: Ozéias Denis de A. Tavares, Igor Diniz Camargo, Filipe de Lacerda Grangeiro (entrou alguns minutos atrasado), Thaís Cristina Pino Diehl (gerente People Analytics) e **Francisco Ligabue Ribeiro** (especialista People Analytics, recém-chegado no time da Thaís — participante novo, não citado nas atas anteriores). **Não foi reunião de decisão/aprovação** — Ozéias abriu a call explicando que o objetivo era retomar o assunto (parado há meses) e levantar como o RH faz pesquisas hoje antes de especificar solução técnica. Igor fechou a call confirmando: ainda falta "bastante coisa pra decidir antes de conseguir desenvolver".

## Como o RH faz pesquisas hoje

**Recorrentes, identificadas (não anônimas):**
- **Jornada 90 dias** — colaborador responde em 4 momentos (5, 30/35, 70/75, 90 dias); o líder dele responde sobre o mesmo colaborador em 2 momentos (35 e 70 dias) — 6 disparos no total. Hoje via Microsoft Forms, link único igual pra todo mundo, CPF coletado manualmente pra cruzar com a base. Contrato de experiência é 45+45 dias — o objetivo da jornada é decidir se mantém o colaborador antes dos 90 dias baterem.
- **Nova etapa de 180 dias** — **não é processo separado**: é uma 5ª etapa dentro da mesma Jornada 90 dias, só que nichada pro público administrativo (loja não entra). Confirmado por Francisco: "a diferença é só a configuração do gatilho que elege o público-alvo".
- **Entrevista de desligamento** — link enviado quando o colaborador sai, mede motivos de saída pra análise de turnover.
- Loja não tem e-mail (nem o gerente — só e-mail da loja). Hoje o alcance é 100% manual: folheto físico + WhatsApp do líder + QR code.

**Pontuais, anônimas (fotografia, não recorrente):** pesquisa de clima/engajamento, feita anual ou semestralmente. Também via Forms, com CPF coletado "por trás" só pra permitir corte por loja/regional — depois o nome é deletado, só uma pessoa da empresa tem acesso ao arquivo bruto. Regra: só a primeira resposta da pessoa conta (demais são saneadas).

**🔴 Falha de segurança já identificada e confirmada em produção:** por ser link aberto sem controle de identidade real, **já aconteceu de alguém pegar o CPF de outra pessoa e responder em nome dela pra toda uma unidade** — Thaís confirmou isso como fato ocorrido, não hipótese.

**Também podem existir pesquisas pontuais de percepção** ("tiro rápido", ex.: reação dos colaboradores à PEC da escala 5x2) — não recorrentes, não precisam ser anônimas.

## O problema central: anonimato tem 3 camadas, não 1

Francisco (a contribuição técnica mais relevante dele na call) separou o "anonimato" em três problemas distintos, que a Especificação Funcional trata como um só:

1. **No acesso/resposta** — impedir que a mesma pessoa responda mais de uma vez, sem necessariamente identificá-la (ex.: por dispositivo).
2. **Na base de dados** — usar um ID/log em vez do CPF como chave, mantendo campos suficientes (loja, cargo) pra permitir agregação depois.
3. **Na interface analítica** — agregação mínima (Thaís já usa ≥5 respondentes por corte) antes de mostrar qualquer dado, pra não expor indivíduo em grupo pequeno.

**Modelo que Ozéias propôs e ninguém fechou contra:** o sistema *sabe* quem respondeu (precisa, pra impedir resposta duplicada e permitir segmentar por loja/cargo/liderança), mas a **equipe de RH nunca vê a identidade** — só metadados agregados (ex.: "essa resposta é de alguém da loja 310", "essa pessoa é líder ou não"). Anonimato é uma garantia pro RH, não uma incógnita real pro sistema.

**Referência trazida pela Thaís (de uma empresa anterior, não é decisão para cá):** login por chave composta (6 primeiros dígitos do CPF + dia de aniversário + iniciais do nome) — resposta chega como só um ID de log + horário; complexo demais pra alguém repassar de propósito. Igor levantou, sem fechar, se um **link único por colaborador** (magic link) já não resolveria o mesmo problema de forma mais simples — fica como algo a explorar com o time técnico e segurança.

## Por que não usar o módulo de pesquisa do próprio Senior (decisão já fechada)

Thaís confirmou que já avaliou e descartou: no módulo do Senior, **o gestor direto vê as respostas individuais e nominais** — quebra o requisito central do projeto. Ferramentas prontas de mercado também foram descartadas por custo (cobram por licença/colaborador cadastrado, custo escala com headcount independente de quem sai/entra). Confirma a decisão de construir internamente.

## Gap de escopo novo: tipo de pergunta "nuvem de palavras"

Thaís citou que o RH já usa nuvem de palavras como formato de pergunta hoje — **não está na lista de tipos de pergunta da Especificação Funcional** (que lista resposta curta, parágrafo, múltipla escolha, caixa de seleção, escala linear + regra 3.19 menciona Likert/NPS/nota 0-10). Escopo real é maior que o documento formal.

## O maior achado da call: comunicação via contato pessoal pode mudar a arquitetura do projeto

Hoje 100% do alcance é manual (folheto, WhatsApp do líder, QR code) porque loja não tem e-mail corporativo. Opções levantadas:

- **Usar e-mail pessoal/celular já cadastrados na folha de pagamento** pra WhatsApp/SMS/e-mail automático direto da plataforma — Thaís já sondou informalmente com jurídico e "existe a possibilidade", mas falta alinhamento formal sobre como e com que texto/identificação enviar. **Igor classificou isso como capaz de "mudar o rumo do projeto de forma muito grande"** — é ação explícita levar pro jurídico antes de avançar.
- **Conviva** (ferramenta de treinamento, roda no Senior) já tem função de pop-up de comunicação e 100% dos colaboradores já têm login lá — viável hoje, mas nunca usado pra pesquisas.
- **Pop-up nativo do Senior** — o Senior tem essa funcionalidade, mas a empresa não contratou. Só fica disponível quando o módulo de ponto eletrônico da Senior for implantado (TAP já aprovada essa semana, é prioridade) — sem data ainda.

## Pontos técnicos menores confirmados

- **Edição de pergunta em campanha já publicada:** mudança vale só daí pra frente — quem já recebeu a versão antiga mantém; próximos que ainda não responderam recebem a nova. Na Jornada 90 dias, mudar pergunta de uma etapa só afeta quem ainda não bateu aquele marco.
- **Líder vs. não-líder na mesma pesquisa:** uma única pesquisa pro grupo todo (não duas pesquisas separadas) — separar despertaria desconfiança. O corte líder/não-líder vem do cargo já cadastrado, nunca de uma pergunta explícita ao colaborador.
- **Trava de exibição por volume mínimo de respostas:** Igor sugeriu implementação simples — travar a liberação dos dados pro RH até bater um número mínimo de respostas, em vez de mecanismo mais complexo.

## Status das 8 dúvidas da call de 08/09, após esta call

| # | Dúvida | Status pós-11/09 |
|---|---|---|
| 1 | Custos/tempo de desenvolvimento | Ainda em aberto — não foi pauta com o RH; cronograma interno já existe ([cronograma-desenvolvimento.md](cronograma-desenvolvimento.md)) mas não foi apresentado à Thaís. |
| 2 | Tabela de aprovações vazia | Não veio à tona. |
| 3 | Capacidade concorrente TI/Dados | Não veio à tona diretamente; confirmado que o plano é construir 100% internamente ("a ideia não é a gente usar algo interno [de mercado]... construir algo dentro de casa" — Ozéias). |
| 4 | Integração com Senior / criação automática de usuário | **Não discutido nesta call.** Segue sem dono. |
| 5 | Autenticação sem e-mail corporativo | Avançou bastante — ver seções de anonimato acima — mas sem decisão fechada. |
| 6 | LGPD e anonimato | Foi o tema central da call — 3 camadas de anonimato mapeadas, modelo proposto por Ozéias, sem fechamento formal com jurídico/segurança ainda. |
| 7 | Integração com Data Warehouse | Reforçada a necessidade (Thaís precisa cruzar respostas com turnover/absenteísmo por loja/regional), sem avanço técnico. |
| 8 | "Ciacon" | Não veio à tona. |

## Próximos passos (definidos por Ozéias no fechamento)

- [ ] Time interno (Igor/Ozéias/Filipe/Guilherme) discute internamente e monta documento mais especificado — meta informal: até o final de setembro/2026.
- [ ] Levar pro jurídico a viabilidade de comunicação via contato pessoal (e-mail/celular) — classificado como possível ponto de virada do projeto.
- [ ] Marcar nova call com a Thaís pra apresentar propostas concretas (telas/textos) antes de começar a desenvolver — sem data marcada ainda.
- [ ] Reconciliar o gap do tipo de pergunta "nuvem de palavras" com a Especificação Funcional.
- [ ] Retomar com o time técnico a ideia do link único por colaborador (alternativa mais simples ao esquema de chave composta) como possível solução pro anonimato de acesso.
