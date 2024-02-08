import matplotlib.pyplot as plt
import numpy as np

# Define the functions
def f(x):
    return x**2 - 4 * x * np.sin(x) + (2 * np.sin(x))**2

# Generate x values
x_values = np.linspace(-10, 10, 500)  # Adjust the range as needed

# Calculate corresponding y values for function f(x)
y_f = f(x_values)

# Plot f(x)
plt.plot(x_values, y_f, label='f(x) = x^2 - 4x*sin(x) + (2*sin(x))^2')

# Plot g(x) = 0 line by creating a horizontal line at y=0 for the same x range
plt.axhline(y=0, color='red', linestyle='--', label='g(x) = 0')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of x^2 - 4x*sin(x) + (2*sin(x))^2 = 0')
plt.legend()
plt.grid()
plt.show()
