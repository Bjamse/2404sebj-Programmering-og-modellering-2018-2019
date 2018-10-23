#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

a, b, c = float(input("tast inn 3 tall med enter mellom")), float(input()), float(input())

x = np.arange(0.0, 10.0, 0.01)
y = a*x**2 + b*x + c


plt.plot(x, y)

plt.show()