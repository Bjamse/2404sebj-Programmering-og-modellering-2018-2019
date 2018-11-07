import sympy as spy
import numpy as np
import matplotlib.pyplot as plt

a = 1
b = -2
c = -5
d = 6


#x = spy.symbols('x') #etablerer symbolet x
#print(x)
x1 = 6
#f = a*x**2 + b*x + c 

#Plotting:
x = np.arange(0.0, 4.0, 0.1)
print('x er liste: {}'.format(x)) 
f = a*x**3 + b*x**2 + c*x + d
print('f er liste etter beregninger i forrige linje: {}'.format(f))
fder = 3*a*x**2+2*b*x+c 

# Koden under beskriver hvordan koordinatsystemet skal se ut
plt.plot(x,f)
plt.plot(x,fder)
plt.xlabel('x-akse') # Navn på x-akse
plt.ylabel('f-akse') # Navn på y-akse
plt.title('Tredjegradsfunksjon') # Tittel på grafen
plt.grid(True) # Rutenett
plt.savefig("test.png") # Filnavn på bildet som lagres
plt.show() # Vis bildet
