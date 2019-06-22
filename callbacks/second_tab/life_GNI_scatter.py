# module to create callback for life_GNI_scatter
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
    Output('life_GNI_scatter','figure'),
    [Input('slider_year2','value')])

def update_life_GNI(year):
    gen_subset=gen[gen['Year']== year]

    return {
        'data':[
            go.Scatter(
                x=gen_subset['GNI per capita, Atlas method (current US$)'],
                y=gen_subset['Life expectancy at birth, total (years)'],
                text = gen_subset['Country Name'].map(str),
                hoverinfo = 'text',
                hoverlabel= {
                    'bgcolor': '#e377c2'
                    },

                mode = 'markers',
                marker = {
                    'size' : 10,
                    'color' : '#17becf',
                    'line' : {'width': 1}
                    }
                )],
        'layout' : go.Layout(
            title = 'World Health and Wealth',
            xaxis = {'title':'GNI per capita (US$)','range':[0,90000]},
            yaxis = {'title': 'Life expentancy (years)', 'range':[45,90]},
            hovermode = 'closest',
            margin=go.layout.Margin(
                l=75,
                r=50,
                b=50,
                t=50,
                pad=4
                ),
        )
    }
