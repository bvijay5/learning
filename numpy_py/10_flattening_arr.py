import numpy as np

"""
.ravel() -> views
.flatten() -> copy
"""

arr = np.array([[1,2,3],[4,5,6]])
r = arr.flatten()
r[0] = 99
print(arr)
print(arr.ravel())

print(arr.flatten())

print(arr)