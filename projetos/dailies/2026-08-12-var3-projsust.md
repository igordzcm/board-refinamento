# Daily VAR 3.0 — Proj/Sust — 12/08/2026

> Resumo (não transcrição literal), convertido de `VAR 3.0 - Daily Proj_Sust (1).docx` (raiz do workspace, movido pra cá). 9m0s.

**Participantes:** Gustavo (lead), Franklin, Kevin, Nicolas, Guilherme Oliveira, Wanderleia, Moises, Kovalski, Matheus Donato, Guilherme Caixeta, Felipe Pinheiro.

## Por pessoa

- **Guilherme Oliveira** — Continua na unificação 4G + Tap on Phone com o Walter; queda de energia/internet no dia, seguiu de 4G no celular. Overlimit segue sem resposta da Rigolon.
- **Wanderleia** — Replicando o código da correção de CNPJ numa branch nova (a partir da 65, pra evitar os erros de compilação da anterior); a branch antiga será descartada depois.
- **Moises** — Card "12237" enviado, aguardando revisão do Felipe. Segue sem task nova.
- **Kovalski** — Seguindo SSO; entrando na integração do Siga — projeto complexo de rodar localmente (notebook limitado). Estimativa de terminar o desenho até sexta (14/08). Depois volta pra Automação Fiscal (Indy/VAR), só se não houver imprevisto.
- **Matheus Donato** — Segue só no projeto de etiqueta remarcada — nada do VAR/Engine.
- **Guilherme Caixeta** — Testes de integração da **rotina de desconto** (Motor de Descontos): cenários de caminho feliz passando, alguns com problema, corrigindo. Muita combinação de desconto a testar, "primeira compra" é o cenário mais complicado. **Sem gap identificado na história até agora** — confirmado ao Gustavo que vai revalidar tudo antes de fechar.
- **Nicolas / Felipe Pinheiro** — 4G: testado, falta testar localmente; correção da Danf a decidir se sobe nessa release. Dev box do Moises pronto, aguardando decisão se entra nessa sprint ou na próxima.
- **Kevin** — Ponto levado offline com o Gustavo, sem detalhe na daily.

## Pontos de atenção

- Motor de Descontos sendo validado pelo lado loja/PDV (Guilherme Caixeta) na mesma janela em que o Leonardo (Retaguarda) começa a desenhar a arquitetura de sincronização nas lojas — ver [motor-descontos/contexto.md](../motor-descontos/contexto.md). Nenhum gap de cenário reportado até 12/08.
