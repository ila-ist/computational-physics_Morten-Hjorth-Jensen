import matplotlib.pyplot as plt
import numpy as np

x = 2 ** 0.5


def f_2(h):
    f_p2 = (np.arctan(x + h) - np.arctan(x)) / h
    return f_p2


def f_3(h):
    f_p3 = (np.arctan(x + h) - np.arctan(x - h)) / (2 * h)
    return f_p3


h = np.arange(1e-7, 1e-3, step=1e-7)
lg_h = np.log10(h)
lg_f2_single = []
lg_f3_single = []

for h_val in h:
    f2_single = f_2(h_val)
    f3_single = f_3(h_val)

    lg_f2_single.append(np.log10(abs((f2_single - 1 / 3)) / (1 / 3)))
    lg_f3_single.append(np.log10(abs((f3_single - 1 / 3)) / (1 / 3)))

plt.figure(figsize=(8, 6))
plt.plot(lg_h, lg_f2_single, label='f2 single pr')
plt.plot(lg_h, lg_f3_single, label='f3 single pr')

plt.xlabel('log10(h)')
plt.ylabel('log10(abs((f - 1 / 3)) / (1 / 3))')

plt.legend()
plt.grid(True)
plt.show()