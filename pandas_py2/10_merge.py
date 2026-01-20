'''
df_mergerd = pd.merge(df1,df2, on = "col_name", how = "type of Join")
'''

import pandas as pd

df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Ramesh", "Suresh", "Kalpesh"]
})

df2 = pd.DataFrame({
    "ID":[1,2,4],
    "Amount":[1000,2000,3000]
})


df_merged = pd.merge(df1,df2, on = "ID", how = "outer") #inner, left, right

print(df_merged)

"""
df_merged = pd.merge(df1,df2, how = "cross")
"""