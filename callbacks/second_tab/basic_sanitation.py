# module to create callback for basic_sanitation
from dash.dependencies import Input, Output, State
import sys
from plotly import graph_objs as go
# app server
sys.path.append('../..')
from server import app

# data loaders
from dataloaders.gen import gen


#############################################################
# Callback Function
#############################################################

@app.callback(
    Output('basic_sanitation','figure'),
    [Input('life_GNI_scatter','hoverData')])

def basic_sanitation(hoverData):
    if hoverData != None:
        gen_subset1 = gen[gen['Country Name']== hoverData['points'][0]['text']]
    else:
        gen_subset1 = gen[gen['Country Name']== 'China']

    return {
        'data':[
            go.Scatter(
                x=gen_subset1['Year'],
                y=gen_subset1['People using at least basic sanitation services (% of population)'],
                mode = 'lines+markers',
                name= 'Total'
            ),
            go.Scatter(
                x=gen_subset1['Year'],
                y=gen_subset1['People using at least basic sanitation services, rural (% of rural population)'],
                mode = 'lines+markers',
                name= 'Rural'
            ),
            go.Scatter(
                x=gen_subset1['Year'],
                y=gen_subset1.iloc[:,6],
                mode = 'lines+markers',
                name= 'Urban'
                )
                ],
        'layout': go.Layout(
            title = 'People using basic sanitation services',
            xaxis = {'range':[2002,2016],'dtick':2},
            yaxis = {'title': '% of population', 'range':[0,100]},
            legend = {'x': 0,'y': -0.1, 'orientation':"h"},
            margin=go.layout.Margin(
                l=50,
                r=50,
                b=50,
                t=50,
                pad=4
                ),
            )

    }
