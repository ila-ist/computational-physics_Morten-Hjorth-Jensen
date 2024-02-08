# ایمپورت کردن کتابخانه‌های مورد نیاز
import numpy as np
import matplotlib.pyplot as plt

# تابع برای محاسبه جمع اعداد از ۱ تا N برای sup و sdown
def calculate_sums(N, precision=np.float64):
    sup = np.sum([1 / n for n in range(1, N + 1)], dtype=precision)  # جمع سری sup
    sdown = np.sum([1 / n for n in range(N, 0, -1)], dtype=precision)  # جمع سری sdown
    print(type(sup))
    return sup, sdown


# تابع برای مقایسه sup و sdown برای مقادیر مختلف N
def compare_sums():
    N_values = np.power(10, np.arange(1, 7))  # مقادیر N از 10^1 تا 10^10
    relative_differences_single = []  # لیست برای single
    relative_differences_double = []  # لیست برای double

    for N in N_values:
        sup_single, sdown_single = calculate_sums(int(N), np.float32)# محاسبه sup و sdown با دقت single
        #print(sup_single, sdown_single)
        sup_double, sdown_double = calculate_sums(int(N), np.float64)  # محاسبه sup و sdown با دقت double
        #print(sup_double, sdown_double)
        relative_diff_single = np.abs((sup_single - sdown_single) / sdown_single)  # محاسبه نسبت single
        relative_diff_double = np.abs((sup_double - sdown_double) / sdown_double)  # محاسبه نسبت double

        relative_differences_single.append(relative_diff_single)  # اضافه به لیست...
        relative_differences_double.append(relative_diff_double)

    log_N_values = np.log10(N_values)  # x_
    log_relative_diff_single = np.log10(relative_differences_single)  # y- single
    log_relative_diff_double = np.log10(relative_differences_double)  # y- double

    plt.figure(figsize=(8, 6))  # ایجاد شکل برای نمودار
    plt.plot(log_N_values, log_relative_diff_single, marker='x', label='Single Precision')
    plt.plot(log_N_values, log_relative_diff_double, marker='.', label='Double Precision')
    plt.xlabel('log10(N)')  # برچسب محور x
    plt.ylabel('log10(|(sup(N)-sdown(N))/sdown(N)|)')  # برچسب محور y
    plt.title('Relative Difference between sup and sdown for different N')  # عنوان نمودار
    plt.legend()  # نمایش نام خطوط در نمودار
    plt.grid(True)
    plt.show()
    print(type(log_N_values))


compare_sums()

