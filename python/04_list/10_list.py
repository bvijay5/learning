# Lists are MUTABLE

eg_list = ["Apple", "Vijay", 5, 5.55, True]
print(eg_list[0])

empt_list = []  #Empty list
print(empt_list)

eg_list[0] = "Avocado"
print(eg_list[0])   #Lists are MUTABLE

# Slicing is similiar to strings: Eg:-
print(eg_list[0][0:3])
print(eg_list[1:4])

