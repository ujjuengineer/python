"""
The any() and all() functions in Python are built-in tools used to evaluate boolean conditions across an entire collection of data (like a list, tuple, or generator).

Think of them as shortcuts for big or and and statements. 

Instead of writing if a or b or c or d:, you can throw them into any().
"""

"""
any() returns True if at least one element in the collection evaluates to True. 

If the collection is completely empty, it returns False. : if collection is empty then there is no any truthy value in the collection, so it return false !!
"""

conditions = [False, False, True, False]

print(any(conditions))  # Output: True (because it found one True)



"""
all() returns True only if every single element in the collection evaluates to True. 

If even one element is False, it immediately fails. 

(Fun quirk: if the collection is empty, it returns True). : because if collection is empty there is no any falsy value in the collection : so it returns true
"""

scores = [True, True, True, True]
print(all(scores))  # Output: True

mixed_scores = [True, True, False, True]
print(all(mixed_scores))  # Output: False (because of that single False)




"""
any() and all() don't just look for literal True and False booleans. They evaluate the "truthiness" of the objects inside. In Python, things like 0, None, empty strings "", and empty lists [] are considered Falsy, while almost everything else is Truthy.
"""

# len() is ignored, it evaluates the contents directly
items = [0, "", None, "Hello", []]

print(any(items))  # Output: True (because "Hello" is a non-empty string, which is Truthy)
print(all(items))  # Output: False (because 0, "", and None are Falsy)








# any() and all() use short-circuit evaluation, they stop checking the moment they find an answer. Combined with a generator, this is incredibly fast and memory-efficient.

# Imagine you want to check if any transaction in a list of millions is negative:
transactions = [120, 450, -20, 890, 1500]

# The generator checks numbers one-by-one. 
# The moment any() hits -20, it stops executing and returns True immediately!
has_negative = any(tx < 0 for tx in transactions)

print(has_negative)  # Output: True



# Imagine checking if a user's password meets all security criteria:
password = "SuperSecretPassword123"

requirements = [
    len(password) >= 8,                # Length check
    any(char.isdigit() for char in password),  # Has numbers?
    any(char.isupper() for char in password)   # Has uppercase?
]

# If all conditions in the list are True, the password passes
if all(requirements):
    print("Password is secure!")



# SUMMARY 
"""
any(): Returns True if it finds one truthy value. It stops looking immediately upon finding it.

all(): Returns True only if everything is truthy. It stops looking immediately upon finding a single falsy value.
"""