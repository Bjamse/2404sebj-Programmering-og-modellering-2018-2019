#Eulers metode for difflikn:
#y'=1  y(0)=1
#y'=y+x
#Symb: f(x)=Ce^x-x-1
from pylab import * #importer pakke

#Tidssteg
''' def fSymb(C,x):
    return C*exp(x)-x-1

print(fSymb(1,1))'''
N=1000 #antall intervaller
a=0.0  #startverdi
b=5.0 #sluttverdi
h= (b-a)/(N-1)  #steglengde
y0 = 1  #initial(start)verdi for y

# Den deriverte av fynksjonen f(x) eller y
def yder(y,x):
    #return y+x
    return 1

#Matriser
x = zeros(N)
y = zeros(N)

#Symbolsk løsning
xS = arange(0.0, 5.0, 0.1)
#xS = linspace(0,5,100) 
#yS = fSymb(1,xS)

y[0] = y0

#Eulers metode
for i in range(N-1):
    y[i+1] = y[i] + yder(y[i],x[i])*h
    x[i+1] = x[i] + h

plot(x,y,'b-')
#plot(xS,yS,'r-')
grid(True)  #slår på rutenett
show()