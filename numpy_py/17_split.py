import numpy as np

"""
np.split(arr, parts)


np.hsplit()
np.vsplit()
"""

arr = np.array([10,20,30,40,50,60])
print(np.split(arr,3))

arr_2D = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print(np.hsplit(arr_2D, 3))