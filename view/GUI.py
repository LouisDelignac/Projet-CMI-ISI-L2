import plotly.express as px

from dash import dcc
from dash import dash_table

def build_dropdown_menu(menu_items):
    return dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} for x in menu_items],
        value=menu_items[0],
        clearable=False,
    )

#bar chart
def init_graph_barChart():
    return dcc.Graph(id="bar-chart")

def build_figure_barChart(df, attributes):
    x, y, z = attributes
    fig = px.bar(df, x=x, y=y,
                 color=z, barmode="group")
    return fig

#scatter
def init_graph_scatter():
    # la fonction initialise le graph et crée un ID
    return dcc.Graph(id="scatter_chart")

def build_figure_scatter(df, attributes):
    # la fonction récupère le tableau de données et les noms de colonnes en paramètres
    # et renvoie le graphique à afficher
    # x -> axe des abscisses
    # y -> axe des ordonnées
    # color -> une couleur différente pour chaque élément différent de la colonne
    # size -> taille des points en fonction des valeurs
    x, y, z = attributes
    fig = px.scatter(df, x=x, y=y, color=z, size=y) # création de la figure
    return fig

#sunburst
def init_graph_sunburst():
    # la fonction initialise le graph et crée un ID
    return dcc.Graph(id="sunburst-chart")

def build_figure_sunburst(df, attributes):
    # la fonction récupère le tableau de données et les noms de colonnes en paramètres
    # et renvoie le graphique à afficher
    # path -> les différents "étages" du diagramme
    # values -> valeur affichée lorsque l'on survole une "case" du diagramme
    x, y, z, v = attributes
    fig = px.sunburst(df, path=[x, y, z], values=v) 
    return fig

#table
def data_table(dataframe):
    return dash_table.DataTable(data=dataframe.to_dict('records'),
                                columns=[{"name": i, "id": i} for i in dataframe.columns],
                                page_size=30,
                                sort_action="native",
                                sort_mode="multi",
                                style_data={'whiteSpace': 'normal', 'height': 'auto'},
                                )
