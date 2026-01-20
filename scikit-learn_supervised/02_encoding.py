# Label Encoding
# One-Hot Encoding

from  sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv("sample_data.csv")

df_label = df.copy()

le = LabelEncoder()

df_label["Gender_Encoded"] = le.fit_transform(df_label["Gender"])
df_label["Passed_Encoded"] = le.fit_transform(df_label["Passed"])

print(df_label[["Name", "Gender", "Gender_Encoded","Passed", "Passed_Encoded"]])


df_encoded = pd.get_dummies(df, columns = ["City"], dtype = int)
# if u don't use dtype then result will be boolean


print("\n One-Hot encoding\n")
print(df_encoded)
