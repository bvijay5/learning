#head() shows top 5(default) rows
#tail()

import pandas as pd

data = pd.read_csv("learning/pandas_py/sales_data_sample.csv", encoding ="latin1")

print(data.head(10))