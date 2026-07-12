# you can measure how much time your code execution takes 
print()

import time

# time.time() -> gives you time passes since 1970 in sec 

def measure_runtime(func):
    """take input of a function, and execute it from here and measure its execution time"""
    start = time.time() 
    func() # execute the function
    end = time.time() 

    return end - start


def powers(limit):
    return [x*x for x in range(limit)]

runtime = measure_runtime(lambda: powers(100000000)) # you can't directly pass function with arguments inside the function, instead of passing it, it will execute the function, so we use lamda function to pass the function as an arguments
print(runtime)
print()

"""
syntax of lambda function : 
lambda arguments : expression


arguments : A comma-separated list of inputs (parameters) passed into the function. You can have zero, one, or multiple arguments.

expression : A single line of code that evaluates and automatically returns a value. You do not (and cannot) use the return keyword here
"""