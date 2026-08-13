# Roadmap de Testes — Portal Retaguarda

## Objetivo

Implementar cobertura de testes completa no Portal Retaguarda cobrindo **3 camadas**:

1. **Unit Tests (Jest)** — Testa services isolados com mocks. Valida logica de negocio, validacoes, calculos e fluxos internos sem dependencia de banco ou servicos externos.

2. **E2E Backend (Jest + Supertest)** — Testa endpoints da API com NestJS TestingModule. Valida rotas, guards, DTOs, status codes e integracao entre controller/service/repository usando banco real (Postgres) e mocks para Oracle/S3/email.

3. **E2E Automatizado (Playwright)** — Testa fluxos completos no browser. Valida navegacao, formularios, permissoes, filtros e interacoes de usuario de ponta a ponta com API e Front rodando.

## Arquitetura de Testes

```
Concilia%C3%A7%C3%A3oCaixaAPI/
├── test/                              # E2E Backend
│   ├── test-modules.config.ts         # Ativa/desativa modulos para teste
│   ├── helpers/
│   │   └── test-app.module.ts         # NestJS module minimo para E2E
│   ├── fixtures/
│   │   └── auth.fixture.ts            # Seed users, JWT helpers
│   └── term.e2e-spec.ts              # Spec E2E do termo
├── test/unit/                         # Unit Tests
│   └── person/
│       └── person.service.spec.ts     # 161 testes do person service
├── jest.config.ts                     # Config unit (le test-modules.config)
├── jest.e2e.config.ts                 # Config E2E (le test-modules.config)
└── src/modules/<modulo>/__tests__/    # Unit tests colocados por modulo

Concilia%C3%A7%C3%A3oCaixaFront/
├── e2e/
│   ├── fixtures/
│   │   ├── index.ts                   # mergeTests entry point
│   │   └── auth.fixture.ts            # authedPage + restrictedPage
│   ├── support/
│   │   ├── env.ts                     # URLs por ambiente
│   │   ├── helpers/api.ts             # programmaticLogin
│   │   └── factories/user.factory.ts  # Usuarios de teste
│   └── tests/
│       ├── auth/                      # Login smoke
│       └── terms/                     # Fluxo completo do termo
└── playwright.config.ts
```

## Como ativar um modulo para testes

```ts
// test/test-modules.config.ts
export const TEST_MODULES = {
  auth: false,    // mude para true
  term: true,     // ja ativo
  store: false,   // mude para true
  // ...
};
```

Isso controla automaticamente:
- `npm run test` — roda unit tests dos modulos ativos
- `npm run test:e2e` — roda E2E backend dos modulos ativos
- `npm run test:cov` — roda com coverage

## Comandos

| Comando | O que faz |
|---------|-----------|
| `npm run test` | Unit tests dos modulos ativos |
| `npm run test:cov` | Unit tests com coverage (threshold 80%) |
| `npm run test:e2e` | E2E backend (Jest + Supertest) |
| `make test-all` | Sobe Docker + roda tudo (unit + E2E + Playwright) |
| `make test-cov` | Unit com coverage |
| `make seed-test-oracle` | Popula Oracle local com dados de teste |

## Status Atual

| Tipo | Cobertura | Modulos | Observacao |
|------|-----------|---------|------------|
| Unit Tests | **98%** person.service | term | 161 testes passando, threshold 80% |
| E2E Backend | **14 testes** | term | Endpoints de termo validados |
| Automatizado | **26 testes** | auth + term | Login, sidebar, fluxo do termo |

## Pipeline CI/CD

```
PR aberta → pr-validation.yml
  ├── PR - Validacao do Titulo
  ├── QualityGate - Unit (coverage + resultados)
  ├── QualityGate - E2E Backend
  └── QualityGate - Automatizado (Playwright)

Merge → main.yml
  ├── Deploy (Hotfix/Develop/Production)
  └── Testes Manuais (clique para rodar)
```

---

## Cards por Prioridade

---

### FASE 1 — Auth + Term (CRITICA) :white_check_mark: PARCIALMENTE CONCLUIDA

#### Card 1.1 — Unit Tests: Auth Guards
**Tipo:** Unit Test
**Modulo:** `src/auth/guards/`
**Arquivo:** `src/auth/guards/tests/*.spec.ts`
**O que fazer:**
- Corrigir specs existentes (`RoleEnum.ADMIN` → `RoleEnum.ADMINISTRADOR`)
- AtGuard: token valido, expirado, invalido, ausente
- AssignmentsGuard: usuario com/sem permissao, permissao parcial
- RolesGuard: ADMINISTRADOR, ANALISTA, USER
- GroupGuard: usuario com/sem grupo
- KeycloakGuard: token Keycloak valido/invalido

