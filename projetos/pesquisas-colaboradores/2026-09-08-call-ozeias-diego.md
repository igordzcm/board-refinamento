# Pauta + Ata — Call Igor + Ozéias, Ferramenta Pesquisas Colaboradores (08/09/2026)

> Preparada em cima da leitura da TAP (Termo de Abertura, 25/02/2026, Ozéias Tavares — equipe Pessoas e Cultura) e da Especificação Funcional (26/03/2026, Ozéias Tavares, revisor Diego Aoki), ambas em [pesquisas-colaboradores/](.). Objetivo da call: validar escopo do lado técnico e tirar dúvidas antes de qualquer aprovação formal.
>
> **⚠️ Correção pós-call:** os participantes reais foram **Ozéias, Igor, Filipe de Lacerda Grangeiro e Luiz Spineli Lucchi Neto ("Spin")** — **Diego não participou** desta call (transcrição "Bate-Papo Pesquisa Colaboradores", 27min30s, 08/09). Na prática foi um **alinhamento interno de preparação**, não a reunião de validação/aprovação que eu tinha assumido no título original — a reunião de decisão de verdade é **amanhã, 09/09 às 16h, com o time de RH (Thaís e outros)**. Boa parte das perguntas abaixo ficou pendente pra essa reunião de amanhã, não porque não foram levantadas, mas porque o grupo de hoje não tinha quem respondesse.

## O que é (resumo)

Ferramenta interna (substitui solução de mercado) pra criação, disparo, coleta e análise de pesquisas com colaboradores. Consome cadastro do Senior (origem oficial), cria usuário automaticamente, segmenta público (administrativo/CD/loja + cargo/regional), monta formulários estilo Google Forms, e integra respostas ao Data Warehouse pra consumo em People Analytics/Power BI. Módulo dedicado pra Jornada 90 Dias (etapas em 5/35/70/90 dias, parametrizáveis).

A Especificação Funcional (26/03) já está bem mais detalhada que a TAP (25/02) — inclui 43 regras de negócio e telas de escopo (login, home colaborador, responder pesquisa, dashboard RH, criar pesquisa, resultados, Jornada 90 Dias). Bom sinal de que o desenho avançou desde a abertura.

## Pontos em aberto no próprio documento — status pós-call

1. **Custos/Tempo de desenvolvimento ("Em Levantamento")** — ⏳ **Ainda sem estimativa.** O Spin perguntou isso direto na call ("a gente está sem estimativa de esforço total, como é que a gente está com isso?"). Igor respondeu que vai **rodar uma estimativa inicial (usando IAC + parâmetros de outros projetos)** — Spin pediu que seja feito **junto com o Lacerda antes da reunião de amanhã (09/09) com o RH**, pra já levar uma noção de esforço. **Ação pendente do Igor, com prazo amanhã de manhã.**
2. **Tabela de aprovações vazia** — não veio à tona nesta call. Segue pendente de confirmação.
3. **Capacidade concorrente de TI/Dados / quem desenvolve** — não foi perguntado nem respondido explicitamente. Indício pelo tom da call: Igor está ativamente envolvido (vai rodar a estimativa, participa das reuniões de definição), o que sugere que cai pelo menos parcialmente na órbita dele/Retaguarda, mas **isso não foi dito explicitamente** — não tratar como confirmado.

## Dúvidas técnicas — status pós-call

4. **Integração com o Senior** — ⚠️ **Parcialmente respondido, e não é trivial.** Puxar os dados em si é fácil — Ozéias confirmou que já existe uma **view no Logix** pra isso. Mas **ninguém sabe como automatizar a criação do usuário/acesso no momento da contratação** ("não faço a mínima ideia de como a gente faria isso" — Ozéias). Filipe levantou uma pista: hoje quando alguém é contratado, cria-se um usuário no **AD**, e a partir do AD seriam criados os demais acessos — mas isso não foi confirmado como caminho, só uma hipótese solta. **Gap técnico real, sem dono ainda.**
5. **Autenticação sem e-mail corporativo** — não foi discutida a validação formal com Segurança da Informação. Ficou claro que o modelo pretendido é baseado em **CPF**, no mesmo padrão do "Conviva" (ferramenta de treinamento interna que já funciona assim pra todos os colaboradores, inclusive loja). Validação de segurança formal **ainda pendente**.
6. **LGPD e anonimato** — não veio à tona nesta call.
7. **Integração com Data Warehouse** — mencionada de forma vaga ("integração analítica", "informações do BI"), sem responsável nomeado nem aprofundamento. **Ainda pendente.**

