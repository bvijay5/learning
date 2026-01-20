import numpy as np

"""
np.insert(array,index,value, axis = None)
array - orignal array
index - 
value -
asix = None (then value is inserted into flattend array)
axis = 0 (row)
axis = 1 (column)

array size is fixed
it creates another array and makes changes(insert) in it
"""

arr = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
print(arr)
new_arr = np.insert(arr,2,5,axis = 0)
print(new_arr)
