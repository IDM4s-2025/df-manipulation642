import pandas as pd

def name_on_id(id: int, dataframe: pd.DataFrame) -> str: 
    """"" Regresa el nombre de un pasajero en base a su id

    Args:
        id (int): Id del pasajero
        dataframe (pd.DataFrame): Dataframe que se va a usar

    Returns:
        str: nombre del pasajero
    """
    name = dataframe.loc[dataframe["PassengerId"] == id, "Name"].astype(str).values[0]

    return name

def id_on_name(name: str, dataframe: pd.DataFrame) -> int:
     """"" Regresa el id de un pasajero en base a su nombre

    Args:
        nombre (str): nombre del pasajero
        dataframe (pd.DataFrame): Dataframe que se va a usar

    Returns:
        int: id del pasajero
    """
     id = dataframe.loc[dataframe["Name"] == name, "PassengerId"].astype(int).values[0]
     return id

if __name__ == '__main__':
     print("Hello")