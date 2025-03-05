import pandas as pd 


def get_name( df, id):
    return df.loc[df.PassengerId == id, 'Name'].values[0]

def get_id(df, name):
    return df.loc[df.Name == name, 'PassengerId'].values[0]
