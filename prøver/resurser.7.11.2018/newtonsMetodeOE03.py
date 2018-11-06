import math

a=1
b=-9
c=14   #Skal gi løsningene 2 og 7

#a=float(input("a:"))
#b=float(input("b:"))
#c=float(input("c:"))

x1=(-b-math.sqrt(b**2-4*a*c))/(2*a)
x2=(-b+math.sqrt(b**2-4*a*c))/(2*a)
print('x1 har verdien {} og x2 har verdien {}'. format(x1,x2))

# Importerer nødvendige biblioteker
import matplotlib.pyplot as plt
import numpy as np

# Funksjonsdata
x = np.arange(0.0, 10.0, 0.01)
    # Angir definisjonsmengden til funksjonen - Punkter for hver 0.01
f = a*x**2+b*x+c

# tangent:
x1=1
x1=int(input("x:"))
y1=a*x1**2+b*x1+c
fd = 2*a*x+b
fdy = 2*a*x1+b
print('a = {} b = {} x1 = {} y1 = {} fdy = {}'.format(a,b,x1,y1,fdy))
ftang = (fdy)*x-(fdy)*x1+y1

plt.plot(x, f) # Plotter f(x)
plt.plot(x, ftang) # Plotter f(x)

# Koden under beskriver hvordan koordinatsystemet skal se ut
plt.xlabel('x-akse') # Navn på x-akse
plt.ylabel('y-akse') # Navn på y-akse
plt.title('Annengradsfunksjon') # Tittel på grafen
plt.grid(True) # Rutenett
plt.savefig("test.png") # Filnavn på bildet som lagres
plt.show() # Vis bildet