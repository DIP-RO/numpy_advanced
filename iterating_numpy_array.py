import numpy as np

# iteration

var = np.array([9, 8, 6, 5, 4])
print(var)
print()
for i in var:
    print(i)
# 2d
c = np.array([[1, 2, 3, 4], [4, 5, 6, 7]])

for j in c:
    print(j)
    for k in j:
        print(k)
# 3d
c = np.array([[[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]]])
for j in c:
    print(j)
    for k in j:
        print(k)
        for x in k:
            print(x)

#using nditer()
c = np.array([[[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]]])
for i in np.nditer(c):
    print(i)
for i in np.nditer(c, flags=['buffered'],op_dtypes=["S"]):
    print(i)
for i in np.ndenumerate(c):
    print(i)