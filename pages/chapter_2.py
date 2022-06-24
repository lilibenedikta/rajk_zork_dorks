import os

from collections import defaultdict
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
from flask import send_from_directory
import dash_bootstrap_components as dbc

from session_state import SessionState
import pandas as pd

import dash

dash.register_page(__name__, path="/chapter_two")


edge_data = pd.read_csv("data/RAJK_ZORK_edges.csv").set_index("FROM")
node_data = pd.read_csv("data/RAJK_ZORK_nodes.csv").set_index("NODE_ID")


STATES = defaultdict(SessionState)




layout = html.Div(
    children = [dcc.Markdown(id="situation_2", className="good_text"),
        dcc.RadioItems(id="option_selector_2", className="good_radio", inline=False),
        dbc.Button("Submit", id="submit_gomb_2", n_clicks=0),
        dbc.Button("Befejezés", id = "finish_gomb_2", href="/finish"),
        dbc.Button("2. fejezet", id = "chapter_2_gomb_2", href="/chapter_two_divider"),
        dbc.Button("3. fejezet", id = "chapter_3_gomb_2", href="/chapter_three_divider"),
        dbc.Button("4. fejezet", id = "chapter_4_gomb_2", href="/chapter_four_divider"),
]
)

@callback(
    [
        Output("situation_2", "children"),
        Output("option_selector_2", "options"),
        Output("submit_gomb_2", "style"),
        Output("chapter_2_gomb_2", "style"),
        Output("chapter_3_gomb_2", "style"),
        Output("chapter_4_gomb_2", "style"),
        Output("finish_gomb_2", "style")
    ],
    Input("submit_gomb_2", "n_clicks"),
    [
        State("option_selector_2", "value"),
        State("current_user_id", "value"),
    ],
)
def continue_game(n_clicks, selector_value, session_id):
    sesh = STATES[session_id]
    if n_clicks:
        sesh.decide(selector_value)
    next_text = node_data.loc[sesh.current_state, "TEXT_N"]        

    if sesh.current_state in {
        "T_III_0"
    }:
        next_radio = []
        submit_button_style = {"visibility":"hidden"}
        chapter_2_gomb = {"visibility":"hidden"}
        chapter_3_gomb = {"visibility":"visible"}
        chapter_4_gomb = {"visibility":"hidden"}
        finish_button_style = {"visibility":"hidden"}

    else:
        next_radio = edge_data.loc[sesh.current_state].apply(
            lambda r: dict(label=r["TEXT_E"], value=r["OPTION_NUM"]), axis=1
        )
        submit_button_style = {"visibility":"visible"}
        chapter_2_gomb = {"visibility":"hidden"}
        chapter_3_gomb = {"visibility":"hidden"}
        chapter_4_gomb = {"visibility":"hidden"}
        finish_button_style = {"visibility":"hidden"}
    return next_text, next_radio, submit_button_style, chapter_2_gomb, chapter_3_gomb, chapter_4_gomb, finish_button_style, 