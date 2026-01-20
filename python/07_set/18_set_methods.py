# Sample sets
fruits = {"apple", "banana", "cherry"}
more_fruits = {"banana", "mango", "orange"}

# len() – number of elements in the set
print(len(fruits))  # 3

# add(x) – adds an element
fruits.add("grape")
print(fruits)  # {'apple', 'banana', 'cherry', 'grape'}

# update(iterable) – adds multiple elements
fruits.update(["kiwi", "pear"])
print(fruits)  # {'apple', 'banana', 'cherry', 'grape', 'kiwi', 'pear'}

# remove(x) – removes element (error if not present)
fruits.remove("banana")
print(fruits)  

# discard(x) – removes element (no error if not present)
fruits.discard("banana")  # safe
print(fruits)

# pop() – removes and returns a random element
print(fruits.pop())  
print(fruits)

# clear() – removes all elements
copy_fruits = fruits.copy()
copy_fruits.clear()
print(copy_fruits)  # set()

#copying
extra_fruits = {"apple", "banana"}
copy_set = extra_fruits.copy()
print(copy_set)  # {'apple', 'banana'}
