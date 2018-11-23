import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 3, 0.1)
f = 2 * (x - 3) ** 2
areal = []
def FavX(verdi):
    return 2 * (verdi - 3) ** 2


def tegnTrekjant(x):
    return [0,x,x,0], [0,0,FavX(x),0] # returnerer en x og en y liste


for i in range(0,30,5):
    xtrekant, ytrekant = tegnTrekjant(i/10)
    plt.plot(xtrekant, ytrekant)
    areal.append((FavX(i/10)*(i/10)) * 0.5 ) # regner arealet av trekanten med å ta høyden av trekanten ganger lengden delt på 2

print("største arealet var : {} ved x verdi {} ".format(max(areal), areal.index(max(areal)) * 0.5))

plt.plot(x, f)
plt.title("oppgave1d")
plt.xlabel("x-akse")
plt.ylabel("y-akse")
plt.grid()
plt.show()
