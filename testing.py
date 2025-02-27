import pandas as pd

data = pd.read_csv("df-manipulation642/train.csv")
ageid = data.index[data['Age'] >= 60].tolist()
surviveid = data.index[data["Survived"] == 1].tolist()
survived_60 = list(set(ageid) & set(surviveid))


for i in survived_60:
    print(data.iloc[i])