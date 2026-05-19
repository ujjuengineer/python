import numpy as np

arr = np.array([1,2,3,4])
print(arr)



# multiply all ele by 2
arr = arr * 2
print(arr)



# there are multiple dimension of array we can create

# 0 dim array
arr = np.array('a')
print(); print(arr)
print("dimension of arr :" ,arr.ndim)

# 1 dim array
arr = np.array(['a'])
print(); print(arr)
print("dimension of arr :" ,arr.ndim)

# 2 dim array
arr = np.array([['a', 'b'], 
                ['c', 'd'],
                ['e', 'f']])
print(); print(arr)
print("dimension of arr :" ,arr.ndim)

# 3 dim array
arr = np.array([
    [['a', 'b'],['c', 'd']],
    [['e', 'f'],['g', 'h']]
    ])
print(); print(arr)
print("dimension of arr :" ,arr.ndim)