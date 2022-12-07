import numpy as np

# dimensions in arrays

# nd = 0
print('Array ND = 0')
arr = np.array(10)
print(arr)

# nd = 1
print('\nArray ND = 1')
arr1 = np.array([1,2,3,4,5])
print(arr1)

# nd = 2 
print('\nArray ND = 2')
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# nd = 3 
print('\nArray ND = 3')
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3)


# checking num of dimensions

print('\nChecking dimensions')
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)