import numpy as np

var2 = np.array([2, 3, 4, 5, 2, 3, 4, 5])
print("min: ", np.min(var2), np.argmin(var2))
print("max: ", np.max(var2), np.argmax(var2))
print('SQRT: ', np.sqrt(var2))
print('sin: ', np.sin(var2))
print('cos: ', np.cos(var2))
print('cumsum: ', np.cumsum(var2))

var22 = np.array([[2, 3, 4, 5], [2, 3, 4, 5]])
print(np.min(var22, axis=1))
var22 = np.array([[2, 3, 4, 5], [2, 3, 4, 5]])
print(np.min(var22, axis=0))
