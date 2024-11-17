# we can access a part of string as follow
str = "ujjwal kumar sharma"
str_part = str[0 : 7] # str[starting index : last index] , last index not included
print(str_part)

# let suppose we have to print till last index, then we can use len(str) or just let the second part empty
print(str[0 : len(str)]) 
print(str[2 : ]) # it means [2 : len(str)]
print(str[ : 5]) # it means [0 : 5]


# negative index are only availabe for slicing purpose
"""
 a  p  p  l  e    last character have index -1 
-5 -4 -3 -2 -1

"""

new_str = "apple"
print("slice using negative index :",new_str[-4 : -1]) # -1 index not included