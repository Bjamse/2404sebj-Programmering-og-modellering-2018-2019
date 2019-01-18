#Eulers metode for difflikn:
#y'=1  y(0)=1

from pylab import * #importer pakke

N=100 #antall intervaller
a=0.0  #startverdi
b=5.0 #sluttverdi
h= (b-a)/(N-1)  #steglengde
y0 = 3  #initial(start)verdi for y

# Den deriverte av fynksjonen f(x) eller y
def yder(y,x):
    #Egentlig difflikningen y'=1
    return 1

#Matriser
x = zeros(N)   #
y = zeros(N)

y[0] = y0

#Eulers metode
for i in range(N-1):
    y[i+1] = y[i] + yder(y[i],x[i])*h   #f(x+dx)=f(x)+f'(x)*dx
    x[i+1] = x[i] + h  #lar neste x-verdi være denne x-verdi + tilveksten h

plot(x,y,'b-')
grid(True)  #slår på rutenett
show()