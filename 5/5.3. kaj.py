def f(x): # تعریف تابع دلخواه
    return 4 / (1 + x**2)

m = 2 # تعداد نقاط فرد

def sim(a, b): # قاعده سیمپسون
    sum = 0
    fa = f(a)
    fb = f(b)
    h = (b - a) / int(m)

    for i in range(1, m):
        x = a + i * h
        if i % 2 == 1:
            fx = 4 * f(x)
        else:
            fx = 2 * f(x)
        sum += fx

    result = ((fa + sum + fb) * h) / 3
    return result

a = 0
b = 1

res1 = sim(a, b)

m = 4

cou = 0
res2 = sim(a, b)

D = [[] for _ in range(int(m ** 0.5))]
print('d', D)

while abs(res2 - res1) > 1e-6: # richardson
    print(D)
    for i in range(int(m ** 0.5)):
        for j in range(i + 1):
            if j == 0:
                D[i].append(res1)
                res1 = res2
                res2 = sim(a, b)
            else:
                if len(D[i]) <= j:
                    D[i].append(0)  # اضافه کردن مقدار پیش‌فرض به زیرلیست
                D[i][j] = D[i][j - 1] + (D[i][j - 1] - D[i - 1][j - 1]) / ((4.0 ** j) - 1.0)

    m *= 2

    cou += 1
    #print(m)
    #print("     \nD\n  ", D)
    #print("result: ", D[int(m ** 0.5) -1][int(m ** 0.5) -1])
    #print(cou)
def f(x): # تعریف تابع دلخواه
    return 4 / (1 + x**2)

m = 2 # تعداد نقاط فرد

def sim(a, b): # قاعده سیمپسون
    sum = 0
    fa = f(a)
    fb = f(b)
    h = (b - a) / int(m)

    for i in range(1, m):
        x = a + i * h
        if i % 2 == 1:
            fx = 4 * f(x)
        else:
            fx = 2 * f(x)
        sum += fx

    result = ((fa + sum + fb) * h) / 3
    return result

a = 0
b = 1

res1 = sim(a, b)

m = 4

cou = 0
res2 = sim(a, b)

D = [[] for _ in range(int(m ** 0.5))]

while abs(res2 - res1) > 1e-6: # richardson
    for i in range(int(m ** 0.5)):
        for j in range(i + 1):
            if j == 0:
                D[i].append(res1)
                res1 = res2
                res2 = sim(a, b)
            else:
                if len(D[i]) <= j:
                    D[i].append(0)  # اضافه کردن مقدار پیش‌فرض به زیرلیست
                D[i][j] = D[i][j - 1] + (D[i][j - 1] - D[i - 1][j - 1]) / ((4.0 ** j) - 1.0)

    m *= 2
    cou += 1

# نمایش جواب نهایی بعد از پایان حلقه
print("Result:", D[int(m ** 0.5) -1][int(m ** 0.5) -1])
