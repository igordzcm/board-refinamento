# Ferramenta Pesquisas Colaboradores — cronograma de desenvolvimento (estimativa inicial)

> Base: Especificação Funcional (26/03/2026, 43 regras, 7 telas) + TAP (25/02/2026) + [call Ozéias/Igor de 08/09](2026-09-08-call-ozeias-diego.md). Estimativa bottom-up por módulo, não paramétrica — primeira passada pra levar à reunião com o RH, não uma estimativa fechada. Assume **1 desenvolvedor a 36h úteis/semana** (desconta reuniões, refino, outras demandas da fila da Retaguarda). Com 2 devs em paralelo nas fases 1 e 2, o prazo total cai proporcionalmente, mas a Fase 0 (fundação) não paraleliza bem — é sequencial por natureza.

## Estrutura das fases (já alinhada com Ozéias/Spin em 08/09)

Entrega faseada: 1) pesquisa comum → 2) analytics → 3) Jornada 90 Dias (mais complexa, por último). A Fase 0 é fundação técnica que nenhuma das três funciona sem.

## Estimativa por módulo

| Fase | Módulo | Horas | Semanas (36h) |
|---|---|---:|---:|
| **0 · Fundação** | Setup de projeto (repo, ambientes, CI/CD) | 24h | |
| | Modelagem de dados core (colaborador, chave funcional empresa+tipo+matrícula) | 16h | |
| | Autenticação CPF + senha + troca obrigatória + reset admin | 24h | |
| | Perfis de acesso (admin/criador/leitura gerencial/colaborador) | 16h | |
| | Integração Senior — leitura do cadastro | 20h | |
| | **Criação automática de usuário + bloqueio no desligamento** ⚠️ | 40h | |
| | **Subtotal Fase 0** | **140h** | **≈ 3,9 semanas** |
| **1 · Pesquisa comum (MVP)** | Construtor de pesquisa (CRUD campanha) | 24h | |
| | Editor de perguntas (7 tipos, obrigatoriedade, ordenação/seções) | 40h | |
| | Segmentação de público (macro + detalhada + cargo) | 32h | |
| | Publicação + cálculo de elegibilidade | 20h | |
| | Home do colaborador (pendentes) | 16h | |
| | Tela de responder pesquisa (render dinâmico, rascunho, envio único, congelamento de contexto) | 40h | |
| | Trilha de auditoria (eventos principais) | 16h | |
| | Testes e ajustes | 24h | |
| | **Subtotal Fase 1** | **212h** | **≈ 5,9 semanas** |
| **2 · Analytics / Dashboard RH** | Dashboard RH (impactados/respondidos/pendentes, taxa de resposta) | 32h | |
| | Tela de resultados (gráficos, filtros regional/loja/cargo) | 32h | |
| | Exportação (Excel/PDF) | 20h | |
| | Anonimização em agregações pequenas | 16h | |
| | Integração com Data Warehouse (fatos/metadados, carga) | 40h | |
| | Testes e ajustes | 16h | |
| | **Subtotal Fase 2** | **156h** | **≈ 4,3 semanas** |
| **3 · Jornada 90 Dias** | Configuração de marcos parametrizáveis | 20h | |
| | Motor de disparo automático por admissão | 24h | |
| | Questionários independentes por etapa (reusa construtor da Fase 1) | 16h | |
| | Elegibilidade dinâmica (ativo/desligado) | 20h | |
| | Tela dedicada + acompanhamento por colaborador | 32h | |
| | Testes e ajustes | 20h | |
| | **Subtotal Fase 3** | **132h** | **≈ 3,7 semanas** |
| | **Total** | **640h** | **≈ 17,8 semanas (≈ 4 a 4,5 meses)** |

## Cronograma semana a semana (1 desenvolvedor, 36h/semana)

| Semana | Entregável |
|---|---|
| 1–4 | Fase 0 — fundação técnica completa (auth, perfis, integração Senior, criação automática de usuário) |
| 5–10 | Fase 1 — pesquisa comum completa e testável ponta a ponta (criar → publicar → responder) |
| 11–14 | Fase 2 — dashboard RH, resultados, exportação, integração DW |
| 15–18 | Fase 3 — Jornada 90 Dias completa |

**Com 2 desenvolvedores a partir da Fase 1** (Fase 0 continua sequencial, pois é a base que tudo depende): Fase 1 cai pra ≈3 semanas, Fase 2 ≈2,2 semanas, Fase 3 ≈1,9 semanas — total ≈ **11 semanas (≈ 2,5 meses)** a partir do fim da Fase 0.

## Maior risco de prazo: a Fase 0 pode estourar

As 40h da "criação automática de usuário" são um **palpite com folga, não uma medição** — a call de 08/09 confirmou que **ninguém sabe como automatizar isso ainda** (nem o Ozéias: "não faço a mínima ideia de como a gente faria isso"). A única pista é a hipótese solta do Filipe (via AD), não validada. Dois cenários:

- **Se a via AD funcionar de forma direta:** as 40h estimadas se sustentam.
- **Se precisar de um conector novo com o Senior ou um processo manual/batch:** essa única linha pode dobrar ou mais, empurrando a Fase 0 inteira e, em cascata, todo o cronograma — sem afetar as fases 1-3 em si, só quando elas começam.

**Recomendação para a reunião de hoje:** tratar isso como o item nº1 a destravar antes de qualquer compromisso de prazo — é a única incógnita capaz de mudar a ordem de grandeza da estimativa, não só o detalhe.

## O que este cronograma não cobre

- Validação de segurança da informação para autenticação por CPF (item 5 das dúvidas técnicas) — pode adicionar retrabalho se exigir mudança de abordagem depois de já codado.
- Confirmação se "Ciacon" é o mesmo projeto — se for, pode haver sobreposição de escopo a reconciliar.
- Capacidade concorrente real de TI/Dados (a própria Especificação Funcional cita isso como restrição, sem resposta ainda).
- Calendário real em datas — aqui está em semanas relativas ao início efetivo do desenvolvimento, que ainda não tem data confirmada.
