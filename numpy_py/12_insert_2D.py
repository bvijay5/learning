import numpy as np

"""
np.insert(array,index,value, asix = None)
array - orignal array
index - 
value -
asix = None (then value is inserted into flattend array)
asix = 0 (row)
asix = 1 (column)

array size is fixed
it creates another array and makes changes(insert) in it
"""

arr = np.array([[1,2],[3,4]])
print(arr)
new_arr = np.insert(arr,1,(7,5),axis = 1)
print(new_arr)
