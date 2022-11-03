import numpy as np
a = [[1, 2, 3], [4, 5, 6]]
b = [[3, 2, 1], [6, 5, 4]]
c = [[1, 2], [2, 4], [2, 3]]
A = np.array(a)
B = np.array(b)
C = np.array(c)
E = A * B
D = A @ C
print(C)
print(D)