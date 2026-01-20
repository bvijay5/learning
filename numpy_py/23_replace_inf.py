# np.nan_to_num(arr, posinf = value, neginf = value)


import numpy as np

arr = np.array([1,np.inf,4,5,-np.inf,6])

cleaned = np.nan_to_num(arr, posinf = 1000, neginf =-1000)
print(cleaned)