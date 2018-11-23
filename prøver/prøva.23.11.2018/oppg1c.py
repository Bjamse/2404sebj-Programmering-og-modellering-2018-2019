import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 3, 0.1)
f = 2 * (x - 3) ** 2


def FavX(verdi):
    return 2 * (verdi - 3) ** 2


def tegnTrekjant(x):
    return [0,x,x,0], [0,0,FavX(x),0] # returnerer en x og en y liste


for i in range(0,30,5):
    xtrekant, ytrekant = tegnTrekjant(i/10)
    plt.plot(xtrekant,ytrekant)

plt.plot(x, f)
plt.title("oppgave1c")
plt.xlabel("x-akse")
plt.ylabel("y-akse")
plt.grid()
plt.show()
