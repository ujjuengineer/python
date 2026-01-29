
# PYTHON TUPLES 


# A tuple is:
# - ordered
# - immutable (cannot change after creation)
# - allows duplicate elements
# - can store mixed data types

# Syntax:
# tuple_name = (item1, item2, item3)


# Creating tuples

# for creating empty tuple
empty_tuple = () # you can also use tuple() function
print(empty_tuple)
print(type(empty_tuple))   # <class 'tuple'>


# creating tuples with elements

t1 = (1, 2, 3)
t2 = ("apple", "banana", "cherry")
t3 = (1, "apple", 3.5, True)

print(t1)
print(type(t1))   # <class 'tuple'>

# IMPORTANT:
# Parentheses are optional, comma defines tuple
t4 = 1, 2, 3
print(type(t4))   # tuple

# Single element tuple
# WITHOUT comma → not a tuple 
t5 = (5)
print(type(t5))   # int 

# WITH comma → tuple
t6 = (5,)
print(type(t6))   # tuple 




# Accessing tuple elements

t = (10, 20, 30, 40)

# Indexing
print(t[0])      # 10
print(t[-1])     # 40


# Slicing
print(t[1:3])    # (20, 30)
print(t[:2])     # (10, 20)
print(t[2:])     # (30, 40)
print(t[:])      # (10, 20, 30, 40)

# you can add steps in slicing
print(t[::2])    # (10, 30)
print(t[::-1])   # (40, 30, 20, 10)



# Immutability of tuples

# Tuples cannot be modified
# t[0] = 100     #  TypeError

# No add / remove / update operations
# t.append(5)   # 
# t.remove(10)  # 



# Tuple with mutable elements

t = ([1, 2], [3, 4])

# Tuple itself is immutable
# But objects inside can be mutable
t[0].append(99)
print(t)   # ([1, 2, 99], [3, 4])

# Structure fixed, content inside may change 



# Tuple operations

a = (1, 2, 3)
b = (4, 5)

# Concatenation
c = a + b
print(c)   # (1, 2, 3, 4, 5)

# Repetition
print(a * 2)   # (1, 2, 3, 1, 2, 3)

# Membership
print(2 in a)     # True
print(10 in a)    # False

# Length
print(len(a))



# Tuple methods (VERY LIMITED)

t = (1, 2, 2, 3, 4)

# count(x) → number of occurrences
print(t.count(2))   # 2

# index(x) → first index of x
print(t.index(3))   # 3



# Tuple unpacking

t = (10, 20, 30)

a, b, c = t
print(a, b, c)

# Unpacking with *
t = (1, 2, 3, 4, 5)
a, *b, c = t
print(a)   # 1
print(b)   # [2, 3, 4]
print(c)   # 5



# Tuple as function return value 
# if function returns multiple values, they are returned as a tuple

def get_values():
    return 10, 20, 30   # returns a tuple

x, y, z = get_values()
print(x, y, z)



# Tuple vs List (IMPORTANT DIFFERENCE)

# List → mutable
lst = [1, 2, 3]
lst[0] = 10   # allowed

# Tuple → immutable
t = (1, 2, 3)
# t[0] = 10   # error



# Tuples and sets

# Tuples can be elements of a set (if contents immutable) 
s = {(1, 2), (3, 4)}
print(s)

# List cannot be set element
# s = {[1,2]}  # error



# When to use tuples

# Use tuple when:
# - data should NOT change
# - want faster access than list
# - want to use as dict key / set element
# - representing fixed records (x, y), (id, name)

# Examples:
point = (10, 20)
rgb = (255, 128, 0)
db_row = (101, "Ujjwal", "CSE")




# Tuples:
# - slightly faster than lists
# - use less memory
# - safe from accidental modification



# Summary 
# Tuple = ordered + immutable + allows duplicates
# Tuple size fixed, content may mutate if object inside is mutable
# Limited methods: count(), index()
# Best for fixed, read-only data
