import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import plotly.express as px
import numpy as np
from dash.dependencies import Input, Output
from flask import Flask

server = Flask(__name__)
app = dash.Dash(server=server)

x = np.linspace(-10, 10, 1000)

app.layout = html.Div([
    dcc.Graph(id='graph'),
    html.Button('Show/Hide Inflection Points', id='button'),
    html.Div([
        html.Label("Enter equation:"),
        dbc.Input(id='equation-input', type='text', value='x**3', style={'width': '50%'}),
    ]),
])


@app.callback(
    Output('graph', 'figure'),
    [Input('button', 'n_clicks'),
     Input('equation-input', 'value')]
)
def update_graph(n_clicks, equation):
    y = eval(equation)
    fig = px.line(x=x, y=y)
    if n_clicks % 2 == 1:
        fig.add_scatter(x=[0], y=[0], mode='markers')
    return fig


if __name__ == '__main__':
    app.run_server()