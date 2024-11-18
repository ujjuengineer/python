# few meathods of dictionary are

student = {
    "name" : "ujjwal",
    "age" : 21,
    "hobby" : "tympass",
    "talent" : "searching"
}

print(student.keys()) # return all the keys
print()

# we can even create a list of these keys and store it 
print(list(student.keys())) # typecasted to list
keyslist = list(student.keys()) # stored it in list
print("the list is : ",keyslist)
print()



student.values() # returns all values
valuList = list(student.values())
print(valuList)
print()


student.items() # return all (keys,val) pair as tuples
itemList = list(student.items())
print(itemList)
# we can change the list
itemList[0] = ("name", "rass")
print("changed list is :",itemList)


print(student.get("name")) # to get the keys
# see why we need this get meathod in next file
print()

# to add new keys
student.update({"height" : "5'11"})
print(student)
print()

# we could have also done like
newDir = {"eyes" : 2, "legs" : 2, "ears" : 2}
student.update(newDir) # add the newdir in student
print("student after adding new dir : ",student)
print()

# if we pass the same key then it will rewrite the prev key value with new value, it will not create duplicate keys as it is not allowed