## Ponto solto — confirmar se é a mesma coisa

8. **"Ciacon" não veio à tona nesta call.** Segue pendente de confirmar se tem relação com este projeto — perguntar na próxima oportunidade (talvez direto ao Spin, que estava na call).

## Fora de escopo

Não foi revisitado nesta call — segue como estava na Especificação Funcional (seção 4).

## 🆕 O que saiu desta call (não estava na pauta original)

**Contexto real do projeto:** motivado por um pedido específico do time financeiro (precisam de uma pesquisa a semana que vem, e hoje "tem 14 portais fazendo a mesma coisa" — Ozéias quer algo escalável). Problema central: pesquisas com **loja** hoje não funcionam de verdade porque o time de loja não tem e-mail corporativo (só dá pra usar Microsoft Forms pro pessoal de escritório, via e-mail). O modelo de acesso proposto é o mesmo do **Conviva** (login por CPF).

**3 funcionalidades identificadas por Ozéias** (confirma o que já estava na Especificação Funcional): (1) pesquisas comuns (tipo Google Forms), (2) analytics/resultados, (3) Jornada 90 Dias — considerada a mais trabalhosa das três.

**Jornada 90 Dias — parametrização por pessoa ou geral?** Pergunta do Filipe, respondida por Ozéias como "geral, não por pessoa" — mas o próprio Ozéias marcou como **não 100% certo** ("a gente pode perguntar isso [pro RH] amanhã, mas não acho que faça sentido ser por pessoa"). Tratar como resposta provisória, a confirmar amanhã.

**Maior risco identificado na própria call: baixa adesão por falta de incentivo.** Sem e-mail corporativo, não dá pra cobrar o colaborador de loja por e-mail como se faz hoje com o financeiro/escritório. Ideia levantada (não fechada): notificar o **gerente da loja** por e-mail sempre que um funcionário dele receber uma pesquisa, pra ele cobrar de viva voz na reunião diária de "bom dia" — só uma ideia, vai pra pauta de amanhã com o RH.

**Riscos da TAP revisados ao vivo:** "inconsistência cadastral" foi confirmado como risco real e não totalmente mitigável ("se a gente não tiver a informação, não tem como o sistema saber — é risco mesmo", Filipe/Ozéias). "Retrabalho analítico" foi só mencionado, sem aprofundar.

**Entrega faseada — decidido internamente:** Igor propôs entregar em fases (1. pesquisa comum, 2. analytics, 3. Jornada 90 Dias por último, por ser mais complexa) em vez de tudo de uma vez. Spin e Ozéias concordaram ("eu gosto de separar" — Spin). Ozéias destacou que o mais trabalhoso não é o portal em si, e sim as integrações (Senior e afins).

**🔗 Cruza com Motor de Descontos:** Spin mencionou que Ozéias tem reunião marcada **amanhã (09/09) às 11h com o Fabio**, sobre o projeto de **desconto por SKU/grade em campanha** — o mesmo projeto que saiu confirmado na call de hoje com o Fabio sobre Motor de Descontos (ver [motor-descontos/2026-09-08-call-fabio.md](../motor-descontos/2026-09-08-call-fabio.md), item 5). Vale acompanhar essa reunião de amanhã também, já que o Igor participou da descoberta desse cruzamento pelos dois lados.

**Documentos:** Ozéias vai mandar a TAP + Especificação Funcional pro Filipe (ele ainda não tinha recebido).

## Depois da call

- [ ] Igor rodar estimativa inicial de esforço (com Lacerda) antes da reunião de amanhã (09/09) com o RH.
- [ ] **Reunião de verdade é amanhã, 09/09 às 16h, com Thaís/RH** — é lá que a maior parte das perguntas 1-8 acima tem chance real de resposta.
- [ ] Acompanhar a reunião de amanhã 11h (Ozéias + Fabio) sobre desconto por SKU — cruza com Motor de Descontos.
- [ ] Atualizar [minhas-pendencias.md](../minhas-pendencias.md) (item "Ler o TAP + Especificação Funcional...") com o resultado desta call — ainda incompleto, próxima atualização depois de amanhã.
- [ ] Perguntar sobre "Ciacon" na próxima oportunidade (não veio à tona hoje).
- [ ] Considerar criar um `contexto.md` em pesquisas-colaboradores/ depois da reunião de amanhã, quando o escopo estiver mais validado.
