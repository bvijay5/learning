import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


miles = pd.DataFrame({"Farthest_run": [50,62,np.nan, 100,26,13,31,50]})

print(miles.isnull().sum())

imp_mean = SimpleImputer(strategy='mean', add_indicator=True)   #adding indicator
print(pd.DataFrame(imp_mean.fit_transform(miles)))

imp_median = SimpleImputer(strategy='median')
print(pd.DataFrame(imp_median.fit_transform(miles)))

imp_mode = SimpleImputer(strategy='most_frequent')
print(pd.DataFrame(imp_mode.fit_transform(miles)))

imp_const = SimpleImputer(strategy='constant', fill_value=5)
print(pd.DataFrame(imp_const.fit_transform(miles)))

