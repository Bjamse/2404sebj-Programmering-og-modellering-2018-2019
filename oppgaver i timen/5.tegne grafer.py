import matplotlib.pyplot as plt
import numpy as np

print()
print("oppgave 1")
print()


x = np.arange(0.0, 10.0, 0.01)
y = 2*x
plt.plot(x, y)
plt.grid()
plt.show()

print()
print("oppgave 2 / 3 / 4")
print()

x = np.arange(0.0, 10.0, 0.01)
y = -x**2 + 10*x
g = 2*x - 5
plt.plot(x, y, "b")
plt.plot(x,g, "r")
plt.xlabel('x')
plt.ylabel('y)')
plt.title('-x^2 + 10x')
plt.grid()
plt.show()
