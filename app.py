#-----------------------Importando blibliotecas-----------------------
from dash import Dash, html, dcc, Input, Output, callback #importando o dash, html e componentes do dashboard(dcc)
import dash_bootstrap_components as dbc #fornece componentes estilizados e responsivos (botões, tabelas, layouts etc.) usando o framework Bootstrap.
from dash_bootstrap_templates import ThemeSwitchAIO #omponente que permite alternar entre temas Bootstrap, claro e escuro, no nosso caso
from dash_bootstrap_templates import load_figure_template
import plotly.express as px #usado para criar os graficos
import pandas as pd #trabalhar com os dados
from datetime import date
import plotly.graph_objects as go
import json

#-----------------------Importando Bibliotecas-----------------------
import requests
import pandas as pd
from datetime import datetime


#-----------------------Recolhendo dados (INFLAÇÂO)-----------------------
def df_inflacaoFun():
    dados_inflacao = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.13522/dados?formato=json'

    # Fazendo a requisição à API
    requisiscao_inflacao = requests.get(dados_inflacao)

    # Convertendo o JSON em um dicionário
    historico_inflacao = requisiscao_inflacao.json()

    # Criando o DataFrame a partir dos dados JSON
    df_inflacao = pd.DataFrame(historico_inflacao)

    # Convertendo a coluna 'data' para o formato datetime
    df_inflacao['data'] = pd.to_datetime(df_inflacao['data'], format='%d/%m/%Y')

    # Convertendo a coluna 'valor' para float
    df_inflacao['valor'] = df_inflacao['valor'].astype(float)

    return df_inflacao  # Retorna o DataFrame com os dados da inflacao

df_inflacao = df_inflacaoFun()


#-----------------------Recolhendo dados (Dóllar)-----------------------

def df_dollarFun():
    dados_dollar = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json'

    # Fazendo a requisição à API
    requisiscao_dollar = requests.get(dados_dollar)

    # Convertendo o JSON em um dicionário
    historico_dollar = requisiscao_dollar.json()

    # Criando o DataFrame a partir dos dados JSON
    df_dollar = pd.DataFrame(historico_dollar)

    # Convertendo a coluna 'data' para o formato datetime
    df_dollar['data'] = pd.to_datetime(df_dollar['data'], format='%d/%m/%Y')

    # Convertendo a coluna 'valor' para float
    df_dollar['valor'] = df_dollar['valor'].astype(float)

    return df_dollar  # Retorna o DataFrame com os dados do Dólar

df_dollar = df_dollarFun()



#-----------------------Recolhendo dados (SELIC)-----------------------
def df_selicFun():
    dados_selic = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json'

    # Fazendo a requisição à API
    requisiscao_selic = requests.get(dados_selic)

    # Convertendo o JSON em um dicionário
    historico_selic = requisiscao_selic.json()

    # Criando o DataFrame a partir dos dados JSON
    df_selic = pd.DataFrame(historico_selic)

    # Convertendo a coluna 'data' para o formato datetime
    df_selic['data'] = pd.to_datetime(df_selic['data'], format='%d/%m/%Y')

    # Convertendo a coluna 'valor' para float
    df_selic['valor'] = df_selic['valor'].astype(float)

    return df_selic  # Retorna o DataFrame com os dados da Selic

df_selic = df_selicFun()

#-----------------------Recolhendo dados (PIB VALORES CORRENTES R$)-----------------------
def df_pibFun():
    # URL para a API do PIB
    dados_pib = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1207/dados?formato=json'

    # Fazendo a requisição à API
    requisiscao_pib = requests.get(dados_pib)

    # Convertendo o JSON em um dicionário
    historico_pib = requisiscao_pib.json()

    # Criando o DataFrame a partir dos dados JSON
    df_pib = pd.DataFrame(historico_pib)

    # Convertendo a coluna 'data' para o formato datetime
    df_pib['data'] = pd.to_datetime(df_pib['data'], format='%d/%m/%Y')

    # Convertendo a coluna 'valor' para float
    df_pib['valor'] = df_pib['valor'].astype(float)

    return df_pib  # Retorna o DataFrame com os dados do PIB

df_pib = df_pibFun()

