x = float(input("Enter a real number: "))
xp = x + 1
xm = x - 1
x_p = []
x_m = []
while xp != x:
    xp = (x + xp) / 2
    x_p.append(xp)
    #print(xp)

while xm != x:
    xm = (x + xm) / 2
    x_m.append(xm)


print(x_p[-2])
print(x_m[-2])

# using numpy library
import numpy as np


x_minus = np.nextafter(x, float('-inf'))
x_plus = np.nextafter(x, float('inf'))

print(f"The two nearest machine numbers of {x} are {x_minus} and {x_plus}.")