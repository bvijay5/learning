import pandas as pd


# reading files in CSV
df = pd.read_csv("learning/pandas_py/sales_data_sample.csv", encoding = "latin1") # utf-8

print(df)

# reading in json
# df = pd.read_json()

# reading in excel
# df = pd.read_excel()