#-----------------------Recolhendo dados (PIB per capita R$)-----------------------
def df_pibpercapFun():
    dados_pibpercapita = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.21775/dados?formato=json'

    # Fazendo a requisição à API
    requisiscao_pibpercapita = requests.get(dados_pibpercapita)

    # Convertendo o JSON em um dicionário
    historico_pibpercapita = requisiscao_pibpercapita.json()

    # Criando o DataFrame a partir dos dados JSON
    df_pibpercapita = pd.DataFrame(historico_pibpercapita)

    # Convertendo a coluna 'data' para o formato datetime
    df_pibpercapita['data'] = pd.to_datetime(df_pibpercapita['data'], format='%d/%m/%Y')

    # Convertendo a coluna 'valor' para float
    df_pibpercapita['valor'] = df_pibpercapita['valor'].astype(float)

    return df_pibpercapita  # Retorna o DataFrame com os dados do PIB Per Capita

df_pibpercapita = df_pibpercapFun()



#-----------------------Recolhendo dados (INPC mensal)-----------------------
def df_inpcFun():
    dados_inpc = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.188/dados?formato=json'

    # Fazendo a requisição à API
    requisiscao_inpc = requests.get(dados_inpc)

    # Convertendo o JSON em um dicionário
    historico_inpc = requisiscao_inpc.json()

    # Criando o DataFrame a partir dos dados JSON
    df_inpc = pd.DataFrame(historico_inpc)

    # Convertendo a coluna 'data' para o formato datetime
    df_inpc['data'] = pd.to_datetime(df_inpc['data'], format='%d/%m/%Y')

    # Convertendo a coluna 'valor' para float
    df_inpc['valor'] = df_inpc['valor'].astype(float)

    return df_inpc  # Retorna o DataFrame com os dados do inpc

df_inpc = df_inpcFun()




#-----------------------Recolhendo dados (salario minimo mensal)-----------------------
def df_salariominFun():
    dados_salariomin = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1619/dados?formato=json'

    # Fazendo a requisição à API
    requisiscao_salariomin = requests.get(dados_salariomin)

    # Convertendo o JSON em um dicionário
    historico_salariomin = requisiscao_salariomin.json()

    # Criando o DataFrame a partir dos dados JSON
    df_salariomin = pd.DataFrame(historico_salariomin)

    # Convertendo a coluna 'data' para o formato datetime
    df_salariomin['data'] = pd.to_datetime(df_salariomin['data'], format='%d/%m/%Y')

    # Convertendo a coluna 'valor' para float
    df_salariomin['valor'] = df_salariomin['valor'].astype(float)

    # Agrupando os dados por ano e calculando a média do salário mínimo
    df_salariomin['ano'] = df_salariomin['data'].dt.year
    df_ano = df_salariomin.groupby('ano')['valor'].mean().reset_index()

    # Filtrando os dados para mostrar apenas de 2000 para frente
    df_ano = df_ano[df_ano['ano'] >= 2000]

    return df_ano  # Retorna o DataFrame agrupado por ano

# Obtendo o DataFrame de salários mínimos por ano
df_salariomin = df_salariominFun()

#-----------------------Recolhendo dados (desemprego mensal)-----------------------
def df_desempregoFun():
    dados_desemprego = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.24369/dados?formato=json'

    # Fazendo a requisição à API
    requisiscao_desemprego = requests.get(dados_desemprego)

    # Convertendo o JSON em um dicionário
    historico_desemprego = requisiscao_desemprego.json()

    # Criando o DataFrame a partir dos dados JSON
    df_desemprego = pd.DataFrame(historico_desemprego)

    # Convertendo a coluna 'data' para o formato datetime
    df_desemprego['data'] = pd.to_datetime(df_desemprego['data'], format='%d/%m/%Y')

    # Convertendo a coluna 'valor' para float
    df_desemprego['valor'] = df_desemprego['valor'].astype(float)

    return df_desemprego  # Retorna o DataFrame com os dados do desemprego

df_desemprego = df_desempregoFun()



#-------------------------APP----------------------
import dash

tab_card = {'height':'100%'} #Para que os cards fiquem 100% da coluna

main_config = {
    "hovermode": "x unified",
    "legend": {"yanchor":"top", 
                "y":0.9, 
                "xanchor":"left",
                "x":0.1,
                "title": {"text": None},
                "font" :{"color":"white"},
                "bgcolor": "rgba(0,0,0,0.5)"},
    "margin": {"l":10, "r":10, "t":10, "b":10}
}

config_graph={"displayModeBar": False, "showTips": False} #botões do plotly removidas

template_theme1 = "flatly"
template_theme2 = "darkly"
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY


