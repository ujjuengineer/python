# we can access keys student["name"], but this is not best practice
student = {
    "name" : "ujjwal",
    "age" : 21,
    "hobby" : "tympass",
    "grade" : "fail"
}

# we can access key as
# print(student["name"])

# now by mistake if we did 
# print(student["name1"]) , this will show error, as there is no such key "name1"

# as soon we get error, the remaining code below the error will not work, and this may cause problem in our project, to get rigid of that we use get meathod
print(student.get("name")) 
print()

# now if we do student.get("name1"), this will not show error, rather this will give none and the code below this will work without any problem

# for example
# print("before")
# print(student["name1"])
# print("after") # this will not be printed

# now if we do the same using get
print("before")
print(student.get("name1")) # this will give none
print("after")
print()