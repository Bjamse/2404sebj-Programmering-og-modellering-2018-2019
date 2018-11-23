import numpy as np
import matplotlib.pyplot as plt


def getFloat():
    while True:
        try:
            return float(input("skriv inn et tall : "))
        except:
            print("er ikke et tall, prøv igjenn!")


print("skriv inn en x verdi for a")
a = np.array([getFloat(), -1])
b = np.array([6, 1])
c = np.array([2, 2])
d = np.array([4, 6])
AB = b - a
AC = c - a
CD = d - c
cm = c + AB
CCM = cm - c
parAreal = np.abs(np.cross(AB, AC))
# tar vi kryssproduktet får vi prarralellogrammet. deler vi det i to får vi trekanten vi vil ha
trekantAreal = np.abs(np.cross(CD, CCM) / 2)
print("a = {}, b = {}, c = {}, d = {}, cm = {}, AB = {}, AC = {}, CD = {}, CCM  = {}".format(a,b,c,d,cm,AB,AC,CD,CCM))
print("arealet av parralellogrammet er {}".format(parAreal))
print("arealet av trekant er {}".format(trekantAreal))
print("arealet av hele greia er {}".format(trekantAreal + parAreal))

# parralellogramm
px = [a[0], b[0], cm[0], c[0], a[0]]
py = [a[1], b[1], cm[1], c[1], a[1]]

# trekant
tx = [d[0], c[0], cm[0], d[0]]
ty = [d[1], c[1], cm[1], d[1]]

plt.plot(tx, ty)
plt.plot(px, py)
plt.grid()
plt.xlabel("x akse")
plt.ylabel("y akse")
plt.title("oppgave 2 f")
plt.show()
