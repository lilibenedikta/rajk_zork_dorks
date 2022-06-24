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

# STATES = defaultdict(SessionState)

app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, "style.css"],
    use_pages=True,
    suppress_callback_exceptions=True,
)
server = app.server

app.layout = html.Div(
    children=[
        html.Link(href="/assets/style.css", rel="stylesheet"),
        # dcc.Dropdown(["A", "B"], value="A", id="initial_user_id"),
        html.A(
            id="current_user_id", className="user_id_text_topright"
        ),  # színt kéne adni neki
        dcc.Markdown(id="user_id", className="user_id_text_topright"),
        dash.page_container,
    ]
)

# USER_IDS = defaultdict(STATES.keys.user_id) ### Ebben nem vagyok annyira magabiztos


@app.server.route("/assets/<path:path>")
def static_file(path):
    static_folder = os.path.join(os.getcwd(), "assets")
    return send_from_directory(static_folder, path)


# @app.callback(
#    Output("initial_user_id", "value"),
#    Input("user_id", "value"),
#    State("initial_user_id", "value")
# )
# def store_session_state(overwrite_initial_user_id,initial_user_id):
#    sesh = STATES[initial_user_id]
#    sesh.user_id = overwrite_initial_user_id

colors = {"background": "#000000", "text": "#39FF14"}

if __name__ == "__main__":
    app.run_server(debug=True)
