# Review/Retro Retaguarda (15/09/2026)

> Review + Retrospectiva de sprint do squad Retaguarda (Sprint 28), 35min. Transcrição original em `Review e Retrospectiva de Sprint (1).docx` (raiz do workspace). Participantes: Igor Diniz Camargo (PO), Diego Oliveira Andrade Rafael, Matheus Gabriel Donato Alves, João Bernardo Ferreira Neto (JB), Gabriel Aparecido Kovalski Lopes, Fernando Caetano de Lima, Danilo Santos Manzoli. **Esta é a reunião de review/retro que fecha a sprint — aconteceu "ontem" em relação ao dia de hoje (16/09), quando roda a Sprint Planning seguinte** (ver [`2026-09-16-planning-retaguarda.md`](2026-09-16-planning-retaguarda.md)).

## Review — o que foi feito na sprint

- **Diego**: sprint "bem mais tranquila que a última". Sustentação em Conciliação Fase 2 — melhorias no fluxo de gerenciar perdas (agente do Financeiro aprova divergência, layout padronizado, opção de vincular a qualquer CPF via input manual, mantendo o padrão de retornar dados do operador sênior por default). Achou e corrigiu um bug novo no mesmo fluxo (divergências tipadas como "perda") — mapeado e corrigido numa branch de urgência, sem impacto confirmado até agora. Também trabalhou no sistema de conexão com o ERP Oracle — PR aberta aguardando review do Valdo, deve "resolver de vez" a abertura de contas no Oracle.
- **Donato**: início de sprint com validações junto ao Spineli (mesclagem VAR 3.0 + 4G) e testes de app de remarcação com Ozéias, focados em firmware novo de impressora (funcionar sem a bobina original) — time assumiu quando voltou de férias. Depois entrou o Motor de Descontos (SKU completo em vez de só código do item — visão mais micro pra identificar produto parado/fora de estoque/velho na gôndola). Ontem (14/09): atualização importante — tabela de controle nova pra facilitar a passagem de dados da retaguarda pra loja pro Thalison (mesmo achado já documentado em [`../motor-descontos/contexto.md`](../motor-descontos/contexto.md)).
- **JB**: começou a semana verificando um problema que achavam ser dele (não era); criou cards, passou pro Fernando; entregou o demonstrativo de caixa e todos os relatórios de e-mail "igual o Léo tinha pedido, o falecido" (referência bem-humorada à saída do Léo, ver seção própria abaixo); agora trabalhando no "Ren view". Semana tranquila.
- **Kovalski**: sem novidade — 2 semanas de deploy/configuração de servidor, "a parte de DevOps"; 2 portais novos que o Spin pediu (esqueceu os nomes, sem envolver o time). Achado relevante: sistema de "Pessoas" com um banco de dados descrito como "uma bomba" — quem tinha acesso ao **portal de admin não está mais na empresa**, ninguém tem mais acesso; precisa liberar um DNS; **"não tem muito que a gente possa fazer"** — mesmo achado do Apex Oracle citado na Sprint Planning do dia seguinte (ver arquivo linkado acima).
- **Fernando**: sprint tranquila, bugs simples e melhorias pequenas do portal; alguns cards do JB relacionados a deploy.
- **Danilo**: GMUD grande (muita coisa subiu) foi complexa mas correu bem. Bloqueio que segue no seu lado: **o próprio bug de permissionamento de usuário** (recorrente, não fechado — mesmo item das dailies anteriores). Melhorando fluxo de testes com apoio externo ("Geek"/nome não confirmado na transcrição) trazendo pontos de melhoria. Entregas cada vez melhores, menos bugs chegando em produção.

## 🔴 Saída do Léo — impacto direto no fluxo do time

Igor traz o assunto formalmente na retro (já anunciado na daily do dia anterior, ver [`../dailies/2026-09-09-a-15-digest-retaguarda.md`](../dailies/2026-09-09-a-15-digest-retaguarda.md)): *"vou contar com a ajuda de vocês [...] sobre como talvez aconteçam umas mudanças depois que o Léo saiu."* Dois efeitos concretos discutidos:

1. **Fila de code review crescendo** — 16 cards parados no momento da retro. Igor: *"não tenho certeza como estava antes do Léo sair de férias, mas eu acredito que ele ainda fazia bastante [code review]."* Pede que todo o time adote a rotina que o Kauã já tem (checar a fila toda manhã/depois do almoço) em vez de depender de um único revisor.
2. **Criação de cards por Ozéias muda de dinâmica sem o Léo** — Igor explica que o Léo ajudava a cobrar Ozéias pra criar cards com antecedência e bem descritos; sem ele, Igor espera sentir mais o impacto de cards chegando em cima da hora ou já quase prontos/implementados, exigindo mais atenção própria (ver seção "O que não foi bem" abaixo).

