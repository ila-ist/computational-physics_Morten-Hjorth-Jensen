def laguerre_polynomial(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return 1 - x
    else:
        L = [1, 1 - x]
        for i in range(2, n + 1):
            Ln = ((2 * i - 1 - x) * L[i - 1] - (i - 1) * L[i - 2]) / i
            L.append(Ln)
        return L


def hermite_polynomial(n, x):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 2 * x]
    else:
        H = [1, 2 * x]
        for i in range(2, n + 1):
            Hn = 2 * x * H[i - 1] - 2 * (i - 1) * H[i - 2]
            H.append(Hn)
        return H

n = 4
x = 2

laguerre_result = laguerre_polynomial(n, x)
print("Laguerre Polynomials:")
for i in range(n + 1):
    print(f"L{i}({x}) = {laguerre_result[i]}")

hermite_result = hermite_polynomial(n, x)
print("\nHermite Polynomials:")
for i in range(n + 1):
    print(f"H{i}({x}) = {hermite_result[i]}")
