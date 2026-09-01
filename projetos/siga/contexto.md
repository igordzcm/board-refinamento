# SIGA — contexto geral

> Arquivo de contexto do projeto. Atualizado a partir do board do Azure DevOps (levantamento completo em 13/08/2026), de dailies e do dashboard executivo. Ler antes de qualquer reunião sobre qualquer uma das frentes do SIGA.

## O que é

"SIGA" é um sistema à parte do Portal Retaguarda (ligado à gestão de pessoas/RH — escala, lotacionograma, indicadores de performance por loja). Não é um projeto único — são **3 frentes distintas** no board do Azure DevOps, cada uma com seu próprio épico e status. Não confundir uma com a outra ao ler daily ou conversar com o time.

## As 3 frentes

### 1. SSO no SIGA — em andamento ativo (Kovalski)

Integrar o SIGA ao novo login único (Keycloak/Kong), tirando a autenticação própria do sistema. Parte do épico maior de SSO (**#11853**).

| Card | O que é | Status |
|---|---|---|
| [#12498](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12498) | Documentação e arquitetura da implementação | **Accepted** (concluído) |
| [#12499](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12499) | Implementação front-end + back-end (redirecionamento Keycloak via Kong, callback, validação de token, sessão/cookies) | **Dev Review** — Kovalski, 8 pts |

**Atualização 28/08:** implementação tecnicamente pronta (integrou Siga e Ciacon, eliminou o microsserviço de login antigo dentro do SIGA), mas **deploy bloqueado** — Pablo (quem faz o deploy) está de férias, e a WAF bloqueou alguns acessos por questão de contrato. Novo ambiente não subiu ainda pro time testar.

**Novidade operacional (31/08):** as máquinas físicas do Siga chegam segunda-feira — a partir daí, **SigaPub e o restante do Siga viram responsabilidade direta da Retaguarda** (hoje na mão de uma única pessoa do lado de fora). Kovalski sinalizou que não dá conta sozinho, vai precisar de apoio do Diego/Kauã pra assumir.

**É isso que o Kovalski cita nas dailies desta semana** — **não tem relação com o item 2 abaixo (Performance de Indicadores)**, apesar de os dois aparecerem juntos em conversa por serem do mesmo sistema.

### 1.1 Ciacon — sistema novo, integração fechada (Kovalski)

Sistema separado do Siga, ligado à remarcação de preço (Donato tem a documentação de negócio) — login/autenticação diferentes do Siga, exigiu engenharia reversa própria. Entrou no escopo do Kovalski em 24/08. Cards filhos do mesmo Epic SSO (**#11853**):

| Card | O que é | Status |
|---|---|---|
| [#12813](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12813) | Levantamento e documentação técnica | Refinement — Kovalski diz que já terminou (28/08), mas ainda não formalizado no ADO (0 comentários) |
| [#12814](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/12814) | Implementação | **Dev Review** — PR já aberto pro Spin (27-28/08) |

**Risco de processo:** Kovalski descreveu o próprio fluxo de aprovação do PR como "eu faço, eu valido e eu aprovo" — sem segunda revisão. Vale considerar pedir revisão de outro dev antes de mesclar.

### 2. Performance de Indicadores [SIGA] — bloqueado, precisa ser refeito

Dashboard de indicadores de performance por loja/área (Venda Mercantil, Produtos Financeiros, NPS, Gestão de Pessoas, POP, Prevenção de Perdas). Épico **[#10373 — Performance de Indicadores \[SIGA\]](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/10373)**, State: Doing.

**Levantamento completo em 13/08: os 18 cards filhos do épico estão TODOS em "To do"** — nada foi de fato entregue ainda, apesar de ter sido citado na reunião de planejamento de 12/08 como "em tese está tudo desenvolvido, só falta o Danilo validar". **Correção do Igor (13/08): essa leitura estava errada — o que tinha sido desenvolvido no passado estava errado, segue bloqueado.** Já existem conversas em andamento pra retomar essa frente, mas ainda sem solução definida.

Cards do backlog (todos To do, épico #10373 salvo indicação contrária):
- Disponibilizar dados do SIGA por bloco: Venda Mercantil (#9789), Produtos Financeiros (#9790), NPS (#9791), Gestão de Pessoas (#9792), POP (#9793), Prevenção de Perdas (#9794)
- Mecanismos de upload por indicador: Participação (#9795), % Ativados (#9796), Digitados (#9797), PCJ (#9798), POP-Ranking (#9799), Descontos (#9800)
- Desenvolvimento dos gráficos iniciais (#10868)
- Job de congelar dados (#11010) + mecanismo de congelar dados do passado (#11011)
- Ajustar/padronizar indicadores conforme documentação de operações (#11014)
- Padronizar filtro de data (mês/trimestre) (#11140)
- Novos indicadores — Produtos Financeiros, Posição no Ranking (#11156)
- Automatizar indicadores — Gestão de Pessoas (#11157), Prevenção de Perdas (#11159)
- Import manual — Gestão de Pessoas (#11829), Prevenção de Perdas (#11831)
- Ajustar carga histórica de Ranking/NPS (#11834)
- Automação dos indicadores de RH no Painel (#12047)
- Implementar indicadores de Conversão de Produtos Financeiros (#12011, parent diferente — épico #11037)

**Sem dono de dev confirmado ainda pra essa retomada** — a pendir de definição nas conversas que estão começando agora (13/08).

### 3. SIGA (Sustentação) — maioria entregue, sustentação contínua

Épico guarda-chuva **[#7330 — SIGA (Sustentação)](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/7330)**, State: Doing. Escala, Lotacionograma (mapa de quadro de pessoal), relatórios operacionais — a maior parte já **Done**:

- Lotacionograma: Fases 1/2/3 (#7901/#7903/#7905), ajustes (#9866, #10328), bug de afastados (#10630) — todos Done.
- Escala: alterações de layout/RN (#7331, #7332) — Done. **Em aberto:** "Ajustes e Validações no Preenchimento em Massa da Escala no SIGA" (#8818) — **Dev Review** (quase pronto).
- Outros itens Done: Produtos Financeiros Hora a Hora (#7883), Relatório sem operador (#8311), Peça p/ Cupom por operador (#8812), teste regressivo pós-Node (#10617), revalidação de filtros (#11210), bug de faixa de horário (#8024), bug de folga/férias massivas (#8064), bug de contabilização de Aprendiz no quadro (#11565).
- **Não iniciado:** "Sofia no SIGA" (#9832) — To do, sem mais contexto levantado ainda.

## Próxima atualização

Preencher aqui quando: (1) o Kovalski terminar #12499 (meta 14/08) e o SSO no SIGA entrar em produção; (2) as conversas sobre retomar Performance de Indicadores (#10373) definirem dono/escopo/prazo; (3) "Sofia no SIGA" (#9832) ganhar mais contexto; (4) #8818 (Dev Review) sair de revisão.
