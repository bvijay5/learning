# Sample Dictionary
student = {"name": "Vijay", "age": 18, "course": "CSE"}

# len() – number of items in dictionary
print(len(student))  # 3

# dict.get(key, default) – returns value of key, or default if not found
print(student.get("age"))       # 18
print(student.get("grade", "N/A"))  # N/A

# dict.keys() – returns all keys
print(student.keys())  # dict_keys(['name', 'age', 'course'])

# dict.values() – returns all values
print(student.values())  # dict_values(['Vijay', 18, 'CSE'])

# dict.items() – returns list of key-value pairs as tuples
print(student.items())  
# dict_items([('name', 'Vijay'), ('age', 18), ('course', 'CSE')])

# dict.update(other_dict) – adds/updates dictionary with another dict
student.update({"age": 19, "year": 1})
print(student)  
# {'name': 'Vijay', 'age': 19, 'course': 'CSE', 'year': 1}

# dict.pop(key) – removes key and returns its value
print(student.pop("course"))  # CSE
print(student)  # {'name': 'Vijay', 'age': 19, 'year': 1}

# dict.popitem() – removes last inserted key-value pair
print(student.popitem())  # ('year', 1)
print(student)  # {'name': 'Vijay', 'age': 19}

# del dict[key] – removes a key-value pair
del student["age"]
print(student)  # {'name': 'Vijay'}

# dict.clear() – removes all items
student.clear()
print(student)  # {}
