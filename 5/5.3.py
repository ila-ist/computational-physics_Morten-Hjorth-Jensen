import numpy as np


class integration:
    def __init__(self, f):
        self.f = f


    def simpson(self, a, b, m):
        sum_val = 0
        fa = self.f(a)
        fb = self.f(b)
        h = (b - a) / int(m)

        for i in range(1, m):
            x = a + i * h
            if i % 2 == 1:
                fx = 4 * self.f(x)
            else:
                fx = 2 * self.f(x)
            sum_val += fx

        result = ((fa + sum_val + fb) * h) / 3
        return result


    def richardson(self, h, dime):
        D = np.zeros((dime, dime), dtype=float)
        for i in range(dime):
            for j in range(i + 1):
                if j == 0:
                    D[i][j] = self.simpson(0, 1, 2 ** (i + 1))
                else:
                    D[i][j] = D[i][j - 1] + (D[i][j - 1] - D[i - 1][j - 1]) / ((4.0 ** j) - 1.0)  # ??
            h /= 2.0
        return D

def function(x):
    return 4 / (1 + x ** 2)


a = 0
b = 1


integration = integration(function)
result = integration.richardson(1, 4)
print(result)
