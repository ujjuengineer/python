"""

* (Single Asterisk): Used for unpacking ordered iterables like lists, tuples, or sets (positional arguments).

(Double Asterisk): Used for unpacking dictionaries (keyword arguments).

"""



def calculate_volume(length, width, height):
    return length * width * height


dimensions = [5, 3, 2]


# wihtout unpacking
result = calculate_volume(dimensions[0], dimensions[1], dimensions[2])

# with unpacking 
result = calculate_volume(*dimensions)
print(result)  # Output: 30






"""
The Strict Rule: When unpacking dictionaries with **, the keys inside the dictionary must exactly match the variable names inside the function definition. 

If you have an extra key or misspell a key, Python will throw a TypeError.
"""

def create_user(username, email, age):
    print(f"User: {username} | Email: {email} | Age: {age}")



user_data = {
    "username": "coder_99",
    "email": "coder@mail.com",
    "age": 24
}


# The keys in the dict match the parameter names perfectly
create_user(**user_data)
# Output: User: coder_99 | Email: coder@mail.com | Age: 24








"""
In modern Python, you can also use * to merge collections or extract items into separate variables during standard assignments:
"""
# Merging lists cleanly
list_a = [1, 2]
list_b = [3, 4]
combined = [*list_a, *list_b]  # [1, 2, 3, 4]

# Grabbing head and tail
first, *middle, last = [10, 20, 30, 40, 50]
print(first)   # 10
print(middle)  # [20, 30, 40] -> It grabs whatever is left in the middle!
print(last)    # 50