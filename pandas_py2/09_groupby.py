import pandas as pd

data = {
    "Name": ["Vijay","Sourabh", "Krrish", "Saugat", "Devansh"],
    "Age": [18,18,18,19,19],
    "Marks": [10,10,9,9,10],
}

df = pd.DataFrame(data)

print(df.groupby("Age")["Marks"].sum())

print(df.groupby(["Age", "Name"])["Marks"].mean())