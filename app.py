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

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, "style.css"],prevent_initial_callbacks=True)
server = app.server

option_to_edge_dict = {"option text": "edge_id"}
#from ... import game_graph, edge_df

STATES = defaultdict(SessionState)


@app.server.route("/assets/<path:path>")
def static_file(path):
    static_folder = os.path.join(os.getcwd(), "assets")
    return send_from_directory(static_folder, path)


colors = {"background": "#000000", "text": "#39FF14"}

app.layout = html.Div(
    [
        html.Link(href="/assets/style.css", rel="stylesheet"),
        dcc.Dropdown(["A", "B"], value="A", id="session-id"),
        html.P(id="paragraph-one", className="good-text"),
        html.P(id="paragraph-two", className="good-text"),
        dbc.Button("Submit", id="textarea-state-example-button", n_clicks=0),
        dcc.Input(
            placeholder="Enter a value...", type="text", id="text-input-small", value=""
        ),
        # dcc.Dropdown(["1", "2", "3"], "Choose", id="text-input-small"),
    ]
)

intro = "Eltöprengesz, mi történhetett. Mit csinálsz?"


@app.callback(
    [Output("paragraph-one", "children"), Output("paragraph-two", "children")],
    Input("textarea-state-example-button", "n_clicks"),
    [
        State("text-input-small", "value"),
        State("paragraph-two", "children"),
        State("session-id", "value"),
    ],
)
def update_output(_, text_input_value, current_text_of_para_2, session_id):

    session_state = STATES[session_id]

    next_para_1 = [
        "Paragraph 2 was",
        html.Br(),
        current_text_of_para_2,
        html.Br(),
        "And you entered",
        html.Br(),
        text_input_value,
    ]
    next_para_2 = session_state.proc_input(text_input_value)

    return next_para_1, next_para_2


if __name__ == "__main__":
    app.run_server(debug=True)
