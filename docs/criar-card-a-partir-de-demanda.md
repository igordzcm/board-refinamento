# Criar um card a partir de uma demanda

Você passa a demanda em texto livre para o Claude Code, e o agente `refinement-gate` devolve o card criado no Azure DevOps, já no padrão da casa: história, cenários com rótulo, estimativa, épico e links.

## O que vai neste pacote

| Arquivo | Para que serve |
| --- | --- |
| `.claude/agents/refinement-gate.md` | O agente que entende a demanda, escreve e cria o card. Também refina cards que já existem |
| `.claude/skills/refinement-checklist/` | O padrão de card da casa: modelo da história, cenários Dado/Quando/Então, rótulos, Definition of Ready e os cuidados com a API do ADO. O agente segue esta skill à risca |
| `.claude/skills/agile-product-owner/` | Usada pela skill para estimar e quebrar histórias grandes |
| `.claude/skills/senior-architect/` | Usada quando o card pede um fluxograma técnico |
| `.claude/skills/process-mapper/` | Usada quando o card pede um fluxograma de processo de negócio |
| `docs/processo-de-refinamento.md` | A versão longa do padrão, com exemplos, para leitura humana |
| `docs/criar-card-a-partir-de-demanda.md` | Este guia |

## Preparação (uma vez)

1. Copie as pastas `.claude/` e `docs/` para a raiz da pasta onde você usa o Claude Code. Se você já usa o repositório board-refinamento, elas já estão lá e não precisa copiar nada.
2. Instale o Node.js e o Azure CLI e conecte o Claude ao Azure DevOps rodando no terminal:

   ```
   claude mcp add ado -- npx -y @azure-devops/mcp@latest GrupoAvenida --authentication azcli
   ```

3. Rode `az login` e faça o MFA. A sessão expira pela política da empresa: quando o Claude disser que não consegue ler o ADO, faça o login de novo.
4. Opcional, para a Nota técnica: clone os repositórios `ConciliaçãoCaixaAPI` e `ConciliaçãoCaixaFront` (projeto "Projeto - Conciliação de Caixa" no ADO) na pasta **ao lado** da pasta de trabalho. Sem eles o card sai sem Nota técnica, o que é aceitável.
5. Teste pedindo: "leia o card #13423". Se ele trouxer o card, está tudo ligado.

## Como pedir

Escreva a demanda do jeito que ela chegou e diga, se souber, o projeto:

> Crie um card a partir desta demanda: o Arthur pediu que a campanha do Motor de Descontos possa ter um item só, hoje o mínimo é dois.

> Transforma isso num card do projeto Conciliação Fase 2: "o job da noite não processa a última loja", relatado pelo Danilo na daily de hoje.

Quanto mais contexto (quem pediu, em que reunião, qual tela, qual regra), melhor o card. Pode colar o trecho da transcrição ou da mensagem inteiro.

## O que o agente faz

1. Lê a demanda e o `contexto.md` do projeto (e o TAP, se houver).
2. **Se a necessidade não estiver clara, não cria nada** e devolve as perguntas que você precisa responder antes.
3. Procura no ADO se já existe card para isso. Se existir, avisa em vez de duplicar.
4. Acha o épico do projeto.
5. Escreve o card no padrão da casa:
   - título com a necessidade, não com a solução;
   - história "Eu, enquanto … poderia/gostaria/devo … para/tal que/por que …";
   - cenários Dado/Quando/Então, cada um com o rótulo de como será testado;
   - Nota técnica só se houver algo verificado no código.
6. Cria como Product Backlog Item (ou Bug, se for bug) em **Refinement**, sem sprint e sem responsável.
7. Liga o card ao épico e aos cards relacionados.
8. Propõe uma estimativa em Fibonacci, comentada como proposta do PO a confirmar com o time.
9. Registra em comentário de onde veio a demanda (reunião, data, quem pediu). Isso nunca vai na descrição.
10. Diz se o card precisa de fluxograma ou mock. Mock só é feito depois que você confirmar.
11. Devolve o link do card e a coluna recomendada no board (Precisa refinar, Quase pronto ou 100% pronto).

## Depois que o card é criado

- **Leia o card no ADO antes de qualquer coisa.** A IA escreve, mas quem responde pelo card é o PO.
- Se estiver certo e passar na Definition of Ready, mova para **Ready for Dev** pela interface.
- Se precisar ajustar, peça em linguagem natural ("no card #13500, troque o cenário 2 por…") ou edite direto no ADO.
- Para conferir o card de novo depois de mexer: "refine o card #13500".

## Regras que o agente já segue

- História com a **necessidade**, nunca a solução de tela ("gostaria de pagar minha equipe", não "gostaria de um modal de pagamento").
- O verbo muda conforme o caso: poderia (capacidade), gostaria (desejo), devo (obrigação).
- Descrição e cenários sem detalhe técnico; tabela, arquivo e SQL só na Nota técnica.
- Sem data nem "quem pediu" na descrição.
- Quando o time diz "task", é PBI.
- Comentários no ADO em Markdown.
- A API do ADO não volta card de Verified ou Dev Review para trás: isso se faz pela interface.
