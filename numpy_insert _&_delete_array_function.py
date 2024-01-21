import numpy as np

# insert
var = np.array([1, 2, 3, 4, 5])
c = np.insert(var, 2, 40)
x = np.append(var, 5)
print(c)
print(x)

# 2d
var1 = np.array([[1, 2, 3], [4, 5, 6]])
v1 = np.insert(var1, 2, [22, 23, 24], axis=0)
v2 = np.append(var1, [[21, 2, 2]], axis=0)
print(v1)
print(v2)


#delete
var_d = np.array([1, 2, 3, 4, 5])
c = np.delete(var_d, 2)
print(c)
