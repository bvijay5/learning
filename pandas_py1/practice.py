import pandas as pd

data = {
    "Name": ["Vijay", "Sourabh", "Saugat", "Krrish"],
    "Age": [20,19,18,19]
}

df = pd.DataFrame(data, index = [1,2,3,4])

print(df)

df.to_csv("Output.csv")
