# Ferramenta Pesquisas Colaboradores — contexto geral

> Arquivo de contexto do projeto. Ler antes de qualquer reunião sobre este projeto.

## O que é

Ferramenta interna (substitui Microsoft Forms + processos manuais) pra criação, disparo, coleta e análise de pesquisas com colaboradores — RH quer uma plataforma, não só um formulário. Consome cadastro do Senior (origem oficial), cria usuário automaticamente, segmenta público (administrativo/CD/loja + cargo/regional), monta formulários estilo Google Forms, integra respostas ao Data Warehouse (People Analytics/Power BI). Módulo dedicado pra Jornada 90 Dias (5 etapas parametrizáveis: 5, 30/35, 70/75, 90 e — nova — 180 dias, esta última nichada pro administrativo).

Documentos-fonte: TAP (25/02/2026, Ozéias, Pessoas e Cultura) e Especificação Funcional (26/03/2026, Ozéias, revisor Diego Aoki, 43 regras + 7 telas) — ambos em [`./`](.). **Motivação real do projeto** (não está nos documentos formais): pedido do time financeiro por uma pesquisa urgente + hoje "tem 14 portais fazendo a mesma coisa" (Ozéias).

## Status atual (11/09/2026) — ainda em levantamento, sem desenvolvimento iniciado

Nenhuma linha de código escrita ainda. O projeto está na fase de **descoberta/especificação**, não de construção. Duas calls realizadas até agora:

1. **[08/09 — Ozéias/Igor/Filipe/Spin](2026-09-08-call-ozeias-diego.md)** — alinhamento interno de preparação (não a call de validação, apesar do nome do arquivo). Levantou 8 dúvidas/pontos em aberto.
2. **[11/09 — Thaís/Francisco (RH, People Analytics)](2026-09-11-call-thais-francisco.md)** — primeira call de descoberta com o RH depois de meses parado. **Não foi reunião de decisão** — o próprio Igor fechou dizendo que ainda falta "bastante coisa pra decidir antes de conseguir desenvolver". Mapeou como o RH faz pesquisas hoje e destrinchou o problema de anonimato em 3 camadas (acesso, base de dados, interface analítica).

**Cronograma de desenvolvimento** já existe como estimativa inicial interna — [cronograma-desenvolvimento.md](cronograma-desenvolvimento.md), ~640h/~18 semanas (1 dev, 36h/semana) — **mas ainda não foi apresentado à Thaís/RH**. O maior risco de estouro é a criação automática de usuário via Senior, que segue sem solução técnica definida (ver dúvida #4 abaixo).

## Status das dúvidas em aberto (atualizado após a call de 11/09)

| # | Dúvida | Status |
|---|---|---|
| 1 | Custos/tempo de desenvolvimento | Estimativa interna existe (cronograma), não compartilhada com RH ainda. |
| 2 | Tabela de aprovações vazia | Sem confirmação. |
| 3 | Capacidade concorrente TI/Dados | Confirmado: será construído 100% internamente, não com ferramenta de mercado. |
| 4 | **Integração com Senior / criação automática de usuário** | 🔴 **Maior gap técnico, sem dono.** Ninguém sabe como automatizar ainda; hipótese solta (via AD) nunca confirmada. Não veio à tona nem na call de 11/09. |
| 5 | Autenticação sem e-mail corporativo | Avançou bastante em 11/09 — ver "Anonimato" abaixo — sem decisão fechada. |
| 6 | LGPD e anonimato | Foi o tema central de 11/09 — 3 camadas mapeadas, modelo proposto, sem fechamento formal com jurídico. |
| 7 | Integração com Data Warehouse | Necessidade reforçada pela Thaís, sem avanço técnico. |
| 8 | "Ciacon" (mesmo projeto?) | Nunca veio à tona em nenhuma das duas calls. |

## Anonimato — o requisito mais crítico do projeto

Modelo proposto (Ozéias, 11/09, não fechado formalmente): o **sistema sabe** quem respondeu (necessário pra impedir resposta duplicada e permitir segmentação por loja/cargo/liderança), mas a **equipe de RH nunca vê identidade** — só metadados agregados. Francisco (People Analytics) separou o problema em 3 camadas que a Especificação Funcional trata como uma só: (1) anonimato no acesso — impedir múltiplas respostas sem necessariamente identificar; (2) anonimato na base — ID/log em vez de CPF como chave; (3) anonimato analítico — agregação mínima (≥5 respondentes) antes de exibir. Ver detalhamento completo em [2026-09-11-call-thais-francisco.md](2026-09-11-call-thais-francisco.md).

**Risco de segurança já confirmado em produção** (não hipótese): já aconteceu de alguém responder uma pesquisa "anônima" em nome de outra pessoa usando o CPF dela, porque o link é aberto sem controle de identidade real.

## Achado que pode mudar a arquitetura: comunicação via contato pessoal

Loja não tem e-mail corporativo — hoje o alcance é 100% manual (folheto físico, WhatsApp do líder, QR code). A RH já sondou informalmente com o jurídico usar e-mail/celular pessoal (já cadastrados na folha de pagamento) pra disparo automático via WhatsApp/SMS/e-mail — "existe a possibilidade", mas sem alinhamento formal. **Igor classificou isso como capaz de mudar o rumo do projeto de forma muito grande.** Alternativas já existentes: Conviva (ferramenta de treinamento, já tem pop-up de comunicação, 100% dos colaboradores logados lá) e pop-up nativo do Senior (existe, mas não contratado — só fica disponível quando o módulo de ponto eletrônico do Senior, TAP já aprovada, for implantado).

## Decisão já fechada: não usar o módulo de pesquisa do próprio Senior

Avaliado e descartado pela Thaís — o gestor direto vê respostas individuais/nominais no módulo do Senior, quebra o requisito de anonimato. Ferramentas de mercado prontas também descartadas por custo (licença por colaborador cadastrado, escala com headcount).

## Gap de escopo: "nuvem de palavras"

Tipo de pergunta usado hoje pelo RH, não listado nos tipos de pergunta da Especificação Funcional (regras 3.18/3.19). Precisa ser reconciliado no próximo documento de especificação.

## Próximos passos

- [ ] Time interno (Igor/Ozéias/Filipe/Guilherme) discutir e produzir documento mais especificado — meta informal: até fim de setembro/2026.
- [ ] Levar pro jurídico a viabilidade de comunicação via contato pessoal.
- [ ] Marcar nova call com a Thaís pra apresentar proposta concreta (telas/textos) antes de codar — sem data ainda.
- [ ] Destravar a dúvida #4 (criação automática de usuário via Senior) — segue sem dono desde 08/09.
- [ ] Explorar magic link por colaborador como alternativa mais simples ao esquema de chave composta que a Thaís trouxe de outra empresa.

## Reuniões

- [08/09/2026 — Ozéias/Igor/Filipe/Spin](2026-09-08-call-ozeias-diego.md)
- [11/09/2026 — Thaís/Francisco (RH)](2026-09-11-call-thais-francisco.md)
