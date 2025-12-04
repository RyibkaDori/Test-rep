import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
M = np.array([134, 169, 207.8, 261.3, 326.3])
Omega = np.array([66.81, 83.8, 102.7, 129.5, 161.6])
def least_squares(x, y):
    coeff = np.mean(x*y)/np.mean(x**2)
    err = 1 / np.sqrt(len(x)) * np.sqrt((y*y).mean() / (x*x).mean() - coeff ** 2)
    return coeff, err
'''
k, err_k = least_squares(M, Omega)
print(k, err_k)
plt.errorbar(M, Omega, fmt='.')
plt.plot(M, k * M)
plt.grid()
plt.xlabel('M')
plt.ylabel('Omega')
plt.legend()
plt.show()
'''