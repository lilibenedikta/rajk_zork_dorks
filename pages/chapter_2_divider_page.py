import os

from collections import defaultdict
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
from flask import send_from_directory
import dash_bootstrap_components as dbc

import dash


dash.register_page(__name__, path="/chapter_two_divider")

layout = html.Div(
    children = [
        html.Link(href="/assets/style.css", rel="stylesheet"),
        html.H1("Gratulálunk, teljesítetted az első fejezetet!", className="centre_text"),
        html.H3("Várnak még rád a tábor további izgalmai. Folytatod a játékot, vagy mentesz és kilépsz?", className="centre_text_5"),
        dbc.Button("Folytatom!", id = "folytatás_gomb", href="/chapter_two", className="centre_button_left"),
        dbc.Button("Mentek és kilépek", id = "mentes_es_kilepes_gomb", href="/gameon", className="centre_button_right"),
    ]
    
)