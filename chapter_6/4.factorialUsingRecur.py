# calculating factorial using recursion

# n! = n * (n-1)! -> we will use this

def factorialOf(n) :
    # base case
    if(n == 0 or n == 1) : 
        return 1
    
    # calculating factorial of n and storing it in a variable named "fac"
    fac = n * factorialOf(n-1)
    return fac


print("factorial of 5 is ",factorialOf(5))

