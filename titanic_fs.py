import pandas as pd

def name_to_ID(Name: str, df:pd.DataFrame) -> int:
    """Funcion que cabia el nombre del pasajero por su ID. 

    Args:
        Name (str): Nombre del Pasajero
        df (pd.DataFrame): Data Frame

    Returns:
        int: Id del pasajero
    """
    Id = df[df.Name == Name]. PassengerId

    return Id

name_to_ID('Braund, Mr. Owen Harris', titanic)