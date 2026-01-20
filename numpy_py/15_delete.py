import numpy as np

"""
np.delete(array, index, axis = None)
axis = None (deleteing from flattend array)
"""

arr = np.array([10,20,30,40,50])
new_arr = np.delete(arr, 3,axis = None)
print(new_arr)