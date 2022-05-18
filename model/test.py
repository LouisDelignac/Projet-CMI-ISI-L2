import dash  # use Dash version 1.16.0 or higher for this app to work
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd


df = pd.read_csv('model/data.csv', sep=';')
#dff = df[['Station', 'Year', 'Ntot', 'Mtot']]
#df_agreg = dff[['Station', 'Year', 'Ntot', 'Mtot']].groupby(by=['Station', 'Year']).sum()
#print(df_agreg)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Dropdown(id='dpdn2', value=['Papillon','Josbaig'], multi=True,
                 options=[{'label': x, 'value': x} for x in
                          df.Station.unique()]),
    html.Div([
        dcc.Graph(id='pie-graph', figure={}, className='six columns'),
        dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None, # I assigned None for tutorial purposes. By defualt, these are None, unless you specify otherwise.
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
    ])
])


@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='dpdn2', component_property='value'),
)
def update_graph(country_chosen):
    dff2 = df[df.Station.isin(country_chosen)]
    fig = px.line(data_frame=dff2, x='Year', y='Ntot', color='Station',
                  custom_data=['Station', 'Mtot', 'oneacorn', 'Altitude'])
    fig.update_traces(mode='lines+markers')
    return fig


# Dash version 1.16.0 or higher
@app.callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id='my-graph', component_property='hoverData'),
    Input(component_id='my-graph', component_property='clickData'),
    Input(component_id='my-graph', component_property='selectedData'),
    Input(component_id='dpdn2', component_property='value')
)
def update_side_graph(hov_data, clk_data, slct_data, country_chosen):
    if hov_data is None:
        dff3 = df[df.Station.isin(country_chosen)]
        print(dff3)
        dff3 = dff3[dff3.Station == 2011]
        print(dff3)
        fig2 = px.pie(data_frame=dff3, values='Mtot', names='Station',
                      title='Population for 2011')
        return fig2
    else:
        #print(f'hover data: {hov_data}')
        # print(hov_data['points'][0]['customdata'][0])
        # print(f'click data: {clk_data}')
        # print(f'selected data: {slct_data}')
        dff3 = df[df.Station.isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff3 = dff3[dff3.Year == hov_year]
        fig2 = px.pie(data_frame=dff3, values='Mtot', names='Station', title=f'Population for: {hov_year}')
        return fig2


if __name__ == '__main__':
    app.run_server()

