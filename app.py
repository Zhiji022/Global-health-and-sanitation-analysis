# Global health and sanitation Analysis Dashboard
# Author: Zhiji Ding

# built-in modules

import os
import flask
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime

# server
from server import app, server

# dash layouts
from layouts import first_tab, second_tab, third_tab

#############################
# Dash Layout
#############################
app.title = "Global health and sanitation Analysis"

@server.route('/favicon.ico')
def favicon():
    return flask.send_from_directory(os.path.join(server.root_path, 'static'), 'favicon.ico')

app.layout = html.Div([

    html.Img(src = 'assets/E_SDG_logo_No UN Emblem_horizontal_rgb.png', height = '60vh', width = '280vw', style = {'display': 'inline-block', 'padding-bottom': 8}),

    dcc.Tabs(id = 'tabs',
             children = [first_tab.get_tab_layout(),
                         second_tab.get_tab_layout(),
                         third_tab.get_tab_layout(),
                         ],
             style = {'height': '6vh', 'borderBottom': '1px solid #d6d6d6', 'fontWeight': 'bold'}),

    html.Hr(),
    html.Div([f"Copyright © {datetime.now().year}. Created by ",
              html.A("Zhiji Ding", href = "https://www.linkedin.com/in/zhiji-ding-97824610/", target = '_blank')],
    style = {'font-size': '9pt'})
])


#############################################################
# Importing call-back functions
#############################################################
app.config['suppress_callback_exceptions']=True
from callbacks.first_tab import health_expenditure
from callbacks.first_tab import health_risk
from callbacks.first_tab import life_expectancy_map
from callbacks.first_tab import show_country

from callbacks.second_tab import basic_sanitation
from callbacks.second_tab import life_GNI_scatter
from callbacks.second_tab import well_managed_sanitation

from callbacks.third_tab import basic_drinking_water
from callbacks.third_tab import hand_washing
from callbacks.third_tab import open_defecation
from callbacks.third_tab import well_managed_drinking_water



#############################
# Launching the server
#############################
if __name__ == '__main__':
    app.run_server(debug=True)

#############################################################
#############################################################