## Retrospectiva

**O que foi bem:**
- Independência crescente entre projetos — qualquer dev consegue tocar qualquer parte do Retaguarda (ex.: se o Diego trava na Conciliação Fase 2, o JB consegue seguir), não fica mais um projeto "preso" a uma pessoa só.
- Time unido, cards melhorando, comunicação melhorando "cada vez mais".

**O que não foi bem:**
- **Fila de code review grande** (16 cards) — ver seção do Léo acima. Kauã confirma que "tem um card ali fantasma do Léo" pra remover, e que há comentários pendentes de resolver, inclusive do Donato — a fila "está travada faz tempo".
- **Cards pulando DevBox antes de ir pra QA** — Danilo trouxe esse ponto de novo (recorrência de um problema já discutido no passado). Igor reforça a importância do fluxo completo; se precisar pular por urgência real, **deixar um comentário explicando o motivo antes do Danilo precisar cobrar**. JB dá o exemplo concreto que motivou o comentário: o card do "demonstrativo de caixa" pulou DevBox porque era confirmação de código já existente, não desenvolvimento novo — caso legítimo, mas sem o comentário explicando isso.
- **Demandas chegando sem card formal** — Igor cita que aconteceu bastante na sprint (ex.: caso do Diego, que zerou a fila de cards e teve que esperar um novo ser passado por Ozéias mais de uma vez). Relaciona ao fato de que os "projetos grandes" (Gamificação, Conciliação Fase 2, Motor de Descontos) já estão entregues/em andamento — o que resta é manutenção/pequenas implementações, difíceis de planejar sprint inteira com antecedência. Ainda não sabe se é falha de comunicação do Ozéias ou falta de antecedência real da demanda dele — segue conversando com Spin sobre isso.
- **Cards do Ozéias nascem já prontos ou quase prontos**, às vezes sem AC claro — Danilo: *"o Ozéias cria o card direto como ele cria e só ele sabe entender [...] não vou ter a memória em si pra lembrar e desenvolver o teste certinho [...] pelo menos ter o critério de aceite do card, tendo uma descrição ali, já é fácil pra mim desenvolver os testes."* Alguns cards nasceram já implementados/em produção, servindo só de registro histórico — Danilo relata ter descoberto isso ao perguntar ao time e ouvir "isso aí já tá rodando em prod". **Proposta do Danilo**: participar ativamente da escrita do Critério de Aceite junto com a criação do card do Ozéias, em vez de só validar depois — Igor gostou da ideia, vai testar na próxima sprint.

## Discussão: usar IA pra validar PR

Ponto trazido informalmente durante a retro (não card formal). Posições:
- **Kovalski**: contra usar IA como validador principal — cita um caso concreto em que ele e o Léo (antes de sair) concordaram que a IA validou apontando coisas "nem referentes à PR" — "pelo menos deu uma segunda validada", mas não substitui revisão humana.
- **Kauã**: incomodado com excesso de comentários da IA em coisas triviais; sugere incluir **auto-review automático no fluxo de commit** (IA revisa antes do commit, nos padrões do projeto) em vez de revisão de PR pesada depois.
- **JB**: defende posição oposta — usa a IA pra criar um worktree, rodar o projeto, testes e build antes de revisar manualmente; acha que ajuda bastante, mesmo com comentários "meio feios".
- **Diego**: usa como auxiliar, não substituto — dá exemplo real (PR do Donato) onde a IA pegou um worker com dependências não declaradas no import que passaria despercebido.
- **Igor**: se inclina pra revisão mais humana, preocupado com qualidade se a validação virar 100% IA ("a boa parte do código hoje já é feito via IA... usar IA completamente pra revisar eu acho perigoso"), mas endossa o uso como auxiliar/segunda camada.

**Combinado:** sem decisão formal fechada — Igor vai acompanhar como está indo o code review nas próximas dailies e retomar o tema na próxima retrospectiva.

## Fechamento

Igor não chegou a passar pelo dashboard do time (vai revisar antes da Planning ou durante ela). Vai produzir uma ata pra enviar ao Spin com os pontos principais — sobretudo criação de cards e relação com Ozéias — pra ajudar a pressionar por mudança.
