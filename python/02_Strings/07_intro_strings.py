a ='Vijay'      # Single quoted string
b = "Vijay"     # Double quoted string
c = '''Vijay''' # Triple quoted string


"""
slicing
Indexing
(0 ,1 ,2 ,3 ,4)
(-5,-4,-3,-2,-1)

The index in a sting starts from 0 to (length -1) in Python. In order to slice a string, we use
the following syntax:
sl= name[ind_start : ind_end] #ending indix will not be included
"""

name = "Bhupathiraju"
print(len(name))
sl1 = name[0:4]
sl2 = name[1:len(name)]
sl3 = name[-12: -5]
sl4 = name[-12: len(name)]

sl5 = name[1:10:2] #[start_indx : end_indx : jump]

print(sl1)
print(sl2)
print(sl3)
print(sl4)
print(sl5)
