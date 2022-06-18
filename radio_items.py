from dash import Dash, dcc, html, Input, Output, State
from matplotlib.pyplot import axis

# from player import Player
import pandas as pd

edge_data = pd.read_csv("data/RAJK_ZORK_edges.csv").set_index("FROM")
node_data = pd.read_csv("data/RAJK_ZORK_nodes.csv").set_index("NODE_ID")
state = "T_I_1"

app = Dash(__name__, prevent_initial_callbacks=True)

app.layout = html.Div(
    children=[
        html.Button("start", id="start"),
        html.H4(id="situation"),
        dcc.RadioItems(id="option_selector"),
    ]
)


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
