# list is like an array in python, it can store element of different of different type
marks = [45.6, 43.2, 65.4, 85.3, 46.9]
print(marks) # we can print list like any other variable
print(marks[0], marks[1]) # we can print it using index
print("length of the marks is:",len(marks)) # we can print length of the list
print()

# we can store element of different types together in the list unlike array in cpp
student = ["ujjwal", 21, 8.79]
print(student[0])

# note that strings are immutabel in python whereas lists are mutable, i.e., we can change the lists using index, (can also be done in cpp)
student[0] = "ras"
print("student after mutation :",student)

