import numpy as np

x = [1, 2, 3, 4, 5]
y = np.array(x)
print(y)
print(type(y))
print(y.ndim)

# user input
l = []
for i in range(1, 3):
    int_1 = int(input("enter value:"))
    l.append(int_1)

print(np.array(l))


# 2dim
ar2 = np.array([[1, 2, 3], [2, 3, 4]])
print(ar2)
print(ar2.ndim)


# 3dim
ar3 = np.array([[[1, 2, 3], [2, 3, 4]]])
print(ar3)
print(ar3.ndim)


# Ndim
arn = np.array([1, 2, 3], ndmin=10)
print(arn)
print(arn.ndim)
