import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,3,0.1)
f = 2*(x-3)**2

plt.plot(x,f)
plt.title("oppgave1a")
plt.xlabel("x-akse")
plt.ylabel("y-akse")
plt.grid()
plt.show()
