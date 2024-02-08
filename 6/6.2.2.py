import numpy as np
from scipy.linalg import lu_factor, lu_solve


#Cholesky Decomposition
def cholesky_decomposition(A):
    n = len(A)
    L = np.zeros_like(A)

    for i in range(n):
        for j in range(i+1):
            if i == j:
                L[i, j] = np.sqrt(A[i, i] - np.sum(L[i, :j]**2))
            else:
                L[i, j] = (A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]

    return L

def solve_linear_equations_cholesky(A, b):
    L = cholesky_decomposition(A)
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(L.T, y)

    return x

def solve_linear_equations_lu(A, b):
    LU = lu_factor(A)
    x = lu_solve(LU, b)

    return x


A = np.array([[0.05, 0.07, 0.06, 0.05],
              [0.07, 0.10, 0.08, 0.07],
              [0.06, 0.08, 0.10, 0.09],
              [0.05, 0.07, 0.09, 0.10]])

b = np.array([0.23, 0.32, 0.33, 0.31])

x_cholesky = solve_linear_equations_cholesky(A, b)
print("Solution using Cholesky method:")
print(x_cholesky)

x_lu = solve_linear_equations_lu(A, b)
print("\nSolution using LU decomposition:")
print(x_lu)
