# sets is a collection of unordered items
# each elements in the set must be unique and immutable

collection = {1,2,2,3,3,3,4,5,"ujjwal","ram","ujjwal","ram"} 
# repeated elements stored only once, so it resolved to {1,2,3,4,5,"ujjwal","ram"}
print(collection) # it will ignore the duplicates value
print()

# if you try to print the length of the set, it will only count the unique ele
print(len(collection))
print()


# note that if you try to print the collection, the elements are printed in random order, this is because sets are unordered


# how to create empty sets
sets = {} # this is not empty set, this is actually empty dictionary
# to create an empty set we follow this syntax
sets1 = set() # syntax to create empty set