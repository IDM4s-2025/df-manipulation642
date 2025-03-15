import pandas as pd

#1
def id_to_name(df:pd.DataFrame,id: int) -> str:
    passenger_name = df[df.PassengerId == id].Name
    return passenger_name[id-1]

#2
def name_to_id(df:pd.DataFrame,name: str)-> int:
    passenger_id = df[df.Name == name].PassengerId
    return passenger_id.iloc[0]

#3
def print_passenger_id(df: pd.DataFrame, name: str) -> int:
  passenger_id = name_to_id(df, name)
  return print(f'The ID of passenger {name} is {passenger_id}')

#4
def Id_to_name(df: pd.DataFrame, id:int)->str:
    passenger_name=df[df.PassengerId == id].Name
    return print(f'The passenger  with {id} ID is {passenger_name[id-1]}')

#5
def info_old(df:pd.DataFrame)->pd.DataFrame:
    passenger_info = df[df.Age == df.Age.max()]
    return print(passenger_info)
