import sympy as spy
import numpy as np
import matplotlib.pyplot as plt
'''
a = 1
b = -2
c = -5
d = 6
'''
def derivert(liste):
 #return [-5,-4,3]
 retur=[]
 for i in range(0,len(liste)-1):
     retur.append(liste[i+1]*(i+1))
 print("liste:",liste)
 print("deivertListe:",retur)
 return retur




#x = spy.symbols('x') #etablerer symbolet x
#print(x)
x1 = 6
poly = [6,-5,-2,1]
#polyDer =[-5,-4,3]
polyDer = derivert(poly)
#f = a*x**2 + b*x + c #

#Plotting:
x = np.arange(0.0, 4.0, 0.1)
print('x er liste: {}'.format(x))
f = poly[3]*x**3+poly[2]*x**2+poly[1]*x+poly[0]
fder = polyDer[2]*x**2+polyDer[1]*x+polyDer[0]
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
