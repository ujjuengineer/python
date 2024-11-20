# tupple are builtin data type in python just like a list, but the difference is that tupples are immutable unlike list
tup = (1,2,3,4,"ujj")
print(type(tup))
print()

# we can access the elements of tupple using index but we can't assign the value

# we can create an empty tupple
tup2 = ()
print("type of tup2 is",type(tup2)) # tuple
print()

# we can create tupple of single element as well
tup3 = (1,) # we need to put a , because if we didn't do it then python will assume it as an integer
print(type(tup3))
print()


# just like list and string, we can do slicing here as well
print(tup[0:2])
print()

# meathods in tupple

# finding the first occurrence of any element
newTup = (5,3,6,3,5,6,7,3,63,56,3)
print(newTup.index(3)) # give the index of first occurrence of 3
print(newTup.count(3)) # give frequency of 3
print()

# to sort a tup we use 
print(sorted(newTup)) # sorted(tup) will create a new tupple, will make any changes in original tup as tupple are immutable
