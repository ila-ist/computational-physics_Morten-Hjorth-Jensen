import numpy as np
import matplotlib.pyplot as plt

def solve_poisson_equation(n, potential_type, V0=1):
    h = 1.0 / (n + 1)
    x = np.linspace(0, 1, n+2)

    if potential_type == 1:
        u = V0 * (x / x[-1])**(4/3)
    elif potential_type == 2:
        u = V0 * (x / x[-1])**2
    elif potential_type == 3:
        u = x * (1 - x) * np.exp(x)
    else:
        raise ValueError("Invalid potential type")

    return x, u


def solve_poisson_equation_jacobi(n, potential_type, V0=1):
    h = 1.0 / (n + 1)  # step ha
    x = np.linspace(0, 1, n+2)

    if potential_type == 1:
        u = V0 * (x / x[-1])**(4/3)
    elif potential_type == 2:
        u = V0 * (x / x[-1])**2
    elif potential_type == 3:
        u = x * (1 - x) * np.exp(x)
    else:
        raise ValueError("Invalid potential type")


    u_jacobi = np.copy(u)
    max_iterations = 1000
    tolerance = 1e-6

    for _ in range(max_iterations):
        u_new = np.zeros_like(u)
        for i in range(1, n+1):
            u_new[i] = 0.5 * (u[i-1] + u[i+1] - h**2 * u[i])
        if np.linalg.norm(u_new - u_jacobi) < tolerance:
            break
        u_jacobi = np.copy(u_new)

    return x, u_jacobi


def solve_poisson_equation_gauss_seidel(n, potential_type, V0=1):
    h = 1.0 / (n + 1)  # step ha
    x = np.linspace(0, 1, n+2)

    if potential_type == 1:
        u = V0 * (x / x[-1])**(4/3)
    elif potential_type == 2:
        u = V0 * (x / x[-1])**2
    elif potential_type == 3:
        u = x * (1 - x) * np.exp(x)
    else:
        raise ValueError("Invalid potential type")

    u_gauss_seidel = np.copy(u)
    max_iterations = 1000
    tolerance = 1e-6

    for _ in range(max_iterations):
        for i in range(1, n+1):
            u_gauss_seidel[i] = 0.5 * (u_gauss_seidel[i-1] + u_gauss_seidel[i+1] - h**2 * u_gauss_seidel[i])
        if np.linalg.norm(u_gauss_seidel - u) < tolerance:
            break

    return x, u_gauss_seidel

x, u = solve_poisson_equation(100, 1, V0=1)
plt.plot(x, u, label='Case 1: φ = V0 * (x/d)^(4/3)')

x, u = solve_poisson_equation(100, 2, V0=2)
plt.plot(x, u, label='Case 2: φ = V0 * (x/d)^2')

x, u = solve_poisson_equation(100, 3)
plt.plot(x, u, label='Case 3: φ = x(1 - x) * exp(x)')

x, u_jacobi = solve_poisson_equation_jacobi(100, 1, V0=1)
plt.plot(x, u_jacobi, label='Jacobi Method: Case 1')

x, u_gauss_seidel = solve_poisson_equation_gauss_seidel(100, 1, V0=1)
plt.plot(x, u_gauss_seidel, label='Gauss-Seidel Method: Case 1')

plt.xlabel('x')
plt.ylabel('φ(x)')
plt.title('Solutions of the Poisson Equation')
plt.legend()
plt.show()
