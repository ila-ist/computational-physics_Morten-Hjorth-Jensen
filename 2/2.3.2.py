x = float(input())
from math import sin
S = x # جمله اول
jomle = 1
l_sin = []
while abs(x) < 1.9:
    l_sin.append(S)
    S = S * -(x ** 2) / ((2 * jomle + 1) * (2 * jomle))
    jomle += 1
    #print("s", S)
    #print("x", x)
    #print(jomle)
    #print(l_sin)
    if abs(S) < 1e-6:  # شرط متوقف کردن سری مکلارین برای دقت مناسب
        break

l_sin.reverse()
sin_x = sum(l_sin) #  series expansions of sinx answer
#print(sin_x)
#print(math.sin(0.5))


fx = x - sin(x)
f_x = x - sin_x
print('dd', fx)
print('ee', f_x)

if abs(x) >= 1.9:
    print(fx)
else:
    print(f_x)