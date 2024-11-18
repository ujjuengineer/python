# wap to count number of students with A grade in following tuple
tup = ("c","d","a","a","d","d","a")
print(tup.count("a"))

# wap to store the above value in a list and sort them from a to d
list = []
list.append(tup)
list.sort()
print(list) # this will not print the sorted list
""" 
why the above list is not sorted ?
this is because list.append(tup) will add the whole tup as a single element in the list. to get rigid of that we can proceed like follow 
"""

list = sorted(tup)
print(list)