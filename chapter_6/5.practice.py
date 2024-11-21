# write a recursive function to calculate the sum of first n natural number

# sum of n = n + sum(n-1) , we will use this formula to find the sum of n natural number

def sumOf(n) : 
    # base case
    if(n == 1) : 
        return 1
    # storing sum of n using formula
    sum = n + sumOf(n-1)
    return sum

print(sumOf(5))