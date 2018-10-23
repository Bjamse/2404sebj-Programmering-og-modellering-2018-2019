import sympy as spy
import numpy
import matplotlib.pyplot as plt


def spyplotter(funksjon, ukjent, start=0.0, slutt=10.0, steg=0.01):
    lam_x = spy.lambdify(ukjent, funksjon, modules=['numpy'])

    x_val = numpy.arange(start, slutt, steg)
    y_val = lam_x(x_val)

    plt.plot(x_val,y_val)


x = spy.symbols('x')
f = x**2 + 2*x

spyplotter(f,x)

plt.show()

# https://stackoverflow.com/questions/35390187/using-sympy-equations-for-plotting
