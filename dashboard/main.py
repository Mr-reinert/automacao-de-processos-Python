from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd


app = Dash(__name__)

# ler a base de dados
df = pd.read_excel("Vendass.xlsx")

#criando o gráfico
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes = list(df['ID Loja'].unique())
opcoes.append('Todas as lojas')

app.layout = html.Div(children=[
    html.H1(children='Faturamento das lojas'),
    html.H2(children='Gráficos com o faturamento de todos os produtos separados por loja'),

    html.Div(children='''
        Obs: esse gráfico mostra a quantidade de produtos vendidos.
    '''),

    dcc.Dropdown(opcoes, value= 'Todas as lojas', id='lista_lojas'),
    dcc.Graph(
        id='grafico_quantidade_vendas',
        figure=fig
    )
])

@app.callback(
    Output('grafico_quantidade_vendas', 'figure'),
    Input('lista_lojas', 'value')
)
def update_output(value):
    if value == "Todas as lojas":
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja']==value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)






