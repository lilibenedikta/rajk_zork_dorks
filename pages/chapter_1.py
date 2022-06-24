import os

from collections import defaultdict
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
from flask import send_from_directory
import dash_bootstrap_components as dbc

from session_state import SessionState
import pandas as pd

import dash

dash.register_page(__name__, path="/gameon")


edge_data = pd.read_csv("data/RAJK_ZORK_edges.csv").set_index("FROM")
node_data = pd.read_csv("data/RAJK_ZORK_nodes.csv").set_index("NODE_ID")

state = "T_I_1"

STATES = defaultdict(SessionState)



layout = html.Div(
    children = [dcc.Markdown(id="situation", className="good_text"),
        dcc.RadioItems(id="option_selector", className="good_radio", inline=False),
        dbc.Button("Submit", id="submit_gomb", n_clicks=0),
        dbc.Button("Befejezés", id = "finish_gomb", href="/finish"),
        dbc.Button("2. fejezet", id = "chapter_2_gomb", href="/chapter_two_divider"),
        dbc.Button("3. fejezet", id = "chapter_3_gomb", href="/chapter_three_divider"),
        dbc.Button("4. fejezet", id = "chapter_4_gomb", href="/chapter_four_divider"),
]
)


@callback(
    [
        Output("situation", "children"),
        Output("option_selector", "options"),
        Output("submit_gomb", "style"),
        Output("chapter_2_gomb", "style"),
        Output("chapter_3_gomb", "style"),
        Output("chapter_4_gomb", "style"),
        Output("finish_gomb", "style")
    ],
    Input("submit_gomb", "n_clicks"),
    [
        State("option_selector", "value"),
        State("initial_user_id", "value"),
    ],
)
def continue_game(n_clicks, selector_value, session_id):
    sesh = STATES[session_id]
    if n_clicks:
        sesh.decide(selector_value)
    next_text = node_data.loc[sesh.current_state, "TEXT_N"]

    if sesh.current_state in {
        "T_I_11112_2113",
        "T_I_11112_2112",
        "T_I_11112_2111",
        "T_I_11112_214",
        "T_I_11112_22",
        "T_I_11111_423",
        "T_I_11111_422",
        "T_I_11111_421",
        "T_I_11111_11",
    }:
        next_radio = []
        submit_button_style = {"visibility":"hidden"}
        chapter_2_gomb = {"visibility":"visible"}
        chapter_3_gomb = {"visibility":"hidden"}
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