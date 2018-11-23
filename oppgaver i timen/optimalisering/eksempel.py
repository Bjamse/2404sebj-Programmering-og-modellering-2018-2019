# Importerer nødvendige biblioteker
import matplotlib.pyplot as plt
import numpy as np


def A(x):
    return 30 * x - x ** 2


x = []
y = []

# Løkke som fyller tabell
for i in range(31):
    x.append(i)
    y.append(A(i))

# Utskrift av data
plt.grid()  # Lager rutenett
plt.xlabel('$x$')  # Merker x-aksen
plt.ylabel('$A(x)$')  # Merker y-aksen
plt.plot(x, y, 'bo-.', label='$A(x)=30x - x^2$')
plt.legend()
plt.show()

m = max(y)
h = y.index(max(y))

print("Det største arealet av rektangelet er: {} m^2".format(m))  # Finner toppunktet til A(x)
print("Når arealet er størst er høyden {} meter.".format(h))  # Finnver ved hvilken x-verdi dette er.
