import os

from collections import defaultdict
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
from flask import send_from_directory
import dash_bootstrap_components as dbc

import pandas as pd

import dash

dash.register_page(__name__, path="/chapter_two_divider")

edge_data = pd.read_csv("data/RAJK_ZORK_edges.csv").set_index("FROM")
node_data = pd.read_csv("data/RAJK_ZORK_nodes.csv").set_index("NODE_ID")

layout = html.Div(
    children = [
        #dcc.Markdown(id="situation_ch_2", className="good_text"),
        html.Link(href="/assets/style.css", rel="stylesheet"),
        html.H1("Gratulálunk, teljesítetted az első fejezetet!", className="centre_text"),
        html.H3("Várnak még rád a tábor további izgalmai. Folytatod a játékot, vagy mentesz és kilépsz?", className="centre_text_5"),
        dbc.Button("Folytatom!", id = "folytatás_gomb", href="/chapter_two", className="centre_button_left"),
        dbc.Button("Mentek és kilépek", id = "mentes_es_kilepes_gomb", href="/gameon", className="centre_button_right")
    ]
    
)
