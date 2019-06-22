# module to create callback for Life_expentancy_map
from dash.dependencies import Input, Output, State
import sys

# app server
sys.path.append('../..')
from server import app

@app.callback(
    Output('show_country','children'),
    [Input('Life_expentancy_map','hoverData')
    ])

def show_country(hoverData):
    if hoverData == None:
        return 'China'

    return(hoverData['points'][0]['text'])
