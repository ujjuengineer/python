# membership operator in Python : in , not in
# used to check if a value exists in a sequence (like string, list, tuple, set, dictionary)
# returns True or False

# Example with list
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)      # True
print(6 not in my_list)  # True

print()

# Example with string
my_string = "Hello, World!"
print("Hello" in my_string)   # True
print("Python" not in my_string)  # True

# Example with dictionary (checks keys)
my_dict = {'a': 1, 'b': 2, 'c': 3}
print('a' in my_dict)    # True
print(2 in my_dict)      # False

# Example with set
my_set = {1, 2, 3, 4, 5}
print(4 in my_set)       # True
print(10 not in my_set)  # True

# membership operator can be used in conditional statements
if 'b' in my_dict:
    print("Key 'b' exists in the dictionary")   

if 10 not in my_list:
    print("10 does not exist in the list")  

# membership operator with tuple
my_tuple = (10, 20, 30, 40)
print(20 in my_tuple)    # True
print(50 not in my_tuple) # True