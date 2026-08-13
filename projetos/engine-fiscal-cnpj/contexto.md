# Engine Fiscal — CNPJ Alfanumérico — contexto geral

> Arquivo de contexto do projeto. **Este é um documento de ARQUIVO/REFERÊNCIA, não um projeto ativo — não agendar reunião de status para isto.** Mantido porque o padrão técnico (função canônica de formatação de CNPJ, checklist de auditoria DDL, dependência do fornecedor InvoiCy) é reutilizável caso surja uma iniciativa fiscal semelhante no futuro.

## O que era

Suporte a CNPJ alfanumérico (novo padrão RFB) nos dois serviços fiscais — **Engine Fiscal** (NestJS, branch `release/3.2.3`) e **EngineWebhookAPI** (NestJS, branch `develop`). Trocava a sanitização destrutiva (`replace(/\D/g, '')`, que descartava letras) por uma função canônica de normalização (`formatCnpj` / `normalizeCnpj`) aplicada em todos os pontos de emissão, persistência, contingência/reemissão e logs (com mascaramento LGPD).

## Status — SHIPPED

Confirmado como **entregue** via `DONE/done-var30-16-23-jun-2026.md` (período 16–23/06/2026): bloco "CNPJ Alfanumérico" lista 13 PBIs concluídos em 23/06/2026, cobrindo Flutter (`CpfCnpjUtil`), os 3 backends Java (`CpfCnpjUtils`), refatoração de DTOs/validações em VendaMercantil, AvenueCustomerCard e VarService, migração de entidades JPA `Long→String`, substituição de `replaceAll` destrutivos, ajuste de teclado/formatter/máscara nos apps, ajuste do `CnpjaService` (validação de contratos CNPJa + SEFAZ) e suíte de regressão E2E nos 5 projetos com massa numérica + alfanumérica.

## O que ficou documentado como reutilizável

- **Função canônica de formatação/normalização de CNPJ** — regex final `/^[A-Z0-9]{14}$/`, normalização de minúsculas para maiúsculas, `padStart` só para numérico puro (nunca para alfanumérico curto), classe de erro `InvalidCnpjError`. Especificada em duas variantes (`formatCnpj` no Engine Fiscal, `normalizeCnpj` no EngineWebhookAPI) — mesmo contrato, nomes diferentes por serviço.
- **Checklist de auditoria DDL Oracle** — padrão para confirmar que colunas que guardam CNPJ (`VARCHAR2(14 CHAR)` ou superior, charset compatível com A-Z, sem `CHECK`/índice funcional/trigger que assuma numérico) estão prontas para alfanumérico. Lista de colunas auditadas em ambos os serviços (`W03EST.W03ETBCGC`, `DOC001.DOCCNPJ`, `DOC001.DOCDANFE`, `DOC007.DO7CNPJ`, `SAT.SATCNPJSH`, `GAV_NF_INUTILIZ.CNPJ`, entre outras).
- **Padrão de dependência do fornecedor InvoiCy** — três frentes formais de confirmação com o fornecedor (`libInvoiCyFramework`): aceitação de alfanumérico nos parâmetros da lib C, cálculo correto do dígito verificador módulo-11 ASCII-48 da chave de acesso de 44 dígitos com CNPJ alfa embutido (posições 7–20), e confirmação de versão da API REST. Modelo replicável para qualquer mudança de layout fiscal que dependa de vendor externo.
- **Padrão de mascaramento de log (LGPD)** — helper `maskCnpj`/similar preservando 4 primeiros + 4 últimos caracteres, com override total em `LOG_LEVEL=debug`.

## US relacionada, status desconhecido

`user_story_orquestrador_descarte_nfce.md` — **Orquestrador Inteligente de Descarte de NFCe**: substitui o evento único de descarte (`DescartarDocumento` do InvoiCy) por um orquestrador que lê DOC001 + DOC007 para decidir entre Cancelamento (`EveTp=110111`, nota autorizada com protocolo), Inutilização (sem protocolo, status não terminal) ou no-op (nota já em estado terminal sem protocolo — `DO7SITCOD` ∈ [108, 109, 111]). Mantém compatibilidade do endpoint (`isCancelNfce: true`), retornando um novo campo `action`. É um **escopo distinto** dentro da mesma pasta `PROJETOS/ENGINE`, sem evidência de conclusão encontrada nas fontes revisadas — não foi localizado no bloco "Done" de 16–23/06. Se este item for retomado, tratar como projeto próprio, não como parte do CNPJ Alfanumérico.

## Reuniões

Nenhuma reunião registrada ainda — e não deveria ser agendada uma só para revisar este arquivo de referência.

## Próxima atualização

Não aplicável como sustentação ativa. Atualizar apenas se: (a) surgir uma nova mudança regulatória fiscal semelhante que possa reaproveitar este padrão, ou (b) alguém confirmar o status real do orquestrador de descarte de NFCe (US relacionada, ainda sem confirmação de entrega).
