# function : it is a block of reusable code that performs a specific task
# place () after the name of the function to call it

# defining a basic function
def greet():
    print("Hello, welcome to Python functions!")

# calling the function
greet()


# ==================================================================================

# function with parameters
def add(a, b):
    return a + b
result = add(5, 3)
print("Sum:", result)


# ==================================================================================

# return statement : it is used to exit a function and return a value
def multiply(x, y):
    return x * y

product = multiply(4, 6) # calling the function and storing the returned value
print("Product:", product)

# ==================================================================================

# positional arguments : arguments are passed based on their position
# just like above add(5, 3) → 5 is assigned to a and 3 to b


# default arguments : if no argument is passed, the default value is used
def power(base, exponent=2):
    return base ** exponent
print("Power with default exponent:", power(3)) # 3^2
print("Power with custom exponent:", power(2, 3)) # 2^3

# we can't plce a non-default argument after a default argument
# def invalid_func(a=1, b): # this will raise a syntax error

# ==================================================================================

# keyword arguments : arguments are passed by explicitly naming them, regardless of their position
# order of the arguments does not matter
# useful for functions with many parameters, improves readability

def describe_person(name, age, city="Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}")

describe_person(age=30, name="Alice") # city will use default value
describe_person(name="Bob", age=25, city="New York")

# make sure to use keyword arguments after positional arguments when mixing both
describe_person("Charlie", age=28, city="Los Angeles") # valid
# describe_person(age=28, "Charlie", city="Los Angeles") # invalid, will raise syntax error


# in print() function, we often use keyword arguments like sep and end
print("Hello", "World", sep=", ", end="!\n") # Output: Hello, World!

# this sep and end are keyword arguments of print funciton

# ====================================================================================

# arbitrary arguments : when we don't know in advance how many arguments will be passed to a function, also known as variadic functions 

# use *args for arbitrary positional arguments and **kwargs for arbitrary keyword arguments

def arbitrary_func(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

arbitrary_func(1, 2, 3, name="Alice", age=30)
# here, 1, 2, 3 are captured in args as a tuple
# name="Alice", age=30 are captured in kwargs as a dictionary

# keyword arguments can be accessed like a normal dictionary
# args can be accessed like a normal tuple

# keyword arguments must come after positional arguments when calling the function, if we put keyword arguments first, it will raise a syntax error
# arbitrary_func(name="Alice", 1, 2, 3) # invalid, will raise syntax error

# ====================================================================================
print();print()
# some more example of variadic functions

def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

sum_result = sum_all(1, 2, 3, 4, 5)
print("Sum of all numbers:", sum_result)


# similarly for keyword arguments
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
    
print_info(name="Alice", age=30, city="New York")