# Summary of Common String Methods:
# len()          → length of string
# find()         → index of first occurrence of substring
# rfind()        → index of last occurrence of substring
# capitalize()  → capitalizes first character
# upper()       → converts to uppercase
# lower()       → converts to lowercase
# isdigit()     → checks if all characters are digits
# isalpha()     → checks if all characters are alphabetic
# replace()     → replaces substring with another substring
# count()       → counts occurrences of substring
# strip()       → removes leading/trailing whitespace
# split()       → splits string into list based on delimiter

# string methods 
# strings in python come with built-in methods that allow you to manipulate and work with string data easily.

# example string
name = "ujjwal sharma"

# 1. len() : returns the length of the string
print(len(name))  # Output:  13 (including spaces)

# 2. find() : returns the index of the first occurrence of the substring, otherwise -1
index = name.find("a")
print(index)  # Output: 4

# rfind() : returns the index of the last occurrence of the substring
last_index = name.rfind("a")
print(last_index)  # Output: 12

# 3. capitalize() : capitalizes the first character of the string
cap_text = name.capitalize()
print(cap_text)  # Output: "Ujjwal sharma"

# 4. upper() and lower() : converts the string to uppercase or lowercase
upper_text = name.upper()
lower_text = name.lower()
print(upper_text)  # Output: "UJJWAL SHARMA"
print(lower_text)  # Output: "ujjwal sharma"

# 5. isdigit() : checks if all characters in the string are digits
print(name.isdigit())  # Output: False
num_str = "12345"
print(num_str.isdigit())  # Output: True

# 6. isalpha() : checks if all characters in the string are alphabetic
print(name.isalpha())  # Output: False (because of space)
alpha_str = "Ujjwal"
print(alpha_str.isalpha())  # Output: True

# 7. replace() : replaces occurrences of a substring with another substring
new_text = name.replace("sharma", "kumar")
print(new_text)  # Output: "ujjwal kumar"

# 8. count() : counts occurrences of a substring in the string
count_a = name.count("a")
print(count_a)  # Output: 3

# 9. strip() : removes leading and trailing whitespace
text_with_spaces = "   Hello, World!   "
stripped_text = text_with_spaces.strip()
print(stripped_text)  # Output: "Hello, World!"

# 10. split() : splits the string into a list of substrings based on a delimiter
words = name.split(" ")
print(words)  # Output: ['ujjwal', 'sharma']

# help() : provides information about methods available for spefic data types
# for example, to see all string methods, you can use:
# help(str)
