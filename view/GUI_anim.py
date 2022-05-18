import plotly.express as px

from dash import dcc
from dash import dash_table

def build_dropdown_animation(menu_items):
    return dcc.Dropdown(id='dpdn2', value=['Papillon','Josbaig'], multi=True,
                 options=[{'label': x, 'value': x} for x in menu_items])



def init_graph_animation_graph():
    return dcc.Graph(id='my-graph', figure={}, className='six columns')


def build_figure_animation_graph(dff3, attributes):
    #x=year, y=Ntot, z=Station
    x, y, z = attributes
    fig = px.line(data_frame=dff3, x=x, y=y, color=z,
                  custom_data=['Station', 'Mtot', 'oneacorn', 'Altitude'])
    fig.update_traces(mode='lines+markers')
    return fig


def init_graph_animation_pie():
    return dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None,
                  config={
                      'staticPlot': False,     # True, False
                      'scrollZoom': True,      # True, False
                      'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                      'showTips': False,       # True, False
                      'displayModeBar': True,  # True, False, 'hover'
                      'watermark': True,
                      # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                        },
                  className='six columns'
                  )


def build_figure_animation_pie(dff3, attributes):
    
    x, y = attributes 
    fig2 = px.pie(data_frame=dff3, values=x, names=y, title='Ntot for: 2011')
    return fig2
