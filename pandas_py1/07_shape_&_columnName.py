"""
1- how big is ur data
2- what are the names of column
"""

import pandas as pd

data = {
    "Name": ["Vijay","Sourabh", "Krrish", "Saugat", "Devansh"],
    "Age": [18,19,20,19,19],
    "Marsk": [100,99,98,97,96]
}

df = pd.DataFrame(data)

df1 = pd.read_csv("learning/pandas_py1/sales_data_sample.csv", encoding = "latin1")

print(df)
print(f"Size of DF is: {df.shape}")
print(f"Columns: {df.columns}")