**Ativar:** `auth: true` em `test-modules.config.ts`
**Estimativa:** 3-5h

---

#### Card 1.2 — E2E Backend: Auth Controller
**Tipo:** E2E Backend
**Modulo:** `src/auth/auth.controller.ts`
**Arquivo:** `test/auth.e2e-spec.ts`
**O que fazer:**
- `POST /auth/login` — admin, dev seed user, senha errada, user inexistente
- `GET /auth/me` — com token, sem token, token expirado
- `GET /auth/refresh` — refresh valido, invalido
- `GET /auth/dev-users` — lista em dev, 404 em prod
- `POST /auth/login/keycloak` — fluxo Keycloak
- Todos os endpoints devem validar 401 sem token

**Estimativa:** 3-5h

---

#### Card 1.3 — Unit Tests: Person Service :white_check_mark: CONCLUIDO
**Status:** 161 testes, 98% coverage
**Metodos cobertos:** validateUser, validateUserPosition, validateTermDocument, calculateRemainingTime, getTemplateName, findTermById, updateTermStatus, findTermHistory, findTermRequests, findAllTermRequests, persistTermDocument, rollbackTermCreation, handlePdfGenerationError, createNewTermHistory, migrateSlaForExistingTerms, getTermDocuments, uploadSignedTerm, generatePdfWithLogixDataAsync, generatePdfFromExistingData, buildTermOwnershipFilter, resolveAuthorType, formatCompanyAddress, getRegionalManagerName, formatStockData, calculateStockTotals, createTermRequest, mapTermTransitionToEmail, differenceInHours, differenceInMinutes

---

#### Card 1.4 — Automatizado: Fluxo Completo do Termo
**Tipo:** Playwright (Frontend E2E)
**Modulo:** `e2e/tests/terms/`
**O que fazer:**
- Criar termo completo via sidebar navigation (CPF 10021030456)
- Preencher todos os campos (CPF, loja, motivo, data, saldo, PDF, divergencia)
- Submeter e verificar sucesso (toast + redirect)
- Aprovar termo (PENDING → TERM_PENDING_SIGNATURE) no financeiro
- Upload de documento assinado
- Aprovacao final (TERM_SIGNED → APPROVED)
- Rejeitar termo (comentario obrigatorio)
- Cancelar termo (modal + confirmacao)
- Filtros da listagem (status, loja, CPF, data, SLA)
- Permissoes (restricted user nao ve financeiro)

**Estimativa:** 8-12h

---

### FASE 2 — Modulos Financeiros

#### Card 2.1 — Cash Movement (Unit + E2E Backend + Automatizado)
**Modulo:** `src/modules/cash-movement/`

**Unit Tests:**
- CashMovementService: logica de export, formatacao, mapeamento
- CashMovementStoreAccessService: permissao por loja
- ClosedDayValidator: validacao de dia fechado
- ExcelExportService: geracao de Excel
- CashMovementMapper: mapeamento de dados

**E2E Backend:**
- `GET /cash-movement/allowed-stores` — permissao FINANCEIRO + ANALISTA
- `GET /cash-movement/export` — export Excel (storeCode, date, operatorCode)
- `GET /cash-movement/export.pdf` — export PDF
- 401 sem token em todos os endpoints
- 403 sem permissao FINANCEIRO

**Automatizado (Playwright):**
- Navegar via sidebar: Financeiro → Estorno → Movimentacao
- Selecionar loja e data
- Gerar relatorio
- Exportar Excel/PDF
- Verificar que restricted user nao acessa

**Ativar:** `cashMovement: true`
**Estimativa:** 8-12h

---

#### Card 2.2 — Cash Balance (Unit + E2E Backend + Automatizado)
**Modulo:** `src/modules/cash-balance/`

**Unit Tests:**
- CashBalanceService: geracao de relatorio, agregacao
- Repository: queries de saldo

**E2E Backend:**
- `GET /cash-balance/report` — relatorio de saldo
- `GET /cash-balance/records` — registros
- `GET /cash-balance/regionals` — dados regionais
- `GET /cash-balance/last-cash-balance/` — ultimo saldo
- Filtros por loja, data, regional

**Automatizado (Playwright):**
- Navegar: Retaguarda de Loja → Saldo
- Consultar saldo de loja
- Verificar dados na tela

**Ativar:** `cashBalance: true`
**Estimativa:** 5-8h

---

