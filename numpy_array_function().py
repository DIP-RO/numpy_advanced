import numpy as np

# search
var = np.array([1, 2, 2, 3, 4, 5, 6, 67, 4, 5, 67])
x = np.where(var == 2)  # where()
print(x)

# search sorted array
var = np.array([1, 2, 2, 3, 4, 5, 6, 7, 8])
x = np.searchsorted(var, 5)  # searchshorted()
x1 = np.searchsorted(var, 5, side="right")
x2 = np.searchsorted(var, [2, 3, 4], side="right")
print(x)
print(x1)
print(x2)

# sort()
var = np.array([1, 2, 2, 3, 4, 5, 6, 67, 4, 5, 67])
c = np.sort(var)
print(c)

# filter()
var3 = np.array(["a", "v", "c"])
f = [True, False, True]
c = var3[f]
print(c)

# shuffle
var = np.array([1, 2, 2, 3, 4, 5, 6, 7, 8])
np.random.shuffle(var)
print(var)

# unique
c = np.array([1, 1, 2, 2, 3, 4, 5, 6, 7, 8])
c1 = np.unique(c)
c2 = np.unique(c, return_index=True, return_counts=True)
print(c2)
print(c1)

# resize
c = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.resize(c, (3, 3))
print(y)

# flatten  (2d to 1d)
c = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.resize(c, (3, 3))
print(y.flatten())
print(y.flatten(order="F"))

# ravel
print("Ravel : ", np.ravel(y, order="F"))
