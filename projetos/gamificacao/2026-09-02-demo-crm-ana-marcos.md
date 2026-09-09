# Gamificação — Demo pro CRM (Ana Carina / Marcos), 02/09/2026

> Reunião de demonstração/homologação do Portal de Gamificação (Roleta 3.0) pra área de negócio (CRM). Transcrição: `GAMEFICAÇÃO.docx`, ~1h15min. Participantes: Ozéias Denis de A. Tavares (dono de negócio, conduziu a demo), Kauã Miguel da Cunha (dev, apoiando), Ana Carina Araujo Souza (coordenadora CRM), Marcos Eidi Yonamine (gerente CRM), Igor Diniz Camargo (participação breve, só pra avisar de um bloqueio técnico). **Não é daily nem review/retro/planning de sprint** — é uma reunião de validação funcional com a área, arquivada aqui (mesmo padrão usado em `../conciliacao-fase-2/reuniao-ozeias-apresentacao-inicial.md` e `../dashboard-cds/reuniao-maria-2026-08-12.md`).

## O que foi mostrado

Fluxo completo de cadastro de campanha (roleta, raspadinha, caça-níquel — gol premiado só citado) e a experiência do cliente final: seleção de mecânica, nome, datas, lojas, valores, prioridade entre campanhas concorrentes (agrupamento), segmentação por base de CPF (import via Excel), banners, regulamento, FAQ por campanha + FAQ geral do site, revisão e rascunho salvável. Do lado cliente: login por CPF + data de nascimento (sem senha), tela de jogos disponíveis, jogo (roleta/raspadinha/caça-níquel) com animação, geração/resgate de voucher, listagem de cupons (disponíveis/usados/a vencer), meu perfil.

## Dois bugs achados ao vivo durante a demo

1. **Sistema quebrou ao tentar acessar com CPF de teste** — root cause: acesso de homologação ao banco foi bloqueado (Igor entrou na call só pra avisar disso; Kauã confirmou "zero acesso ao banco"). Bloqueou a demonstração por ~5-10 minutos até o Alisson (citado, não presente na call) resolver do lado da infra.
2. **Editar rótulo/valor de símbolo no cadastro do caça-níquel quebra a tela de configuração** — reproduzido ao vivo (Kauã já sabia que ia quebrar antes de o Ozéias tentar); funcionou numa segunda tentativa, mas o bug em si não foi investigado/corrigido durante a call.

## Decisões e pedidos de ajuste levantados durante a demo

- **Remover a validação de "campanha ativa por tipo"** — hoje só é possível ter uma campanha ativa de um mesmo jogo por vez; a ideia validada com CRM é permitir várias campanhas simultâneas (inclusive do mesmo jogo) segmentadas por base de CPF/loja/valor, sem bloqueio por data. Ozéias/Ana/Marcos concordaram que faz sentido remover essa trava — **ainda não é decisão 100% fechada tecnicamente**, Ozéias anotou pra validar depois.
- **Nova opção de validade de voucher "até o fim da campanha"** (hoje só dá pra configurar em dias fixos) — pedido de Ana/Marcos, Ozéias concordou que faz sentido, vai implementar.
- **Novo campo "nome da campanha pro cliente"** — separar o nome interno de controle (visível só pra Ana/CRM) do nome amigável exibido ao cliente final. A implementar.
- **Decisão pendente sobre banner customizável por campanha** — hoje a imagem é padrão fixa por tipo de jogo; Ana se inclinou por permitir upload de imagem própria por campanha ("fica mais a cara da Avenida"), mas ficou como próximo passo a decidir, não fechado.
- **Remover a contagem somada de "jogadas disponíveis"** (ex.: mostrava "13" somando rodadas de campanhas distintas) — Ozéias avaliou que não faz sentido manter, vai tirar.
- **Ideias levantadas mas não compromissadas:** som que muda conforme o valor do prêmio; botão "salvar na agenda" (ICS nativo do navegador — Kauã confirmou ser trivial); botão "compartilhar com um amigo" via WhatsApp com UTM (Marcos pediu que o rastreamento venha certinho — ficou como próximo assunto a mapear, não escopo fechado).
- **Regra de "1 cupom por dia" levantada pela Ana** (pra evitar cliente dividir uma compra grande em várias pra usar vários cupons) — conclusão da call: isso teria que ser controlado no **VAR**, não no portal de Gamificação, e é difícil de bloquear de fato; no máximo dá pra colocar um aviso informativo, sem trava real. **Sem decisão de implementar.**
- **Ponto de LGPD/privacidade sem fechamento**: exibir nome do cliente pós-login sem segunda validação além da data de nascimento — Ozéias/Marcos decidiram manter como está por ora (dado só visível internamente), mas reconheceram que precisa validar melhor com jurídico/segurança.
- Ana pediu mapeamento das tabelas de "Tudo a Ver" pro Emerson (BI) conseguir enxergar os dados atualizados — ação pendente do lado Ozéias.

## Fora de escopo desta fase (explicitamente adiado)

- **Pré-aprovação de cartão** (rodar motor de crédito no momento do cadastro) — fica pra uma fase futura; Ozéias sugeriu informalmente "fevereiro" como possível janela, sem compromisso formal.
- **"Inteligência de recompensa"** (ajustar probabilidade dinamicamente conforme movimento da loja) — mencionado como próxima fase, sem escopo.
- **Programa de indicação ("catch member"/indique amigos)** — Marcos levantou a ideia como conceito relacionado mas distinto, não entra nesse projeto.
- Redesenho do material de PDV pela área de Marketing (agora precisa ser "material curinga", já que várias campanhas podem rodar ao mesmo tempo) — ação do lado CRM/Marketing, fora do escopo de dev.

## Plano de rollout combinado

No go-live, este portal **substitui tanto o "Chute ao Gol" quanto a "Roleta"** atuais — o link da roleta atual vai ganhar redirect pro novo portal, chute ao gol é descontinuado. Meta informal combinada na call: produção **até o final de setembro/2026**, destacada como mais simples por **não depender de nenhuma mudança no VAR**. Próximo passo imediato: Ana/Marcos ganham acesso de homologação (recadastro de 2FA via Microsoft Authenticator) pra rodar a própria bateria de testes contra a especificação funcional já combinada, em paralelo aos ajustes pontuais listados acima.

## Pendências

- Confirmar tecnicamente a remoção da validação de bloqueio por tipo de campanha.
- Fechar decisão sobre banner customizável por campanha.
- Corrigir o bug de edição de símbolo/rótulo no cadastro do caça-níquel (reproduzido ao vivo, não investigado a fundo).
- Confirmar com jurídico/segurança se a exibição do nome do cliente pós-login (validação única por data de nascimento) está OK do ponto de vista de LGPD.
- Ana/Marcos rodarem a própria bateria de testes em homologação e reportar achados.
