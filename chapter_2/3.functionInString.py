str = "ujjwal kumar sharma"
print(str.endswith("ma")) # return true if str ends with "ma" else return false
print()

print(str.capitalize()) # capatlise the first character
# note that str.capitalize() is not making any changes in original string, it is actually creating new string, if we print(str) it will remains the same
print(str)
print()

# to capitalize the first character of original string we can do like
str = str.capitalize()
print(str)
print()

# to replace old characters to new characters
print(str.replace("a","i"))
print(str.replace("Ujjwal","Ram")) # we can even replace a part of string
# note that using above 2 meathod, the original string is not getting changed, it will remains the same, if we print our original string it will show the same
print(str)
print()

# to find any character or word in a string
print(str.find("a")) # return the first occurrence of the "a"
print(str.find("kumar")) # return the index of "k"
print(str.find("her")) # if something is not found then it will return -1
print()

# to count the occurrence of any substring 
str2 = "my name is ujjwal kumar sharma. my best friend name is ram. my father name is ram. my mother name is ram."
print(str2.count("ram"))