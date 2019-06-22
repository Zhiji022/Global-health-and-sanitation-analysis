# module to create callback for open_defecation
from dash.dependencies import Input, Output, State
import sys
from plotly import graph_objs as go
# app server
sys.path.append('../..')
from server import app

# data loaders
from dataloaders.sanitation import sans


#############################################################
# Callback Function
#############################################################

@app.callback(
    Output('open_defecation','figure'),
    [Input('Mortality_map','hoverData')])

def open_defecation(country):
    if country != None:
        sans_country=sans[sans['CODE']==country['points'][0]['location']]
    else:
        sans_country=sans[sans['CODE']=='CHN']
    return {
        'data':[
            go.Scatter(
                x=sans_country['Year'],
                y=sans_country['People practicing open defecation (% of population)'],
                mode = 'lines+markers',
                name= 'Total'
            ),
            go.Scatter(
                x=sans_country['Year'],
                y=sans_country['People practicing open defecation, rural (% of rural population)'],
                mode = 'lines+markers',
                name= 'Rural'
            ),
            go.Scatter(
                x=sans_country['Year'],
                y=sans_country['People practicing open defecation, urban (% of urban population)'],
                mode = 'lines+markers',
                name= 'Urban'
            )
        ],
        'layout': go.Layout(
            title = 'Open defecation',
            xaxis = {'range':[2002,2015],'dtick':2},
            yaxis = {'range':[0,100]},
            legend = {'x': 0,'y': -0.2, 'orientation':"h"},
            margin=go.layout.Margin(
                l=35,
                r=30,
                b=40,
                t=30,
                pad=1)
        )
    }
