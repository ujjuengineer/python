# sets are unordered collections of unique elements. they are mutable, meaning we can add or remove elements after creation. 

# However, the elements themselves must be immutable (like numbers, strings, or tuples). 

# you cannot have mutable elements like lists or dictionaries as set elements.

# summary of set methods:
# add() - adds an element to the set

# remove() - removes a specified element from the set, raises KeyError if the element is not found
# discard() - removes a specified element from the set, does not raise an error if the element is not found

# pop() - removes and returns an arbitrary element from the set
# clear() - removes all elements from the set
# union() - returns a new set with elements from both sets
# intersection() - returns a new set with elements common to both sets
# difference() - returns a new set with elements in the first set but not in the second
# symmetric_difference() - returns a new set with elements in either set but not in both
# issubset() - checks if all elements of the set are in another set 
# issuperset() - checks if the set contains all elements of another set


#  PYTHON SETS — SHORT NOTES

# A set is:
# - unordered
# - mutable
# - stores UNIQUE elements only
# - elements must be IMMUTABLE (hashable)

# Creating a set

my_set = {1, 2, 3, "apple", (4, 5)}   # tuple allowed, list not allowed
print(my_set)
print(type(my_set))   # <class 'set'>

# for creating empty set
empty_set = set()



# Accessing elements

# Sets are unordered → no indexing
# You can only iterate
for item in my_set:
    print(item)



# Adding elements

my_set.add("banana")   # adds single element
print(my_set)

# my_set.update([10, 20, 30])  # add multiple elements



# Removing elements

my_set.remove(2)   #  KeyError if element not found
print(my_set)

my_set.discard(10) #  no error if element not found, there is no such method as discard() in list, so in list check before removing using 'in'
print(my_set)

popped_item = my_set.pop()  # removes ANY random element
print("Popped item:", popped_item)
print(my_set)



# Set operations

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union → all elements
print("Union:", set_a.union(set_b))  
# or: set_a | set_b

# Intersection → common elements
print("Intersection:", set_a.intersection(set_b))
# or: set_a & set_b

# Difference → elements in set_a but not in set_b
print("Difference:", set_a.difference(set_b))
# or: set_a - set_b

# Symmetric Difference → elements NOT common
print("Symmetric Difference:", set_a.symmetric_difference(set_b))
# or: set_a ^ set_b



# Membership check
if 3 in set_a:
    print("3 exists in set_a")



# Set size
print("Length of set_a:", len(set_a))


# Clearing a set
set_a.clear()
print("Cleared set_a:", set_a)



# IMPORTANT EXTRA NOTES

#  Lists & sets cannot be elements of a set 
# { [1,2,3] }   → ERROR
# { {1,2} }     → ERROR

#  Tuples & frozensets allowed
# {(1,2), (3,4)}

# Real immutable set:
fs = frozenset([1, 2, 3])  # cannot add/remove elements

# Use set when:
# - you need uniqueness
# - fast lookup (O(1))
# - order does NOT matter

# Sets do NOT support:
# - indexing
# - slicing
# - duplicate values

# To see all methods:
# help(set)
