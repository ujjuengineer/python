# broadcasting : it allow numpy to perform operation on arrays with different shapes by virtually expanding dimensions so they match the larger array shape


# we can broadcaste them if
# the dimnsions have the same size or
# one of the dimensions has a size of 1 

import numpy as np

arr1 = np.array([[1,2,3,4]])
arr2 = np.array([[1],[2],[3],[4]])

print(arr1.shape) # (1, 4)
print(arr2.shape) # (4, 1)

# since one the first col of both arr has 1, so we can broadcaste them
# similarly one of the second col of both the arr has 1, so we can broadcaste them as well

print(arr1 * arr2)