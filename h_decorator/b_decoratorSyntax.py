# decorator with @ syntax

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

"""
def say_hi():
    print("Hi!")

say_hi = my_decorator(say_hi)
say_hi()

"""

# instead of above code we can use @ syntax to apply decorator

@my_decorator
def say_hi():
    print("Hi!")

# this simpley means say_hi = my_decorator(say_hi) 
# in simple if you execute say_hi(), the wrapper function will be executed 

say_hi()