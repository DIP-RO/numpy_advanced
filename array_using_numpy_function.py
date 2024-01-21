import numpy as np

# zeros

ar_zero = np.zeros(4)
ar_zero1 = np.zeros((3, 4))
print(ar_zero)
print()
print(ar_zero1)

# ones

ar_one = np.ones(4)
ar_one1 = np.ones((3, 4))
print(ar_one)
print()
print(ar_one1)

# empty
print("empty:")
ar_empty = np.empty(4)
ar_empty1 = np.empty((3, 4))
print(ar_empty)
print()
print(ar_empty1)

# range

print("Range:")
ar_rn = np.arange(4)
print(ar_rn)
print()

# diagonal

print("Digonal:")
ar_dig = np.eye(4)
print(ar_dig)
print()
ar_dig1 = np.eye(3, 5)
print(ar_dig1)
print()

# linspace

print("Linspace:")
ar_lin = np.linspace(1, 10, num=5)
print(ar_lin)
print()
