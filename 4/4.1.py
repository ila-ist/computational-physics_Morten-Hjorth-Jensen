from math import sin, cos


def func(x):
    #return x ** 2 -1
    #return x ** 2 - 4 * x * sin(x) + (2 * sin(x)) ** 2
    return 2 * x - 4 * sin(x) - 4 * x * cos(x) + 8 * sin(x) * cos(x) #chon 3 rishe mozaaf vojud dare

def d_f(x):
    #return 2 * x
    #return 2 * x - 4 * sin(x) - 4 * x * cos(x) + 8 * sin(x) * cos(x)
    return 4 * x * sin(x) - 8 * cos(x) + 10


def bisection(a, b, xacc, iter_max):
    iterations = 0
    fa = func(a)
    fb = func(b)

    roots = []

    if fa == 0:
        roots.append(a)

    if fb == 0:
        roots.append(b)

    #if fa * fb > 0:
        #return "No roots found in this interval"

    else:
        for i in range(iter_max):
            iterations += 1
            c = (a + b) / 2
            fc = func(c)

            if abs(b - a) < xacc or abs(fc) < xacc:
                roots.append(c)
                break

            if fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc

        if iterations == iter_max:
            print("too many iterations in bisection method")
            return None
        else:
            return roots, iterations

def newton(a, b, xacc, iter_max):
    iterations = 0
    roots = []
    r = (a + b) / 2

    for j in range(iter_max):
        iterations += 1
        f = func(r)
        df = d_f(r)

        if df == 0:
            print("division by zero in newton")

        dx = f / df
        r -= dx

        if (a - r) * (r - b) < 0:
            print("jumped out")
            return None

        if abs(dx) < xacc:
            roots.append(r)
            break

    if iterations == iter_max:
        print("too many iterations by newton method")
        return None
    else:
        return roots, iterations


def secant(a, b, xacc, iter_max):
    iterations = 0
    roots = []

    for i in range(iter_max):
        fa, fb = func(a), func(b)

        if fb == fa:
            print("division by zero in secant ")
            break
        c = (fb * a - fa * b) / (fb - fa)
        fc = func(c)

        a, b = b, c
        fa, fb = fb, fc

        iterations += 1

        if abs(fb - fa) < xacc:
            roots.append(c)
            break

    if iterations == iter_max:
        print("Too many iterations by secant method")
        return None
    else:
        return roots, iterations


bisection_res = []
newton_res = []
secant_res = []
intervals = [(-1, 1), (1, 4), (-4, -1)]

for interval in intervals:
    result_bisection = bisection(interval[0],interval[1], 0.0001, 100)
    bisection_res.append(result_bisection)

    result_newton = newton(interval[0], interval[1], 0.0001, 100)
    newton_res.append(result_newton)

    result_secant = secant(interval[0], interval[1], 0.0001, 100)
    secant_res.append(result_secant)


print(f"root and iterations respectively by bisection {bisection_res}")
print(f"root and iterations respectively by newton    {newton_res}")
print(f"root and iterations respectively by secant    {secant_res}")


