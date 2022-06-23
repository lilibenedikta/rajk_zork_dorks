import os

from collections import defaultdict
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from flask import send_from_directory
import dash_bootstrap_components as dbc

import dash


dash.register_page(__name__, path="/page-2")

layout = html.Div(
    children = [
        html.Link(href="/assets/style.css", rel="stylesheet"),
        html.H1("Hello World", className="good-text")
    ]
)



