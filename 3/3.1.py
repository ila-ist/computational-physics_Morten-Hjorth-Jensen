import matplotlib.pyplot as plt
import numpy as np
import sympy
# نتیجه به نظر درست نمیاد.... میتونم دستی h رو محدود کنم برای precision
# 15 و 7 رقم اعشار
# مقدار دقیق
x = 2**0.5

#precision


def f_2(h, precision=np.float64):
    h = round(h, 5)
    f_p2 = (sympy.atan(x + precision(h)) - sympy.atan(x)) / precision(h) # two point
    return f_p2

def f_3(h, precision=np.float64):
    f_p3 = (sympy.atan(x + precision(h)) - sympy.atan(x - precision(h))) / (2 * precision(h)) #three point
    return f_p3

h = np.arange(1e-7, 1e-3, step=1e-7)
lg_h = np.log10(h)
lg_f2_single = []
lg_f3_single = []
lg_f2_double = []
lg_f3_double = []

for h_val in h:
    f2_single = np.array(f_2(h_val, np.float32), dtype=np.float32)
    f3_single = np.array(f_3(h_val, np.float32), dtype=np.float32)
    f2_double = np.array(f_2(h_val, np.float64), dtype=np.float64)
    f3_double = np.array(f_3(h_val, np.float64), dtype=np.float64)

    lg_f2_single.append(np.log10(abs((f2_single - 1 / 3)) / (1 / 3)))
    lg_f3_single.append(np.log10(abs((f3_single - 1 / 3)) / (1 / 3)))
    lg_f2_double.append(np.log10(abs((f2_double - 1 / 3)) / (1 / 3)))
    lg_f3_double.append(np.log10(abs((f3_double - 1 / 3)) / (1 / 3)))

plt.figure(figsize=(8, 6))
plt.plot(lg_h, lg_f2_single, label='f2 single pr')
plt.plot(lg_h, lg_f3_single, label='f3 single pr')
plt.plot(lg_h, lg_f2_double, label='f2 double pr')
plt.plot(lg_h, lg_f3_double, label='f3 double pr')

plt.xlabel('log10(h)')
plt.ylabel('log10(abs((f - 1 / 3)) / (1 / 3))')

plt.legend()
plt.grid(True)
plt.show()
