# Sample Tuple
fruits = ("apple", "banana", "cherry", "apple")

# Length of tuple
print(len(fruits))  # 4

# Accessing elements (indexing)
print(fruits[0])   # apple
print(fruits[-1])  # apple (last element)

# Slicing
print(fruits[1:3])  # ('banana', 'cherry')

# count(x) – counts how many times x occurs
print(fruits.count("apple"))  # 2

# index(x) – returns the first index of x
print(fruits.index("cherry"))  # 2

# Tuples can contain different data types
mixed = (1, "hello", 3.14, True)
print(mixed)  # (1, 'hello', 3.14, True)

# Nested tuples
nested = ("apple", ("banana", "cherry"))
print(nested[1][0])  # banana

# Tuple unpacking
a, b, c, d = fruits
print(a)  # apple
print(b)  # banana

# Concatenation (joining tuples)
new_fruits = fruits + ("mango", "orange")
print(new_fruits)
# ('apple', 'banana', 'cherry', 'apple', 'mango', 'orange')

# Repetition
print(fruits * 2)
# ('apple', 'banana', 'cherry', 'apple', 'apple', 'banana', 'cherry', 'apple')

# Converting list to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # (1, 2, 3)

# Converting tuple to list (to modify elements)
temp_list = list(fruits)
temp_list.append("grape")
fruits = tuple(temp_list)
print(fruits)  # ('apple', 'banana', 'cherry', 'apple', 'grape')
