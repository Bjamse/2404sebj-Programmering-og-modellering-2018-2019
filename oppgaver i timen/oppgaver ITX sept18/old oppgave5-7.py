import sympy as spy
import numpy as np
import matplotlib.pyplot as plt
# dette er en løsning for 5 til 7 fordi du kan løse det polynomet du vil ved å bare taste det inn
#  for f og bytte abc og x1 verdiene

a = 3
b = 2
c = 1
x = spy.symbols('x')
x1 = 4
xPlot = np.arange(-5.0, 6.0, 0.01)

f = a * x ** 2 + b * x + c
deriverte = spy.diff(f, x)
for i in range(9):

    fx1 = f.subs(x, x1)  # f(x) der x = x_en
    fdx1 = deriverte.subs(x, x1)  # f'(x) der x = x_en
    tangenten = fdx1 * x - fdx1 * x1 + fx1  # finner tangenten til f(x) i punktet (x_en, f(x_en))

    tangentplot = fdx1 * xPlot - fdx1 * x1 + fx1
    plt.plot(xPlot, tangentplot)

    likningNullpunktTangent = spy.Eq(tangenten, 0)

    losningNullpunktTangent = spy.solve(likningNullpunktTangent, x)[0]
    x1 = losningNullpunktTangent


fplot = a * xPlot ** 2 + b * xPlot + c

plt.plot(xPlot,fplot)
plt.grid()

plt.show()
