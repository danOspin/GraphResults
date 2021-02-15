# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Pacientes": ["Paciente 1", "Paciente 2", "Paciente 3", "Paciente 1", "Paciente 2", "Paciente 3"],
    "Puntaje": [4, 4, 5, 5, 1, 2],
    "Dificultad": ["Facil", "Facil", "Facil", "Medio", "Medio", "Medio"]
})

fig = px.bar(df, x="Pacientes", y="Puntaje", color="Dificultad", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Escenario Prueba'),

    html.Div(children='''
        Resultados para la fecha 13/02/2021.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)