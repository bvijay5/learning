import pandas as pd

data = pd.read_csv("learning/pandas_py1/sales_data_sample.csv", encoding = "latin1")

print(data.info())