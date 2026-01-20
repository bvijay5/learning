"""
column = df["column"]
subset = df[["coulmn1", "column2"]]
"""

"""
BASED ON SIGLE CONDITION
filterd_row = df[df["salary"]> 100000]

Combine Multiple conditions
filtered_rows = df[(df["salary"]> 500000) & (df["Age"]>20)]
"""

import pandas as pd


data = {
    "Name": ["Vijay","Sourabh", "Krrish", "Saugat", "Devansh"],
    "Age": [18,19,20,19,19],
    "Marsk": [100,99,98,97,96]
}

df = pd.DataFrame(data)

print(df[["Name", "Age"]])
