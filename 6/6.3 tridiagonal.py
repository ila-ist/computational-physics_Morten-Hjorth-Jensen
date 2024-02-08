import numpy as np
import matplotlib.pyplot as plt


def calculate_f(n):
    h = 1 / (n + 1)
    f = np.zeros(n)
    for i in range(1, n + 1):
        f[i - 1] = h ** 2 * (i * h * 3.0 + (i * h) ** 2) * np.exp(i * h)
    return f


def solve_tridiagonal(f):
    n = len(f)
    a = np.ones(n - 1) * (-1.0)
    b = np.ones(n) * 2.0
    c = np.ones(n - 1) * (-1.0)
    u = np.zeros(n)  # Solution array

    temp = np.zeros(n - 1)

    btemp = b[0]

    for i in range(1, n):
        temp[i - 1] = c[i - 1] / btemp
        btemp = b[i] - a[i - 1] * temp[i - 1]
        u[i] = (f[i] - a[i - 1] * u[i - 1]) / btemp

    for i in range(n - 2, -1, -1):
        u[i] -= temp[i] * u[i + 1]

    return u


n_values = [10, 100, 1000]
for n in n_values:
    solution = solve_tridiagonal(calculate_f(n))
    x = np.linspace(0, 1, n+2)[1:-1]  # Generating x values excluding boundary points
    plt.plot(x, solution, label=f'n = {n}')

plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.title('Solution of the Tridiagonal System')
plt.show()
