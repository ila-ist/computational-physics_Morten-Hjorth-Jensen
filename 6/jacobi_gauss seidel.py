import numpy as np


def jacobi_method(A, f, initial_guess, tol=1e-6, max_iterations=1000):
    n = len(A)
    x = initial_guess.copy()
    x_new = np.zeros_like(x)

    D = np.diag(np.diag(A))
    L = np.tril(A, k=-1)
    U = np.triu(A, k=1)

    for _ in range(max_iterations):
        for i in range(n):
            x_new[i] = (f[i] - np.dot((L + U)[i], x) + A[i][i] * x[i]) / A[i][i]

        if np.linalg.norm(x_new - x) < tol:
            return x_new

        x = x_new.copy()

    return x_new  # Returns the approximate solution


def gauss_seidel_method(A, f, initial_guess, tol=1e-6, max_iterations=1000):
    n = len(A)
    x = initial_guess.copy()
    x_new = np.zeros_like(x)

    for _ in range(max_iterations):
        for i in range(n):
            x_new[i] = (f[i] - np.dot(A[i, :i], x_new[:i]) - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

        if np.linalg.norm(x_new - x) < tol:
            return x_new

        x = x_new.copy()

    return x_new  # Returns the approximate solution


def calculate_f(n):
    h = 1 / (n + 1)
    f = np.zeros(n)
    for i in range(1, n + 1):
        f[i - 1] = h ** 2 * (i * h * 3.0 + (i * h) ** 2) * np.exp(i * h)
    return f




def A(n):
    main_diag = 2 * np.ones(n)
    sub_diag = -1 * np.ones(n - 1)

    A = np.diag(main_diag) + np.diag(sub_diag, k=1) + np.diag(sub_diag, k=-1)
    return A

n = 10

initial_guess = np.zeros(n)

solution = jacobi_method(A(n), calculate_f(n), initial_guess)
print("Solution using Jacobi's method:", solution)

solution = gauss_seidel_method(A(n), calculate_f(n), initial_guess)
print("Solution using Gauss-Seidel method:", solution)
