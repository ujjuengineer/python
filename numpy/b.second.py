import numpy as np

arr = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

# you can select the row as     arr[start : end : step]

print(arr[0]) # first row [1,2,3,4]
print(arr[1]) # second row 

print(arr[0:2]) # row from 0 to 1 (last index excluded)

print(arr[0:]) # from 0th row to last

print(arr[0::2]) # from 0th row, select every 2nd row


print();print()
# you can select col as arr[row][col]
# another way to do this : arr[row, col]

# let we have to select first col of all the row
print(arr[:, 0])


print(); print()

print(arr[:, -1]) # last col of all the row 
print()

print(arr[:, 0:3]) # col from 0 to 3(excluded) of all the row
print()

print(arr[:, ::-1]) # col form 0 to last, in reverse order of all the row