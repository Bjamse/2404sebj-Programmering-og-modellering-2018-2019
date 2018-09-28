import sympy as spy
import numpy as np
import matplotlib.pyplot as plt


a = 3
b = 2
c = 1
x = spy.symbols('x')
x1 = 4
xPlot = np.arange(0.0, 10.0, 0.01)

f = a * x ** 2 + b * x + c
deriverte = spy.diff(f, x)
for i in range(3):

    fx1 = f.subs(x, x1)  # f(x) der x = x_en
    fdx1 = deriverte.subs(x, x1)  # f'(x) der x = x_en
    tangenten = fdx1 * x - fdx1 * x1 + fx1  # finner tangenten til f(x) i punktet (x_en, f(x_en))

    tangetplot = fdx1 * xPlot - fdx1 * x1 + fx1

    likningNullpunktTangent = spy.Eq(tangenten, 0)

    losningNullpunktTangent = spy.solve(likningNullpunktTangent, x)[0]


fplot = a * xPlot ** 2 + b * xPlot + c