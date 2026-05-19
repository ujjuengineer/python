# aggregate function : summarise data and return a single value

import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])

print(np.sum(arr)) # sum of the array
print(np.mean(arr)) # mean of the arrya
print(np.std(arr)) # standard deviation
print(np.var(arr)) # variation (square of the std)

print(np.min(arr)) # min ele
print(np.max(arr)) # max ele

print(np.argmin(arr)) # position of min ele
print(np.argmax(arr)) # position of max ele







# matrix multiplication 

arr1 = np.array([
    [1,2,3],
    [4,5,6]
])

arr2 = np.array([
    [1,2],
    [3,4],
    [5,6]
])

# using np.matmul
print(np.matmul(arr1, arr2))
print()

# using dot
print( np.dot(arr1, arr2) )
print()

# or you can do something like this
print( arr1.dot(arr2)); print()


# the third way is simpley use @ operator
print(arr1 @ arr2)