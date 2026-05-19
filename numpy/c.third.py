# scalar arithmetic on numpy array

import numpy as np
print("scalar arithmetic operations")
arr = np.array([1,2,3])

print(arr * 2)

print(arr + 1)

print(arr - 1)

print(arr / 2)

print(arr ** 2)

print();print()

print("vectorised maths function in numpy")

arr = np.array([1.4, 2.3, 3.99])

print(np.sqrt(arr))
print(np.round(arr))
print(np.floor(arr))
print(np.ceil(arr))

print()

print("element wise arithemetic")

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 / arr2)
print(arr2 ** arr1)


print()

print("comparision oeprator")

arr1 = np.array([40, 60,30,90])

print(arr1 < 50) # give true and false ele wise [ True False  True False]

arr1[arr1 < 50] = 0 # assign 0 to all those ele which is less than 50
print(arr1)