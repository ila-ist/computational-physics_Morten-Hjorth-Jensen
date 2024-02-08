import numpy as np


def recurrence_relation(N, x):
    b = np.zeros(N + 1)
    b[0] = 2
    b[1] = 2 * np.cos(x) * 2 + 1.5

    for n in range(2, N + 1):
        b[n] = 2 * np.cos(x) * b[n - 1] - b[n - 2] + (n + 2) / (n + 1)

    return b[N - 1] - b[N] * np.cos(x)

def compute_series(N, x):
    f_series = 0.0
    for n in range(N + 1):
        an = (n + 2) / (n + 1)
        f_series += an * np.cos(n * x)
    return f_series

a = recurrence_relation(1000, 0)
b = compute_series(1000, 0)
print('',a,'\n', b)
