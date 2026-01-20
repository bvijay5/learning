import os

f = open("Sample.txt", "w")
f.write("MY name is Vijay")
f.close()

f = open("Sample.txt", "r")
data = f.read()

data = data.replace("V", "v")
print(data)

# os.remove("Sample.txt")