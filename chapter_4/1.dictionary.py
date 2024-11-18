"""
Dictionaries are used to store data value in key:value pair , (just like class in cpp)
they are unordered, mutable and don't allow duplicate keys.

"""

# keys can be string, number but it can't be list, but the values can be !

student = {
    "name" : "ujjwal kumar sharma",
    "age" : 21,
    "grade": "fail",
    "hobby" : ["sleeping", "timepass", "eating", "cricket"],
    "marks" : (23,43,35,23,53)
}

# now we can print it
print(student)
print(); print()

# to get specific keys we can proceed like
print(student["name"]) 

# we can change the keys value
student["name"] = "rass" #overwrite
student["grade"] = "A+"
print(student)
print()


# we can add new keys 
student["newKey"] = "hello ujjwal"

print(student)
print()

# we can even change the datatype of the prev key
print(type(student["name"]))
student["name"] = 99
print(type(student["name"]))
print()



# we can even create null dict
her = {}

# now we can add keys and its value to this dics
her["name"] = "ras"
her["grade"] = "A+"
print(her)