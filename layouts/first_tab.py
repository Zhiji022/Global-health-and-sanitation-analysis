# layout for the first tab of the dashboard

# built-in modules
import dash_table
import dash_core_components as dcc
import dash_html_components as html

# configs
from configs.DashConfigs import graph_config_style, selected_tab_style

# dataloaders
from dataloaders.health_system import hsys
from dataloaders.country_codes import codes


#############################################################
# Data Preparation
#############################################################




#############################
# Layout Functions
#############################
def get_tab_layout():
    return dcc.Tab(label = "Health Expenditures",
                   children = [
                html.Div([
                   html.Div([
                       html.H1(children="World Health Expenditures and Risks"),
                       dcc.RadioItems(
                           id='radio_items',
                           options=[
                               {'label': 'Life expentancy (year)', 'value': 'Life expectancy at birth, total (years)'},
                               {'label': 'Total health expenditure per capita (US$)', 'value': 'Current health expenditure per capita (current US$)'}
                           ],
                           value = 'Life expectancy at birth, total (years)',
                           labelStyle={'display': 'inline-block'},
                           ),
                       dcc.Graph(
                           id='Life_expentancy_map',
                           figure={
                           })
                           ,


                       html.Div([
                           dcc.Slider(
                               id='slider_year',
                               min=2000,
                               max=2015,
                               marks={
                                   2000: '2000', 2002: '2002', 2004: '2004', 2006: '2006',2008: '2008', 2010: '2010', 2012: '2012', 2014: '2014', 2015: '2015'
                                   },
                               value=2015,
                           ),
                           ], className='ten columns'),
                       html.P(" .  "),
                       html.H3(
                           id='show_country'
                       ),
                       ]),
               html.Div([
                   html.Div([
                       dcc.Graph(
                           id='Health expenditure composition',
                           style = {'width':'49vw','height':'70vh','float':'top'},
                           figure={
                           }
                       )
                       ], style= {'display': 'inline-block'}),

                    html.Div([
                        dcc.Graph(
                            id='Risks of shortage in health expenditures',
                            style = {'width':'49vw','height':'70vh','float':'top'},
                            figure={
                               }
                           )
                       ], style= {'display': 'inline-block'})
                           ], style= {'display': 'inline-block'})



    ])
    ])
