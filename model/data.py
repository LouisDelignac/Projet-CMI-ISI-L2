import pandas as pd

df = pd.read_csv('model/data.csv', sep=';')
select_column = 'Valley'



def get_unique_values():
    return df[select_column].unique()

def extract_df(value):
    mask = df[select_column] == value
    df_valley = df[mask]
    # attributes used to specify grouping (and view)
    x_att = 'Year'
    y_att = 'Ntot'
    z_att = 'Station'

    df_agreg = df_valley[[x_att, y_att, z_att]].groupby(by=[x_att, z_att]).sum()
    df_agreg = df_agreg.reset_index()
    return df_agreg, (x_att, y_att, z_att)


def extract_df_pie(value):
    mask = df[select_column] == value
    df_valley = df[mask]
    # ici on fait le mask, pour trier les données par valley
    #on définit les attributs
    x_att = 'Year'
    y_att = 'Mtot'
    z_att = 'Station'

    df_agreg = df_valley[[x_att, y_att, z_att]].groupby(by=[x_att, z_att]).sum()
    df_agreg = df_agreg.reset_index()
    return df_agreg, (x_att, y_att, z_att)

def extract_df_scatter(value):
    mask = df[select_column] == value
    df_valley = df[mask]
    # ici on fait le mask, pour trier les données par valley
    #on définit les attributs
    y_att3 = 'Mtot'
    t_att3 = 'Ntot'
    z_att3 = 'Station'

    df_agreg = df_valley[[y_att3, t_att3, z_att3]].groupby(by=[y_att3, z_att3]).sum() #on fait une somme pour "regrouper" les données, on les trie en les regroupant par stations, Mtot
    df_agreg = df_agreg.reset_index()
    return df_agreg, (y_att3, t_att3, z_att3)  

def extract_df_scatter2():
    # attributes used to specify grouping (and view)
    x_att = 'Year'
    y_att = 'Ntot'
    z_att = 'Station'
    
    df_agreg = df[[x_att, y_att, z_att]].groupby(by=[x_att, z_att]).sum()
    df_agreg = df_agreg.reset_index()
    return df_agreg, (x_att, y_att, z_att)

def extract_df_sunburst():
    # attributes used to specify grouping (and view)
    x_att = 'Year'
    y_att = 'Valley'
    z_att = 'Station'
    v_att = 'Ntot'

    df_agreg = df[[x_att, y_att, z_att, v_att]].groupby(by=[x_att, y_att, z_att]).sum()
    df_agreg = df_agreg.reset_index()
    return df_agreg, (x_att, y_att, z_att, v_att)
