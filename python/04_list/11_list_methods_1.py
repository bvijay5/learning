# Sample List
fruits = ["apple", "banana", "cherry", "apple"]

# Length of list
print(len(fruits))  # 4

# list.append(x) – adds element at the end
fruits.append("mango")
print(fruits)  # ['apple', 'banana', 'cherry', 'apple', 'mango']

# list.insert(index, x) – inserts element at specific position
fruits.insert(1, "orange")
print(fruits)  # ['apple', 'orange', 'banana', 'cherry', 'apple', 'mango']

# list.remove(x) – removes first occurrence of element
fruits.remove("apple")
print(fruits)  # ['orange', 'banana', 'cherry', 'apple', 'mango']

# list.pop() – removes and returns last element
print(fruits.pop())  # mango
print(fruits)  # ['orange', 'banana', 'cherry', 'apple']

# list.pop(index) – removes and returns element at index
print(fruits.pop(1))  # banana
print(fruits)  # ['orange', 'cherry', 'apple']

# list.index(x) – returns first index of element
print(fruits.index("apple"))  # 2

# list.count(x) – counts occurrences of element
print(fruits.count("apple"))  # 1

# list.sort() – sorts the list (ascending order)
fruits.sort()
print(fruits)  # ['apple', 'cherry', 'orange']

# list.sort(reverse=True) – sorts in descending order
fruits.sort(reverse=True)
print(fruits)  # ['orange', 'cherry', 'apple']

# list.reverse() – reverses list order
fruits.reverse()
print(fruits)  # ['apple', 'cherry', 'orange']

# list.copy() – returns a shallow copy of list
copy_fruits = fruits.copy()
print(copy_fruits)  # ['apple', 'cherry', 'orange']

# list.clear() – removes all elements
copy_fruits.clear()
print(copy_fruits)  # []
