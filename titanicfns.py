def id_to_name(df, id: int) -> str:
    """_summary_

    Args:
        df (pd.DataFrame): El dataframe de pandas
        id (int): El id del pasajero

    Returns:
        str: Nombre del pasajero
    """
    return df[df.PassengerId == id].Name.values[0]


def name_to_id(df, name: str) -> int:
    """_summary_

    Args:
        df (pd.DataFrame): El dataframe de pandas
        name (str): El nombre del pasajero

    Returns:
        int: El id del pasajero
    """
    return df[df.Name == name].PassengerId.values[0]

if __name__ == '__main__':
    import pandas as pd
    df = pd.read_csv('train.csv')
    print(id_to_name(df, 1))
    print(name_to_id(df, 'Braund, Mr. Owen Harris'))