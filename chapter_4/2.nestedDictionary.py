# we can create dictionaries inside a dictionary

student = {
    "name" : "ujjwal",
    "age" : 21,
    "marks" : {
        "phy" : 98,
        "chem" : 37,
        "maths" : "fail"
    }
}

print(student)
print()

# we can print the marks 
print(student["marks"])
print()

# we can even specify the marks of a prticular subject
print(student["marks"]["phy"])