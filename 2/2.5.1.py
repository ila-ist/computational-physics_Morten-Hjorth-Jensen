import math


def quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        return x1, x2
    # Complex roots
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        x1 = complex(real_part, imaginary_part)
        x2 = complex(real_part, -imaginary_part)
        return x1, x2

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

x1, x2 = quadratic_equation(a, b, c)
print("The solutions are: ")
print("x1 =", x1)
print("x2 =", x2)
