import numpy as np
import pandas as pd




def id_nombre(id: int, df: pd.DataFrame) -> str:
    """
    Devuelve el nombre del pasajero con el id específico.

    Args:
        id (int): id del pasajero.
        df (pd.DataFrame): el data frame de pandas.

    Returns:
        str: el nombre con el id asignado.
    """
    return df.loc[df.PassengerId == id, "Name"].iloc[0]




def nombre_id(nombre: str, df: pd.DataFrame) -> int:
    """Devuelve el nombre dado su id

    Args:
        nombre (str): Nombre del pasajero
        df (pd.DataFrame): Tabla de titanic

    Returns:
        int: Id del pasajero
    """
    return df.loc[df.Name == nombre, "PassengerId"].iloc[0]

