import numpy as np

# matrix
var = np.matrix([[1, 2, 3], [4, 5, 6]])
print(var)
print(type(var))

var1 = np.array([[1, 2, 3], [4, 5, 6]])
print(var1)
print(type(var1))

# arithmetic operation in matrix
var = np.matrix([[1, 2, 3], [4, 5, 6]])
var1 = np.matrix([[1, 2, 3], [4, 5, 6]])
print("Addition: ", var + var1)

var = np.matrix([[1, 2, 3], [4, 5, 6]])
var1 = np.matrix([[1, 2, 3], [4, 5, 6]])
print("Subtract: ", var - var1)

# Multiplication
var = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
var1 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Multiplication: ", (var.dot(var1)))

# Matrix function in numpy arrays (transpose , swapaxes , inverse , power , determinate)
var = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.transpose(var))
print(np.swapaxes(var, 0, 1))

# inverse
c = np.matrix([[1, 2], [3, 4]])
print(np.linalg.inv(c))

# np.lanalg.Matrix_power(var , n) #power()
x = np.matrix([[1, 2], [3, 4]])
print(x)
print()
print(np.linalg.matrix_power(x, 2))
print(np.linalg.matrix_power(x, 0))
print(np.linalg.matrix_power(x, -2))

# determinante
x = np.matrix([[1, 2], [3, 4]])
print(np.linalg.det(x))
