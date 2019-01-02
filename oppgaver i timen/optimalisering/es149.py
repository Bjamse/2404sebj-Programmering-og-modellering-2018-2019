import pylab as pl

N = 1000
a = .0
b = 5.0
h = (b-a)/(N-1)

y0 = 3


def yder(y,x):
    return 1


x = pl.zeros(N)
y= pl.zeros(N)

y[0] = y0
for i in range(N-1):
    y[i+1] = y[i] + yder(y[i],x[i])*h
    x[i+1] = x[i]

pl.plot(x,y,"b-")
pl.show()