import model.data
import view.GUI

import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

server = Flask(name)
app = dash.Dash(name, server = server, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.SKETCHY])

# styling the sidebar
SIDEBAR_STYLE = {
	"position": "fixed",
	"top": 0,
	"left": 0,
	"bottom": 0,
	"width": "16rem",
	"padding": "2rem 1rem",
	"background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
	"margin-left": "18rem",
	"margin-right": "2rem",
	"padding": "2rem 1rem",
}

sidebar = html.Div(
	[
		html.H2("CMI ISI", className="display-4"),
		html.Hr(),
		html.P(
			"Forêt Pyrénnées", className="lead"
		),
		dbc.Nav(
			[
				dbc.NavLink("Histogramme", href="/", active="exact"),
				dbc.NavLink("Tableur", href="/table", active="exact"),
                dbc.NavLink("Pie-chart", href="/pie", active="exact"), #on créé l'url pour afficher le pie-chart
                dbc.NavLink("Graphique", href="/graph", active="exact"), #on créé l'url pour le graphe
                dbc.NavLink("Dispersion", href="/scatter-plot", active="exact"), #Louis
                dbc.NavLink("Diagramme en rayons de soleil", href="/sunburst-chart", active="exact"), #Louis
			],
			vertical=True,
			pills=True,
		),
	],
	style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
	dcc.Location(id="url"),
	sidebar,
	content
])

@app.callback(
	Output("page-content", "children"),
	[Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        dropdown = view.GUI.build_dropdown_menu(model.data.get_unique_values())
        graph = view.GUI.init_graph()
        return [
            html.Div([
                dropdown, graph
                ])
            ]
    elif pathname == "/table":
        # fetch client info
        return [
            html.H1('Données forêt pyrénnées (tableur)', id='table_view',
                    style={'textAlign':'left'}),
            html.Hr(style={'width': '75%', 'align': 'center'}),
            html.Div(id='data_table', children = view.GUI.data_table(model.data.df))
            ]
    
    elif pathname == "/pie":
        # fetch client info"
        dropdown = view.GUI.build_dropdown_menu(model.data.get_unique_values()) #on appelle le dropdown
        graph = view.GUI.init_graph2() #on appelle le graph
        return [
            html.H1('Relation entre la masse et les stations', id='pie_view',
                    style={'textAlign':'left'}),
            html.Hr(style={'width': '75%', 'align': 'center'}),
            html.Div([
                dropdown, graph #on fait apparaître le dropdown et le graphe dans cet ordre
                ])
            ]
    
    elif pathname == "/graph":
        #fetch clinet info
        dropdown = view.GUI.build_dropdown_menu(model.data.get_unique_values()) #on appelle le dropdown
        graph = view.GUI.init_graph3() #on appelle le graph
        return [
            html.H1('Relation entre la masse et le nombre des glands', id='scatter_view',
                    style={'textAlign':'left'}),
            html.Hr(style={'width': '75%', 'align': 'center'}),
            html.Div([
                dropdown, graph #on fait apparaître le dropdown et le graphe dans cet ordre
                ])            
            ]
    
    elif pathname == "/scatter-plot":
        graph = view.GUI.init_graph_scatter() # on initialise le graph
        return [ # on renvoie un code html qui affiche le titre de la page, une
                 # barre de séparation et le graphique
            html.H1('Diagramme de dispersion', id='scatter_view',
		style={'textAlign':'left'}),
            html.Hr(style={'width': '75%', 'align': 'center'}),
            html.Div([
                graph
            ])
        ]
    
    elif pathname == "/sunburst-chart":
        graph = view.GUI.init_graph_sunburst() # on initialise le graph
        return [ # on renvoie un code html qui affiche le titre de la page, une
                 # barre de séparation et le graphique
            html.H1('Diagramme en rayon de soleil', id='sunburst_view',
		style={'textAlign':'left'}),
            html.Hr(style={'width': '75%', 'align': 'center'}),
            html.Div([
                graph
                ])
            ]
            
    
    else:
        return html.Div(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
                ]
            )

@app.callback(
    Output("bar-chart", "figure"),
    [Input("dropdown", "value")])
def update_bar_chart(value):
    sub_df, attributes = model.data.extract_df(value)
    return view.GUI.build_figure(sub_df, attributes)

@app.callback(
    Output("pie-chart", "figure"),
    [Input("dropdown", "value")])
def update_pie_chart(value):
    sub_df, attributes = model.data.extract_df_pie(value)
    return view.GUI.build_figure2(sub_df, attributes) #selon ce qu'on choisi via le dropdown, on change les données

@app.callback(
    Output("scatter-chart", "figure"),
    [Input("dropdown", "value")])
def update_scatter_chart(value):
    sub_df, attributes = model.data.extract_df_scatter(value)
    return view.GUI.build_figure3(sub_df, attributes) #selon ce qu'on choisi via le dropdown, on change les données

@app.callback(
    # le callback s'active lorsqu'on arrive sur l'url correspondant à la figure
    # en renvoyant le pathname à la fonction update
    Output("scatter_chart", "figure"),
    [Input("url", "pathname")])
def update_scatter_plot(pathname):
    # la fonction récupère la variable pathname du callback et met à jour la figure
    sub_df, attributes = model.data.extract_df_scatter2() # on extrait les données
    return view.GUI.build_figure_scatter(sub_df, attributes)


@app.callback(
    # le callback s'active lorsqu'on arrive sur l'url correspondant à la figure
    # en renvoyant le pathname à la fonction update
    Output("sunburst-chart", "figure"),
    [Input("url", "pathname")])
def update__sunburst_chart(pathname):
    # la fonction récupère la variable "pathname" du callback et met à jour la figure
    sub_df, attributes = model.data.extract_df_sunburst() # on extrait les données
    return view.GUI.build_figure_sunburst(sub_df, attributes)


if __name__=='__main__':
	app.run_server()

               
