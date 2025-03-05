import pandas as pd
tabla=pd.read_csv ('dataaa/train.csv')

tabla
tabla[tabla.PassengerId==1].Name

def id_to_name(df: pd.DataFrame, id:int)->str:
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        id (int): _description_

    Returns:
        str: _description_
    """
    result = df.loc[df["PassengerId"] == id, "Name"]
    return result.iloc[0] 
def name_to_id(df: pd.DataFrame, name: str) -> int:
    result = df.loc[df["Name"] == name, "PassengerId"]
    return result.iloc[0] 

    return "nombre de pasajero"
id_to_name(tabla,1)
nombre = "Montvila, Rev. Juozas"
passengerid = name_to_id(tabla, nombre)
pnombre = id_to_name(tabla, 42)
oldpassenger = tabla.loc[tabla["Age"] == tabla["Age"].max()]

print(f"El ID del pasajero  {nombre} es {passengerid}")
print(f"El pasajero con ID 42 es {pnombre}")
print('El pasajero con más edad es\n')
print(oldpassenger)
