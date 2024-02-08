from math import atan


def func(x):
    return atan(x)


def derivative(x, f, h):
    f3 = (f(x + h) - f(x - h)) / (2.0 * h)
    return f3



def lagrange(h, hi, fi):
    result = 0
    for i in range(len(hi)):
        term = fi[i]
        for j in range(len(hi)):
            if j != i:
                term *= (h - hi[j]) / (hi[i] - hi[j])

        result += term

    return result



x = 2 ** 0.5
h_val = 0.1

hi = []
fi = []


for jomle in range(5):
    hi.append(h_val)
    f_i = derivative(x, func, h_val)
    fi.append(f_i)
    h_val /= 2

print(hi, '\n', fi)
print(lagrange(0, hi, fi))