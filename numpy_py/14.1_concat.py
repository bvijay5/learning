import numpy as np

"""
np.concatinate((arr1,arr2),axis=0)
axis = 0 - row
axis = 1 - column
"""

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 6],
                 [7, 8]])

# Concatenate side by side (along columns)
new_arr = np.concatenate((arr1, arr2), axis=0)
print(new_arr)