import math
import matplotlib.pyplot as plt

def f(x):
    return math.exp(x)

def second_derivative(x, h):
    if h < 1e-10:  # Minimum threshold for h to avoid division by zero
        h = 1e-10
    return (f(x + h) - 2*f(x) + f(x - h)) / (h**2)

def compute_error_ratio(derivative_computed, derivative_exact):
    return math.log10(abs(derivative_computed - derivative_exact) / abs(derivative_exact))

x = 10
exact_second_derivative = math.exp(x)

# Step length values
num_steps = 10
h_values = [1/(10**i) for i in range(1, num_steps+1)]

# Computed second derivatives for single and double precision
second_derivatives_single = []
second_derivatives_double = []

# Compute second derivatives and error ratios
error_ratios_single = []
error_ratios_double = []

for h in h_values:
    hp = round(h, 7)
    second_derivative_single = second_derivative(x, hp) # ????????????????
    second_derivative_double = second_derivative(x, h)

    second_derivatives_single.append(second_derivative_single)
    second_derivatives_double.append(second_derivative_double)

    error_ratio_single = compute_error_ratio(second_derivative_single, exact_second_derivative)
    error_ratio_double = compute_error_ratio(second_derivative_double, exact_second_derivative)

    error_ratios_single.append(error_ratio_single)
    error_ratios_double.append(error_ratio_double)

# Plot the error ratios
log_h_values = [math.log10(h) for h in h_values]

plt.plot(log_h_values, error_ratios_single, label='Single Precision')
plt.plot(log_h_values, error_ratios_double, label='Double Precision')

plt.xlabel('log10(h)')
plt.ylabel('log10(|f\'\'computed - f\'\'exact| / |f\'\'exact|)')
plt.legend()
plt.grid(True)
plt.show()