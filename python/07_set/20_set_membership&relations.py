x = {1, 2}
y = {1, 2, 3, 4}

# issubset() – check if set is inside another
print(x.issubset(y))  # True

# issuperset() – check if set contains another
print(y.issuperset(x))  # True

# isdisjoint() – True if no common elements
print(x.isdisjoint({5, 6}))  # True
