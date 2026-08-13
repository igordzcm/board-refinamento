# Dashboard CDS — prep pra reunião com a Maria

> Notas de preparação. Objetivo: sair da reunião com o que falta pra escrever o card direito.

## Contexto do projeto

Épico **[#10810 — Dashboard CD](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/10810)** (Var Retaguarda), status **Doing**. O que já foi entregue:

| Card | O que é | Status |
|---|---|---|
| [#10811](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/10811) | Coletar e tratar dados do **WMS** | Done |
| [#10812](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/10812) | Coletar e tratar dados de **BI** | Done |
| [#10813](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/10813) | Validar dados do Excel (etapa antes da integração automática) | Done |
| [#10814](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/10814) | Criação do Dashboard (consolida WMS + BI) | Done — com histórico de QA (ver abaixo) |
| [#11370](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11370) | POC IA — CDS | Done |
| [#11973](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11973) | Trocar PowerAutomate por FTP no Dashboard CDS | **To do** — sem definição técnica completa |

## Bloqueios e pendências atuais

- **#11973 (FTP no lugar do PowerAutomate)** — QA (Danilo) já apontou duas vezes que a descrição não dá pra entender o fluxo completo. Falta: host, protocolo (FTP/SFTP/FTPS), credenciais, formato/layout do arquivo, e o mapeamento 1:1 das funcionalidades que o PowerAutomate faz hoje. Card ainda não tem definição técnica suficiente pra virar Ready for Dev.
- **Dependência de dados "certinhos" pro cron job** — comentário do João Neto (06/04/2026) no #10814: *"Falta os dados do WMS e BI certinho para fazer o cron job rodar corretamente. Assim que tiver o depara do BI pronto."* Ou seja, o pipeline de atualização automática do dashboard depende de um de-para de BI que, até abril, ainda não estava pronto. **Isso é o motivo direto da reunião** — se a Maria trocou de fonte ou parou de usar o WMS, esse de-para pode estar desatualizado ou nem fazer mais sentido.
- **#10814 (Dashboard) — pendência de QA menor em aberto**: formatação de data após atualização das informações (não trava a funcionalidade, mas ficou registrado, sem confirmação de correção).

## Objetivo da reunião

1. **Puxar com a Maria todas as mudanças** que aconteceram no processo/fontes — é o que falta pra escrever o card direito (atualizar #11973 ou abrir um novo, dependendo do que mudou).
2. **Pegar a planilha** que ela usa hoje (provavelmente o de-para do BI, ou a fonte que substituiu o WMS).
3. **Perguntar se ela trocou as fontes de dado e parou de usar o WMS.**

## Perguntas pra levar

- [x] O que mudou no processo desde a última vez que isso foi definido? — ver resumo abaixo (data do inventário, tabela de loja nova, gráfico novo, base de rotas unificada, PROCV de peças, fórmula de lead time corrigida).
- [x] Ela trocou as fontes de dados? Quais são as fontes hoje? — **Não trocou.** Fontes seguem as mesmas (WMS + BI).
- [x] Ela parou de usar o WMS? Se sim, o que substituiu, e desde quando? — **Não parou.** Encontraram e contornaram o problema original sem precisar trocar de fonte.
- [ ] Pode compartilhar a planilha atual (de-para, ou o que for a fonte hoje)? — Maria disse que ia atualizar e mandar no grupo ainda em 12/08; **confirmar se chegou**.
- [ ] O fluxo do FTP pro Dashboard CDS (card #11973) ainda é necessário do jeito que foi descrito, ou o escopo mudou junto com a fonte de dados? — **Não foi discutido nesta reunião** (o foco acabou sendo 100% nas mudanças de cálculo/gráfico da planilha). Como a fonte de dados (WMS) não mudou, a premissa original de que a planilha corrigida "eliminaria a necessidade do FTP" não se confirma nem se descarta aqui — fica pendente de uma conversa específica sobre #11973.
- [x] Quem são os destinatários/consumidores do dashboard hoje — mudou desde a criação original? — Confirmado: painel **operacional**, pro pessoal de carregamento decidir o que dá/não dá pra carregar; será exibido numa TV (não é sobre tempo de entrega, que é outro escopo, levantado por um tal "Francisco"/"Porteiro" fora do CD).

## Depois da reunião

- [ ] Atualizar o card #11973 (ou abrir um novo, se o escopo mudou) com as definições coletadas — **ainda pendente**, já que #11973 nem foi discutido nesta rodada; decidir se ele segue válido ou se vira card obsoleto numa próxima conversa.
- [ ] Salvar a planilha recebida em `board-refinamento/referencias/` (seguindo a convenção: `<card-id>-<slug>`) — aguardando Maria enviar a planilha atualizada no grupo.
- [x] Se ela confirmar que não usa mais WMS: revisar se #10811 ficou obsoleto — **não se aplica**, ela confirmou que continua usando WMS.
- [x] Registrar aqui o resumo da reunião — ver abaixo.
- [ ] **Novo:** replicar no sistema as mudanças que a Maria já fez na planilha (prioridade nº1 combinada na reunião, antes de qualquer melhoria nova).
- [ ] **Novo:** falar com Sergio (da Silva) sobre a mudança de data no relatório do WMS que chega pro time.
- [ ] **Novo:** registrar como pedidos de melhoria (pós-paridade): filtro no gráfico, campo "último carregamento" (manual, por rota), exibir "média da rota" ao lado da capacidade disponível, números sempre visíveis no gráfico (sem precisar de hover — vai pra uma TV).

## Resumo da reunião

> Transcrição completa em [transcricao-reuniao-maria-2026-08-12.md](transcricao-reuniao-maria-2026-08-12.md).

**Não houve troca de fonte de dados.** A dúvida que motivou a reunião (Maria teria trocado de fonte e parado de usar o WMS) foi descartada logo no início: o time da Maria identificou e contornou o problema original sem precisar mudar de fonte. WMS e BI seguem sendo as fontes.

**Mudanças que a Maria já fez na planilha dela (replicar no sistema, nessa ordem):**

1. **Data de referência** — passou a puxar a partir de 29/06 (data do último inventário nos dois CDs), em vez da lógica de data anterior.
2. **Tabela de lojas nova** — lista todas as lojas do CD com soma das peças há mais de 7 dias.
3. **Gráfico novo — Top 20 lojas com peças a mais de 7 dias + lead time médio** — substitui o gráfico anterior, agora nos dois CDs (80 e 83) juntos. Colunas: loja, qtd. de peças, lead time. Ordenado pelo lead time (maior → menor), não pela quantidade de peças. Mantém o corte de Top 20 (senão fica extenso, são muitas lojas).
4. **Faturado no CD e rotas unificados** — antes eram 2 bases separadas por CD; hoje é uma base só (o time de transporte unificou o carregamento entre os CDs, como já era feito em Alagoas). PROCV já traz o CD automaticamente — não precisa mais checar manualmente se a rota bate com a loja.
5. **Quantidade de peças via PROCV** — coluna auxiliar sobre o campo "pack" (pack = qtd. de peças por pack) pra resolver divergências antigas de contagem, puxando do BI. Quando o PROCV não encontra ("nada"), Maria filtra/copia os packs faltantes manualmente pro BI.
6. **Fórmula do lead time geral corrigida** — estava fazendo média sobre média (errado); corrigido pra **média ponderada** por quantidade de lojas/peças de cada rota, nos dois CDs. Fórmula exata capturada em print: `=SOMARPRODUTO(AJ2:AJ8;AM2:AM8)/SOMA(AJ2:AJ8)` — ver [formula-lead-time-ponderado.png](formula-lead-time-ponderado.png). Precisa bater com a planilha de estoque do CD 83 ao replicar.
7. **Relatório do WMS** — só mudou a data (nada de estrutura); falar com **Sergio da Silva** pra atualizar o relatório que chega pro time.
8. **Mapa** — sem mudanças por enquanto (ainda não está em uso).

**Pedidos de melhoria levantados (só depois de bater a paridade acima):**

- **Filtro no gráfico** — tema levantado por Maria/Laurysson antes, sem detalhe fechado ainda.
- **"Último carregamento" por rota** — campo auxiliar (pode ser preenchimento manual, ao menos inicialmente) pra sinalizar quando uma rota "disponível" na verdade já carregou e não tem a capacidade real que o relatório mostra. Possível cruzamento futuro com o SIACON, não confirmado. Exemplo do tipo de visão que Maria descreveu (mercadoria disponível vs. outbound criado, rota disponível/indisponível, por rota no CD 80): [grafico-rotas-disponibilidade-cd80.png](grafico-rotas-disponibilidade-cd80.png).
- **"Média da rota"** — pedido do Francisco: exibir a média de carregamento por rota (já existe na planilha de estoque) ao lado da capacidade disponível atual, pra dar noção de % da rota carregada.
- **Números sempre visíveis no gráfico** — hoje só aparecem no hover; o painel vai pra uma TV operacional, então precisa aparecer sempre.

**Combinado:** prioridade imediata é replicar as mudanças 1–8 acima pra manter sistema e planilha compatíveis; só depois entrar nas melhorias novas. Maria vai desenhar um esboço/protótipo antes de qualquer mudança visual nova ser implementada, pra validar entendimento antes de ir pro programa. Maria vai atualizar as rotas na planilha e enviar a versão nova pro grupo ainda em 12/08.



criar cards a partir dessa reuniao