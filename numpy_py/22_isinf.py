# to check if any value is infinite
# np.isinf(arr)


import numpy as np

arr = np.array([1,np.inf,4,5,-np.inf,6])

print(np.isinf(arr))