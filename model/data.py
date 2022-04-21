import pandas as pd

import sys

# add your project directory to the sys.path
project_home = '/home/LouisDelignac/mysite'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

df = pd.read_csv(project_home+'/model/Repro_IS.csv', sep=';')
select_column = 'Valley'

def get_unique_values():
    return df[select_column].unique()

def extract_df_barChart(value):
    mask = df[select_column] == value
    df_valley = df[mask]
    # attributes used to specify grouping (and view)
    x_att = 'Year'
    y_att = 'Ntot'
    z_att = 'Station'

    df_agreg = df_valley[[x_att, y_att, z_att]].groupby(by=[x_att, z_att]).sum()
    df_agreg = df_agreg.reset_index()
    return df_agreg, (x_att, y_att, z_att)

def extract_df_scatter():
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