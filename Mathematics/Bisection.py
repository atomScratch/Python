import numpy as np
output = 1
accuracy = 0.00000001
def cube(x):
    return np.sin(float(x))

def rootfind(f, a, b):
    if (f(a) > 0) and (f(b) > 0):
        return("Both of those values are above the x-axis, try again!")
    elif (f(a) < 0) and (f(b) < 0):
        return("Both of those values are below the x-axis, try again!")
    while ((np.abs(f(a)) > accuracy) or (np.abs(f(b)) > accuracy)):
        if f((a+b)/2) > 0:
            a = (a+b)/2
        elif f((a+b)/2) < 0:
            b = (a+b)/2
        print((a+b)/2)
    return((a+b)/2)

print(rootfind(cube, 3, 3.5))