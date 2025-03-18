# f = x^2 + y^2 - xy - x - y

import numpy as np
def f(x):
    return x[0]**2 + x[1]**2 - x[0]*x[1] - x[0] - x[1]
def df(x):
    return np.array([2*x[0] - x[1] - 1, 2*x[1] - x[0] - 1])
def Hf(x):
    return np.array([[2, -1], [-1, 2]])

# this method derives from the base Newton method for finding roots of a function.
def newton(x0):
    x = x0
    for i in range(10):
        iH = np.linalg.inv(Hf(x))
        D = df(x).T
#         print('df = ', D)
        y = iH.dot(D)
        if np.linalg.norm(y) == 0:
            break
        x = x - y
    return (x, f(x), i)

def GD(alpha, x0):
    x = x0
    for i in range(1000):
        if np.linalg.norm(df(x)) < 1e-3:
            break
        x = x - alpha*df(x)
    return (x, f(x), i)
    
print(newton(np.array([-5, -5])))
print(GD(1e-2, np.array([-5, -5])))