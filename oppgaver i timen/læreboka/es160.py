from pylab import *

# initsielle betigelser
H0 = 2000
G0 = 10
a = 0.1
b = 10000
c = 0.005
d = 0.00005
e = 0.06

# tidssteg
N = 100000
tid = 400
dt = tid/(N-1)

# matriser
t = zeros(N)
H = zeros(N)
G = zeros(N)
Hder = zeros(N)
Gder = zeros(N)

# initierer matrisen
H[0] = H0
G[0] = G0

# Eulers metode
for i in range(N-1):
    Hder[i] = a*H[i]*(1-H[i]/b)- c*H[i] * G[i]
    Gder[i] = d*H[i]*G[i] - e*G[i]
    H[i+1] = H[i] + Hder[i]*dt
    G[i + 1] = G[i] + Gder[i] * dt
    t[i+1] = t[i] + dt

# plotting
fig = figure()
ax = fig.add_subplot(111)
data1 = ax.plot(t, H, "-b", label="harer")
ax2 = ax.twinx()
data2 = ax2.plot(t,G,"r",label="gauper")

data = data1+data2

datatittel = [l.get_label() for l in data]
ax.legend(data,datatittel,loc=0)
ax.grid()
ax.set_xlabel("tid (måneder)")
ax.set_ylabel("antall harer")
ax2.set_ylabel("antall gauper")
# ax2.set_ylim(0,200)
# ax.set_ylim(0,5000)
plt.show()