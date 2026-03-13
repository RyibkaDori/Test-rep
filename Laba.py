import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Данные (1/T и ln(eta) для всех 16 точек)
one_over_T = np.array([
    1/293, 1/293, 1/303, 1/303, 1/313, 1/313, 1/323, 1/323,   # Стекло
    1/293, 1/293, 1/303, 1/303, 1/313, 1/313, 1/323, 1/323    # Сталь
])

ln_eta = np.array([
    np.log(1.446), np.log(1.446), np.log(0.848), np.log(0.791),  # Стекло 1-4
    np.log(0.401), np.log(0.380), np.log(0.193), np.log(0.191),  # Стекло 5-8
    np.log(1.444), np.log(1.426), np.log(0.800), np.log(0.611),  # Сталь 1-4
    np.log(0.460), np.log(0.345), np.log(0.156), np.log(0.134)   # Сталь 5-8
])

# Метод наименьших квадратов для всех точек
slope, intercept, r_value, p_value, std_err = stats.linregress(one_over_T, ln_eta)

# Создание графика
plt.figure(figsize=(12, 8))

# Все точки одним цветом и маркером
plt.scatter(one_over_T, ln_eta,
            color='purple', marker='o', s=80,
            label='Экспериментальные точки (все материалы)',
            alpha=0.7, edgecolors='black', linewidth=1.5)

# Линия аппроксимации
x_fit = np.linspace(min(one_over_T)-0.00005, max(one_over_T)+0.00005, 100)
y_fit = slope * x_fit + intercept

plt.plot(x_fit, y_fit,
         'g-', linewidth=3,
         label=f'МНК: ln(η) = {slope:.2f}/T')

# Настройка графика
plt.xlabel(r'$1/T$, K$^{-1}$', fontsize=14)
plt.ylabel(r'$\ln(\eta)$, Па·с', fontsize=14)
plt.title('Зависимость логарифма вязкости от обратной температуры\n(объединенные данные для стекла и стали)',
          fontsize=16, fontweight='bold')

# Легенда
plt.legend(loc='best', fontsize=12, frameon=True, shadow=True)

# Сетка
plt.grid(True, alpha=0.3, linestyle='--')

# Добавление текста с параметрами аппроксимации
textstr = f'Параметры аппроксимации:\n'
textstr += f'Угловой коэффициент: {slope:.4f}\n'


plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=11,
         verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.show()

# Вывод параметров в консоль
print("=" * 60)
print("РЕЗУЛЬТАТЫ АППРОКСИМАЦИИ (ВСЕ ТОЧКИ)")
print("=" * 60)
print(f"\nУравнение регрессии: ln(η) = {slope:.4f}/T + {intercept:.4f}")
print(f"Коэффициент детерминации R² = {r_value**2:.6f}")
print(f"Коэффициент корреляции R = {r_value:.6f}")
print(f"Стандартная ошибка: {std_err:.6f}")
print(f"Энергия активации вязкого течения: E_a = {-slope * 8.314:.2f} Дж/моль")

# Дополнительная статистика
print("\n" + "=" * 60)
print("СТАТИСТИЧЕСКИЕ ХАРАКТЕРИСТИКИ")
print("=" * 60)
print(f"Среднее значение 1/T: {np.mean(one_over_T):.6f} K⁻¹")
print(f"Среднее значение ln(η): {np.mean(ln_eta):.6f}")
print(f"Стандартное отклонение 1/T: {np.std(one_over_T):.6f}")
print(f"Стандартное отклонение ln(η): {np.std(ln_eta):.6f}")