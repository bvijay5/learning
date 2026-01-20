import numpy as np

# 1_D ARRAY
ar_1D = np.array([1,2,3,4,5,6])
print(ar_1D)


# 2_D ARRAY
arr_2D = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print(arr_2D)


# Creating array with default values
zero_arr = np.zeros(2)      # 1D
one_arr = np.ones((2,3))    # 2D
print(zero_arr)
print(one_arr)

five_array = np.full((2,2),5)   # used to create array of default values other than 1 and 0
print(five_array)



# create an array of numbers in sequence
# arange(start, stop, step)
seq = np.arange(1,10,2)     #[1 3 5 7 9]
print(seq)

#creating indentitity Matrix
identity_matrix = np.eye(3)
print(identity_matrix)

