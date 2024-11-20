"""
store following word meaning in python dictionary
table : "a piece of furniture", "list of facts and figures"
cat : "a small animal"

"""

meaning = {
    "table" : ["piece of furniture", "list of facts and figures"],
    "cat" : "a small animal"
}

"""
you are given a list of subject for students. assume 1 classroom is required for 1 subject. how many class room are needed by all students.
"""

# given list
subject = ["python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"]

# logic : we will create a set and add these list into it, and finally calculate the length of the set, the set will give length considring unique elements only.

newset = set()
length = len(subject)
i = 0
while i < length :
    newset.add(subject[i])
    i+=1

print(len(newset))


