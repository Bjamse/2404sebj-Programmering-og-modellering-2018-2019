import sympy as spy
import numpy as np
import matplotlib.pyplot as plt

a = 3
b = 2
c = 1
x = spy.symbols('x')
x_en = 4


f = a*x**2 + b*x + c
deriverte = spy.diff(f, x)
fx1 = f.subs(x,x_en)  # f(x) der x = x_en
fdx1 = deriverte.subs(x,x_en)  # f'(x) der x = x_en
tangenten = fdx1 * x-fdx1 * x_en + fx1  # finner tangenten til f(x) i punktet (x_en, f(x_en))

likningNullpunktTangent = spy.Eq(tangenten, 0)

losningNullpunktTangent = spy.solve(likningNullpunktTangent,x)

print("yverdien for grafen ved xverdien lik nullpunktet til tangenten er = ",
      f.subs(x, likningNullpunktTangent))
