import pandas as pd

data = pd.read_csv("df-manipulation642/test.csv")
print(data["PassengerId"][0])
print(data["PassengerId"].keys())
print(len(data["PassengerId"].keys()))
print(len(data["PassengerId"].index))

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

print(id_from_name("Doyle, Miss. Elizabeth",data))

print(name_from_id(945,data))