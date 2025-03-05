import pandas as pd

#1
def id_to_name(df: pd.DataFrame, id: int) -> str:
    """Regresa ek nombre del pasajero dado su id

    Args:
        df (pd.DataFrame): El conjuno de datos
        id (int): El id del pasajero

    Returns:
        str: El nombre del pasajero
    """
    return df[df.PassengerId==id].Name.values[0]


#2
def name_to_id(df: pd.DataFrame, name: str) -> int:
    """Regresa el id del pasajero dado su nombre

    Args:
        df (pd.DataFrame): El conjunto de datos
        name (str): El nombre del pasajero

    Returns:
        int: El id del pasajero
    """
    return int(df[df.Name==name].PassengerId.values[0])