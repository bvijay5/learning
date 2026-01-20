import numpy as np

# # .shape        -> to know the structure of array (row, column)
# arr_2d = np.array([[1,2,3],
#                   [4,5,6]])

# print(arr_2d.shape)     #(2,3)

# # .size         -> to know size of array(total elements)
# print(arr_2d.size)      # 6

# # .ndim         -> to know number of dimensions
# print(arr_2d.ndim)      # 2

# # .dtype        -> to know the type of data stored in array
# print(arr_2d.dtype)     # int64

# .astype       -> to change the data type of a variable
arr = np.array([1.1,2.6,3.5])
print(arr.dtype)
arr_int = arr.astype(int)
print(arr_int)
