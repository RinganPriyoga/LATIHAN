#Punya Muhammad Ringan Priyoga
#Duh kudu nonton tutorial dulu baru jadi hayya

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from fractions import Fraction

#Definisi fungsi
def f(x):
    return x**2 + 2*x

#Interval integrasi
a, b = 1, 3

#Hitung nilai integral
integral_value, _ = quad(f, a, b)

#Ini biar bentuknya jadi pecahan
frac_result = Fraction(integral_value).limit_denominator()

#Ngeprint hasil integralnya
print(f"Integral dari f(x) = x^2 + 2x pada interval [{a}, {b}] adalah {frac_result} atau {integral_value:.4f}")

#Buat grafik
x_vals = np.linspace(a - 1, b + 1, 400)
y_vals = f(x_vals)

#Area di bawah kurva
x_fill = np.linspace(a, b, 200)
y_fill = f(x_fill)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, 'b', label='f(x) = x² + 2x')
plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.5, label='Area di bawah kurva')
plt.title('Integral dari f(x) = x² + 2x pada interval [1, 3]')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
