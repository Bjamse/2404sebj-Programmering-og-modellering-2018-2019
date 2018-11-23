import numpy as np
import matplotlib.pyplot as plt


a = np.array([1, -1])
b = np.array([6, 1])
c = np.array([2, 2])
d = np.array([4, 6])
AB = b-a
AC = c-a
CD = d-c
cm = c + AB
print("c = {}, d = {}, CD = {}".format(c,d,CD))
print("arealet av parralellogrammet er {}".format(np.abs(np.cross(AB, AC))))
# parralellogramm
px = [a[0], b[0], cm[0], c[0], a[0]]
py = [a[1], b[1], cm[1], c[1], a[1]]

# trekant
tx = [d[0], c[0], cm[0], d[0]]
ty = [d[1], c[1], cm[1], d[1]]

plt.plot(tx,ty)
plt.plot(px,py)
plt.grid()
plt.xlabel("x akse")
plt.ylabel("y akse")
plt.title("oppgave 2 d")
plt.show()

