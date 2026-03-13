from cProfile import label

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
one_overT = np.array([
    0.003412969,   # 1/293
    0.003412969,   # 1/293
    0.00330033,    # 1/303
    0.00330033,    # 1/303
    0.003194888,   # 1/313
    0.003194888,   # 1/313
    0.003095975,   # 1/323
    0.003095975,   # 1/323
    0.003412969,   # 1/293
    0.003412969,   # 1/293
    0.00330033,    # 1/303
    0.00330033,    # 1/303
    0.003194888,   # 1/313
    0.003194888,   # 1/313
    0.003095975,   # 1/323
    0.003095975    # 1/323
])
ln_eta  = np.array([
    0.368958,   # ln(1.446)
    0.368958,   # ln(1.446)
    -0.164873,  # ln(0.848)
    -0.234467,  # ln(0.791)
    -0.913794,  # ln(0.401)
    -0.967584,  # ln(0.380)
    -1.644045,  # ln(0.193)
    -1.655085,  # ln(0.191)
    0.367525,   # ln(1.444)
    0.355405,   # ln(1.426)
    -0.223144,  # ln(0.800)
    -0.492685,  # ln(0.611)
    -0.776529,  # ln(0.460)
    -1.064211,  # ln(0.345)
    -1.858080,  # ln(0.156)
    -2.009921   # ln(0.134)
])
def least_squares(x, y):
    coeff = (np.mean(x*y)-np.mean(x)*np.mean(y))/((x*x).mean()-np.mean(x)**2)
    err = 1 / np.sqrt(len(x)) * np.sqrt(((y*y).mean()-np.mean(y)**2 )/ ((x*x).mean()-np.mean(x)**2) - coeff ** 2)
    return coeff, err
k, err_k = least_squares(one_overT, ln_eta)
print(k, err_k)
plt.errorbar(one_overT, ln_eta, fmt='.', label='Экспериментальные точки')
plt.plot(one_overT, k * one_overT, label='Зависимость $ln(\eta)$ от (1\T)')
plt.grid()
plt.xlabel('1/T')
plt.ylabel('$ln(\eta)$')
plt.legend()
plt.show()

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

F = np.array([6.86, 9.26, 11.67, 14.07, 16.48, 18.88, 21.28, 23.69, 26.09, 28.49])
n1 = np.array([23.3, 25, 26.7, 28.3, 29.8, 31.4, 32.8, 34.4, 35.8, 37.2])
n2 = np.array([23.4, 25.2, 26.8, 28.4, 29.9, 31.4, 33, 34.5, 35.9, 37.2])

def least_squares(x, y):
    coeff = np.mean(x*y)/np.mean(x**2)
    err = 1 / np.sqrt(len(x)) * np.sqrt((y*y).mean() / (x*x).mean() - coeff ** 2)
    return coeff, err

k1, err_k1 = least_squares(F, n1)
k2, err_k2 = least_squares(F, n2)
print(f"k1 = {k1:.4f} ± {err_k1:.4f}")

# Создаем график
fig, ax = plt.subplots(figsize=(10, 6))

# Второй набор данных: треугольники вниз
ax.errorbar(F, n1, fmt='.', markersize=8, capsize=4,
            label='n1', color='red')

ax.errorbar(F, n2, fmt='.', markersize=8, capsize=4,
            label='n2', color='blue')

# Аппроксимирующие прямые: пунктирные линии
ax.plot(F, k1 * F, 'b--', linewidth=2,
        label=f'l: y = {k1:.3f}x')
ax.plot(F, k2 * F, 'r--', linewidth=2,
        label=f'l: y = {k2:.3f}x')

# Настройка графика
ax.grid(True, alpha=0.3, linestyle='-')
ax.set_xlabel('F', fontsize=12)
ax.set_ylabel('n', fontsize=12)
ax.set_title('Зависимость n от F', fontsize=14)

# Легенда с расположением
ax.legend(loc='best', fontsize=10, framealpha=0.9)

# Улучшаем внешний вид
plt.tight_layout()
plt.show()
'''