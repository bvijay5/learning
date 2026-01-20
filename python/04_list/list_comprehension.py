# mylist = [1,2,3,4,5]

# """
# lis = [(expression) (for loop) (if condition)]
# """

# b = [i*i for i in mylist]
# print(mylist)
# print(b)


# NESO ACADEMY
names = ["James", "Jhone", "Emmy", "Miechel", "Jimmy"]
j_names = []
for name in names:
    if "J" in name:
        j_names.append(name)

print(j_names)

j1_names = [name for name in names if "J" in name]
print(j1_names)