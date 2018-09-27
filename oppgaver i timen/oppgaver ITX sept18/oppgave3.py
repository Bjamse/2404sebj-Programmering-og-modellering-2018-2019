import sympy as spy
import numpy as np
import matplotlib.pyplot as plt

a = 3
b = -6
c = 3


x = spy.symbols('x')
x_en = 4
f = a*x**2 + b*x + c
deriverte = spy.diff(f, x)
fx1 = f.subs(x,x_en)
fdx1 = deriverte.subs(x,x_en)
y = fdx1 * x-fdx1 * x_en + fx1


x = np.arange(0.0, 10.0, 0.01)

#måtte definere f og y fordi vi fikk nye x-er itilleg var de gamle funksjonene liksom sånne sympy funksjoner. så de måtte
# ha den nye x verdien får å funke
#rettere sagt, jeg fårstår hvorfåp men kan ikke forkalre
f = a*x**2 + b*x + c

y = fdx1 * x-fdx1 * x_en + fx1

plt.plot(x, y)
plt.plot(x,f)
plt.grid()
plt.show()
