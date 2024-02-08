from math import sin, cos, tan





class RootFindingMethods:
    def __init__(self, func, d_f):
        self.func = func
        self.d_f = d_f

    def bisection(self, a, b, xacc, iter_max):
        iterations = 0
        fa = self.func(a)
        fb = self.func(b)
        roots = []

        if fa == 0:
            roots.append(a)

        if fb == 0:
            roots.append(b)

        else:
            for i in range(iter_max):
                iterations += 1
                c = (a + b) / 2
                fc = self.func(c)

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
                print("Too many iterations in bisection method")
                return None
            else:
                return roots, iterations

    def newton(self, a, b, xacc, iter_max):
        iterations = 0
        roots = []
        r = (a + b) / 2

        for j in range(iter_max):
            iterations += 1
            f = self.func(r)
            df = self.d_f(r)

            if df == 0:
                print("Division by zero in newton method")
                return None

            dx = f / df
            r -= dx

            if (a - r) * (r - b) < 0:
                print("Jumped out newton")
                return None

            if abs(dx) < xacc:
                roots.append(r)
                break

        if iterations == iter_max:
            print("Too many iterations in newton method")
            return None
        else:
            return roots, iterations

    def secant(self, a, b, xacc, iter_max):
        iterations = 0
        roots = []

        for i in range(iter_max):
            fa, fb = self.func(a), self.func(b)

            if fb == fa:
                print("Division by zero in secant method")
                break
            c = (fb * a - fa * b) / (fb - fa)
            fc = self.func(c)

            a, b = b, c
            fa, fb = fb, fc

            iterations += 1

            if abs(fb - fa) < xacc:
                roots.append(c)
                break

        if iterations == iter_max:
            print("Too many iterations in secant method")
            return None
        else:
            return roots, iterations



m = 938
V = 60
a = 1.45
h = 41.33e-7 / (3.14*2) #hbar_ MeV * s

def func(E):
    k = ((m * (V - E)) ** 0.5) / h
    beta = ((m * E) ** 0.5) / h
    return k * (1 / tan(k * a)) + beta

def d_f(x):
    #return 2 * x
    #return 2 * x - 4 * sin(x) - 4 * x * cos(x) + 8 * sin(x) * cos(x)
    return 4 * x * sin(x) - 8 * cos(x) + 10

roots = RootFindingMethods(func, d_f)

bisection_res = []
newton_res = []
secant_res = []
intervals = [(1.9, 3),]

for interval in intervals:
    result_bisection = roots.bisection(interval[0], interval[1], 0.0001, 100)
    bisection_res.append(result_bisection)

    result_newton = roots.newton(interval[0], interval[1], 0.0001, 100)
    newton_res.append(result_newton)

    result_secant = roots.secant(interval[0], interval[1], 0.0001, 100)
    secant_res.append(result_secant)


print(f"root and iterations respectively by bisection {bisection_res}")
print(f"root and iterations respectively by newton    {newton_res}")
print(f"root and iterations respectively by secant    {secant_res}")