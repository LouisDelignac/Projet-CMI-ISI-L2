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


def init_graph():
    return dcc.Graph(id="bar-chart")

def build_figure(df, attributes):
    x, y, z = attributes
    fig = px.bar(df, x=x, y=y,
                 color=z, barmode="group")
    return fig

def data_table(dataframe):
    return dash_table.DataTable(data=dataframe.to_dict('records'),
                                columns=[{"name": i, "id": i} for i in dataframe.columns],
                                page_size=30,
                                sort_action="native",
                                sort_mode="multi",
                                style_data={'whiteSpace': 'normal', 'height': 'auto'},
                                )




def init_graph2():
    return dcc.Graph(id="pie-chart")

def build_figure2(df, attributes):
    x, y, z = attributes
    
    fig = px.sunburst(df, path=[z, y], values=x) #le path équivaut au section dans le pie chart
    
    return fig

def init_graph3():
    return dcc.Graph(id="scatter-chart")

def build_figure3(df, attributes):
    y, z, t = attributes
    
    fig = px.scatter(df, x=y, y=t, size=y, color=z, log_x=True, size_max=55) #la couleur permet de distinguer les différentes stations
            #on peut intéragir en appuyant sur les noms des stations, l'échelle change selon les données qui restent
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
