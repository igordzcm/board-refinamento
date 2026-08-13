# Apresentação inicial da Conciliação Fase 2 — pro Ozeias

> Reunião pra apresentar a versão inicial (v1) da Conciliação Fase 2 e pegar a opinião do Ozeias **antes** de levar pras áreas que vão usar (Financeiro, Contábil, RH, Diretoria).

## Objetivo

Essa é a etapa "apresentar ao responsável" do fluxo de validação (ver [fluxograma](https://claude.ai/code/artifact/2b33340a-6d0a-415e-835c-87cfd64943ee)). Sair da reunião com o aval do Ozeias pra agendar as sessões de validação com as 4 áreas (US13, card #12400).

## O que mostrar

- **Visão geral do que foi entregue** (US8–US12, todas em homologação técnica desde 10/08):
  - Envio automático de arquivos — cron + retry (US8)
  - Webhooks de entrega, bounce e leitura (US9)
  - Reenvio individual, download auditado e retenção de arquivos (US10)
  - Atualização em tempo real de Perdas e Vales (US11)
  - Homologação técnica / QA (US12)
- **O que vem depois** (US13/US14): validação com Financeiro/Contábil/RH/Diretoria → treinamento → go-live/hypercare.
- Se der, uma navegação ao vivo do fluxo em homologação (não só slides).

## Pontos a levantar com transparência

- [ ] Confirmar se os 2 bloqueios técnicos levantados no refinamento já foram resolvidos:
  - US8: credenciais/mecanismo de envio (MTA) — pendente de Spin/Taunay
  - US9: autorização do tenant Microsoft (Mail.Read) pros webhooks
- [ ] Mencionar o risco ativo do **job noturno instável** (duplicação de lojas, 3+ ocorrências no período) — time já testando mover pra worker dedicado. Perguntar se isso deveria atrasar a homologação de negócio ou pode rodar em paralelo.
- [ ] US13 e US14 têm bloqueio externo real de agenda (áreas de negócio) e ambiente/infra — não é algo que se resolve nessa reunião, só avisar que está mapeado.

## O que perguntar / decidir com o Ozeias

- [ ] A v1 está pronta pra ser levada às áreas, ou falta ajuste antes?
- [ ] Aprovação pra eu (PO) agendar as sessões de validação com Financeiro, Contábil, RH e Diretoria?
- [ ] Alguma área tem prioridade ou ordem sugerida pra validar primeiro?
- [ ] Quem mais precisa estar na apresentação pras áreas (o Ozeias participa, ou só aprova o material)?

## Depois da reunião

- [ ] Atualizar `contexto.md` desta pasta com o que foi decidido.
- [ ] Se aprovado: atualizar o card #12400 no Azure com a confirmação e seguir pro agendamento.
- [ ] Se pedir ajuste: registrar o que precisa mudar antes da próxima rodada.

## Resumo da reunião

*(preencher depois)*
