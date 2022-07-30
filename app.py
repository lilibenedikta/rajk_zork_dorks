import os

from collections import defaultdict
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from flask import send_from_directory
import dash_bootstrap_components as dbc

from session_state import SessionState, Starting_SessionState
import pandas as pd

import dash

import boto3

client = boto3.client(
    's3',
    aws_access_key_id = 'AKIASJIEFZIWUUY5K5DG',
    aws_secret_access_key = '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',
    region_name = 'us-east-1'
)

RAJK_ZORK_edges_from_AWS_server = client.get_object(
    Bucket = 'szovegek',
    Key = 'RAJK_ZORK_edges.csv'
)
RAJK_ZORK_nodes_from_AWS_server = client.get_object(
    Bucket = 'szovegek',
    Key = 'RAJK_ZORK_nodes.csv'
)
    
edge_data = pd.read_csv(RAJK_ZORK_edges_from_AWS_server['Body']).set_index("FROM")
node_data = pd.read_csv(RAJK_ZORK_nodes_from_AWS_server['Body']).set_index("NODE_ID")

state = "T_I_1"

STATES = defaultdict(SessionState)


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, "style.css"], use_pages=True)
server = app.server

app.layout = html.Div(
    children = [
        html.Link(href="/assets/style.css", rel="stylesheet"),
        dcc.Dropdown(["A", "B"], value="A", id="initial_user_id"), # ezt ki kell majd törölni, de msot még hibára fut nélküle
        dcc.Markdown(id="display_user_id", className="user_id_text_topright"),
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
