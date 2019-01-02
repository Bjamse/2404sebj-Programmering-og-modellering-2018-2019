import pylab as pl

N = 11
v0 = 0
a = .14
t = pl.linspace(0,10,N)
s = v0*t+0.5*a*t**2

fil = open("res.txt", "w")

for i in range(N):
    fil.write(str(t[i]))
    fil.write("    ")
    fil.write(str(s[i]) + " \n")

fil.close()
