import pandas as pd

# Name given an Id
def id_to_name(df: pd.DataFrame, id: int) -> str:
  return df[df.PassengerId == id].Name.iloc[0]

# Id given Name
def name_to_id(df: pd.DataFrame, name: str) -> int:
  return df[df.Name == name].PassengerId.iloc[0]

