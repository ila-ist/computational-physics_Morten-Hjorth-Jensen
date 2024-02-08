from math import factorial, pi, cos
from cmath import exp
import numpy as np
import matplotlib.pyplot as plt

#double factorial
def double_factorial(x):
    if x < 0:
        return 1  # pi**0.5
    result = 1
    for i in range(x, 0, -2):
        result *= i
    return result

# Legendre polynomial
def P(M, L, x):
    if L == M:
        return ((-1) ** M) * double_factorial(2 * M - 1) * ((1 - x ** 2) ** (M / 2))
    elif L == M + 1:
        return x * (2 * M + 1) * P(M, M, x)
    else:
        return ((2 * L - 1) * x * P(M, L - 1, x) - (L + M - 1) * P(M, L - 2, x)) / (L - M)

#spherical harmonics
def spherical_harmonics(M, L, theta, phi):
    x = cos(theta)
    prefactor = (((2 * L + 1) * factorial(L - M)) / (4 * pi * factorial(L + M)))**0.5
    associated_legendre = P(M, L, x)
    exponential_term = exp(1j * M * phi)
    real_part = prefactor * associated_legendre * exponential_term.real
    return real_part

theta_values = np.linspace(pi / 2 - 0.1, pi / 2 + 0.1, 50)
theta_valuess = np.linspace(0, pi, 50)# Array of theta values from 0 to pi
phi_value = 0  # Setting phi value to 0

L_values = [0, 1, 2, 3, 4, 5, 20]  # Values of L = M to plot
plt.figure(figsize=(10, 6))

# Loop through L values to plot spherical harmonics for various L = M
for L in L_values:
    M = L  # Setting M to be equal to L
    Y_values = [spherical_harmonics(M, L, theta, phi_value) for theta in theta_values]
    Y_valuess = [spherical_harmonics(M, L, theta, phi_value) for theta in theta_valuess]
    plt.plot(theta_valuess, Y_valuess, label=f'L = {L}s')
    plt.plot(theta_values, Y_values, label=f'L = {L}')  # Plotting Y_M^L(θ, φ=0) for current L
      # Plotting Y_M^L(θ, φ=0) for current L

plt.title('Spherical Harmonics for Various L = M as Functions of θ (φ = 0)')
plt.xlabel('θ (radians)')
plt.ylabel('Y_M^L(θ, φ=0)')
plt.legend()  # Show legend indicating the values of L
plt.grid(True)  # Display grid
plt.show()  # Show the plot
