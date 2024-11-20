"""
Note that sets are mutable i.e., we can add or delete the elements of the set but
the element of the sets are immutable, i.e., we can't change the value of the
elements.

this is why we can't add list in sets as its element, as we know list's elements can 
be changed. we can pass tupple and string as sets elemet as they are immutable.

"""
print()

# adding element in sets
collection = set() # empty set
collection.add("ujjwal") # adding string 
collection.add(("mum","ram")) # adding tupple
collection.add(7)
collection.add(9)
collection.add(22)

print("original set :",collection)
print()

"""
if we try to add a list like
collection.add(["hlw","there","namste"]) this will show error
"""

# to remove any element we use
collection.remove(7)
print("set after removing element 7 :",collection)
print()


collection.pop() # use to remove a random element of the set
print(collection)
print()

# we can print which value is getting removed
print("popped value is :",collection.pop())
print("new set become :",collection)
print()


# to clear or empty the set we use
collection.clear() 
print(len(collection)) # 0 size as now the collection is empty
print()


"""" union and intersection of 2 sets """
set1 = {1,2,3,4}
set2 = {3,4,5,6}

print("union of set1 and set2 is :",set1.union(set2)) # {1,2,3,4,5,6}
# it will combine set1 and set2, and return a new set, note that there is no change in original set1 and set2

# similarly there is intersection of set that will return the unique element of both set
print("intersection of set1 and set2 is :",set1.intersection(set2))

# now if we print the set1 and set2, they will remains the same
print("the original sets are : ",set1, set2,"\n")
