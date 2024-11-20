# in python, we can't leave any loop empty, i.e., you are suppose to do some work inside of loop, otherwise you can expect an error, to get rigid to that we can use pass statement

for el in range(10) :
    pass


"""
wap to find factorial of first n numbers
"""

# taking input of n
n = int(input("enter n : "))


mul = 1 # for storing factorial
for i in range (1,n+1) :
    mul *= i
    print("factorial of",i,"is",mul)
