# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fechas": ["Feb/20/2021", "Feb/21/2021", "Feb/22/2021", "Mar/01/2021", "Mar/06/2021", "Mar/10/2021"],
    "Puntaje": [9, 9, 8, 14, 9, 6],
    "Dificultad": ["Facil", "Facil", "Facil", "Medio", "Medio", "Medio"],

})

df2 = pd.DataFrame({
    "Fechas": ["Feb/20/2021", "Feb/21/2021", "Feb/22/2021", "Mar/01/2021", "Mar/06/2021", "Mar/10/2021"],
    "Puntaje": [10, 20, 18, 14, 9, 6],
    "Dificultad": ["Facil", "Facil", "Facil", "Medio", "Medio", "Medio"],

})
#fig = px.bar(df, x="Pacientes", y="Puntaje", color="Dificultad", barmode="group")


f = go.FigureWidget()
f.add_scatter(y=df["Puntaje"], x=df["Fechas"])
#f.add_bar(y=[1, 4, 3, 2])
f.layout.title = 'Ejercicio Memoria'

f2 = go.FigureWidget()
f2.add_scatter(y=df2["Puntaje"], x=df2["Fechas"])
#f2.add_bar(y=[1, 4, 3, 2])
f2.layout.title = 'Ejercicio Secuencia de Pasos'


app.layout = html.Div(children=[
    html.H1(children='Escenario Prueba'),

    html.Label('Dificultad'),

    html.Div(children='''
        Mostrando los últimos 10 resultados para el paciente: John Doe.
    '''),

    dcc.Dropdown(
        options=[
            {'label': u'Fácil', 'value': u'Fácil'},
            {'label': 'Medio', 'value': 'Medio'},
            {'label': u'Difícil', 'value': u'Difícil'}
        ],
        value= u'Fácil'
    ),

    dcc.Graph(
        id='ejercicio-memoria',
        figure=f
    ),

    dcc.Dropdown(
        options=[
            {'label': u'Fácil', 'value': u'Fácil'},
            {'label': 'Medio', 'value': 'Medio'},
            {'label': u'Difícil', 'value': u'Difícil'}
        ],
        value= u'Fácil'
    ),
    dcc.Graph(
        id='ejercicio-pasos',
        figure=f2
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)