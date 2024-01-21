import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([1, 2, 3,4])
add = arr1 + arr2
print(arr1.shape)
print(add)
print(add.shape)

print()
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1],[2], [3]])
add = arr1 + arr2
print()
print(arr1.shape)
print(arr1.ndim)
print(arr2.shape)
print(arr2.ndim)
print()
print(add)
print()
print(add.shape)


x = np.array([[1],[2]])
print(x)
print(x.shape)
y= np.array([[1,2,3],[1,2,3]])
print(y.shape)
print(y)
print(x+y)