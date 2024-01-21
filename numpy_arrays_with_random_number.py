import numpy as np

# random #rand() #0-1 limit
var = np.random.rand(4)  # 1dim
print(var)
var1 = np.random.rand(3, 2)  # 2dim
print(var1)

# random #randn() #close to zero(+) or (-)
var3 = np.random.randn(5)  # 1dim
print(var3)
var4 = np.random.randn(3, 2)  # 2dim
print(var4)

# random #ranf() #[0.0 , 1.0) limit
print("ranf:")
var5 = np.random.ranf(6)  # 1dim
print(var5)

# random #randint() #(min , max, total_values)
print("randint:")
var6 = np.random.randint(6, 10, size=4)  # 1dim
print(var6)
var6 = np.random.randint(6, 10, 4)  # 1dim
print(var6)
