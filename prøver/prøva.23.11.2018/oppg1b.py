import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 3, 0.1)
f = 2 * (x - 3) ** 2


def FavX(verdi):
    return 2 * (verdi - 3) ** 2


def tegnTrekjant(x):
    return [0,x,x,0], [0,0,FavX(x),0] # returnerer en x og en y liste


xtrekant, ytrekant = tegnTrekjant(2)

plt.plot(x, f)
plt.plot(xtrekant,ytrekant)
plt.title("oppgave1b")
plt.xlabel("x-akse")
plt.ylabel("y-akse")
plt.grid()
plt.show()
