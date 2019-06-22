# module to create callback for health_expenditure

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
    Output('Health expenditure composition','figure'),
    [Input('Life_expentancy_map','hoverData')])

def update_barplot(hoverData):
    if hoverData != None:
        hsys_country=hsys[hsys['CODE']==hoverData['points'][0]['location']]
    else:
        hsys_country=hsys[hsys['CODE']=='CHN']
    return {
    'data': [
        go.Bar(
            x=hsys_country['Year'],
            y=hsys_country['Out-of-pocket expenditure per capita (current US$)'],
            name='Out-of-pocket expenditure per capita'),
        go.Bar(
            x=hsys_country['Year'],
            y=hsys_country['External health expenditure per capita (current US$)'],
            name='External health expenditure per capita'),
        go.Bar(
            x=hsys_country['Year'],
            y=hsys_country['Domestic private health expenditure per capita (current US$)'],
            name='Domestic private health expenditure'),
        go.Bar(
            x=hsys_country['Year'],
            y=hsys_country['Domestic general government health expenditure per capita (current US$)'],
            name='Domestic general government health expenditure per capita')
            ],
    'layout':
        go.Layout(
            barmode='stack',
            title = 'Health Expenditure Composition',

            xaxis = {'range':[1999,2016],'dtick':2},
            yaxis = {'title': 'Health Expenditure (US$)'},
            legend = {'x': 0,
                    'y': -0.3}
        )
    }