FONT_AWESOME = ["https://use.fontawesome.com/releases/v5.10.2/css/all.css"]

app = dash.Dash(__name__, external_stylesheets=FONT_AWESOME)


app.layout = dbc.Container(children=[
    #LINHA 1
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([  
                            html.Legend("Análise Econômica")
                        ], sm=8),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            ThemeSwitchAIO(aio_id="theme", themes=[url_theme1, url_theme2]),
                            html.Legend("Ana Luiza Ribeiro")
                        ])
                    ], style={'margin-top': '10px'}),
                    dbc.Row([
                        dbc.Button("Instagram", href="https://www.instagram.com/analu.szribeiro/", target="_blank",style={'backgroundColor': '#ffe032', 'border': '2px solid #ffe032'})
                    ], style={'margin-top': '10px'})
                ])
            ], style=tab_card)
        ],sm=12, lg=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.Legend('Produto Interno Bruto - PIB')
                        ])
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='pib', className='dbc', config=config_graph)
                        ])
                    ])
                ])
            ])
        ],sm=12, lg=7),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='pib_indicador', className='dbc', config=config_graph)
                        ])
                    ], style=tab_card)
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='pibpercapita_indicador', className='dbc', config=config_graph)
                        ])
                    ], style=tab_card)
                ])
            ], className='g-2 my-auto', style={'margin-top': '7px'})
        ], sm=12, lg=2),
    ], className='g-2 my-auto', style={'margin-top': '7px'}),
    #LINHA2
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col([
                                    html.Legend('Inflação (Em 12 meses)')
                                ])
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    dcc.Graph(id='grafico_inflacao', className='dbc', config=config_graph)
                                ])
                            ])
                        ])
                    ])
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col([
                                    html.Legend('Indice Nacional de Preços ao Consumidor - INPC')
                                ])
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    dcc.Graph(id='grafico_INPC', className='dbc', config=config_graph)
                                ])
                            ])
                        ])
                    ])
                ])
            ], className='g-2 my-auto', style={'margin-top': '7px'})
        ], sm=12, lg=6),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='inflacao_indicador', className='dbc', config=config_graph)
                        ])
                    ], style=tab_card)
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='inpc_indicador', className='dbc', config=config_graph)
                        ])
                    ], style=tab_card)
                ])
            ], className='g-2 my-auto', style={'margin-top': '7px'})
        ], sm=12, lg=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.Legend('Sálario Mínimo (Anual)')
                        ])
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='grafico_salariomin', className='dbc', config=config_graph)
                        ])
                    ])
                ])
            ])
        ], sm=12, lg=4)
    ], className='g-2 my-auto', style={'margin-top': '7px'}),
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col([
                                    html.Legend('Taxa de Desocupação (Mensal)')
                                ])
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    dcc.Graph(id='grafico_desemprego', className='dbc', config=config_graph)
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ],sm=12,lg=8),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='cambio_indicador', className='dbc', config=config_graph)
                        ])
                    ], style=tab_card)
                ])
            ])
        ], sm=12, lg=2),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='selic_indicador', className='dbc', config=config_graph)
                        ])
                    ], style=tab_card)
                ])
            ])
        ], sm=12, lg=2)
    ], className='g-2 my-auto', style={'margin-top': '7px', 'margin-bottom':'10px'})

], fluid=True, style={'height':'100vh'})



#-----------------------CALLBACKS-----------------------
@app.callback(
    Output('pib', 'figure'),  # Atualiza o gráfico com o ID 'pib'
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")   # A entrada é o valor do 'theme', que controla o tema
)
def update_graph(toggle):
    # Defina o template baseado no valor do tema
    template = template_theme1 if toggle else template_theme2

    # Criação do gráfico usando o Plotly
    fig_pib = px.line(df_pib, x='data', y='valor', labels={'valor': 'Valor PIB', 'data': 'Data'})

    fig_pib.update_traces(mode='lines',fill='tonexty', line=dict(color='#ffe032'))

    # Aplica o template escolhido
    fig_pib.update_layout(main_config, template=template, height=200)

    return fig_pib

