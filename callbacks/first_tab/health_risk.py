# module to create callback for health_risk

from dash.dependencies import Input, Output, State
import sys
from plotly import graph_objs as go
# app server
sys.path.append('../..')
from server import app

# data loaders
from dataloaders.health_system import hsys

#############################################################
# Callback Function
#############################################################

@app.callback(
    Output('Risks of shortage in health expenditures','figure'),
    [Input('Life_expentancy_map','hoverData')])

def update_lineplot(hoverData):
    if hoverData != None:
        hsys_country2=hsys[hsys['CODE']==hoverData['points'][0]['location']]
    else:
        hsys_country2=hsys[hsys['CODE']=='CHN']
    return {
        'data':[
            go.Scatter(
                x=hsys_country2['Year'],
                y=hsys_country2['Risk of catastrophic expenditure for surgical care (% of people at risk)'],
                mode = 'lines+markers',
                name= 'Risk of catastrophic expenditure for surgical care'
            ),
            go.Scatter(
                x=hsys_country2['Year'],
                y=hsys_country2['Risk of impoverishing expenditure for surgical care (% of people at risk)'],
                mode = 'lines+markers',
                name= 'Risk of impoverishing expenditure for surgical care'
            )
        ],
        'layout': go.Layout(
            title = 'Risks of shortage in health expenditures',

            xaxis = {'range':[2002,2017],'dtick':2},
            yaxis = {'title': '% of people at risk', 'range':[0,100]},
            legend = {'x': 0,
                    'y': -0.3,
                    'font' : {'size': 14}}
        )
    }
