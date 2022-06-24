import os
import boto3
import pickle
from collections import defaultdict
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
from flask import send_from_directory
import dash_bootstrap_components as dbc

from session_state import SessionState
import pandas as pd

import dash

dash.register_page(__name__, path="/gameon")

AWS_ACCESS_KEY_ID = "9c9aeacb-91e0-4ff4-b422-d80f2fd8e100"
AWS_SECRET_ACCESS_KEY = "GOZK9tCX9BseVfuNPJO8D-0zYfkYIWRtg3higRbSYjf6"
os.environ["AWS_ACCESS_KEY_ID"] = AWS_ACCESS_KEY_ID
os.environ["AWS_SECRET_ACCESS_KEY"] = AWS_SECRET_ACCESS_KEY
bucket = "rajk-zork"
endpoint = "https://s3.eu-de.cloud-object-storage.appdomain.cloud"
s3 = boto3.client("s3", endpoint_url=endpoint)


edge_data = pd.read_csv("data/RAJK_ZORK_edges.csv").set_index("FROM")
node_data = pd.read_csv("data/RAJK_ZORK_nodes.csv").set_index("NODE_ID")

state = "T_I_1"

STATES = defaultdict(SessionState)



key='all_session_states'
pickle_byte_obj = pickle.dumps(STATES) 
s3_resource = boto3.resource('s3')


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
        State("current_user_id", "value"),
    ],
)
def continue_game(n_clicks, selector_value, session_id):
    sesh = STATES[session_id]
    if n_clicks:
        sesh.decide(selector_value)
    next_text = node_data.loc[sesh.current_state, "TEXT_N"]

    if sesh.current_state in {
        "T_I_11111_11",
        "T_I_11112_212",
        "T_I_11112_214",
        "T_I_11112_2113",
        "T_I_11112_2111",
        "T_I_11112_22",
        "T_I_11111_422",
        "T_I_11112_2112",
        "T_I_11111_423"#,
        #"T_I_11111_421"

    }:
        next_radio = []
        submit_button_style = {"visibility":"hidden"}
        chapter_2_gomb = {"visibility":"visible"}
        chapter_3_gomb = {"visibility":"hidden"}
        chapter_4_gomb = {"visibility":"hidden"}
        finish_button_style = {"visibility":"hidden"}
        #s3_resource.Object(bucket,key).put(Body=pickle_byte_obj)
        #s3.put_object(Bucket=bucket, Key="all_session_states", Body=pickle.dump(STATES, open(".p", "wb")))
        s3.put_object(Bucket=bucket, Key="all_session_states", Body=pickle_byte_obj)
        
        # ITT EL KELL MENTENI A SESSIONSTATE-ET (SESH-T)  !!!!!!!!!!!!
 
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