@app.callback(
    Output('pib_indicador', 'figure'),
    Output('pibpercapita_indicador', 'figure'),  # Atualiza o gráfico com o ID 'pib'
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")   # A entrada é o valor do 'theme', que controla o tema
)
def indicador_pibs(toggle):
    # Defina o template baseado no valor do tema
    template = template_theme1 if toggle else template_theme2

    fig_pib_indicador = go.Figure()
    fig_pib_indicador.add_trace(go.Indicator(
    mode='number+delta',  # Exibe o número e a variação (delta)
    value=df_pib['valor'].iloc[-1],  # Valor do indicador
    number={'prefix': 'R$', 'valueformat': '.0s', "font": {"size":30}},  # Adiciona o símbolo de porcentagem
    title={'text': "<span style='font-weight:bold; font-size:20px'>PIB - 2023</span>"},
    delta={'reference': df_pib['valor'].iloc[-2],'relative': True, 'valueformat': '.2%'}  # Valor de referência para calcular o delta
    ))

    fig_pibpercapita_indicador = go.Figure()
    fig_pibpercapita_indicador.add_trace(go.Indicator(
    mode='number+delta',  # Exibe o número e a variação (delta)
    value=df_pibpercapita['valor'].iloc[-1],  # Valor do indicador
    number={'prefix': 'R$', 'valueformat': '.2f', "font": {"size":30}},  # Adiciona o símbolo de porcentagem
    title={'text': "<span style='font-weight:bold; font-size:20px'>PIB per capita</span><br><span style='font-size:10px'>(2023)</span>"},
    delta={'reference': df_pibpercapita['valor'].iloc[-2], 'relative': True, 'valueformat': '.2%'}  # Valor de referência para calcular o delta
    ))


    # Aplica o template escolhido
    fig_pib_indicador.update_layout(main_config, template=template, height=98)
    fig_pibpercapita_indicador.update_layout(main_config, template=template, height=100)
    fig_pib_indicador.update_layout({"margin": {"l":0, "r":0, "t":20, "b":0}})
    fig_pibpercapita_indicador.update_layout({"margin": {"l":0, "r":0, "t":20, "b":0}})

    return fig_pib_indicador, fig_pibpercapita_indicador

#graficos da segunda linha---------------------------------
@app.callback(
    Output('grafico_inflacao', 'figure'),  # Atualiza o gráfico com o ID 'pib'
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")   # A entrada é o valor do 'theme', que controla o tema
)
def update_graphinflacao(toggle):
    # Defina o template baseado no valor do tema
    template = template_theme1 if toggle else template_theme2

    # Criação do gráfico usando o Plotly
    fig_inflacao = px.line(df_inflacao, x='data', y='valor', labels={'valor': 'Valor', 'data': 'Data'})

    fig_inflacao.update_traces(mode='lines',fill='tonexty', line=dict(color='#ffe032'))

    # Aplica o template escolhido
    fig_inflacao.update_layout(main_config, template=template, height=130)

    return fig_inflacao

@app.callback(
    Output('grafico_INPC', 'figure'),  # Atualiza o gráfico com o ID 'pib'
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")   # A entrada é o valor do 'theme', que controla o tema
)
def update_graphinpc(toggle):
    # Defina o template baseado no valor do tema
    template = template_theme1 if toggle else template_theme2

    # Criação do gráfico usando o Plotly
    fig_inpc = px.line(df_inpc, x='data', y='valor', labels={'valor': 'Valor', 'data': 'Data'})

    fig_inpc.update_traces(mode='lines',fill='tonexty', line=dict(color='#ffe032'))

    # Aplica o template escolhido
    fig_inpc.update_layout(main_config, template=template, height=130)

    return fig_inpc

@app.callback(
    Output('inflacao_indicador', 'figure'),
    Output('inpc_indicador', 'figure'),  # Atualiza o gráfico com o ID 'pib'
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")   # A entrada é o valor do 'theme', que controla o tema
)
def indicador_ipcs(toggle):
    # Defina o template baseado no valor do tema
    template = template_theme1 if toggle else template_theme2

    fig_inflacao_indicador = go.Figure()
    fig_inflacao_indicador.add_trace(go.Indicator(
    mode='number+delta',  # Exibe o número e a variação (delta)
    value=df_inflacao['valor'].iloc[-1],  # Valor do indicador
    number={'suffix': '%', 'valueformat': '.2f', "font": {"size":40}},  # Adiciona o símbolo de porcentagem
    title={'text': "<span style='font-weight:bold; font-size:30px'>Inflação</span>"},
    delta={'reference':df_inflacao['valor'].iloc[-13],'relative': True, 'valueformat': '.2%', 'increasing': {'color': 'red'},'decreasing': {'color': 'green'}}  # Valor de referência para calcular o delta
    ))

    fig_inpc_indicador = go.Figure()
    fig_inpc_indicador.add_trace(go.Indicator(
    mode='number',  # Exibe o número e a variação (delta)
    value=df_inpc['valor'].iloc[-1],  # Valor do indicador
    number={'suffix': '%', 'valueformat': '.2f', "font": {"size":40}},  # Adiciona o símbolo de porcentagem
    title={'text': "<span style='font-weight:bold; font-size:30px'>INPC</span><br><span style='font-size:15px'>a.m.</span>"}
    ))


    # Aplica o template escolhido
    fig_inflacao_indicador.update_layout(main_config, template=template, height=175)
    fig_inpc_indicador.update_layout(main_config, template=template, height=174)
    fig_inflacao_indicador.update_layout({"margin": {"l":0, "r":0, "t":20, "b":0}})
    fig_inpc_indicador.update_layout({"margin": {"l":0, "r":0, "t":20, "b":0}})

    return fig_inflacao_indicador, fig_inpc_indicador






