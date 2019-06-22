# layout for the third tab of the dashboard

# built-in modules
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# configs
from configs.DashConfigs import graph_config_style, selected_tab_style


# dataloaders

from dataloaders.sanitation import mort

#############################################################
# Data Preparation
#############################################################




#############################
# Layout Functions
#############################

def get_tab_layout():
    return dcc.Tab(label = "Detailed Sanitation",
                   children = [

            html.Div([
                   html.H1(children='Health Risks from Unsafe Sanitation'),
                   html.H4(children='Mortality rate attributed to unsafe sanitation (per 100,000 population)'),
                   html.Div([
                       html.Div([
                           dcc.Graph(
                               id='Mortality_map',
                               figure={'data': [
                                   go.Choropleth(
                                       locations=mort['CODE'],
                                       z = mort['Mortality rate attributed to unsafe water, unsafe sanitation and lack of hygiene (per 100,000 population)'],
                                       text = mort['Country Name'],
                                       hoverinfo = 'text+z',
                                       hoverlabel= {
                                           'bgcolor': '#e377c2'
                                           },
                                       autocolorscale = True,
                                       colorbar = go.choropleth.ColorBar(
                                           len=1,
                                           thickness=15,
                                           x = 1.01,
                                           ),
                                           )],
                               'layout': go.Layout(
                                   autosize=False,
                                   width=1350,
                                   height=700,
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
                               }),
                       ], className = 'twelve columns')
                       ]),


                   html.Div([
                       html.Hr(style = {'padding-top': 0, 'padding-bottom': 0}),
                       html.H3(id='show_hoverdata'),

                       html.Div([
                           html.Div([
                               dcc.Graph(
                                   id='basic_drinking_water',
                                   style = {'width':'24vw','height':340,'float':'top'},
                                   figure={
                                   }),
                                   ], style = {'display': 'inline-block'}),
                           html.Div([
                               dcc.Graph(
                                   id='well_managed_drinking_water',
                                   style = {'width':'24vw','height':340,'float':'top'},
                                   figure={
                                   }),
                                   ], style = {'display': 'inline-block'}),
                           html.Div([
                               dcc.Graph(
                                   id='hand_washing',
                                   style = {'width':'24vw','height':340,'float':'top'},
                                   figure={
                                   }),
                                   ], style = {'display': 'inline-block'}),
                           html.Div([
                               dcc.Graph(
                                   id='open_defecation',
                                   style = {'width':'24vw','height':340,'float':'top'},
                                   figure={
                                   }),
                                   ], style = {'display': 'inline-block'})
                       ], style = {'display': 'inline-block'})

               ]),



                   ])
                   ])
