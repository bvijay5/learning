import pandas as pd

'''
df.sort_values(by = ["col_name1", "col_name2"], ascending = [True,False], inplace = True)
'''

data = {
    "Name": ["Vijay","Sourabh", "Krrish", "Saugat", "Devansh"],
    "Age": [18,19,20,19,19],
    "Rollno": [1,3,2,5,4],
}

df = pd.DataFrame(data)

df.sort_values(by = "Rollno", ascending=True, inplace = True)

print(df)
