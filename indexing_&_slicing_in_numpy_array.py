import numpy as np

# indexing

var = np.array([1, 2, 3, 4])
#               0 1 2 3
#              -4 -3-2-1
print(var[-1])
# 2d
var1 = np.array([[1, 2, 3], [3, 4, 5]])
print(var1)
print(var1.ndim)
print(var1[0][1])
print(var1[1][2])
print(var1[0, 2])

# 3d
var3 = np.array([[[6, 7, 8], [9, 10, 11], [12, 13, 14]]])
print(var3)
print(var3.ndim)
print(var3[0][2][2])
var3 = np.array([[[6, 7, 8], [9, 10, 11], [12, 13, 14]], [[1, 2, 34], [35, 36, 37], [0, 0, 0]]])
print(var3)
print(var3.ndim)
print(var3[1][1][1])

# slicing
# x[start,stop,step]
print("SLicing part:")
var = np.array([1, 2, 3, 4, 5, 6, 7])
print(var)
print()
print("2 to 5: ", var[1:5])
print("1 to 3: ", var[0:3])
print("2 to end: ", var[1:])
print("step : ", var[::2])
print("2 to 5: ", var[1:5:2])

# 2d
var1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(var1)
print(var1[1, 1:4])
