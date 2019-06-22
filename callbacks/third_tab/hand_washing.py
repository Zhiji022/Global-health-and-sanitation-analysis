# module to create callback for hand_washing
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
    Output('hand_washing','figure'),
    [Input('Mortality_map','hoverData')])

def hand_washing(country):
    if country != None:
        sans_country=sans[sans['CODE']==country['points'][0]['location']]
    else:
        sans_country=sans[sans['CODE']=='CHN']
    return {
        'data':[
            go.Scatter(
                x=sans_country['Year'],
                y=sans_country['People with basic handwashing facilities including soap and water (% of population)'],
                mode = 'lines+markers',
                name= 'Total'
            ),
            go.Scatter(
                x=sans_country['Year'],
                y=sans_country['People with basic handwashing facilities including soap and water, rural (% of rural population)'],
                mode = 'lines+markers',
                name= 'Rural'
            ),
            go.Scatter(
                x=sans_country['Year'],
                y=sans_country['People with basic handwashing facilities including soap and water, urban (% of urban population)'],
                mode = 'lines+markers',
                name= 'Urban'
            )
        ],
        'layout': go.Layout(
            title = 'Handwashing facilities',
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
