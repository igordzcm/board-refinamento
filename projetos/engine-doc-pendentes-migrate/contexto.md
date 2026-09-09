# Engine — Doc Pendentes da Migrate — contexto geral

> Arquivo de contexto do projeto. Levantamento de requisitos em andamento. Squad: VAR 3.0. **Card formal:** [#12901 — VAR 3.0](https://dev.azure.com/GrupoAvenida/VAR%203.0/_workitems/edit/12901), Backlog, filho da Epic #9605 (Engine Fiscal), relacionado ao #12466 (contingência de NFC-e governada pela Engine — mesma direção: Engine assume governança em vez de depender de um terceiro).

## O que é

Quando uma venda é feita, a nota fiscal pode cair em **contingência** — nesse caso, cada loja tem uma pasta de "documentos pendentes" mantida pela **Migrate** (a mesma dependência já conhecida do bloqueio "NFe — rejeição em massa pela Migrate", ver [prioridades-sprint.md](../prioridades-sprint.md)). O problema: notas que caem nessa pasta às vezes **somem** — ficam sem informação de status, sem serem reprocessadas nem reportadas como erro.

## O problema, quantificado

Levantamento aponta **~6.000 notas "mortas"** (sem qualquer informação de status) entre **10/08 e 28/08/2026**, presas na pasta de pendentes da Migrate. Esse número é próximo do "+5.000 notas rejeitadas pela Migrate (erro 297)" já registrado como bloqueio crítico no dashboard executivo (achado por Franklin em 21/08) — **provavelmente o mesmo fenômeno visto por dois ângulos diferentes** (rejeição no primeiro achado, desaparecimento silencioso neste levantamento); precisa confirmar se são a mesma massa de notas ou dois problemas distintos antes de tratar como uma coisa só.

## Direção proposta (ainda em levantamento, não é decisão fechada)

- **Tirar a lógica de doc pendentes da Migrate** — parar de depender da pasta centralizada dela.
- **Deixar os documentos pendentes na própria loja** em vez de centralizar na Migrate.
- **Possível solução técnica:** criar um job de hora em hora pra processar/verificar essas pendências diretamente na loja.

Nenhum desses pontos tem desenho técnico fechado ainda — é o objetivo do levantamento de requisitos em andamento.

## Relação com o bloqueio já rastreado

Este projeto provavelmente **substitui ou aprofunda** a linha "NFe — rejeição em massa pela Migrate (VAR 3.0)" da tabela de bloqueios em [prioridades-sprint.md](../prioridades-sprint.md) — mesma dependência (Migrate/DocPay), mesma janela de tempo (agosto), suspeita de ser a mesma raiz. Ver também a menção em [dailies/2026-08-24-a-28-digest-var3.md](../dailies/2026-08-24-a-28-digest-var3.md) (Donato puxado por Filipe/Spin pra resolver, pedido de limpeza feito ao Vini) e o bloqueio crítico no [dashboard-executivo.html](../dashboard-executivo.html).

## Pendências

- Confirmar se as ~6.000 notas mortas (10-28/08) são a mesma massa das +5.000 notas com erro 297 (achado de Franklin, 21/08), ou dois problemas distintos.
- Validar viabilidade técnica de mover a responsabilidade de doc pendentes pra loja (hoje é tudo centralizado na Migrate) e do job de hora em hora proposto.
- Card #12901 ainda é só o levantamento — falta virar escopo de desenvolvimento (Cenários/AC) depois que a direção técnica for validada.

## Execução — Kovalski confirma início (08/09)

> Fonte: [`../dailies/2026-09-08-digest-retaguarda.md`](../dailies/2026-09-08-digest-retaguarda.md).

Na daily de Retaguarda de 08/09, Kovalski confirmou: **"devo pegar as coisas de doc pendentes pra fazer da engine"**. Isso resolve a ambiguidade que estava em aberto desde o digest de 01–03/09 (lá era só um "talvez", ver [`../dailies/2026-09-01-e-03-digest-retaguarda.md`](../dailies/2026-09-01-e-03-digest-retaguarda.md)) — agora é uma ação do dia, não mais especulação. Isso dá dono de execução ao levantamento, mesmo sem ter havido uma reunião formal.

**Ainda não confirmado:** o que exatamente Kovalski está fazendo (levantamento contínuo, início de desenho técnico, ou outra coisa) — a transcrição não detalha o escopo do trabalho de hoje.

## Reuniões

Nenhuma reunião formal registrada ainda — este contexto nasceu de uma nota direta do Igor (02/09), não de uma call. (Dono de execução confirmado em 08/09, ver seção acima — isso não substitui uma reunião formal de alinhamento.)

## Próxima atualização

Atualizar quando o desenho técnico fechar (transformando #12901 em escopo de dev), quando se confirmar a relação com o bloqueio de "+5.000 notas rejeitadas" já rastreado, ou quando o escopo do trabalho que o Kovalski começou em 08/09 ficar mais claro.
