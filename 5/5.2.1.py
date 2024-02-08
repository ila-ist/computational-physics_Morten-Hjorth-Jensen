def f(x): # تعریف تایع دلخواه
    #return float(x ** 3)
    return 4 / (1 + x**2)

n = 1
m = 2 # تعداد نقاط فرد..
def trapez(a, b):# trapezodial rule
    sum = 0
    fa = f(a) / 2
    fb = f(b) / 2
    h = (b-a) / int(n)
    #print('n: ', n)
    for i in range(1, n):
        x = a + h * i
        sum += f(x)

    result = h * (fa + sum + fb)
    return result


def sim(a, b): #simpson's rule
    sum = 0
    fa = f(a)
    fb = f(b)
    h = (b - a) / int(m)
    #print('m: ', m)

    for i in range(1, m):
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



a = float(input("a: "))
b = float(input("b: "))

result1 = trapez(a, b)
res1 = sim(a, b)

n = 2
m = 4

result2 = trapez(a, b)
res2 = sim(a, b)

while abs(result2 - result1) > 1e-3: #adaptive trapez
    n += 1
    result1 = result2
    result2 = trapez(a, b)
    #print(result1 - result2)

    #print('trapez result: ', result2)


while abs(res2 - res1) > 1e-3: #adaptive simp
    m += 2 #وقتی m فرد هست جواب غیر دقیق
    res1 = res2
    res2 = sim(a, b)
    #print(result1 - result2)

    #print('simp result              : ', res2)


print('in trapez when n is', n, 'the result is: ', result2)
print('in simp when m is', m, 'the result is: ', res2)