#### Card 2.3 — Transaction Reversal (Unit + E2E Backend)
**Modulo:** `src/modules/transaction-reversal/`

**Unit Tests:**
- Service: logica de estorno
- Repository: queries

**E2E Backend:**
- Listagem de estornos
- Criacao de estorno
- Validacao de permissao

**Estimativa:** 3-5h

---

### FASE 3 — Conciliacao

#### Card 3.1 — Divergence (Unit + E2E Backend + Automatizado)
**Modulo:** `src/modules/divergence/`

**Unit Tests:**
- DivergenceService: CRUD, conciliacao, batch
- Repository: queries complexas

**E2E Backend:**
- `GET /divergence` — listar divergencias
- `POST /divergence` — criar divergencia
- `PUT /divergence/:id` — atualizar
- `DELETE /divergence/:id` — deletar
- `POST /divergence/conciliation` — conciliacao
- `PUT /divergence/` — batch update
- `PATCH /divergence/:id/store-justification` — justificativa
- `PUT /divergence/payroll-discount/status` — desconto em folha
- `PUT /divergence/payroll-discount/status/batch` — batch payroll
- `GET /divergence/reports/deduction/:id/:date` — relatorio
- `GET /divergence/conciliation/history/:id` — historico

**Automatizado (Playwright):**
- Navegar: Conciliacao → Lista de Lojas
- Listar divergencias com filtros
- Criar divergencia
- Conciliar
- Justificar
- Deletar

**Ativar:** `divergence: true`
**Estimativa:** 12-16h

---

#### Card 3.2 — Justification (Unit + E2E Backend)
**Modulo:** `src/modules/justification/`

**Unit Tests:**
- JustificationService: CRUD, filtros ativo/inativo

**E2E Backend:**
- CRUD completo (GET, POST, PUT, DELETE)
- Filtro ativo/inativo
- Vinculo com NSU e divergencia
- Justificativa de conta contabil

**Ativar:** `justification: true`
**Estimativa:** 3-5h

---

#### Card 3.3 — Store Conciliation (Unit + E2E Backend)
**Modulo:** `src/modules/store-conciliation/`

**Unit Tests:**
- Service: logica de conciliacao por loja

**E2E Backend:**
- Fluxo de conciliacao
- NSU matching
- Pendencias

**Ativar:** `conciliation: true`
**Estimativa:** 5-8h

---

#### Card 3.4 — Deposit Reconciliation (E2E Backend)
**Modulo:** `src/modules/deposit-reconciliation/`

**Unit Tests:** 40+ specs ja existem (services e repositories)

**E2E Backend (faltante):**
- Importacao de arquivo CNAB
- Reconciliacao de depositos
- Batch operations
- Undo reconciliation

**Ativar:** `depositReconciliation: true`
**Estimativa:** 5-8h

---

### FASE 4 — Loja e Usuarios

#### Card 4.1 — Store Module (Unit + E2E Backend + Automatizado)
**Modulo:** `src/modules/store/`

**Unit Tests:**
- StoreService: job lifecycle, transacoes
- Repository: queries Oracle
- DCX103 recomposition

**E2E Backend:**
- `POST /store/run-job` — trigger job
- `GET /store/progress` — progresso
- `DELETE /store/progress/reset` — reset
- `POST /store/job/one-store` — single store
- `POST /store/recompose-cash-register` — recomposicao
- `GET /store/get-transactions-by-date` — transacoes
- Export Excel

**Automatizado (Playwright):**
- Navegar: Conciliacao → Lista de Lojas
- Selecionar loja
- Ver transacoes
- Exportar Excel

**Ativar:** `store: true`
**Estimativa:** 8-12h

---

#### Card 4.2 — User Module (Unit + E2E Backend + Automatizado)
**Modulo:** `src/modules/user/`

**Unit Tests:**
- UserService: CRUD, grupo, batch

**E2E Backend:**
- `GET /user` — listar usuarios
- `GET /user/:id` — detalhe
- `PUT /user/:id` — atualizar
- `PUT /user/:user_id/group/:group_id` — adicionar grupo
- `PUT /user/:user_id/batch/` — batch update
- Search por assignment, grupo, role

**Automatizado (Playwright):**
- Navegar: Configuracoes → Usuarios
- Listar usuarios
- Editar usuario
- Alterar permissoes

**Ativar:** `user: true`
**Estimativa:** 5-8h

---

#### Card 4.3 — Access Automation (Unit + E2E Backend)
**Modulo:** `src/modules/access-automation/`

**Unit Tests:** 5 specs ja existem

