import pandas as pd

def getPassengerName_byId(df:pd.DataFrame,id: int) -> str:
    """Returns the name of the passenger according to the specified id

    Args:
        df (pd.DataFrame): Dataframe used
        id (int): Id of passenger

    Returns:
        str: A string conaining the name of the passenger
    """
    return df[df.PassengerId == id].Name.iloc[0]

def getPassengerId_byName(df:pd.DataFrame, name: str) -> int:
    """Returns the id of the passenger according to a given name

    Args:
        df (pd.DataFrame): DataFrame used
        name (str): Name of the passenger

    Returns:
        int: Id of the passenger
    """
    return int(df[df.Name == name]["PassengerId"].iloc[0])

def percentage_people_survived(series: pd.Series) -> float:
    """
    Args:
        series (pd.Series): Series of booleans that survived
    Returns:
        float: % of people that survived
    """
    