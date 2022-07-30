import os

from collections import defaultdict
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
from flask import send_from_directory
import dash_bootstrap_components as dbc
from session_state import SessionState, Starting_SessionState

import dash

START_STATES = defaultdict(Starting_SessionState)

dash.register_page(__name__, path="")

layout = html.Div(
    children = [
        html.Link(href="/assets/style.css", rel="stylesheet"),
        html.H1("Sose lesz vége!", className="centre_text"),
        html.H3("Üsd be a neved egy új játékhoz. \
            Ha már rendelkezel mentéssel, akkor pedig folytathatod ugyanonnan.", className="centre_text_5"),
        dcc.Input(id="text_input_small", type="text", placeholder="Enter user ID"),
        dbc.Button("Mehet!", id = "start_gomb", href="/gameon", className="centre_button"),
        dcc.Markdown(id="display_user_id", className="user_id_text_topright"),
        dcc.Markdown(id="most_recent_session_state", className="good_text"),
    ]
    
)

@callback(
    [
        Output("most_recent_session_state", "children"),
        Output("display_user_id", "children"),
    ],
    [
        Input("text_input_small", "value"),
        Input("start_gomb", "n_clicks"),
    ]
)
def start_game(input_text, n_clicks,):
    sesh = START_STATES[input_text]
    new_or_saved_session_state = input_text
    user_id = ""
    if n_clicks:
        user_id = input_text

    return new_or_saved_session_state, user_id