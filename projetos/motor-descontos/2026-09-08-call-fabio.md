# Pauta + Ata — Call Igor + Fabio, Motor de Descontos (terça, 08/09/2026, 15h)

> Preparada em cima da ata da call com Arthur de 02/09 ([2026-09-02-call-arthur.md](2026-09-02-call-arthur.md)) e do risco ativo registrado em [contexto.md](contexto.md). Objetivo: fechar os retornos que Igor prometeu dar ao Arthur por mensagem, mais o alinhamento do job de duplicação que ainda não tem dono de data. **Ata adicionada em 08/09 após a call** (transcrição "Alinhamentos Motor de Descontos", 23min24s — Igor, Fabio M. Barbosa, Kauã Miguel da Cunha).

## Épico: [#6669 — Motor de Descontos](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/6669)

## 1. Campanha por departamento + itens específicos — já está no planejamento? ✅ Respondido

Contexto: Dia das Crianças começa **17/09**. Fabio hoje sobe esse tipo de campanha manualmente.

**Resposta do Fabio:** o Caixeta já ajustou a rotina PRO013 (campanha por departamento) do lado do VAR, e ela foi **revalidada em QA** — inclusive já rodou uma campanha real recente usando isso: **campanha #923** ("Avenida", 24/06 a 30/06). **Ação do Igor:** confirmar com o Caixeta e os QAs que o teste foi mesmo validado, e então **reativar a criação de campanhas PRO013 no portal da Retaguarda** (hoje desabilitada lá desde que foi tirada por não funcionar do lado VAR).

**Loose end levantado pelo Fabio sobre a #923:** essa campanha teve um problema de cadastro — foi registrada como **global** quando deveria ter sido só pra um **grupo de lojas específico**. Ficou anotado pra alinhar à parte, sem solução ainda.

## 2. Cancelamento real de campanha (futura e ativa) — viável? ✅ Respondido — não existe, mecanismo mantido

**Resposta do Fabio:** confirma que **nunca existiu cancelamento/exclusão real** — mesmo quando o negócio pede pra "cancelar" ou "excluir" uma campanha, na prática sempre foi feito **antecipando a data final**. Existe um acordo informal de **48h de antecedência** pra dar tempo de propagar pras lojas (algumas ficam offline e não recebem a atualização na hora).

**Decisão fechada:** manter o mecanismo real por trás (antecipar data), mas Igor propôs — e Fabio gostou — criar um **botão de "Encerrar campanha"** na interface, que deixa explícito pro usuário que o encerramento só é propagado em até 48h (em vez de só deixar editável o campo de data livremente). Melhoria de usabilidade, não muda o back-end.

## 3. Editar lojas de uma campanha já ativa/global — viável? ✅ Respondido — dois cenários distintos

**Cenário A — campanha não-global (lista de lojas específicas), tirar algumas lojas:** Fabio confirmou que **funciona hoje** com o mesmo mecanismo do item 2 — encerra (antecipa a data) só pra loja(s) que vai(ão) sair, as demais continuam ativas normalmente. Sem problema técnico.

**Cenário B — campanha global (todas as lojas), restringir a um subconjunto:** Fabio foi categórico que **editar a global in-place é arriscado** — se encerrar só em algumas lojas no banco local, a Retaguarda continua com a campanha global ativa, e a carga do Thalison pode reativar a campanha errada naquelas lojas. **O correto é encerrar a global inteira e criar uma nova só com as lojas específicas.**

**Decisão:** construir no portal uma funcionalidade de **"criar nova campanha em lojas específicas" que replica os dados de uma campanha existente**, só trocando a lista de lojas — Fabio confirmou que é exatamente esse o fluxo ("replica e abre pra ele selecionar a lista de lojas"). Fica como melhoria futura, sem data ainda.

## 4. 🔴 Job de duplicação de desconto/cupom — reativação/mapeamento ⚠️ NÃO tratado de fato

Na transcrição, Igor menciona de passagem "isso aqui era só coisa do job, mas já está resolvido" e segue pra outro assunto — **mas não há nenhuma discussão real com o Fabio sobre o job de duplicação, reativação ou o mapeamento pendente com o Thalison nessa call.** Não confiar nessa frase solta como se o item estivesse fechado — continua **sem alinhamento formal**, mesmo risco registrado desde 24/08 em [contexto.md](contexto.md). **Ainda pendente**, precisa de uma conversa dedicada com Thalison/Fabio.

