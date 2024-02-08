# پیاده سازی trapez و simps
def f(x): # تعریف تایع دلخواه
    return float(2*x)

def trapez(a, b, n):# trapezodial rule
    sum = 0
    fa = f(a) / 2
    fb = f(b) / 2
    h = (b-a) / int(n)

    for i in range(1, n):
        x = a + h * i
        sum += f(x)

    result = h * (fa + sum + fb)
    return result


def sim(a, b, n): #simpson's rule
    sum = 0
    fa = f(a)
    fb = f(b)
    h = (b - a) / int(n)

    for i in range(1, n):
        x = a + i*h
        if i % 2 == 1:
            fx = 4 * f(x)
        else:
            fx = 2 * f(x)
        #print(fx)
        sum += fx
        #print(sum)
    result = ((fa + sum + fb) * h) / 3
    return result

print(sim(1, 3, 4))