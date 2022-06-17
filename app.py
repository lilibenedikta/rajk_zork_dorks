from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

app = Dash(__name__)

colors = {
    'background': '#000000',
    'text': '#39FF14'
}

app.layout = html.Div([
    'Rajk Zork Kaland',
    dcc.Input(
    placeholder='Enter a value...',
    type='text',
    value='',
    style={
            'width': '100%', 
            'height': 200, 
            'font-family':'Courier', 
            'color':colors['text'],
            'backgroundColor': colors['background']}
    ),
    dcc.Textarea(
        id='textarea-state-example',
        value='Textarea content initialized\nwith multiple lines of text',
        style={
            'width': '100%', 
            'height': 200, 
            'font-family':'Courier', 
            'color':colors['text'],
            'backgroundColor': colors['background']},
    ),
    html.Button('Submit', id='textarea-state-example-button', n_clicks=0),
    html.Div(
        id='textarea-state-example-output', 
        style={'whiteSpace': 'pre-line',
               'font-family':'Courier',
               'color':colors['text'],
               'backgroundColor': colors['background']})
])

@app.callback(
    Output('textarea-state-example-output', 'children'),
    Input('textarea-state-example-button', 'n_clicks'),
    State('textarea-state-example', 'value')
)
def update_output(n_clicks, value):
    if n_clicks > 0:
        return 'You have entered: \n{}'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
