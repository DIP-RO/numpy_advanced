import numpy as np
var = np.array([1,2,3,4])
co = var.copy()
var[2] = 40
print("Var: ", var)
print("copy: ", co)

var = np.array([6,7,8,9])
vi = var.view()
var[2] = 5
print("Var: ", var)
print("View: ", vi)