#graficos da segunda linha---------------------------------
@app.callback(
    Output('grafico_desemprego', 'figure'),  # Atualiza o gráfico com o ID 'pib'
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")   # A entrada é o valor do 'theme', que controla o tema
)
def update_graphdesemprego(toggle):
    # Defina o template baseado no valor do tema
    template = template_theme1 if toggle else template_theme2

    # Criação do gráfico usando o Plotly
    fig_desemprego = px.line(df_desemprego, x='data', y='valor', labels={'valor': 'Valor', 'data': 'Data'})

    fig_desemprego.update_traces(mode='lines',fill='tonexty', line=dict(color='#ffe032'))

    # Aplica o template escolhido
    fig_desemprego.update_layout(main_config, template=template, height=130)

    return fig_desemprego



@app.callback(
    Output('cambio_indicador', 'figure'),
    Output('selic_indicador', 'figure'),  # Atualiza o gráfico com o ID 'pib'
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")   # A entrada é o valor do 'theme', que controla o tema
)

def indicador_cambio_selic(toggle):
    # Defina o template baseado no valor do tema
    template = template_theme1 if toggle else template_theme2

    fig_cambio_indicador = go.Figure()
    fig_cambio_indicador.add_trace(go.Indicator(
    mode='number',  # Exibe o número e a variação (delta)
    value=df_dollar['valor'].iloc[-1],  # Valor do indicador
    number={'prefix': 'R$', 'valueformat': '.4f', "font": {"size":40}},  # Adiciona o símbolo de porcentagem
    title={'text': "<span style='font-weight:bold; font-size:30px'>Dólar</span><br><span style='font-size:12px'>PTAX Venda</span>"}  # Valor de referência para calcular o delta
    ))

    fig_selic_indicador = go.Figure()
    fig_selic_indicador.add_trace(go.Indicator(
    mode='number',  # Exibe o número e a variação (delta)
    value=df_selic['valor'].iloc[-1],  # Valor do indicador
    number={'suffix': '%', 'valueformat': '.2f', "font": {"size":40}},  # Adiciona o símbolo de porcentagem
    title={'text': "<span style='font-weight:bold; font-size:30px'>Taxa Selic</span>"}
    ))


    # Aplica o template escolhido
    fig_cambio_indicador.update_layout(main_config, template=template, height=175)
    fig_selic_indicador.update_layout(main_config, template=template, height=174)
    fig_cambio_indicador.update_layout({"margin": {"l":0, "r":0, "t":20, "b":0}})
    fig_selic_indicador.update_layout({"margin": {"l":0, "r":0, "t":20, "b":0}})

    return fig_cambio_indicador, fig_selic_indicador


@app.callback(
    Output('grafico_salariomin', 'figure'),  # Atualiza o gráfico com o ID 'grafico_salariomin'
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")  # A entrada é o valor do switch, que controla o tema
)
def update_graphsalariomin(toggle):
    # Defina o template baseado no valor do tema
    template = template_theme1 if toggle else template_theme2

    # Criando o gráfico de barras
    figure_salario = px.bar(df_salariomin, x='ano', y='valor', labels={'ano': 'Ano', 'valor': 'Valor do Salário Mínimo'}, color_discrete_sequence=['#ffe032'])

    # Aplica o template escolhido ao gráfico
    figure_salario.update_layout(main_config, template=template, height=350)

    return figure_salario








#-----------------------Inicializa o app-----------------------
if __name__ == '__main__':
    app.run(debug=True, port='8051')