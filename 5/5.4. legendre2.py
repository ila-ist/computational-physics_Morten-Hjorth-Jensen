import numpy as np

class LegendreIntegral:
    def __init__(self, f):
        self.f = f
        self.degrees = {
            0: (np.array([0]), np.array([2])),
            1: (np.array([-np.sqrt(1/3), np.sqrt(1/3)]), np.array([1, 1])),
            2: (np.array([-0.57735, 0, 0.57735]), np.array([0.555556, 0.888889, 0.555556])),
            3: (np.array([-0.774597, -0.339981, 0.339981, 0.774597]), np.array([0.347855, 0.652145, 0.652145, 0.347855])),
            4: (np.array([-0.861136, -0.339981, 0.339981, 0.861136]), np.array([0.236927, 0.478629, 0.478629, 0.236927])),
            5: (np.array([-0.90618, -0.538469, 0, 0.538469, 0.90618]), np.array([0.236927, 0.478629, 0.568889, 0.478629, 0.236927]))
        }

    def calculate(self, n):
        roots, weights = self.degrees[n]
        result = np.sum(weights * self.f(roots))
        return result

def func(x):
    return x ** 3

integral = LegendreIntegral(func)
result = integral.calculate(4)
print("Approximated integral using Legendre polynomials:", result)
