import pandas as pd

df = pd.read_csv('model_animation/data.csv', sep=';')
select_column = 'Station'

def get_unique_values2():
    return df[select_column].unique()

def extract_df_animation_graph(value):
    mask = df[select_column] == value
    df_station = df[mask]
    # attributes used to specify grouping (and view)
    x_att = 'Year'
    y_att = 'Ntot'
    z_att = 'Station'

    df_agreg = df_station[[x_att, y_att, z_att]].groupby(by=[z_att, x_att]).sum()
    df_agreg = df_agreg.reset_index()
    return df_agreg, (x_att, y_att, z_att)

def extract_df_animation_pie(value):
    mask = df[select_column] == value
    df_station = df[mask]
    # attributes used to specify grouping (and view)
    x_att = 'Year'
    y_att = 'Ntot'

    df_agreg = df_station[[x_att, y_att]].groupby(by=[x_att]).sum()
    df_agreg = df_agreg.reset_index()
    return df_agreg, (x_att, y_att)

