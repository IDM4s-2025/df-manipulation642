import pandas as pd

# 1. Create a function that returns the name of a passenger given their PassengerId.
def id_to_name(df: pd.DataFrame, id:int) -> str:
    """Regresa el nombre del pasajero dado su ID

    Args:
        df (pd.DataFrame): Conjunto de datos
        id (int): ID del pasajero

    Returns:
        str: El nombre del pasajero
    """
    name = df.loc[df.PassengerId == id, 'Name']
    valor_n = str(name)
    return valor_n

# 2. Create a function that returns the PassengerId of a passenger given their Name.
def name_to_id(df: pd.DataFrame, name:str) -> int:
    """Regresa el ID del pasajero dado su nombre

    Args:
        df (pd.DataFrame): Conjunto de datos
        id (str): Nombre del pasajero

    Returns:
        int: El ID del pasajero
    """
    id_pass = df.loc[df.Name == name, 'PassengerId']
    valor_id = int(id_pass.iloc[0])
    return valor_id
