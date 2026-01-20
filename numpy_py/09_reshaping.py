import numpy as np


"""
arr.reshape(rows,col) -> It creates a VIEW not copy
"""

# it returns view
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr1 = arr.reshape(4,3)

arr1[0,0] = 5

print(arr1)
print(arr)
