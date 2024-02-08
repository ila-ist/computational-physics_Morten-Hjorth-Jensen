from math import sin
x = 1.
eps = 1e-4
coun = 0
while sin(x) / x - 1/2 >= eps:
    x += 1e-4
    coun += 1
    print(coun, x)
