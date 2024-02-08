

import numpy as np

class LegendreIntegral:
    def __init__(self, f):
        self.f = f

    def legendre(self, n):
        if n == 0:
            roots = np.array([0])
            weights = np.array([2])
        elif n == 1:
            roots = np.array([-np.sqrt(1/3), np.sqrt(1/3)])
            weights = np.array([1, 1])
        else:
            raise ValueError("This code handles only Legendre polynomials of degrees 0 and 1.")

        return roots, weights

    def calculate(self, n):
        roots, weights = self.legendre(n)
        result = np.sum(weights * self.f(roots))
        return result

def func(x):
    return x ** 2

integral = LegendreIntegral(func)
result = integral.calculate(1)
print("Approximated integral using Legendre polynomials:", result)
