import os
import pickle
import boto3
from collections import defaultdict
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
from flask import send_from_directory
import dash_bootstrap_components as dbc
import pandas as pd
import dash
#from pages.chapter_1 import STATES

dash.register_page(__name__, path="/chapter_two_divider")
AWS_ACCESS_KEY_ID = "9c9aeacb-91e0-4ff4-b422-d80f2fd8e100"
AWS_SECRET_ACCESS_KEY = "GOZK9tCX9BseVfuNPJO8D-0zYfkYIWRtg3higRbSYjf6"
os.environ["AWS_ACCESS_KEY_ID"] = AWS_ACCESS_KEY_ID
os.environ["AWS_SECRET_ACCESS_KEY"] = AWS_SECRET_ACCESS_KEY
bucket = "rajk-zork"
endpoint = "https://s3.eu-de.cloud-object-storage.appdomain.cloud"
s3 = boto3.client("s3", endpoint_url=endpoint)
edge_data = pd.read_csv("data/RAJK_ZORK_edges.csv").set_index("FROM")
node_data = pd.read_csv("data/RAJK_ZORK_nodes.csv").set_index("NODE_ID")

layout = html.Div(
    children = [
        #dcc.Markdown(id="situation_ch_2", className="good_text"),
        html.Link(href="/assets/style.css", rel="stylesheet"),
        html.H1("Gratulálunk, teljesítetted az első fejezetet!", className="centre_text"),
        html.H3("Várnak még rád a tábor további izgalmai. Folytatod a játékot, vagy mentesz és kilépsz?", className="centre_text_5"),
        dbc.Button("Folytatom!", id = "folytatás_gomb", href="/chapter_two", className="centre_button_left"),
        dbc.Button("Mentek és kilépek", id = "mentes_es_kilepes_gomb", href="/gameon", className="centre_button_right")

    ]

    
)

@callback(
    Output("current_user_id", "children"),
    Input("mentes_es_kilepes_gomb", "n_clicks"),
    State("current_user_id", "children")
)
def save_session(n_clicks,user_id):
    if n_clicks:
        STATES = pickle.load(s3.get_object(Bucket = bucket, Key = "all_session_states").read())
        s3.put_object(Bucket=bucket, Key=user_id, Body=pickle.dump(STATES[user_id]))

    return user_id
