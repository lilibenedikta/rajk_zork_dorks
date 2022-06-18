import os
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from flask import send_from_directory
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, "style.css"])
server = app.server


@app.server.route("/assets/<path:path>")
def static_file(path):
    static_folder = os.path.join(os.getcwd(), "assets")
    return send_from_directory(static_folder, path)


colors = {"background": "#000000", "text": "#39FF14"}

app.layout = html.Div(
    [
        html.Link(href="/assets/style.css", rel="stylesheet"),
        html.P(id="paragraph-one", className="good-text"),
        html.P(id="paragraph-two", className="good-text"),
        dbc.Button("Submit", id="textarea-state-example-button", n_clicks=0),
        dcc.Input(
            placeholder="Enter a value...", type="text", id="text-input-small", value=""
        ),
        #dcc.Dropdown(["1", "2", "3"], "Choose", id="text-input-small"),
    ]
)

intro = "Eltöprengesz, mi történhetett. Mit csinálsz?"

@app.callback(
    [Output("paragraph-one", "children"), Output("paragraph-two", "children")],
    Input("textarea-state-example-button", "n_clicks"),
    [State("text-input-small", "value"), State("paragraph-two", "children")],
)
def update_output(n_clicks, value, last_para_2):
    if n_clicks > 0:
        return last_para_2, "Ezt választottad: \n{}".format(value)
    return intro, last_para_2


if __name__ == "__main__":
    app.run_server(debug=True)
