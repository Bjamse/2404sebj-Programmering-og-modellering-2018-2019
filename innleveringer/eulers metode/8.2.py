# kilde : http://code.activestate.com/recipes/577647-ode-solver-using-euler-method/
import math


# First Order ODE (y' = f(x, y)) Solver using Euler method
# xa: initial value of independent variable
# xb: final value of independent variable
# ya: initial value of dependent variable
# n : number of steps (higher the better)
# Returns value of y at xb.
def Euler(f, xa, xb, ya, n):
    h = (xb - xa) / float(n)
    x = xa
    y = ya
    for i in range(n):
        y += h * f(x, y)
        x += h
    return y


# oppgave 1
def a(x,y):
    return 1


print(Euler(a, 0, 10, 0, 1000))


# oppgave 2
def b(x,y):
    return x


print(Euler(b, 0, 1, 0, 1000))


# oppgave 3
def c(x,y):
    return 4+3


print(Euler(c, 0, 1, 0, 1000))


# oppgave 4
def d(x,y):
    return -4*y-3*x


print(Euler(d, 0, 1, 0, 1000))


# oppgave 5
def e(x,y):
    return -4*y-3*x


print(Euler(e, 0, 1, 0, 1000))


# oppgave 6
def f2(x,y):
    return -4*y-3*x


print(Euler(f2, 0, 1, 0, 1000))



