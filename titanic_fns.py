import pandas as pd

def name_from_id(id:int,table:pd.DataFrame)->str:
    """Nombre del pasajero.

    Args:
        id(int): numero id del pasajero.
        table(pandas.DataFrame): archivo csv cargado desde pandas.
    
    Return:
        str: Nombre del pasajero del pasajero.
    
    """
    in_num = table["PassengerId"][0]
    fin_num = table["PassengerId"][len(table["PassengerId"].index)-1]
    if ((id>=in_num) and (id<=fin_num)):
        row = id-in_num
        return table["Name"][row]
    else:
        return "id out of range."

def id_from_name(name:str,table:pd.DataFrame)->int:
    """Id del pasajero.

    Args:
        name(str): nombre completo y exacto del pasajero.
        table(pandas.DataFrame): archivo csv cargado desde pandas.
    
    Return:
        int: Numero identificador del pasajero.
    
    """
    for i in range(len(table["Name"].index)):
        if (name == table["Name"][i]):
            return int(table["PassengerId"][i])
    return -1

def porsentage_survived(table:pd.DataFrame,bool_list:pd.Series = pd.Series())->float:
    """Porsentaje de sobrevivientes de un subgrupo.

    Args:
        table(pandas.DataFrame): archivo csv cargado desde pandas.
        bool_list(pandas.Series): Serie booleana de pandas que define que elementos son parte del subset y que elementos no.
    
    Return:
        float: Porcentaje de sobrevivientes.

    """
    subset = table[bool_list.values]