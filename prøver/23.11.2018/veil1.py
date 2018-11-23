import sympy as spy
import numpy as np
import matplotlib.pyplot as plt

def funk(x):
    #print(x)
    return -x**2+4*x+1

x = np.arange(0.0, 4.5, 0.1) #Legg x-verdier i liste:
f = funk(x) #Beregn funksjonsverdier

def plotRect(x): #Plot rektangelet
    x1=(0,x,x,0,0)
    y1=(0,0,funk(x),funk(x),0)
    plt.plot(x1,y1)

#plotRect(x[30])
def arealRect(x):
    return x*funk(x)

xArealListe=[]
arealListe=[]
for i in range(0,45,5):
    plotRect(x[i])
    xArealListe.append(x[i])
    arealListe.append(arealRect(x[i]))

print(x)
print(xArealListe)
print(arealListe)
maks=max(arealListe)
print("Max areal: ",maks)
ind=arealListe.index(maks)
print("Maks for x-verdien: ",xArealListe[ind])
'''
#print('f er liste etter beregninger i forrige linje: {}'.format(f)) 

# Koden under beskriver hvordan koordinatsystemet skal se ut
'''
plt.plot(x,f)

plt.xlabel('x-akse') # Navn på x-akse
plt.ylabel('f-akse') # Navn på y-akse
plt.title('Veiledning1') # Tittel på grafen
plt.grid(True) # Rutenett
plt.savefig("test.png") # Filnavn på bildet som lagres
plt.show() # Vis bildet
