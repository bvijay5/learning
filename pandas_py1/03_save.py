import pandas as pd

data = {
    "Name": ["Vijay", "Sourabh"],
    "Age": [18,19],
    "City": ["Vizag", "Pune"]
}

df = pd.DataFrame(data)
print(df)

df.to_csv("Output.csv", index=False)