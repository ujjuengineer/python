# you can even create your own modules by creating a python file with .py extension
# and defining functions, variables, classes, etc. in it.
# then you can import that module in another python file and use its functions, variables, classes, etc.

# let's create a module named 'my_module.py' with some functions and variables

import my_module as mm

# using functions and variables from my_module
greeting = mm.greet("Ujjwal")
print(greeting)  # Hello, Ujjwal! Welcome to my custom module.

print("Value of pi from my_module:", mm.pi_value) 
total = mm.sum(1, 2, 3, 4, 5)
print("Sum from my_module:", total)  # Sum from my_module: 15
# now you can create more functions and variables in my_module.py
# and use them here by importing the module

# modules can also be organized into packages (folders with __init__.py file)

# organize packages and modules in a folder structure like this: 
# my_package/
#     __init__.py
#     module1.py
#     module2.py


# next topic 
"""
explain circular imports visually 
show how pip packages are structured 
"""