import pandas as pd

"""
fillna(axis = 0/1, inplace =True)
df.fillna()
"""

data = {
    "Name": ["Vijay",None, "Krrish", "Saugat", "Devansh"],
    "Age": [18,None,20,19,19],
    "Rollno": [1,None,3,4,5],
}

'''
df.fillna(0, inplace = True) -> df.fillna(default_val, inplace = True)
'''

df = pd.DataFrame(data)

df["Age"].fillna(df["Age"].mean(), inplace = True)

print(df)
