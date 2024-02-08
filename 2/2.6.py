import numpy as np

x_single = np.float32(input("Enter a real number for single precision x: "))

x_double = np.float64(input("Enter a real number for double precision x: "))

print("Single Precision Information:")
print("Precision in bits:", np.finfo(np.float32).bits)
print("Smallest positive number:", np.finfo(np.float32).tiny)
print("Largest positive number:", np.finfo(np.float32).max)
print("Number of leading digits:", np.finfo(np.float32).precision)

print("Double Precision Information:")
print("Precision in bits:", np.finfo(np.float64).bits)
print("Smallest positive number:", np.finfo(np.float64).tiny)
print("Largest positive number:", np.finfo(np.float64).max)
print("Number of leading digits:", np.finfo(np.float64).precision)
