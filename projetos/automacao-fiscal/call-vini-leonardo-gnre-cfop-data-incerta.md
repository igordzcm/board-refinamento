# Call Vinicius (Migrate/fiscal) ↔ Leonardo (Retaguarda) — GNRE + filtro CFOP

> **Data não confirmada** — fragmento colado diretamente na conversa pelo Igor, sem metadata de data/hora (diferente dos outros digests deste lote, que vêm de `.docx` com timestamp). Truncado no início (abre em "Esse daí que você abriu...") e no fim (corta em "Leonardo Henrique da Silva parou a[transcrição]") — **tratar como fonte parcial**, pode haver assunto tratado antes/depois do trecho que não temos. Nome do arquivo foge da convenção `AAAA-MM-DD-...` de propósito, pela falta de data confirmada — **renomear quando/se a data for confirmada pelo Igor**.

## Participantes

- **Vinicius Guilherme Mazucco Tirloni Dos Santos** ("Vini") — já conhecido no projeto como o responsável por pedidos de limpeza de dados/NFe do lado Migrate (ver [`../prioridades-sprint.md`](../prioridades-sprint.md) e [`../dailies/2026-08-24-a-28-digest-var3.md`](../dailies/2026-08-24-a-28-digest-var3.md)).
- **Leonardo Henrique da Silva** — dev Retaguarda, já responsável por outro chamado de GNRE em 11-12/08/2026 (ver [`../dailies/2026-08-11-retaguarda.md`](../dailies/2026-08-11-retaguarda.md) e [`../dailies/2026-08-12-retaguarda.md`](../dailies/2026-08-12-retaguarda.md) — aquele caso já foi resolvido, é outra ocorrência).

## Por que foi arquivado aqui (Automação Fiscal)

Nem GNRE nem CFOP são mencionados em nenhuma das 6 transcrições `.docx` processadas nesta mesma rodada (busca por "GNR|CFOP" nelas não retornou nada relevante) — não deu pra cruzar data por conteúdo. A escolha de pasta segue o fato de que **GNRE e CFOP já aparecem nominalmente no backlog do projeto Automação Fiscal** (`../automacao-fiscal/contexto.md`, seção "Triagem de backlog em andamento": "provider service da GNRE" e aba "MODELO X CFOP X CST" do relatório fiscal) — é o encaixe mais razoável disponível, **não uma confirmação de que é literalmente o mesmo backlog**. Se Igor souber que pertence a outro projeto (ex.: Engine Fiscal, NFe/Migrate), mover.

## O que foi dito (resumido, só o que está no trecho)

- Vini reportou dois problemas: um relacionado a **GNRE** (não detalhado no trecho que temos) e um **filtro de CFOP** que trava o processo do time do Vini ("trava o processo de vocês... vocês não conseguem utilizar").
- Leonardo classificou o bug de CFOP como simples ("é só colocar o filtro lá no CFOP") e disse que dá pra subir como **deploy emergencial na quarta ou quinta dessa semana**, dependendo da complexidade — o outro item (GNRE) ele ainda vai validar antes de comprometer prazo.
- Vini disse que vai mandar evidências do problema de GNRE; mencionou que a "próxima missão" do time dele é **quarta-feira**, e que, testando, **os valores ainda não estão batendo** ("a gente está conferindo que realmente não está batendo ainda").
- Leonardo também tratou, em paralelo (não é o bug principal, mas veio na mesma call), de separar numa planilha o que subiu na semana anterior e o que ainda falta subir, pra organizar um próximo deploy — prometeu enviar essa relação pro Vini.
- Combinado: Leonardo avisa o Vini na quarta de manhã se o fix subiu ou se vai ficar pra quinta ("deixa aqui um lembrete pra mim").

## Pendências (extraídas só deste trecho — pode haver mais fora do fragmento)

- [ ] Vini enviar evidências do problema de GNRE pro Leonardo.
- [ ] Leonardo validar a complexidade do item de GNRE (o de CFOP já foi classificado como simples).
- [ ] Deploy emergencial do fix de CFOP (e possivelmente GNRE, se a validação permitir) — alvo quarta ou quinta dessa semana. **Sem confirmação de que subiu** — este fragmento não cobre o desfecho.
- [ ] Leonardo enviar a relação do que subiu/falta subir (planilha) pro Vini.
- [ ] **Confirmar a data real desta call** e, se possível, o desfecho do deploy — nenhuma das fontes desta rodada de digest cobre isso.
