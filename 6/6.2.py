import numpy as np

def lu_decomposition(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        L[i][i] = 1.0

    for k in range(n):
        U[k][k] = A[k][k]
        for j in range(k+1, n):
            L[j][k] = A[j][k] / U[k][k]
            U[k][j] = A[k][j]
        for i in range(k+1, n):
            for j in range(k+1, n):
                A[i][j] -= L[i][k] * U[k][j]

    return L, U

def solve_linear_equations(A, b):
    L, U = lu_decomposition(A)
    n = len(A)
    y = [0.0] * n
    x = [0.0] * n

    # ghesmat e Ly = b
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
        y[i] /= L[i][i]

    # ghesmat e Ux = y
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return x


A = [[6, 3, 2], [3, 2, 1], [2, 1, 1]]
L, U = lu_decomposition(A)
print("LU decomposition:")
print("L =", L)
print("U =", U)


A = np.array([[0.05, 0.07, 0.06, 0.05],
              [0.07, 0.10, 0.08, 0.07],
              [0.06, 0.08, 0.10, 0.09],
              [0.05, 0.07, 0.09, 0.10]])
b = np.array([0.23, 0.32, 0.33, 0.31])

x = solve_linear_equations(A, b)
print("\nSolution using LU decomposition:")
print(x)
