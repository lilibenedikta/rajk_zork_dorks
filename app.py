import os

from collections import defaultdict
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from flask import send_from_directory
import dash_bootstrap_components as dbc

from session_state import SessionState
import pandas as pd

edge_data = pd.read_csv("data/RAJK_ZORK_edges.csv").set_index("FROM")
node_data = pd.read_csv("data/RAJK_ZORK_nodes.csv").set_index("NODE_ID")

state = "T_I_1"

STATES = defaultdict(SessionState)


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, "style.css"])
server = app.server

app.layout = html.Div(
    children=[
        html.Link(href="/assets/style.css", rel="stylesheet"),
        dcc.Dropdown(["A", "B"], value="A", id="session-id"),
        dcc.Markdown(id="situation", className="good-text"),
        dcc.RadioItems(id="option_selector", className="good-text", inline=False),
        dbc.Button("Submit", id="submit_gomb", n_clicks=0),
    ]
)


@app.server.route("/assets/<path:path>")
def static_file(path):
    static_folder = os.path.join(os.getcwd(), "assets")
    return send_from_directory(static_folder, path)


colors = {"background": "#000000", "text": "#39FF14"}


@app.callback(
    [
        Output("situation", "children"),
        Output("option_selector", "options"),
        Output("submit_gomb", "children"),
    ],
    Input("submit_gomb", "n_clicks"),
    [
        State("option_selector", "value"),
        State("session-id", "value"),
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
        button_text = "Finish"
    else:
        next_radio = edge_data.loc[sesh.current_state].apply(
            lambda r: dict(label=r["TEXT_E"], value=r["OPTION_NUM"]), axis=1
        )
        button_text = "Submit"
    return next_text, next_radio, button_text

if __name__ == "__main__":
    app.run_server(debug=True)
