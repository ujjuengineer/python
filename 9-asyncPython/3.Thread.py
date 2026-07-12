# single thread example
# these all code blocks are execting line by line in single thread

import time

def ask_user():
    start = time.time() # stores the current time
    input("enter name : ")
    print(f"ask user time : {time.time()-start}")


def complex_calculation():
    start = time.time()
    print("starting calculation.... ")
    [x*2 for x in range(100000000)]
    print(f"complex cal... time : {time.time() - start}")


ask_user()
complex_calculation()