# module to create callback for Life_expentancy_map

from dash.dependencies import Input, Output, State
import sys
from plotly import graph_objs as go
# app server
sys.path.append('../..')
from server import app

# data loaders
from dataloaders.health_system import hsys
from dataloaders.country_codes import codes

#############################################################
# Callback Function
#############################################################


@app.callback(
    Output('Life_expentancy_map','figure'),
    [Input('radio_items','value'),
    Input('radio_items','labelClassName'),
    Input('slider_year','value')])

def update_choropleth(radio,label, year):
    hsys_subset=hsys[hsys['Year']== year]
    if radio == 'Current health expenditure per capita (current US$)':
        csl = [[0, 'rgb(240,255,255)'],
            [0.03, 'rgb(229,245,224)'],
            [0.07, 'rgb(199,233,192)'],
            [0.1, 'rgb(161,217,155)'],
            [0.125, 'rgb(116,196,118)'],
            [0.15, 'rgb(65,171,93)'],
            [0.18, 'rgb(35,139,69)'],
            [1, 'rgb(0,0,255)'],
            ]


    else:
        csl = 'Reds'


    return {
        'data': [
            go.Choropleth(
                locations=hsys_subset['CODE'],
                z = hsys_subset[radio],
                text = hsys_subset['Country Name'],
                autocolorscale = False,
                colorscale = csl,
                hoverinfo = 'text+z',
                hoverlabel= {
                    'bgcolor': '#e377c2'
                    },
                colorbar = go.choropleth.ColorBar(
                    len=1,
                    thickness=15,
                    title = label,
                    x = 1.01,
                    ),
                    )],
        'layout': go.Layout(
            autosize=False,
            width=1200,
            height=600,
            margin=go.layout.Margin(
                l=0,
                r=0,
                b=10,
                t=30,
                pad=1),
            geo = go.layout.Geo(
                showframe = False,
                showcoastlines = True,
                showocean= True,
                oceancolor = 'rgb(153,204,255)',
                projection = go.layout.geo.Projection(
                    type = 'robinson'),
                        ),
                hovermode = 'closest'
            ),
    }
