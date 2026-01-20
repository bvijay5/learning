a = {1, 2, 3}
b = {3, 4, 5}

# union() or | – combine sets
print(a.union(b))   # {1, 2, 3, 4, 5}
print(a | b)        # same as union

# intersection() or & – common elements
print(a.intersection(b))  # {3}
print(a & b)

# difference() or - – elements in a but not in b
print(a.difference(b))  # {1, 2}
print(a - b)

# symmetric_difference() or ^ – elements not common
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
print(a ^ b)
