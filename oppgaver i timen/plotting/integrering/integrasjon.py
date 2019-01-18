import matplotlib.pyplot as plt
import numpy as np

# Deinerer en funksjon
def f(x):
    return -x**2 + 25

x_verdier = []
y_verdier = []

for x in range(-5,6):
    x_verdier.append(x)
    y_verdier.append(f(x))

print("x-verdier: ", x_verdier)
print("y-verdier: ", y_verdier)

plt.plot(x_verdier, y_verdier)
plt.grid()
plt.show()