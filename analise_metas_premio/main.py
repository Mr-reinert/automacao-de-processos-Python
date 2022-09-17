import pandas as pd
from twilio.rest import Client

# Inserir código de conta criada no twilio para poder enviar as notificações por SMS
account_sid = "AXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Inserir Token
auth_token  = "AXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client = Client(account_sid, auth_token)

#define vetor único para comportar os meses de suas respectivas tabelas
lista_meses = ['janeiro', 'fevereiro','março','abril','maio','junho']
meta = 50000

#leitura em todas as tabelas com laço de repetição
for i in lista_meses:
    tabela_vendas = pd.read_excel(f'{i}.xlsx')

#se na tabela 'Vendas' se existe algum número maior que 55.000 então...
    if (tabela_vendas['Vendas'] > meta).any():
        #localizará na tabela (linha/coluna) desejada, e quantos valores{ .loc[(linha),'coluna'].values[0] }
        vendedor = tabela_vendas.loc[(tabela_vendas['Vendas'] > meta),'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > meta,'Vendas'].values[0]

        #envia mensagem com base no seu cadastro no twilio
        message = client.messages.create(
            to="+550000000000",
            from_="+123456789",
            body=f"Metas batidas no mês de {i}:\n Vendedor: {vendedor}\n Vendas: R$ {vendas}\n")
        print(message.sid)

        print(f"Metas batidas no mês de {i}:\n Vendedor: {vendedor}\n Vendas: R$ {vendas}\n")
