# recursion means calling a function recursively

# it consist 1. base case, 2. work that have to performed, 3. function call

# let create a recursive function to print 1 to 5

def fun(x) :
    # base case
    if(x > 5) : 
        return
    
    # kaam
    print(x, end = ", ")

    # recursive call
    fun(x+1) 


# calling the fun function
fun(1) # 1 is the passed argument, so inital value of x in the passed function is 1, and then it will keep increasing by 1 in every call

