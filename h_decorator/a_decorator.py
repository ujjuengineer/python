# decorator : a function that extends the functionality of another function without explicitly modifying the base function 
# pass the base function as an argument to the decorator 



# A decorator replaces a function with another function that calls the original function inside it.

print("==========================================================================================")


# basic structur of a decorator 
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper


def say_hi():
    print("Hi!")

say_hi = my_decorator(say_hi)
say_hi()


# what is happenig here ? step wise explanation :
"""
line 23 : first the right part will be evaluated
          my_decorator function is called -> func will be now pointing to say_hi function
          now my_decorator will return the wrapper function, 
          so in line 23, the say_hi variable is assigned to the wrapper function

line 24 : when say_hi() is called, it is actually calling the wrapper function
            so the wrapper function will execute its code

            wrapper function remembers that "func" 
            code execution of wrapper function : 
            -> print("Before function")
            -> func()  # which is actually say_hi() function
            -> print("After function")

output will be :
Before function
Hi! 
After function

"""

print("==========================================================================================")

# this whole code can be written in simpler way using @ syntax 

# see next file 