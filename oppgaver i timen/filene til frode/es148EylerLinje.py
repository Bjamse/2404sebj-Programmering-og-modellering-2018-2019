#Eulers metode for difflikn:
#f'(x)=1
#Symb: f(x)=x+C
from pylab import * #importer pakke

#Tidssteg
N=10000 #antall intervaller
a=0.0  #startverdi
b=5.0 #sluttverdi
h= (b-a)/(N-1)  #steglengde
y0 = 1  #initial(start)verdi for y

# Den deriverte av fynksjonen f(x) eller y
def yder(y,x):
    return 1

#Matriser
x = zeros(N)
y = zeros(N)

y[0] = y0

#Eulers metode
for i in range(N-1):
    y[i+1] = y[i] + yder(y[i],x[i])*h
    x[i+1] = x[i] + h

plot(x,y)
grid(True)  #slår på rytenett
show()