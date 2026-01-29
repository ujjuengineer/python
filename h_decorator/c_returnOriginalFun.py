# in the case when original function is returning some value, then insted of executing the original function from wrapper, you need to return the original function return value

def my_decorator(func):
    def wrapper():
        return func()
    return wrapper

@my_decorator
def say_hi():
    return 7

print(say_hi()) # it will execute the wrapper function
 # inside wrapper function we are returning func()
 # func() -> return 7 -> this 7 is returned by the wrapper function 