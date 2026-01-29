# collection : single variable use to store multiple values

# list = [] ordered and changeable, duplicates ok, lists are mutable and its elements can be of different data types

# set = {} unordered and ele of sets are immutable, set itself are mutable so we can add/remove ele in sets, no duplicates allowed

# tuple = () ordered and unchangable, duplicates OK, faster, they are immutable, mtlb bna diya to no add, no remove, no update


# lets start with list

# summary of list methods:
# append() - adds an element at the end
# insert() - adds an element at a specified position
# remove() - removes the first occurrence of a specified element
# pop() - removes and returns an element at a specified position (default is the last element
# clear() - removes all elements from the list
# index() - returns the index of the first occurrence of a specified element
# count() - returns the number of occurrences of a specified element
# sort() - sorts the list in ascending order
# reverse() - reverses the order of the list
# copy() - returns a shallow copy of the list, 

# shallow copy means it creates a new list but the elements are references to the same objects, if the elements are mutable and you modify them, the changes will be reflected in both lists
# extend() - extends the list by appending elements from another iterable (like another list, tuple, etc.)




fruits = ["apple", "banana", 45, 6.9, True] # list can store multiple data types
print(fruits)
print(type(fruits))

# accessing list items
print(fruits[1]) # banana
print(fruits[-1]) # True

# slicing
print(fruits[1:4]) # ['banana', 45, 6.9]
print(fruits[:3]) # ['apple', 'banana', 45]
print(fruits[2:]) # [45, 6.9, True]

# change item
fruits[0] = "orange"
print(fruits) # ['orange', 'banana', 45, 6.9, True]

# add item
fruits.append("grape")
print(fruits) # ['orange', 'banana', 45, 6.9, True, 'grape']

fruits.insert(1, "kiwi") # insert at index 1    
print(fruits) # ['orange', 'kiwi', 'banana', 45, 6.9, True, 'grape']

# remove item
fruits.remove(45) # remove the first occurrence of 45
print(fruits) # ['orange', 'kiwi', 'banana', 6.9, True, 'grape']
# if element not found it raises ValueError, you can use 'in' to check if element exists before removing

popped_item = fruits.pop() # removes last item
print(popped_item) # grape
print(fruits) # ['orange', 'kiwi', 'banana', 6.9, True]

# loop through list
for fruit in fruits:
    print(fruit)    

# check if item exists
if "banana" in fruits:
    print('banana exits')

# list length
print(len(fruits)) # 5

# sort 
fruits.sort()
print(fruits) # [6.9, True, 'banana', 'kiwi', 'orange'] - sorts based on ASCII values

# clear list
fruits.clear() # removes all items
print(fruits) # []



# if you want to know other methods availabe for the list just use help function
# help(list)


# we will see sets and tuples in next files

# Note: Lists are mutable, meaning you can change their content (add, remove, modify elements) after creation.
