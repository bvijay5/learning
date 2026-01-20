def my_generator():
    for i in range(5):
        return i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(gen)

for j in gen:
    print(j)