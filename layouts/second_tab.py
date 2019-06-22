# layout for the second tab of the dashboard

# built-in modules
import dash_table
import dash_core_components as dcc
import dash_html_components as html

# configs
from configs.DashConfigs import graph_config_style, selected_tab_style


# dataloaders


#############################################################
# Data Preparation
#############################################################




#############################
# Layout Functions
#############################

def get_tab_layout():
    return dcc.Tab(label = "General Sanitation",
                   children = [

                   html.Div([
                   html.H1(children='Accessibility to Sanitation Services'),
                   html.Div([
                       html.Div([

                               dcc.Graph(
                                   id='life_GNI_scatter',
                                   figure={
                                   },
                                   style = {'width': '68vw','height':550,'float':'left'}
                           )
                           ],style= {'display': 'inline-block'}),
                       html.Div([

                           html.Div([
                               html.Div([
                                   dcc.Graph(
                                   id='basic_sanitation',
                                   style={'padding-left': 0,'padding-right': 0, 'width':'30vw','height':285, 'padding-bottom': 0}
                                   )
                               ]),

                               html.Div([
                                   dcc.Graph(
                                   id='well_managed_sanitation',
                                   style={'padding-left': 0, 'padding-right': 0,'width':'30vw','height':285, 'padding-bottom': 0}
                                   )
                               ])
                           ])

                       ],style= {'display': 'inline-block'})
                       ],style= {'display': 'inline-block'}),
                   html.Div([
                       dcc.Slider(
                           id='slider_year2',
                           min=1970,
                           max=2017,
                           marks={
                               1970: '1970', 1975: '1975',1980: '1980', 1985: '1985', 1990: '1990', 1995: '1995', 2000: '2000',2005:'2005', 2010:'2010',2015:'2015'
                               },
                           value=2016,
                       ),
                   ], className= 'eight columns')

                   ])
                   ])
