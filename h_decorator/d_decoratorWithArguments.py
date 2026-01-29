# earlier you were not passing any argumets in the original function, so we didn't needed the args and kwargs

# but if you paas any argument in the original funciton then it will show error if you don't have args and kwargs in the decorator

def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
    
@my_decorator
def add(a,b):
    return a + b

print(add(4,5))

"""

in line 9, 10 decode to => add = wrapper()
now in line 14 when you execute add(4,5) => you are executing wrapper(4,5) and if your wrapper don't have any args and kwargs then it will show error

so we always add *args and **kwargs to be on the safer side

"""