import numpy as np
from scipy.linalg import lu


A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

P, L, U = lu(A)

print("P:")
print(P)
print("L:")
print(L)
print("U:")
print(U)

n = A.shape[0]
flops = 2/3 * n**3 + 2 * n**2 - 2/3 * n
print("Number of floating point operations:", flops)