Ponto relacionado, ainda não confirmado: possível segunda ocorrência de "desconto duplicado" trazida pelo Caixeta na daily de VAR 3.0 (01/09) — não veio à tona nesta call.

## 5. 🆕 Campanha por grade (cor/tamanho) = mesmo projeto do cadastro por SKU do Arthur — confirmado

Fabio trouxe que Gustavo/Diego já vêm discutindo um pedido antigo (retomado recentemente) de **campanha de desconto por grade** — desdobrar a promoção não só por item, mas por **cor e/ou tamanho** dentro do item (ex: promover só a cor vermelha de um produto que não está vendendo, sem descontar a cor preta que vende bem). **Igor confirmou com o Fabio que é o mesmo projeto que o Arthur mencionou como "cadastro por SKU"** (dúvida que tinha ficado em aberto desde a call de 02/09) — **resolve a ambiguidade registrada em [contexto.md](contexto.md)**.

Fabio: já existe **TAP aberta** pra esse projeto. Maior complexidade fica no **cadastro** (criar um novo tipo de campanha "grade", com filtro de cor/tamanho por item), a aplicação da regra em si é mais simples. Igor: como mexe em estrutura de tabela dos dois lados (Retaguarda + VAR), é candidato a discussão formal separada via TAP, não pauta de refinamento direto.

## 6. 🆕 Conflito de itens entre campanhas — gap identificado (PRO013 não é checado)

Fabio trouxe uma dor recorrente: quando o Arthur manda listas grandes de itens pra incorporar numa campanha ativa (ex: campanha #1240 recente), frequentemente há **itens em conflito com campanhas "sintéticas" por departamento (PRO013)** já vigentes — ex. uma campanha "Leve 3 Pague 2" pro departamento inteiro de DINS conflita com itens de DINS que entram avulsos numa lista de remarcados. Hoje a verificação de conflito automática só cobre **PRO014 ↔ PRO017** (ambas por lista analítica de item), **não cobre PRO013** (por departamento). Fabio também apontou que às vezes a própria lista que o Arthur manda já vem com **itens duplicados** (causou erro de violação de chave numa lista de 800+ itens recentemente).

**Ação:** ampliar a verificação de conflito de itens (já prevista como melhoria de edição de campanha) pra também cruzar contra campanhas PRO013 ativas por departamento — gap técnico novo a considerar no escopo da melhoria de edição.

## 7. Campanha de departamento + itens específicos (Dia das Crianças) — como o Fabio faz hoje

Fabio explicou o processo manual atual: pega todos os itens ativos do departamento pedido, monta uma lista, e faz o cadastro como se fosse uma campanha PRO014 normal (lista de itens) — perde a semântica de "departamento" no cadastro, vira uma lista analítica. Ofereceu passar a query que usa:

```sql
select itedcmcod, dcmnom, itecod, itenom
from var.dcm001, var.ite001
where itedcmcod in (&Departamento)
  and iteexclido = 0
  and dcmcod = itedcmcod
order by itedcmcod, itecod
```

**Decisão:** dá pra fazer uma interface nova no portal que deixa o usuário selecionar visualmente por departamento, mas por trás busca os itens com essa lógica e cria como campanha PRO014 normal — Fabio confirmou que é simples e não é problema mesmo sem a propagação direta da Retaguarda pra loja (é o Thalison que propaga agora). Sem data ainda, mas sem bloqueio técnico. No futuro, pensar em visualização/edição melhor — por ora, mesmo esquema da lista de itens.

## Fora de pauta fechada, não citado nesta call

- Timeout ao subir listas muito grandes (~8.000 itens) — não veio à tona.
- 2 itens de backlog já refinados esperando priorização ([#11813](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/11813), [#11818](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/11818)) — não veio à tona.

## Depois da call

- [ ] Confirmar com Caixeta/QAs a validação da PRO013 e reativar no portal da Retaguarda.
- [ ] Alinhar à parte o problema de cadastro (global vs. grupo de lojas) da campanha #923.
- [ ] **Marcar alinhamento dedicado sobre o job de duplicação** — não foi resolvido nesta call, apesar da menção ambígua do Igor.
- [ ] Atualizar [contexto.md](contexto.md) e [minhas-pendencias.md](../minhas-pendencias.md) com todas as respostas acima.
- [ ] Responder o Arthur por mensagem com os pontos 1-3 (era o combinado da call de 02/09) — agora com resposta real do Fabio, não só a pergunta.
- [ ] Sinalizar a confirmação do projeto "campanha por grade = cadastro por SKU" pro Arthur também.