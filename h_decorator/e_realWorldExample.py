# real world decorator example

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time() # stores the curr time
        func(*args, **kwargs) # pause the execution for 3 sec
        end = time.time() # store the curr time
        print(f"Time taken: {end - start:.4f}s")
    return wrapper

@timer
def slow(sec):
    time.sleep(sec)

slow(3)


"""
what is happening here ??



"""