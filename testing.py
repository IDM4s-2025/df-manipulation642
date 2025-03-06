import numpy as np
import pandas as pd

table = pd.DataFrame({"Names":["Juan","Diego","Santiago","Fernando","Alonso","Imanol","Alejandra","Kare","Pamela","Elena"],
                      "Age":[15,24,36,14,16,24,25,34,19,31]})

target = 10
length =len([True,False,True])
temp = np.tile(np.array([True,False,True]),(target//length) +1)
print(temp[:target])


