import numpy as np

# arithmetic operation(1d)
var = np.array([2, 3, 4, 5])
varAdd = var + 3
print(varAdd)

var1 = np.array([2, 3, 4, 5])
var12 = np.array([2, 3, 4, 5])
varAdd = var1 + var12
print(varAdd)

var = np.array([2, 3, 4, 5])
varAdd = var - 3
print(varAdd)

var = np.array([2, 3, 4, 5])
varAdd = var * 3
print(varAdd)

var = np.array([2, 3, 4, 5])
varAdd = var / 3
print(varAdd)

var = np.array([2, 3, 4, 5])
varAdd = var % 3
print(varAdd)

# using np

print("Using np:")
var1 = np.array([2, 3, 4, 5])
var12 = np.array([2, 3, 4, 5])
varAdd = np.add(var1, var12)
print(varAdd)

var1 = np.array([2, 3, 4, 5])
var12 = np.array([2, 3, 4, 5])
varAdd = np.subtract(var1, var12)
print(varAdd)

var1 = np.array([2, 3, 4, 5])
var12 = np.array([2, 3, 4, 5])
varAdd = np.divide(var1, var12)
print(varAdd)

var1 = np.array([2, 3, 4, 5])
var12 = np.array([2, 3, 4, 5])
varAdd = np.multiply(var1, var12)
print(varAdd)

var1 = np.array([2, 3, 4, 5])
var12 = np.array([2, 3, 4, 5])
varAdd = np.mod(var1, var12)
print(varAdd)

var1 = np.array([2, 3, 4, 5])
var12 = np.array([2, 3, 4, 5])
varAdd = np.power(var1, var12)
print(varAdd)

# reverse function
var = np.array([2, 3, 4, 5])
varAdd = np.reciprocal(var)
print(varAdd)

# 2d array

var2 = np.array([[2, 3, 4, 5], [2, 3, 4, 5]])
var22 = np.array([[2, 3, 4, 5], [2, 3, 4, 5]])
varAdd = np.add(var2, var22)
print(varAdd)
