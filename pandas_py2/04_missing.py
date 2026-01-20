import pandas as pd

data = {
    "Name": ["Vijay","Sourabh", "Krrish", "Saugat", "Devansh"],
    "Age": [18,None,20,19,19],
    "Rollno": [1,None,3,4,5],
}

'''
Nan (Not a Number)
None (for object data type)

isnull()
True - Nan is missing
False - Value is missing
'''

df = pd.DataFrame(data)

print(df.isnull())

# To check no. of null values
print(df.isnull().sum())
