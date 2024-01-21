import numpy as np

# shape
var = np.array([[1, 2, 3], [1, 2, 3]])
print(var)
print()
print(var.shape)

var1 = np.array([1, 2, 3, 4], ndmin=4)
print(var1)
print(var1.ndim)
print(var1.shape)

# convert(reshape)
var3 = np.array([1, 2, 3, 4, 5, 6])
x = var3.reshape(3, 2)  # (row,col)
print(x)

# convert 3d
print('1 d:')
var4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11])
print(var4)
print(var3.ndim)
print()
x1 = var4.reshape(2, 3, 2)  # (row,col,n)
print(x1)
print(x1.ndim)

# 3d to 1d
one = x1.reshape(-1)
print(one)
print(one.ndim)
