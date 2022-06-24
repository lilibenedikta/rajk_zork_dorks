import os
import pandas as pd
from collections import defaultdict
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
from flask import send_from_directory
import dash_bootstrap_components as dbc
from session_state import SessionState

import dash

edge_data = pd.read_csv("data/RAJK_ZORK_edges.csv").set_index("FROM")
node_data = pd.read_csv("data/RAJK_ZORK_nodes.csv").set_index("NODE_ID")
dash.register_page(__name__, path="")

state = "T_I_1"

STATES = defaultdict(SessionState)

layout = html.Div(
    children = [
        html.Link(href="/assets/style.css", rel="stylesheet"),
        html.H1("Sose lesz vége!", className="centre_text"),
        html.H3("Üsd be a neved egy új játékhoz. \
            Ha már rendelkezel mentéssel, akkor pedig folytathatod ugyanonnan.", className="centre_text_5"),
        dcc.Input(id="text_input_small", type="text", placeholder="Enter user ID"),
        dbc.Button("Mehet!", id = "start_gomb", href="/gameon", className="centre_button"),
        dcc.ConfirmDialog(
            id='confirm-saving',
            message='Your data has been saved!',
            displayed=False
        ),
    ]
    
)

@callback(Output('confirm-saving', 'children'),
              Input('start_gomb', 'value'),
              State('text_input_small', 'value'))
def display_confirm(n_clicks, user_id):
    if n_clicks:
        sesh = STATES[user_id]
        sesh.user_id = user_id
        return user_id

#@callback(
 #   Output("current_user_id", "children"),
  #  Input("start_gomb", "n_clicks"),
   # State("text_input_small", "value")
#)
#def store_session_state(n_clicks,user_id):
#    if n_clicks:
#        sesh = STATES[user_id]
#        sesh.user_id = user_id
#        return user_id
                

