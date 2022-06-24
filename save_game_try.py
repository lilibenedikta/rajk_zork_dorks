import time
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Output, Input
from dash_extensions.enrich import Dash, Trigger, ServersideOutput

app = Dash(prevent_initial_callbacks=True)
app.layout = html.Div([
    html.Button("Query data", id="btn"), dcc.Dropdown(id="dd"), dcc.Graph(id="graph"),
    dcc.Loading(dcc.Store(id="store"), fullscreen=True, type="dot")
])

@app.callback(ServersideOutput("store", "data"), Trigger("btn", "n_clicks"), memoize=True)
def query_data():
    time.sleep(1)
    return px.data.gapminder()

@app.callback(Input("store", "data"), Output("dd", "options"))
def update_dd(df):
    return [{"label": column, "value": column} for column in df["year"]]

@app.callback(Output("graph", "figure"), [Input("store", "data"), Input("dd", "value")])
def update_graph(df, value):
    df = df.query("year == {}".format(value))
    return px.sunburst(df, path=['continent', 'country'], values='pop', color='lifeExp', hover_data=['iso_alpha'])

if __name__ == '__main__':
    app.run_server(debug=True)

######### a failed try 

    import os

from collections import defaultdict
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from flask import send_from_directory
import dash_bootstrap_components as dbc

import dash


dash.register_page(__name__, path="")

layout = html.Div(
    children = [
        html.Link(href="/assets/style.css", rel="stylesheet"),
        dcc.Markdown("--____---------------------------_------------------------------------------------------_-", className="centre_text_1"),
        dcc.Markdown("-/ ___|----___----___----___----| |---___---___---____---__---__---___----__-_----___--| |", className="centre_text_2"),
        dcc.Markdown("-\___ \---/ _ \--/ __|--/ _ \---| |--/ _ \-/ __|-|_  /---\ \-/ /--/ _ \--/ _` |--/ _ \-| |", className="centre_text_3"),
        dcc.Markdown("--___) |-| (_) |-\__ \-|  __/---| |-|  __/-\__ \--/ /-----\ V /--|  __/-| (_| |-|  __/-|_|", className="centre_text_4"),
        dcc.Markdown("-|____/---\___/--|___/--\___|---|_|--\___|-|___/-/___|-----\_/----\___|--\__, |--\___|-(_)", className="centre_text_5"),
        dcc.Markdown("-------------------------------------------------------------------------|___/------------", className="centre_text_6"),
        dcc.Input(id="text_input_small", type="text", placeholder="Enter user ID")
    ]

)

