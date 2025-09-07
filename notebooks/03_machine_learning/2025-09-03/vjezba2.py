import numpy as np

x = int(input())
v1 = x * np.ones(10)
v2 = x * np.ones(10)

y = np.dot(v1, v2)
print(y)