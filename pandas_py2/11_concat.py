'''
pd.concat([df1,df2,df3], axis = 0(default), ignore_index = True)
'''
import pandas as pd


df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Ramesh", "Suresh", "Kalpesh"]
})

df2 = pd.DataFrame({
    "ID":[4,5,6],
    "Name":["Baburao", "Shyam", "Raju"]
})

print(pd.concat([df1,df2], ignore_index = True))
