# SSO / Keycloak — contexto geral

> Arquivo de contexto do projeto. Ler antes de qualquer reunião sobre este projeto.

## O que é

Login único dos portais (Keycloak + Kong), com o **sso-hub** (`sso-hub.avenida.com.br`) como portal de gestão: gerar link de acesso, cadastrar usuários e grupos, OTP e troca de senha. Épico **#11853 (SSO)**, dono técnico **Kovalski**. A integração do SIGA ao SSO está descrita em [../siga/contexto.md](../siga/contexto.md).

## Status atual (29/09/2026) — em produção, nova rodada de melhorias

- Portais já no SSO. O SIGA entrou em 27/09 e funcionou: quem cadastrou OTP no sso-hub já usa o novo login.
- Falta só o teste regressivo da geração de link de acesso: [#13055](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13055) (Danilo, Ready for Dev).

## Nova rodada de melhorias (anotações de 29/09)

Fonte: [2026-09-29-anotacoes-melhorias-sso.md](2026-09-29-anotacoes-melhorias-sso.md). Tudo com o Kovalski, Sprint 30.

1. **Link de acesso de uso único:** depois que o usuário entra pelo link e conclui o processo, o link não pode mais ser usado. Tem que bloquear e avisar que o link já foi utilizado.
2. **Erros ao gerar link:** hoje o front do SSO mostra uma mensagem genérica. É preciso capturar o erro real e mostrar mensagens claras.
3. **Trazer usuários e grupos:** hoje o sistema busca no Keycloak e sincroniza com o banco (em HML). Vale a pena, ou é melhor só chamar a rota do Keycloak que já faz isso? Precisa medir a complexidade. **O portal não pode ficar lento de jeito nenhum.**
4. **Melhorias de tela:** criar usuário hoje é Usuários → Criar usuário, que carrega um card. A ideia é abrir uma tela de cadastro. O mesmo vale pra grupos.

### Cards (Sprint 30, Refinement, Kovalski, pai #11853)

- **Item 1 (link de uso único):** já existia no [#13433](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13433), criado pelo próprio Kovalski em 29/09. Ele também exige token de administrador no endpoint de gerar link. Está na Sprint 29, no template antigo e sem estimativa.
- [#13448](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13448) mensagens de erro claras ao gerar link: 3 pts.
- [#13449](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13449) investigação: usuários e grupos direto do Keycloak ou com cópia no banco: 3 pts, time-box. Falta definir o tempo de resposta aceitável.
- [#13450](https://dev.azure.com/GrupoAvenida/Var%20Retaguarda/_workitems/edit/13450) cadastro de usuário e grupo em tela própria: 5 pts. O mock é necessário e não foi feito. Falta saber qual é a dor do card atual.

O código do sso-hub não está nos repositórios locais, então os cards não têm nota técnica.

## Reuniões

(nenhuma registrada)
