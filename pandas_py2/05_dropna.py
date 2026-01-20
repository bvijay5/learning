import pandas as pd

'''
axis = 0(rows)
axis = 1(col)
df.dropna(axis = 0, inplace = True)
'''

data = {
    "Name": ["Vijay",None, "Krrish", "Saugat", "Devansh"],
    "Age": [18,None,20,19,19],
    "Rollno": [1,None,3,4,5],
}

df = pd.DataFrame(data)

df.dropna(axis = 0,inplace = True)
print("\n")
print(df)