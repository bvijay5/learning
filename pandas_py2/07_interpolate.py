'''
df.interpolate(method = "linear", axis = 0(default), inplace = True)
'''

import pandas as pd


data = {
    "Name": ["Vijay","Sourabh", "Krrish", "Saugat", "Devansh"],
    "Age": [18,None,20,19,19],
    "Rollno": [1,None,3,4,5],
}

df = pd.DataFrame(data)

print(df)


#linear, polynomial, time
df.interpolate(method = "linear", inplace = True)
print(df)

'''
df["Value"] = df["Value"].interpolate(method = "linear")
'''