import numpy as np

"""
arr[start:stop:step]
"""

arr = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
print(arr[1:3])
print(arr[:4])
print(arr[::2])
print(arr[::-1])        # reverses an array