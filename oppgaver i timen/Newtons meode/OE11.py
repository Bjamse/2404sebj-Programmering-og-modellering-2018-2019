import sympy as spy
import numpy as np
import matplotlib.pyplot as plt

def polystreng(liste):
    retur = ""
    lengde = len(liste)

    for i in range(lengde,0,-1):
        retur += str(liste[i-1])+"x**"+str(lengde-1)+"+"
    return retur


def derivert(liste):
 retur=[]
 for i in range(len(liste),0,-1): 
     retur.append(liste[i+1]*(i+1))
 print("polynomliste:",liste)
 print("polynomderivertListe:",retur)
 return retur

def beregnPoly(liste,x): #bergner funksjonsverdi fra polynomliste
    retur = 0
    for i in range(len(liste)):
        retur += liste[i]*x**i
    return retur



poly = [4,6,-5,-2,1]
print("Min utskrift",polystreng(poly))
x1 = 6
y1 = beregnPoly(poly,x1)

polyDer = derivert(poly)
print("polyDer: ",polyDer)
fdy = beregnPoly[polyDer,x1]
ftang = (fdy)*x-(fdy)*x1+y1
#Plotting:
x = np.arange(0.0, 4.0, 0.1)
print('x er liste: {}'.format(x))
#f = poly[3]*x**3+poly[2]*x**2+poly[1]*x+poly[0]
f = beregnPoly(poly,x)
#fder = polyDer[2]*x**2+polyDer[1]*x+polyDer[0]
fder = beregnPoly(polyDer,x)
#f = a*x**3 + b*x**2 + c*x + d
print('f er liste etter beregninger i forrige linje: {}'.format(f)) 

# Koden under beskriver hvordan koordinatsystemet skal se ut
plt.plot(x,f)
plt.plot(x,fder)
plt.xlabel('x-akse') # Navn på x-akse
plt.ylabel('f-akse') # Navn på y-akse
plt.title('Tredjegradsfunksjon') # Tittel på grafen
plt.grid(True) # Rutenett
plt.savefig("test.png") # Filnavn på bildet som lagres
plt.show() # Vis bildet
