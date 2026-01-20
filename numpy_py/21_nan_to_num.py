# np.nan_to_num(arr, nan = value)   ->deafult value is 0


import numpy as np

arr = np.array([1,2,np.nan,4,5,np.nan])

cleaned = np.nan_to_num(arr)
print(cleaned)