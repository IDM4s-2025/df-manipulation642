def passenger_id(id,df_train):
    name = df_train.loc[df_train["PassengerId"] == id, "Name"].values[0]
    return name
def name_to_id(name,df_train):
    return df_train.loc[df_train["Name"]==name,"PassengerId"].values[0]
def print_id(name,df_train):
    id = name_to_id(name,df_train)
    print(f"The ID of passenger {name} is {id}")
def print_name(id,df_train):
    name = passenger_id(id,df_train)
    print(f"The name of passenger {id} is {name}")
def oldest_person(df_train):
    oldest = df_train.loc[df_train.loc[:,"Age"].idxmax()]
    return oldest
def pregunta_6(df_train):
    df_5 = df_train.loc[:,["Ticket","Fare","Embarked"]]
    df_5.to_csv("data/port_fares.csv",index=False)
    return df_5.head(100)
def counting(df_train):
    df_60 = df_train[(df_train.Age >60) & (df_train.Survived == 1)]
    print(df_60.head(5))
    print(f"Numero de pesronas que sobrevieron: {len(df_60)}")
    print(f"Porcentaje de personas que sobrevivieron mayores a 60 años: {round(len(df_60)/len(df_train[df_train.Age > 60])*100,2)}%")
def pregunta_10(df_train):
    df_wm_children_S = df_train[((df_train.Age <= 15) | (df_train.Sex == "female"))& (df_train.Survived == 1)]
    df_wm_children_NS = df_train[((df_train.Age <= 15) | (df_train.Sex == "female"))& (df_train.Survived == 0)]
    df_wm_children_S.head()
    len(df_wm_children_S)
    len(df_wm_children_NS)
    print(f"La suma total de mujeres y niños eran {len(df_wm_children_S)+len(df_wm_children_NS)}, de los cuales sobrevivieron {len(df_wm_children_S)} y no sobrevivieron {len(df_wm_children_NS)}")
    print(f"El porcentaje sería {round(len(df_wm_children_S)/len(df_wm_children_S+df_wm_children_NS)*100,2)}%")
    df_Ma_S =  df_train[((df_train.Age>=15) &(df_train.Sex == "male"))& (df_train.Survived == 1)]
    df_Ma_NS = df_train[((df_train.Age>=15) &(df_train.Sex == "male"))& (df_train.Survived == 0)]
    df_Ma_S.head()
    len(df_Ma_S)
    len(df_Ma_NS)
    print(f"La suma total de hombres era {len(df_Ma_S)+len(df_Ma_NS)}, de los cuales sobrevivieron {len(df_Ma_S)} y no sobrevivieron {len(df_Ma_NS)}")
    print(f"El porcentaje sería {round(len(df_Ma_S)/len(df_Ma_S+df_Ma_NS)*100,2)}%")
    print("Por lo que se puede intuir que las mujeres y niños tuvieron una mayor tasa de supervivencia que los hombres mayores de 15 años")
def pregunta_11(df_train):
    print(df_train.Age.mean())
def pregunta_12(df_train):
    print(df_train.Embarked.value_counts())
def pregunta_13(df_train):
    surv_14 = df_train.groupby("Survived")["Pclass"].value_counts()
    print(surv_14)
    #print(surv_14.loc[1,3])
    porcentaje3_s = (surv_14.loc[1,3]/(surv_14.loc[1,3]+surv_14.loc[0,3]))*100
    porcentaje2_s = (surv_14.loc[1,2]/(surv_14.loc[1,2]+surv_14.loc[0,2]))*100
    porcentaje1_s = (surv_14.loc[1,1]/(surv_14.loc[1,1]+surv_14.loc[0,1]))*100
    print(f"El porcentaje de la clase 3 de sobrevivientes es: {round(porcentaje3_s,2)}%")
    print(f"El porcentaje de la clase 2 de sobrevivientes es: {round(porcentaje2_s,2)}%")
    print(f"El porcentaje de la clase 1 de sobrevivientes es: {round(porcentaje1_s,2)}%")
def pregunta_boolean(df_train ,boolean):
    surv = df_train[boolean][(df_train.Survived == 1)&(boolean == True)]
    print(f"El porcentaje de sobrevivientes es {round(len(surv)/len(df_train)*100,2)}%")