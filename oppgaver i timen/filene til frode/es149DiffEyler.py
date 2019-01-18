#Eulers metode for difflikn:
#y'=y+x
#Symb: f(x)=Ce^x-x-1
import matplotlib.pyplot as plt
import numpy as np #importer pakke

'''
#Tidssteg
def fSymb(C,x):
    return C*exp(x)-x-1

print(fSymb(1,1))'''

x1=0.0                      #startverdi
xn=5.0                      #sluttverdi
dx = 0.001                  #steglengde
x= np.arange(x1, xn, dx)
y= np.zeros(len(x))
y[0] = 3                    #initial(start)verdi for y


# Den deriverte av fynksjonen f(x) eller y
def yder(y,x):
    return 3*x**2



#Eulers metode
for i in range(len(y)-1):
    y[i+1] = y[i] + yder(y[i], x[i]) * dx


plt.plot(x,y,'b-')
# plot(xS,yS,'r-')
plt.grid(True)  #slår på rutenett
plt.show()