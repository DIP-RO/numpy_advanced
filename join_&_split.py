import numpy as np

var = np.array([1, 2, 3, 4])
var2 = np.array([3, 4, 5, 6])
ar = np.concatenate((var, var2))
print(ar)

# 2d
var = np.array([[1, 2], [3, 4]])
var2 = np.array([[3, 4], [5, 6]])
ar = np.concatenate((var, var2), axis=1)
ar1 = np.concatenate((var, var2), axis=0)
print(ar)
print(ar1)

var = np.array([[1, 2], [3, 4]])
var2 = np.array([[3, 4], [5, 6]])
stack = np.stack((var, var2), axis=1)
print(stack)
var = np.array([[1, 2], [3, 4]])
var2 = np.array([[3, 4], [5, 6]])
hstack = np.hstack((var, var2))  # row
print(stack)
var = np.array([[1, 2], [3, 4]])
var2 = np.array([[3, 4], [5, 6]])
vstack = np.vstack((var, var2))  # columns
print(vstack)
var = np.array([[1, 2], [3, 4]])
var2 = np.array([[3, 4], [5, 6]])
dstack = np.dstack((var, var2))  # height
print(dstack)

# Split
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
ar_split = np.array_split(x, 3)
print(ar_split)
print(type(ar_split))
print(ar_split[0])

# 2d
x1 = np.array([[1, 2, 3, 9], [4, 5, 6, 7]])
ar_split1 = np.array_split(x1, 3)
print(ar_split1)
print(type(ar_split1))
ar_split12 = np.array_split(x1, 3, axis=1)
print(ar_split12)
