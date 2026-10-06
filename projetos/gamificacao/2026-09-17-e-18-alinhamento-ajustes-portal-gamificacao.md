# Gamificação — alinhamentos de ajustes do portal (17 e 18/09/2026)

> Duas sessões internas conduzidas por Ozéias (dono de negócio) com Kauã (dev), Danilo (QA, anotando) e Igor (ouvinte). Fontes: `GAMEFICAÇÃO 1.docx` (17/09, 13m14s) e `GAMEFICAÇÃO 2.docx` (18/09, 27m50s), datas confirmadas pelo cabeçalho. **São reuniões distintas** do resumo `2026-10-02-resumo-apresentacao-portal-gamificacao.md` (apresentação/UX, data não informada) e da demo de 02/09 ([`2026-09-02-demo-crm-ana-marcos.md`](2026-09-02-demo-crm-ana-marcos.md)): aqui é a lista de ajustes de regra e de tela decididos antes dessas apresentações. A transcrição é bastante ruidosa e Ozéias estava relendo anotações de reunião anterior; onde ele não lembrava o item, está dito.

## Sessão 1 — 17/09 (revisão de pontos mapeados na reunião anterior)

- **Prioridade entre campanhas:** só define a **ordem de apresentação** quando várias campanhas rodam ao mesmo tempo (a de prioridade 1 aparece primeiro). Sem mudança de regra.
- **Validade do voucher:** manter "dias após emissão" e "fim do mês seguinte" e **criar "até o fim da campanha"** (data fixa: vale até o dia que a campanha termina, independentemente de quando foi gerado).
- **Compra mínima:** fica **hard-coded**.
- **"Não ter bloqueio de campanha por quantidade":** ninguém lembrava o que era; sem decisão.
- **Lembrete em calendário:** ao gerar o cupom, gerar um **arquivo .ics** para colocar na agenda, para incentivar a ida à loja.
- **Compartilhar:** botão "convide seus amigos para jogar" abrindo WhatsApp (ideia, sem decisão fechada).
- **FAQ:** mantida **só a FAQ geral** do lado de fora (sem abas por tipo de jogo), e **FAQ própria dentro de cada campanha** (podem existir duas campanhas de roleta com FAQs diferentes).
- **Novos campos:** "nome da campanha para o cliente" (o nome atual passa a ser interno/para o VAR); manter nome e data final; **novo upload de imagem de capa da campanha** na home.
- **Cadastro:** não permitir CPF, e-mail ou celular duplicado. Hoje CPF é único; telefone não dá para verificar sem disparo de SMS; Ozéias: "quem disse primeiro que o número é dele, é dele".
- Próxima reunião ficaria para revisar textos.

## Sessão 2 — 18/09 (varredura das telas, Danilo anotando para virar card do Kauã)

- **Lista de campanhas:** manter total de giros; **repaginar a tela de histórico** (em português), colocá-la em primeiro.
- **Rascunho salvo no navegador:** funcionalidade nova para Ozéias; ajustar botão "descartar" (cor) e **pedir confirmação ao descartar**.
- **Criação de campanha:** campo de nome já limitado em caracteres (Kauã resolveu); prioridade só muda a ordem; Danilo valida criando duas campanhas com prioridades diferentes; **configurar probabilidade de gol premiado** (chute a gol, probabilidade de o goleiro defender); **remover os banners internos por jogo** e manter só o upload do banner principal (decisão de Ozéias, Kauã e Danilo).
- **Tela de acesso:** colocar logo da Avenida no cabeçalho (opcional, a área de marketing deve mandar arte); Kauã pegou o layout do formulário de cadastro existente como referência.
- **"Autoriza meu cadastro no programa Tudo AV":** link que abre **nova aba** com o site do Tudo AV explicando o programa; **termos de uso e política de privacidade da Avenida** e termos/regulamento da própria gamificação, que dependem da área (pendência de Ozéias).
- **Menu superior:** tirar as informações de jogadas; links de cartão Avenida, nossas lojas, guia de compras e "indique e ganhe" devem abrir em **outra página** (regra padrão: todos os hiperlinks abrem fora); validar todos os links e remover itens estranhos copiados do site (rodapé "meia DD / FB" não identificado). "Indique e ganhe" remete a link do site Avenida.
- **Meus cupons:** colocar um indicador (asterisco/"i") com legenda "validar lojas participantes", pois o texto diz "lojas da Avenida" mas a campanha vale em lojas participantes.
- **Retirar banners de dentro dos jogos**, mantendo só o banner que o usuário faz upload.
- **Pendências de Ozéias:** tamanhos de imagem (Kauã passa) para pedir à agência; termos/regulamento; FAQ da área.
- **Encaminhamento:** Danilo registra as anotações como comentário do card que Igor criará para Kauã (mesmo que imprecisas). Igor ficou de baixar as transcrições de 17 e 18/09.

## Relação com os outros arquivos

- Mesma frente que mais tarde foi apresentada (resumo do portal) com críticas de domínio/landing page. Ao menos o card #13452 (ajustes de layout e mobile) e os "cards novos de gamificação" citados nas dailies de 01-02/10 e na planning de 30/09 derivam desses ajustes.
- Não conferido: se todos os itens acima já estão em cards; só foi possível relacionar ao que as dailies mencionam.
