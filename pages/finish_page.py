import os

from collections import defaultdict
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from flask import send_from_directory
import dash_bootstrap_components as dbc

import dash


dash.register_page(__name__, path="/finish")

layout = html.Div(
    children = [
        html.Link(href="/assets/style.css", rel="stylesheet"),
        html.H1("Gratulálunk, sikeresen végigjátszottad a Sose lesz vége!-t!", className="centre_text"),
        html.H1("A statisztikáid:", className="centre_text_5")
    ]
)



