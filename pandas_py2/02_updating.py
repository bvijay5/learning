import pandas as pd

data = {
    "Name": ["Vijay","Sourabh", "Krrish", "Saugat", "Devansh"],
    "Age": [18,19,20,19,19],
}

df = pd.DataFrame(data)

# df.loc[row_idx, "col_name"] = new_value

df.loc[2,"Age"] = 12
df.loc[1,"Age"] = 20

print(df)

# UPDATING ALL ROWS in a Column
# df["Col_name"] = df["Col_name"]*(number)
