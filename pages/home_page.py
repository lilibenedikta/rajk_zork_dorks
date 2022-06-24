import os

from collections import defaultdict
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
from flask import send_from_directory
import dash_bootstrap_components as dbc

import dash


dash.register_page(__name__, path="")

layout = html.Div(
    children = [
        html.Link(href="/assets/style.css", rel="stylesheet"),
        html.H1("Sose lesz vége!", className="centre_text"),
        html.H3("Üsd be a neved egy új játékhoz. \
            Ha már rendelkezel mentéssel, akkor pedig folytathatod ugyanonnan.", className="centre_text_5"),
        dcc.Input(id="text_input_small", type="text", placeholder="Enter user ID"),
        dbc.Button("Mehet!", id = "start_gomb", href="/gameon", className="centre_button"),

    ]
    
)