**E2E Backend (faltante):**
- `GET /access-automation/store/:storeCode/users` — listar
- `POST /access-automation/store/:storeCode/access` — conceder
- `PATCH /access-automation/operator/block` — bloquear
- `PATCH /access-automation/operator/reset-password` — reset
- `GET /access-automation/audit-history` — auditoria
- `POST /access-automation/store/:storeCode/export` — exportar

**Estimativa:** 5-8h

---

#### Card 4.4 — Access Request (Unit + E2E Backend)
**Modulo:** `src/modules/access-request/`

**Unit Tests:**
- Service: CRUD, workflow

**E2E Backend:**
- CRUD completo
- Workflow: criar → historico → finalizar
- Transicoes de status

**Ativar:** `accessRequest: true`
**Estimativa:** 5-8h

---

### FASE 5 — Fiscal

#### Card 5.1 — Engine Fiscal (Unit + E2E Backend)
**Modulo:** `src/modules/engine-fiscal/`

**Unit Tests:** 4 specs ja existem

**E2E Backend:**
- Regras fiscais CRUD
- Excecoes fiscais
- Historico
- Dashboard

**Ativar:** `fiscal: true`
**Estimativa:** 5-8h

---

#### Card 5.2 — SPED (Unit + E2E Backend)
**Modulo:** `src/modules/sped/`

**Unit Tests:**
- Geracao de arquivo SPED
- Devolucao

**E2E Backend:**
- Endpoints de SPED
- Validacao fiscal

**Ativar:** `sped: true`
**Estimativa:** 5-8h

---

#### Card 5.3 — GNRE (Unit + E2E Backend)
**Modulo:** `src/modules/gnre/`

**Unit Tests:**
- Provider: envio e consulta

**E2E Backend:**
- Envio GNRE
- Consulta GNRE
- Fila de processamento

**Ativar:** `gnre: true`
**Estimativa:** 5-8h

---

#### Card 5.4 — Tax Closing (E2E Backend)
**Modulo:** `src/modules/tax-closing/`

**Unit Tests:** 80+ specs ja existem

**E2E Backend (faltante):**
- Download de Excel (streaming)
- Status do job
- Filtros

**Estimativa:** 3-5h

---

### FASE 6 — Campanhas e CRM

#### Card 6.1 — Campaign (Unit + E2E Backend + Automatizado)
**Modulo:** `src/modules/campaign/`

**Unit Tests:** 18+ specs ja existem

**E2E Backend:**
- CRUD de campanhas
- Propagacao para lojas
- Comparacao
- Edicao em massa

**Automatizado (Playwright):**
- Navegar: Planejamento Comercial → Campanhas
- Listar, criar, editar, propagar

**Ativar:** `campaign: true`
**Estimativa:** 8-12h

---

#### Card 6.2 — Campaign Roulette (Unit + E2E Backend)
**Modulo:** `src/modules/campaign-roulette/`

**E2E Backend:**
- Roleta de campanhas
- Fila de processamento

**Estimativa:** 5-8h

---

### FASE 7 — Suporte e Infraestrutura

#### Card 7.1 — Notification (Unit)
**Modulo:** `src/modules/notification/`

**Unit Tests:**
- Listar notificacoes
- Contagem de nao lidas
- Marcar como lida (individual e batch)

**Ativar:** `notification: true`
**Estimativa:** 3-5h

---

#### Card 7.2 — Supplier (Unit + E2E Backend)
**Modulo:** `src/modules/supplier/`

**Unit + E2E:**
- CRUD de fornecedores
- Toggle ativo/inativo

**Estimativa:** 3-5h

---

#### Card 7.3 — Regional + Treasury (Unit)
**Modulos:** `src/modules/regional/` + `src/modules/treasury/`

**Unit Tests:**
- CRUD de regionais
- Gestao de tesouraria

**Ativar:** `regional: true`, `treasury: true`
**Estimativa:** 3-5h

---

#### Card 7.4 — Store Bank Account (Unit)
**Modulo:** `src/modules/store-bank-account/`

**Unit Tests:** 6 specs ja existem
**Estimativa:** 3-5h

---

### FASE 8 — Automatizado Frontend (Playwright)

#### Card 8.1 — Login e Permissoes
**Fluxos:**
- Login via UI (email + senha)
- Login via dev quick select
- Login failure (senha errada, user inexistente)
- Logout
- Sidebar por perfil (admin ve tudo, analista so Conciliacao)
- Redirect ao acessar rota sem permissao

**Estimativa:** 5-8h

---

