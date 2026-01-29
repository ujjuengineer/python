# this is module created by us named 'my_module.py'
# we can define functions, variables, classes, etc. in this module
# and then import this module in another python file to use its contents

def greet(name):
    return f"Hello, {name}! Welcome to my custom module."

pi_value = 3.14159

def sum(*args):
    val = 0
    for num in args:
        val += num
    return val

