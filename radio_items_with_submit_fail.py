from dash import Dash, dcc, html, Input, Output, State
from matplotlib.pyplot import axis

from session_state import SessionState
import pandas as pd

edge_data = pd.read_csv("data/RAJK_ZORK_edges.csv").set_index("FROM")
node_data = pd.read_csv("data/RAJK_ZORK_nodes.csv").set_index("NODE_ID")
starting_state = "T_I_1"
state=starting_state

app = Dash(__name__, prevent_initial_callbacks=True)

app.layout = html.Div(
    children=[
        html.Button("start", id="start"),
        html.H4(id="situation"),
        dcc.RadioItems(id="option_selector"),
        html.P(id="next_choice"),
        html.Button("submit", id="submit"),
        html.H4(id="situation_2"),
        dcc.RadioItems(id="option_selector_2"),
    ]
)



@app.callback(
    [Output("situation", "children"), Output("option_selector", "options"), Output("next_choice", "children")],
    Input("start", "n_clicks"),
)
def start_game(n_clicks):
    if n_clicks:
        return node_data.loc[state, "TEXT_N"], edge_data.loc[state].apply(
            lambda r: dict(label=r["TEXT_E"], value=r["EDGE_ID"]), axis=1
        ), 

@app.callback(
    [Output("situation_2", "children"), Output("option_selector_2", "options")],
    Input("submit", "n_clicks"),
)
def continue_game(n_clicks):
    if n_clicks:
        return node_data.loc[state, "TEXT_N"], edge_data.loc[state].apply(
            lambda r: dict(label=r["TEXT_E"], value=r["EDGE_ID"]), axis=1
        )


if __name__ == "__main__":
    app.run_server(debug=True)
