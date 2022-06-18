import os

from collections import defaultdict
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from flask import send_from_directory
import dash_bootstrap_components as dbc

from session_state import SessionState as sesh
import pandas as pd

edge_data = pd.read_csv("data/RAJK_ZORK_edges.csv").set_index("FROM")
node_data = pd.read_csv("data/RAJK_ZORK_nodes.csv").set_index("NODE_ID")
state = "T_I_1"

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, "style.css"],prevent_initial_callbacks=True)
server = app.server

app.layout = html.Div(
    children=[
        html.Link(href="/assets/style.css", rel="stylesheet"),
        dcc.Dropdown(["A", "B"], value="A", id="session-id"),
        html.Button("start", id="start"),
        html.H4(id="situation", className="good-text"),
        dcc.RadioItems(id="option_selector", className="good-text", inline=False),
        dbc.Button("Submit", id="submit_gomb", n_clicks=0),
        html.H4(id="situation_2", className="good-text"),
        dcc.RadioItems(id="option_selector_2", className="good-text", inline=False),
    ]
)

@app.server.route("/assets/<path:path>")
def static_file(path):
    static_folder = os.path.join(os.getcwd(), "assets")
    return send_from_directory(static_folder, path)

colors = {"background": "#000000", "text": "#39FF14"}

@app.callback(
    [Output("situation", "children"), Output("option_selector", "options")],
    Input("start", "n_clicks"),
)
def start_game(n_clicks):
    if n_clicks:
        return node_data.loc[state, "TEXT_N"], edge_data.loc[state].apply(
            lambda r: dict(label=r["TEXT_E"], value=r["EDGE_ID"]), axis=1
        )


if __name__ == "__main__":
    app.run_server(debug=True)
