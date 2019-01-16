import sympy as spy
import numpy as np
import matplotlib.pyplot as plt

poly = [4,6,-5,-2,1]

def polystreng(liste):
    retur = ""
    lengde = len(liste)
# for liste[3:2:-1] plukker elementer
    for i in range(lengde-1,-1,-1):
        t = liste[i]
        if t >= 0 : retur += "+"
        retur += str(t)
        if i>1 : retur +="x**"+str(i)
        elif i==1 : retur += "x"
    return retur
print("Polynomstreng opg 5",polystreng(poly))

def beregnPoly(liste,x): #bergner funksjonsverdi fra polynomliste
    retur = 0
    for i in range(len(liste)):
        retur += liste[i]*x**i
    return retur
print("Beregnet verdi med x=3 opg 6 ",beregnPoly(poly,3))

def derivert(liste):
 retur=[]
 for i in range(1,len(liste)): 
     retur.append(liste[i]*i)
     print(retur)
 print("polynomliste:",liste)
 print("polynomderivertListe:",retur)
 return retur

polyDer = derivert(poly)
print("polyDer: ",polyDer)
print("Derivert opg 7 f'(x)= ",polystreng(polyDer))
