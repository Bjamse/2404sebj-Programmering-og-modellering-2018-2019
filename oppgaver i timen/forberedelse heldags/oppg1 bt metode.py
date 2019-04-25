import numpy
import matplotlib.pyplot as plt
import math


def Euler(f, xa, xb, ya, n):
    h = (xb - xa) / float(n)
    x = xa
    y = ya
    ly = [y]
    lx = [x]
    for i in range(n):
        y += h * f(x, y)
        x += h
        ly.append(y)
        lx.append(x)

    return {"listY":ly, "listX":lx, "sisteY": y}


def yder(x,y):
    return

# under konstruksjon......