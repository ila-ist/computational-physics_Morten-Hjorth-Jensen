import numpy as np

A = np.array([[-1.0, 1.0, -4.0],
              [2.0, 2.0, 0.0],
              [3.0, 3.0, 2.0]])
w = np.array([0.0, 1.0, 0.5])

# Gaussian elimination:
n = len(w)

for i in range(n - 1):
    max_row = i
    for j in range(i + 1, n):
        if abs(A[j, i]) > abs(A[max_row, i]):
            max_row = j
    A[[i, max_row]] = A[[max_row, i]]
    w[[i, max_row]] = w[[max_row, i]]

    # Elimination
    for j in range(i + 1, n):
        factor = A[j, i] / A[i, i]
        A[j, i:] -= factor * A[i, i:]
        w[j] -= factor * w[i]

x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = (w[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]


print("Solution:")
for i in range(n):
    print(f"x{i + 1} = {x[i]}")
