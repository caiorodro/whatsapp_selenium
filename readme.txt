
Com a library selenium é possível obter acesso direto a rendereização final de qualquer página ativa na web.

O objetivo desse software é Enviar mensagens aos poucos para contatos pré-selecionados vindos de uma requisição web e
fazer a função manual do operador.

O software obtém os dados dos contatos. Tais contatos devem estar cadastrados no celular que vai fazer a autenticação 
pelo whatsapp.

Passo a passo:

1 - Crie uma requisição web que retorne os dados de contatos no seguinte formato:

[{"NICKNAME": "TransAuto Paulo", "CONTEUDO": "Sua mensagem", "CONTATO": "SR. Paulo" }]

2 -  Aguarde a página do QRCode do whatsapp e faça a autenticação com o seu celular.

3 - Os contatos contidos no formato Json acima devem estar cadastrados em seu telefone.

4 - Assista o software fazer o envio de sua mensagem 1 por vez pausando alguns segundos a cada iteração.