#### Card 8.2 — Conciliacao de Lojas
**Fluxos:**
- Navegacao sidebar → Conciliacao → Lista de Lojas
- Listagem com filtros
- Detalhe de loja
- Conciliacao de depositos

**Estimativa:** 8-12h

---

#### Card 8.3 — Divergencias
**Fluxos:**
- Listagem com filtros
- Criar, editar, conciliar, justificar, deletar divergencia

**Estimativa:** 8-12h

---

#### Card 8.4 — Financeiro
**Fluxos:**
- Estorno de movimentacao
- Validacao de termos
- Consulta de acessos
- Relatorio de saldo

**Estimativa:** 8-12h

---

#### Card 8.5 — Fiscal
**Fluxos:**
- SPED, GNRE, NFF
- Motor fiscal
- Tax closing download

**Estimativa:** 8-12h

---

#### Card 8.6 — Campanhas
**Fluxos:**
- Listar, criar, editar, comparar, propagar campanhas

**Estimativa:** 8-12h

---

#### Card 8.7 — Configuracoes
**Fluxos:**
- Grupos e rotas (CRUD)
- Usuarios (listar, editar, permissoes)

**Estimativa:** 5-8h

---

## Resumo de Estimativas

| Fase | Cards | Unit | E2E Backend | Automatizado | Total |
|------|-------|------|-------------|--------------|-------|
| 1 — Auth + Term | 4 | 3-5h | 3-5h | 8-12h | 14-22h |
| 2 — Financeiros | 3 | 5-8h | 5-8h | 5-8h | 15-24h |
| 3 — Conciliacao | 4 | 8-12h | 8-12h | 8-12h | 24-36h |
| 4 — Loja/Usuarios | 4 | 5-8h | 10-16h | 5-8h | 20-32h |
| 5 — Fiscal | 4 | 5-8h | 8-12h | — | 13-20h |
| 6 — Campanhas | 2 | 3-5h | 5-8h | 8-12h | 16-25h |
| 7 — Suporte | 4 | 6-10h | 3-5h | — | 9-15h |
| 8 — Playwright | 7 | — | — | 50-76h | 50-76h |
| **TOTAL** | **32** | **35-56h** | **42-66h** | **84-128h** | **161-250h** |

---

## Checklist por Modulo

Para cada modulo, o dev deve:

### Unit Tests
- [ ] Criar `test/unit/<modulo>/<modulo>.service.spec.ts`
- [ ] Mockar dependencias (repository, prisma, S3, Logix, email)
- [ ] Testar todos os metodos publicos do service
- [ ] Testar caminhos de erro (catch, validacao, not found)
- [ ] Testar edge cases (dados nulos, arrays vazios, tipos invalidos)
- [ ] Coverage minimo: 80% em statements, branches, functions, lines
- [ ] Adicionar reporter JUnit para publicacao no Azure

### E2E Backend
- [ ] Criar `test/<modulo>.e2e-spec.ts`
- [ ] Usar `TestAppModule` com overrideProvider para mocks
- [ ] Testar cada endpoint: status 200, 400, 401, 403, 404, 500
- [ ] Testar com token admin e sem token
- [ ] Testar com usuario restrito (se aplicavel)
- [ ] Validar DTOs (campos obrigatorios, tipos, enums)

### Automatizado (Playwright)
- [ ] Criar `e2e/tests/<modulo>/<modulo>.spec.ts`
- [ ] Usar fixtures: `authedPage` e `restrictedPage`
- [ ] Testar navegacao via sidebar (nao URL direta)
- [ ] Testar todos os campos de formulario
- [ ] Testar validacoes visuais (mensagens de erro)
- [ ] Testar filtros e listagem
- [ ] Testar permissoes (restricted user nao ve)
- [ ] Usar `dispatchEvent('click')` para sidebar accordion
- [ ] Usar `test.describe.configure({ mode: 'serial' })` para fluxos sequenciais

---

## Regras de Teste

1. **Importar de fixtures**: `import { test, expect } from '../../fixtures'` — nunca de `@playwright/test`
2. **Selectors**: preferir `data-testid`, depois `getByRole` / `getByText`
3. **Sem `any`**: tipar mocks e retornos
4. **AAA**: Arrange, Act, Assert nessa ordem
5. **Nome descritivo**: `"retorna 401 sem token"`, nao `"test 1"`
6. **Coverage 80%**: threshold global para statements, branches, functions, lines
7. **Idempotente**: testes nao dependem de ordem nem de dados de outros testes
8. **Cleanup**: fechar conexoes em `afterAll()`
9. **Sem `console.log`**: usar logger do Nest
10. **Sem hardcode de dados**: usar factories e constantes