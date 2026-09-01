RESUMO DA REUNIÃO - PORTAL RETAGUARDA / MÓDULO RH
====================================================
Participantes: Ozéias Denis de A. Tavares (apresentação/dev), Diego, Kauã e
Danilo (desenvolvedores/QA), Gilson Valerio Dos Santos (Gerente - Folha de
Pagamento, Trabalhista, Remuneração e Benefícios), Midia Negrao Do Espirito
Santo Lima (time de RH).

1. CONTEXTO GERAL
------------------
- O sistema apresentado é o "Portal Retaguarda", originalmente criado para
  conciliação de lojas, e hoje ampliado com diversos módulos.
- Foi criado um novo módulo de RH (11º módulo) para centralizar as
  informações que hoje são enviadas por e-mail, permitindo que o time de RH
  faça buscas e coletas mensais diretamente no portal.

2. FLUXO ATUAL APRESENTADO (Financeiro -> RH)
----------------------------------------------
- O analista financeiro realiza a conciliação de loja e, ao identificar uma
  divergência (ex.: perda), pode marcar a justificativa como "desconto em
  folha".
- Esse registro é enviado para a tela "Gerenciar Perdas" (nova versão de
  tela já existente), onde é possível:
  - Filtrar por operador, loja, status (enviado ou não ao RH) e
    divergências.
  - Aprovar ou reprovar a divergência.
  - Ao aprovar, o sistema oferece a opção de parcelamento do desconto em
    folha.
- Após aprovação, a divergência é liberada e o fechamento da conciliação
  pode ser feito normalmente (as regras de conciliação não foram
  alteradas).
- O item aprovado passa então para o módulo de RH > "Aprovação de Vales",
  onde o time de RH (Gilson/Midia) consegue:
  - Ver o ciclo, quantos dias faltam para fechar, quantos vales estão
    pendentes e os descontos em folha.
  - Filtrar por data.
  - Aprovar ou reprovar o vale (com opção de justificar a reprovação, ex.:
    impossibilidade de parcelamento).

3. PONTO DE ATENÇÃO LEVANTADO PELO GILSON (RH)
------------------------------------------------
- Gilson considerou que a etapa de aprovação pelo RH, do jeito que foi
  desenhada, pode gerar trabalho desnecessário para a equipe.
- Ele entende que o RH precisa apenas RECEBER o valor a ser descontado, não
  necessariamente aprovar/reprovar cada item.
- Midia esclareceu que a aprovação do RH só seria necessária quando o
  financeiro enviar o pedido de PARCELAMENTO (não para envios em parcela
  única).
  => Isso conecta diretamente com o ponto abaixo, adicionado pelo usuário.

4. PONTOS ADICIONAIS PARA REVISÃO (levantados pelo usuário)
--------------------------------------------------------------

4.1 Regra de parcelamento
   - Quando o desconto for enviado em 1 (uma) única vez, NÃO deve vir
     como parcelado.
   - Envio em 1 vez já deve ser considerado como ACEITO automaticamente
     (sem necessidade de aprovação extra do RH).

4.2 Revisar as datas do processo de RH e Contábil

   RH
   ---
   Ciclo 1 (Agosto):
     10/08 -> Dia da Conciliação (dia da diferença)
     12/08 -> Dia da aprovação da perda
     13/08 -> Dia do fechamento da conciliação

   Ciclo 2 (Agosto):
     18/08 -> Dia da Conciliação (dia da diferença)
     19/08 -> Dia da aprovação da perda
     19/08 -> Dia do fechamento da conciliação

   CONTÁBIL
   --------
   Ciclo 1 (Agosto):
     10/08 -> Dia da Conciliação (dia da diferença)
     12/08 -> Dia da aprovação da perda
     13/08 -> Dia do fechamento da conciliação

   Ciclo 2 (Agosto):
     22/08 -> Dia da Conciliação (dia da diferença)
     23/08 -> Dia da aprovação da perda
     31/08 -> Dia do fechamento da conciliação

   Fechamento RH: 20/07 -> 19/08 (Mês de referência: Agosto)
   Fechamento Conciliação: 26/07 -> 25/08 (Mês de referência: Agosto)

   OBS: as datas de RH e Contábil estão diferentes entre si (ex.: segundo
   ciclo do RH fecha em 19/08, enquanto o Contábil só fecha em 31/08) -
   necessário validar se isso é intencional ou se precisa de ajuste/
   alinhamento entre as áreas.

4.3 Revisar as regras de loja com quebra de caixa
   - Necessário incluir o envio do CPF do gerente da loja nesse fluxo.

4.4 Revisar o que é enviado para o Contábil (planilha)
   - Solicitação da Adriana: o sistema deve gerar a planilha já no formato
     pronto para ser importada diretamente no Oracle.

5. PRÓXIMOS PASSOS SUGERIDOS
-------------------------------
- Ajustar o fluxo para que envios em parcela única (1x) sejam
  automaticamente aceitos, sem etapa de aprovação do RH.
- Validar e alinhar as datas de fechamento entre RH e Contábil.
- Definir como o CPF do gerente será capturado/exibido na regra de quebra
  de caixa.
- Ajustar a geração da planilha para o Contábil no formato de importação
  do Oracle (alinhar layout com a Adriana).