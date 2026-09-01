# Log da rotina diária (daily-digest + board-sync)

> Atualizado a cada execução da rotina automática (seg-sex, 8h). Entrada mais nova primeiro. Cada entrada documenta **o que rodou, o que mudou, por quê, e com base em qual fonte** — pra revisão rápida pela manhã sem precisar reconstruir o raciocínio.

---

## Formato de cada entrada (referência — apagar depois da primeira execução real)

```
## AAAA-MM-DD HH:MM (America/Sao_Paulo)

### daily-digest
- Transcrições novas encontradas: N (lista de arquivos)
- Já cobertas / puladas como duplicata: N (qual arquivo, qual digest já existente cobria)
- Digest(s) criado(s): [nome do arquivo](dailies/arquivo.md) — período/tema
- Achados principais, por projeto:
  - **<Projeto>**: <achado> — fonte: <trecho/data da transcrição>
- Arquivos sinalizados como desatualizados (NÃO editados por este agente):
  - `<arquivo>` — <o que especificamente parece defasado e por quê>

### board-sync
- Cards com estado/coluna mudados:
  | ID | De | Para | Motivo (fonte) |
  |---|---|---|---|
  | #NNNNN | Refinement (Quase pronto) | Refinement (Precisa refinar) | Comentário do Danilo em DD/MM: "<citação>" |
- Cards removidos do escopo do board (avançaram além de Ready for Dev):
  | ID | Estado atual | Motivo |
  |---|---|---|
- Cards novos descobertos (não rastreados antes):
  | ID | Score DoR (4 pontos) | Coluna onde entrou |
  |---|---|---|
- Checagem de paridade chip/modal: OK / FALHOU (detalhe se falhou)
- Artifact republicado: <URL> — <sim/não, e por quê se não>

### Pendências que ficaram para o Igor decidir
- <qualquer bloqueio externo real encontrado, não resolvido pelo agente>

### Erros/falhas nesta execução
- <qualquer chamada ADO que falhou, arquivo que não abriu, etc — nunca omitir silenciosamente>
```

---

*(entradas reais começam abaixo, mais recente no topo)*

---

## 2026-09-01 (execução manual, sob pedido do Igor — "atualize nosso board de cards")

### daily-digest
Não rodou nesta execução — o pedido foi só board-sync. Nenhuma transcrição nova foi verificada.

### board-sync
- **Cards com estado/coluna mudados:**
  | ID | De | Para | Motivo (fonte) |
  |---|---|---|---|
  | #11941 | 100% pronto (Ready for Dev) | **Quase pronto** (Ready for Dev) | QA (Danilo, comentário 25/08): Cenário 7 (auditoria) tem redação condicional "(se aplicável)" — precisa virar obrigatório ou ser removido antes de sair de Ready for Dev |
  | #12190 | 100% pronto (Refinement) | 100% pronto (**Ready for Dev**, label atualizado) | Estado ADO avançou de Refinement pra Ready for Dev — sem mudança de conteúdo/DoR |

- **Cards removidos do escopo do board (avançaram além de Ready for Dev):**
  | ID | Estado atual | Motivo |
  |---|---|---|
  | #12179 (T1 Gamificação) | In Test / QA | Avançou além de Ready for Dev |
  | #12181 (T2) | In Test / QA | idem |
  | #12183 (T4) | In Test / QA | idem |
  | #12184 (T5) | In Test / QA | idem |
  | #12185 (T6) | In Test / QA | idem |
  | #12186 (T7) | In Test / QA | idem |
  | #12187 (T8) | In Test / QA | idem |
  | #12189 (T10) | In Test / QA | idem |

  **Achado importante:** #12182 (T3 Gamificação) é a ÚNICA da leva T1-T10 que **não** avançou — segue em Refinement/Quase pronto com o bloqueador de QA de 25/08 (ordem do fluxo campanha/cadastro). Isso contradiz o que estava registrado em `gamificacao/contexto.md` ("todos os T1-T10 avançaram pra In Test/QA") — vale corrigir esse arquivo numa próxima rodada de `portfolio-report`.

- **Cards novos descobertos (via WIQL, não rastreados antes):**
  | ID | Score DoR (4 pontos) | Coluna onde entrou |
  |---|---|---|
  | #12813 (Ciacon — levantamento e documentação, Kovalski) | 0/4 — Description/AC vazios, 0 comentários | Precisa refinar |
  | #12812 (Conciliação F2 — planilha Contábil, Diego Rafael) | 0/4 — vazio + bloqueio externo real (Adriana/layout Oracle) | Precisa refinar |

- **Checagem de paridade chip/modal:** OK (27 chips = 27 modais, antes e depois das edições)
- **Artifact republicado:** https://claude.ai/code/artifact/ced8aba8-8054-44d2-a8f9-a4b410264a96 (a versão live estava desatualizada desde 25/08 — as edições anteriores desta sessão nunca tinham sido efetivamente publicadas nela)

### Pendências que ficaram para o Igor decidir
- #12812: bloqueio externo real (Adriana/layout Oracle) — não resolvido, só sinalizado.
- Corrigir `gamificacao/contexto.md`: a afirmação "todos T1-T10 avançaram" está incorreta (T3 não avançou).

### Achado de qualidade de dado
Quase todos os 33 cards consultados via `get_batch` compartilhavam o mesmíssimo `System.ChangedDate` (2026-08-31T13:17:42.557Z) — indício de uma atualização em lote no Azure (provavelmente campo administrativo), não de mudanças reais individuais naquele instante. O diff foi feito comparando `State`/`BoardColumn` atual contra o que o board mostrava, não usando `ChangedDate` como sinal de "mudou recentemente".

### Erros/falhas nesta execução
Nenhuma chamada ADO falhou. A primeira tentativa de publicar o Artifact foi recusada (exigia reconfirmar leitura da versão live antes de publicar) — resolvido reconfirmando a leitura e republicando.
