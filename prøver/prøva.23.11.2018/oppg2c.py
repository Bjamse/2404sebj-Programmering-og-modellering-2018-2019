import numpy as np
import matplotlib.pyplot as plt


a = np.array([1, -1])
b = np.array([6, 1])
c = np.array([2, 2])
d = np.array([4, 6])
AB = b-a
AC = c-a
cm = c + AB

print("arealet av parralellogrammet er {}".format(np.abs(np.cross(AB, AC))))

x = [a[0], b[0], cm[0], c[0], a[0]]
y = [a[1], b[1], cm[1], c[1], a[1]]


plt.plot(x,y)
plt.grid()
plt.xlabel("x akse")
plt.ylabel("y akse")
plt.title("oppgave 2 c")
plt.show()

