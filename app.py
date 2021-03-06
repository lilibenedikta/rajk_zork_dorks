import os

from collections import defaultdict
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from flask import send_from_directory
import dash_bootstrap_components as dbc

from session_state import SessionState
import pandas as pd

import dash


edge_data = pd.read_csv("data/RAJK_ZORK_edges.csv").set_index("FROM")
node_data = pd.read_csv("data/RAJK_ZORK_nodes.csv").set_index("NODE_ID")

state = "T_I_1"

STATES = defaultdict(SessionState)


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, "style.css"], use_pages=True)
server = app.server

app.layout = html.Div(
    children = [
        html.Link(href="/assets/style.css", rel="stylesheet"),
        dcc.Dropdown(["A", "B"], value="A", id="initial_user_id"),
        dcc.Markdown(id="user_id", className="user_id_text_topright"),
        dash.page_container,
    ]
)


@app.server.route("/assets/<path:path>")
def static_file(path):
    static_folder = os.path.join(os.getcwd(), "assets")
    return send_from_directory(static_folder, path)


colors = {"background": "#000000", "text": "#39FF14"}

if __name__ == "__main__":
    app.run_server(debug=True)
