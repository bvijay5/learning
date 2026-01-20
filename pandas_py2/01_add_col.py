import pandas as pd

data = {
    "Name": ["Vijay", "Sourabh", "Arnav", "Harsh"],
    "age": [19,20,20,18],
    "Marks": [80,76,75,72]
}

df = pd.DataFrame(data, index = [i for i in range(1,5)])
df["Percentage"] = df["Marks"]*(100/80)

print(df)

# Using insert fn
# df.insert(loc, "Col_name", data)      -> loc(0 based indexing)

df.insert(3, "CWS", df["Marks"]-10)

print("\n")
print(df)
