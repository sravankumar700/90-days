####### Working With Matrix in Python #####

from numpy import * 
# arr1 = array([
#                 [1,2,3,5,4,7],
#                 [4,5,4,5,9,6]
# ])

# arr2 = arr1.flatten()
# arr3 = arr2.reshape(3,2,2)
# print(arr1)
# print(arr1.dtype)
# print(arr1.ndim)
# print(arr1.shape)
# print(arr1.size)
# print(arr2)
# print(arr3)



# m = matrix(arr1)
# n = matrix('1,2;3,4;5,6;7,8')
    # n1 = matrix('1,2,3;4,5,6;7,8,9')
    # n2 = matrix('1,2,3;4,5,6')
# print(m)
    # print(n)
    # print(n1)
    # print(n2)
# print(diagonal(m))
# print(diagonal(n))
# print(diagonal(n2))



m1 =  matrix('1 2 3')
m2 = matrix('4 5 9')
m3 = m1+m2;
m3 = m1*m2;
m3 = m1/m2;
print(m3) 