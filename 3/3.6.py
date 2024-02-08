from numpy import arctan


def f(x):
    return arctan(x)


class Derivative:
    def __init__(self, x, h):
        self.x = x
        self.h = h

    def f_2(self):
        f2c = (f(self.x + self.h) - f(self.x)) / self.h
        print('f2c =', f2c)

    def f_3(self):
        f3c = (f(self.x + self.h) - f(self.x - self.h)) / (2 * self.h)
        print('f3c =', f3c)

    def f_5(self):
        f5c = (f(self.x - 2 * self.h) - 8 * f(self.x - self.h) + 8 * f(self.x + self.h) - f(self.x + 2 * self.h)) / (
                    12 * self.h)
        print('f5c =', f5c)


a = Derivative(2 ** 0.5, 10e-5)

a.f_2()
a.f_3()
a.f_5()
