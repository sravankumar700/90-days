####### Working With Matrix in Python #####

from numpy import * 
arr1 = array([
                [1,2,3,5,4,7],
                [4,5,4,5,9,6]
])

arr2 = arr1.flatten()
arr3 = arr2.reshape(3,4)
print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
print(arr1.size)
print(arr2)
