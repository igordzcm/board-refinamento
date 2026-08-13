# Gamificação (Roleta 3.0) — contexto geral

> Arquivo de contexto do projeto. Atualizado a partir dos planos técnicos (v9.3 e EP1/EP2/EP3), de dailies e do dashboard executivo. Ler antes de qualquer reunião sobre este projeto.

## O que é

Portal de Gamificação Avenida (Roleta 3.0): cliente identifica-se por CPF, é elegível a campanhas com diferentes mecânicas de jogo (Roleta, Raspadinha, Caça-Níquel, Gol Premiado) e recebe voucher de desconto gerado pela lógica de voucher já existente no VAR (campo PRO015). Inclui backoffice step-by-step para cadastro de campanhas, antifraude/auditoria de cadastro e analytics (CRM/BI + pixel).

Épico: **[#11950 — Gameficação](https://dev.azure.com/GrupoAvenida/409b9844-c75c-4e46-8a4d-17e4c455ca1b/_workitems/edit/11950)** (Var Retaguarda). Cards ativos hoje: **T7–T10** (#12186–#12189), em **Refinement**.

## Dono

Dev: **Kauã**. Dono de negócio: **Ozéias Tavares**.

## Status atual (12/08/2026, via reunião de planejamento de sprint)

> Fonte: [`../dailies/2026-08-12-planejamento-sprint.md`](../dailies/2026-08-12-planejamento-sprint.md).

**Kauã volta pra Gamificação em breve.** Combinado entre Igor e Ozéias em 12/08: como o que resta da Conciliação Fase 2 tende a ser correção pontual (não mais desenvolvimento novo — Diego segue sozinho nisso), o Kauã libera e volta pra Gamificação, "que ele tem bastante coisa pra fazer ainda".

**Alerta de visibilidade em homolog**: Ozéias reportou que não consegue mais ver o Portal Gamificação em homolog — "sempre quando eu olho homolog nunca mais está lá. Será que tiraram de homolog?" — não foi investigado na própria reunião, fica como pendência a checar antes do Kauã retomar.

Confirma o padrão histórico: projeto **perpetuamente despriorizado** sempre que a Conciliação Fase 2 precisa do Kauã, não é um bloqueio pontual. Via daily de 04/08 (info anterior): ajustes no mockup de front-end ainda estavam sendo feitos a pedido do Ozéias.

## Mapeamento entre a numeração original (T1–T10) e os cards T7–T10 do Azure

O plano técnico completo (`us_gamificacao_v2_completo.md`, v9.3, 19/06/2026) organiza o projeto em **4 épicos e 10 tasks (T1–T10, 528h)**:

| Épico do plano original | Tasks | Horas |
|---|---|---|
| Épico 1 — Front mockado | T1–T4 | 208h |
| Épico 2 — APIs e integração | T5–T8 | 204h |
| Épico 3 — Jogos e animações | T9 | 64h |
| Épico 4 — Fechamento (QA e go-live) | T10 | 52h |

Isso **confirma diretamente** a leitura de que os cards atuais no Azure (T7, T8, T9, T10 = #12186–#12189) são a cauda final deste mesmo projeto: T7 e T8 caem dentro do Épico 2 (APIs e integração), T9 é o Épico 3 inteiro (jogos e animações) e T10 é o Épico 4 inteiro (performance, QA, go-live). O mapeamento não precisou ser tratado como incerto — a numeração T1–T10 do plano bate exatamente com a numeração dos cards no board.

**Atenção para não confundir:** existe um segundo documento fonte na mesma pasta, `us_gamificacao_ep1_ep2_ep3-v2.md` (responsável Ozéias Tavares, revisor Diego Aoki), que reorganiza o mesmo escopo em **EP1/EP2/EP3 com códigos A01–A02, B01–B03, C01–C06** (consolidação de 18 → 11 cards). Essa numeração **não corresponde 1:1** à numeração T1–T10 — são dois recortes diferentes do mesmo projeto, feitos em momentos distintos. Ao usar qualquer um dos dois documentos como referência técnica, confirmar qual dos dois é o vigente antes de citar um código de card para o time.

## Bloqueios (cards T8/T9/T10, via card Azure)

- **T8** — depende de dados de CRM/BI + pixel vindos da área de Marketing.
- **T9** — depende de assets de design (arte, sprites das 4 mecânicas de jogo) ainda não entregues.
- **T10** — depende de ambiente de produção e disponibilidade de stakeholders de negócio para a sessão de homologação.

Todos são bloqueios externos reais, não just falta de capacidade de dev — mas a falta de capacidade (Kauã sendo puxado para Conciliação Fase 2) segue sendo o fator que mais atrasa o avanço mesmo quando os bloqueios externos se resolvem.

## Reuniões

Nenhuma reunião registrada ainda.

## Próxima atualização

Preencher aqui quando o Kauã voltar a ter capacidade dedicada a este projeto: status dos bloqueios de T8 (CRM/BI+pixel), T9 (assets de design) e T10 (ambiente/stakeholders), se os ajustes de mockup pedidos pelo Ozéias em 04/08 foram fechados, e **se o sumiço do portal em homolog (flagado por Ozéias em 12/08) foi investigado e explicado**.
