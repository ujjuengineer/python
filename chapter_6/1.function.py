# we use "def" to define any function, followed by the function name

# here a and b are called parameters
def sum(a,b) :
    return a + b 

# calling function
x = 5; y = 10
print(sum(x,y)) # here x and y are called arguments

# two types of function * built-in * user-defined


# default parameters in function : used when no argument are passed during call the function

def randonFun(a = 3, b = 4): 
    return a + b

print("value using default parameters : ",randonFun()) 
# if we don't pass any argument here, then randomFun will use its default parameters


"""
note that, default parameter is always declated after empty parameter, i.e., we can't do like

def fun(a = 4, b) : # this is wrong, 

we should do like 
def fun(b, a = 4) : 


"""

