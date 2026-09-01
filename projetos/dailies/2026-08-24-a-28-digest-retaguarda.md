# Digest — Dailies Retaguarda, 24–28/08/2026

> Síntese das 5 dailies do squad Retaguarda nesse período (24, 25, 26, 27, 28/08). Transcrições originais já descartadas após leitura — conteúdo relevante capturado aqui e nos `contexto.md` de cada projeto.

## Conciliação Fase 2 — módulo RH (Diego)

- **24/08**: devbox com o Danilo (sexta) passando todo o fluxo (guards no front, back, equipe do Valeria API). Reunião com a área do Financeiro — Ozéias mapeou pontos de correção/melhoria, Diego começou a implementar.
- **25/08**: aplicou os ajustes, apresentou pro Ozéias — aprovado, com 2 pontos novos não mapeados. Começou a trabalhar neles. PR pronta, devbox com Danilo. Reunião paralela com a área de RH sobre SIGA Performance de Indicadores.
- **26/08**: **alerta** — "todo o fluxo não está condizente com o que o Financeiro esperava"; card em rework, Diego considerou pausar e esperar decisão sobre o projeto.
- **27/08**: alinhamento resolveu a dúvida — validou plano de "pequena e grande refatoração" com Danilo/Ozéias/Igor. Começou implementação, meta: terminar até o fim do dia.
- **28/08**: **concluído** — devbox com Ozéias aprovou, com uma exigência nova (fallback de CPF manual na tela Gerenciar Perdas quando o sistema não resolve sozinho). Devbox final com Danilo+Kauã confirmou fluxo + fallback. PR pronta.

## SIGA — Performance de Indicadores (Diego)

- 25/08: reunião com a área de RH alinhou retomada do projeto.

## Dashboard CDs (JB)

- 24-27/08: seguiu ajustando mapas e gráficos pedidos pela Maria. 25/08: pediu a planilha de novo (mandada às 18h, tarde demais pra conferir). 27/08: "acredito que já fiz quase tudo", tentando marcar validação final com ela.

## Motor de Descontos (Leonardo)

- 24/08: conversou com Thalison/Fábio (sexta) sobre desativar o job que duplica desconto/cupom nas lojas — vai trabalhar nisso com o Kauã. Pendência de reativar uma tabela "03".
- 25/08: mandou mensagem no zap pro Igor sobre o tema, aguardando resposta.
- Igor (25/08): respondeu ao Arthur sobre a US5, tentando marcar reunião — resultou na call confirmada de 02/09.

## Gamificação (Kauã)

- 24-27/08: passou PRs pro Léo, aguardando aprovação; job de Conciliação com bug visual mas funcional.
- 28/08: painel administrativo subiu no portal, com bugs de auto-increment em investigação. Plano de testar tudo de ponta a ponta na semana de 01/09.

## Ciacon / SSO SIGA (Kovalski)

- 24/08: levantamento de arquitetura do Ciacon feito (sexta), documentação enviada ao Spin/Filipe. Reversão do SSO do SIGA continua.
- 26/08: começou implementação do Ciacon (WSL travou o PC) — engenharia reversa do login (mesmo padrão do Siga, grupos diferentes), achou o proxy, ganhou acesso às máquinas, trocou versão do Keycloak pra resolver CVE de troca de senha. Confirmou com Igor a criação dos 2 cards (#12813/#12814).
- 27/08: terminando integração, abrindo PR pro Spin. Achou pontos não mapeados na engenharia reversa em homolog.
- 28/08: **fechou a integração do Ciacon, PR aberto** — mas describeu o fluxo como "eu faço, eu valido e eu aprovo" (sem segunda revisão). Documentação completa Siga+Ciacon feita, ainda não formalizada no ADO. Alertou que precisa de ajuda (Diego/Kauã) porque segunda (31/08) as máquinas físicas do Siga chegam e SigaPub + outro sistema Siga viram responsabilidade direta do time.

## Automação de testes do portal (Fernando)

- 24-28/08: seguiu com testes automatizados de front (Playwright), resolvendo erros de pipeline, quase terminando.

## QA (Danilo)

- 24/08: bloqueado de novo por VPN.
- 25-26/08: revisou cards em Kanban, moveu ~4 pra refinamento; comentou em cards que precisam de teste com área — maioria de Automação Fiscal. Estudando TAPs e arquivos de indicadores de performance que Igor mandou.
- 26-28/08: focado em devboxes de Conciliação Fase 2 e Gamificação.

## Tesouraria (Sola, via daily separada)

- 25/08: rollout virou 2º terço; terceiro e último terço subiu à noite do mesmo dia — **100% do parque concluído**.
