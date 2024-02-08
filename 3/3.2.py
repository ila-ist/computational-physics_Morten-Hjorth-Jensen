import numpy as np
from math import atan
#Richardson Extrapolation

# تابع دلخواه
def function(x):
    return atan(x)


def richardson_derivative(f, x, h, dime):
    D = np.zeros((dime, dime), dtype=float)
    for i in range(dime):
        for j in range(i + 1):
            if j == 0:
                D[i][j] = (f(x + h) - f(x - h)) / (2.0 * h) #مشتق سه نقطه ای

            else:
                D[i][j] = D[i][j - 1] + (D[i][j - 1] - D[i - 1][j - 1]) / ((4.0 ** j) - 1.0)  #????
        h /= 2.0

    #print(D)

    return D[dime - 1, dime - 1]

# نقطه‌ی شروع و تعداد مراحل تقسیم
x_value = 2 ** 0.5
h_value = 0.1
iterations = 4

#نتیجه
result = richardson_derivative(function, x_value, h_value, iterations)
print("مقدار مشتق در نقطه x =", x_value, "میشه:", result)

