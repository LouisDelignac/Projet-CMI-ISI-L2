import dash  # use Dash version 1.16.0 or higher for this app to work
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px

df = pd.read_csv('data.csv', sep=';')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    dcc.Dropdown(id='dpdn2', value= ['Josbaig'], multi=True,
                 options=[{'label': x, 'value': x} for x in
                          df['Station'].unique()]),
    html.Div([
        dcc.Graph(id='pie-graph'),
        dcc.Graph(id='my-graph')
    ])
])


@app.callback(
    Output('my-graph', 'figure'),
    Input('dpdn2', 'value'),
)
def update_graph(value):
    print(value)
    mask = df['Station'] == value
    dff = df[mask]
    print(dff)
    fig = px.line(dff, x='Year', y='Ntot', color='Station')
    #fig.update_traces(mode='lines+markers')
    return fig


# Dash version 1.16.0 or higher
@app.callback(
    Output('pie-graph', 'figure'),
    Input('my-graph', 'hoverData'),
    Input('my-graph', 'clickData'),
    Input('my-graph', 'selectedData'),
    Input('dpdn2', 'value')
)
def update_side_graph(hov_data, clk_data, slct_data, value):
    if hov_data is None:
        dff2 = df[df['Station']==value]
        dff2 = dff2[dff2['Year'] == 2011]
        #print(dff2)
        fig2 = px.pie(dff2, values='Mtot', names='Station',
                      title='Mtot for 2011')
        return fig2
    else:
        # print(f'hover data: {hov_data}')
        # print(hov_data['points'][0]['customdata'][0])
        # print(f'click data: {clk_data}')
        # print(f'selected data: {slct_data}')
        dff2 = df[df['Station']==value]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2['Year'] == hov_year]
        fig2 = px.pie(dff2, values='Mtot', names='Station')
        return fig2


if __name__ == '__main__':
    app.run_server()