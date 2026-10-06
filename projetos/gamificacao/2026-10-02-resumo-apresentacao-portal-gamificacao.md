# Portal Gamificação — apresentação e revisão de UX (resumo)

> **Data da reunião: não informada.** O resumo foi recebido em 02/10/2026 e a transcrição original ("Portal Gamificação - Apresentação") não está na pasta. Participante citado: Jonas. Não se sabe se Ana Carina ou Marcos (CRM) estavam presentes.

## Natureza da reunião

Foi mais uma **apresentação do estado atual do portal + revisão de experiência digital/UX** do que uma discussão de regra de negócio.
- **Avaliação geral:** funcionalmente o projeto está bem avançado, mas surgiram pontos importantes de jornada, integração com o site Avenida, design e mensuração, que precisam ser tratados antes de considerar a experiência fechada.
- **Regras de negócio:** já desenvolvidas, validadas e aprovadas. Faltam principalmente os feedbacks finais de CRM/Marketing, incluindo textos.
- **Jonas:** nos próximos ciclos, a homologação deveria chegar com esses ajustes já resolvidos, porque homologação deveria ser algo praticamente pronto pra produção.

## O que foi demonstrado

- **Cadastro de campanha pelo CRM:** tipo de jogo, nome interno e nome pro cliente, chamada, período, lojas participantes, prêmios e probabilidades.
- **Recursos novos:**
  - quantidade de jogadas;
  - prioridade e concorrência entre campanhas;
  - validade do voucher;
  - segmentação por CPF;
  - banners;
  - regulamento/FAQ;
  - acompanhamento da campanha.

## Pontos de melhoria levantados

1. **Gamificação dentro do domínio principal da Avenida.** Crítica forte ao portal numa URL separada. Pode ter redirect ou páginas específicas, mas sempre reforçando o domínio principal e evitando aparência de página externa ou falsa.
2. **Landing page antes do cadastro.** O cliente não deveria cair direto no formulário de CPF. Primeiro ele vê a campanha e o que pode ganhar, clica em Jogar e só então se identifica. O objetivo é reduzir o abandono no início do funil.
3. **Landing page por campanha**, com conteúdo próprio e slug específico.
4. **QR Code por campanha**, pra divulgação em cartazes, vitrines e materiais de loja, levando direto à ação.
5. **Menos fricção no cadastro.** Todos os campos precisam ser obrigatórios? A data de nascimento tem usos válidos (aniversariantes, validação). **A decisão é do CRM.**
6. **Não pedir identificação de novo:** aproveitar sessão/cache quando possível.
7. **Analytics do funil inteiro:** entrada, abandono na primeira página, clique na campanha, cadastro, avanço pro jogo e conclusão, não só vouchers gerados. Google Analytics e tagueamento foram citados.
8. **Revisão forte do design/look & feel:** fundo, fontes, cores, identidade visual e unidade entre site, portal e futuro app. Os layouts finais dependem das artes da agência, e precisa de mais alinhamento com Marketing e CRM.
9. **Seguir com o Mobile First.** A versão mobile já está sendo reformulada, e boa parte dos clientes usa o celular, inclusive na loja.
10. **Campanhas regionalizadas tratadas antes de jogar.** O cliente não pode ganhar um voucher que não consegue usar. Avaliar CEP, praça/região ou geolocalização, ou pelo menos deixar a elegibilidade muito clara antes da participação.
11. **Produto multicanal:** site, SMS, app, redes sociais, QR Code e loja podem levar às campanhas. A experiência precisa ser fluida e mensurável de qualquer origem.
12. **Campanhas segmentadas no site aberto:** como mostrar uma campanha exclusiva pra um grupo de CPFs numa tela pública? Uma possibilidade é nem mostrá-la publicamente e usá-la só em comunicação direcionada.
13. **Integração com o site Avenida.** Criar as landing pages foi considerado simples. A maior dependência é integrá-las ao site atual. **Combinado conversar com o Marcos/time do site** pra definir a implementação.

## Os maiores temas

1. Landing page antes do cadastro.
2. Gamificação dentro do ecossistema/domínio Avenida.
3. UX/design + Mobile First.
4. Analytics/funil de conversão.
5. Regionalização/elegibilidade antes de jogar.

## Relação com cards existentes

- **[#13452](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13452)** "Ajustes de Layout e Experiência Mobile — Portal de Gamificação" (Kauã, Verified em 02/10): cobre parte da revisão visual e mobile. O **carrossel de prêmios no mobile** (cenário 3 do card) não foi pedido nessa reunião. É um ajuste do time, e a reunião pediu uma revisão de design/mobile mais ampla.
- **#12187 (T8 — Analytics, CRM/BI e LGPD, Verified):** pelo resumo, mede vouchers, mas não o funil de navegação no site.
