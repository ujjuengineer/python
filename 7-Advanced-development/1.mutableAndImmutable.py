
"""
mutable are those data which can be change after it created and vice verce for immutable

you might thinking isn't all data in python are mutable, like we can do a = 5 and then a = 6

but here 'a' is not a data, it is a variable which is storing the data !!!!
"""


"""
immutable objects are : 

integer,
floats,
strings,
tuples
"""

print(); print('------part-1-------'); print()

# how mutable objects behaves

li = [1,2,3,4]
print('id of li before modifying :', id(li))
li += [5,6] # this is modifying the same list by calling li.__iadd([5,6])
print('id of li after modifying :', id(li))
# the id of li before and after modifying will be same





print(); print('---------Part-2----------'); print()

# now if you do something like li = li + [5,6], it will create a brand new list by calling 
# li.__add__([5,6])

li = [1,2,3]
print('id of li before modifying :', id(li))
li = li + [4,5]
print('id of li after modifying :', id(li))







print(); print('---------Part-3----------'); print()
# how immutable objects behves

a = 5
print('id of a before modifying ', id(a))
a += 1
print('id of a after modifying ', id(a))

# the id of a changes after modifying the data !



