import pandas as pd


data = {
    "Name": ["Vijay","Sourabh", "Krrish", "Saugat", "Devansh"],
    "Age": [18,19,20,19,19],
    "Rollno": [1,2,3,4,5],
}

df = pd.DataFrame(data)

# df.drop(columns = ["Col_name", "Col_name2"], inplace = True)

df.drop(columns=["Age","Rollno"], inplace = True)
print(df)
