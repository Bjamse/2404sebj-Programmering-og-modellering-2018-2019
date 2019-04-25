# Eulers metode for difflikn:
# f'(x)=1
# Symb: f(x)=x+C
from pylab import *  # importer pakke
import numpy as np

# Tidssteg
N = 100000  # antall intervaller
a = 0.0  # startverdi x
b = 30.0  # sluttverdi x
h = (b - a) / (N - 1)  # steglengde
y0 = 35000  # initial(start)verdi for y


# Den deriverte av fynksjonen f(x) eller y
def yder(y, x):
    return 0.015 * y


# Matriser
x = zeros(N)
y = zeros(N)

y[0] = y0

# Eulers metode
for i in range(N - 1):
    y[i + 1] = y[i] + yder(y[i], x[i]) * h
    x[i + 1] = x[i] + h


# funksjonenr
# ----------------------------------------------------------------------------------------------------
def getFloat():
    try:
        return float(input("skriv inn et tall: "))
    except:
        print("du skrev inn noe som ikke var et tall! prøv igjen!")


# bør ikke kalles før euklers funksjon er kjørt minst en gang!!!!
# kommer til å fæile...
def getEtAar():
    while True:
        print("velg et år mer eller lik enn 0")
        BVAAR = getFloat()  # bruker valgt år

        if BVAAR >= 0:
            break
        else:
            print("du vlgte et år som som ikke var mer eller lik 0!")

    nux = 0  # nermeste under index
    nolx = 0  # nermeste over/lik
    faa = 0  # folketall år
    for counter, value in enumerate(x):
        if value < BVAAR:
            nux = counter
        else:
            nolx = counter
            break

    if np.abs(BVAAR - x[nolx]) < np.abs(BVAAR - x[nux]):
        faa = nolx
    else:
        faa = nux

    return faa


# ______________________________________________________________________________________________




# oppgave a)
print("oppgave a er plottet som blir vist")
plot(x, y)
grid(True)  # slår på rytenett
show()

# oppgave b)
# vises kun når viduet til a er lokket.
# kan endres på ved å flytte hele b over a
print("oppgave b) \n")
print("velg et år å finne folketallet til")

EtAArValgtAvBrukeren = getEtAar()

print("nermeste året kalkulert er året: ", x[EtAArValgtAvBrukeren])
print("folketallet dette året er : ", y[EtAArValgtAvBrukeren])

# oppgave c)

print("oppgave c) \n")
print("finn økningen et år")

EtAArValgtAvBrukeren = getEtAar()

print("nermeste året kalkulert er året: ", x[EtAArValgtAvBrukeren])
print("stigningen i folketallet dette året er : ", yder(y[EtAArValgtAvBrukeren], 0))

# oppgave d)
print("\n\noppgave d)")
print("skriv inn antal folk og finn ut når det var så mange (må velge mer enn 35000)")

while True:
    print("velg en mengde")
    BVF = getFloat()  # bruker valgt folkemende
    if BVF >= 35000:
        break
    else:
        print("du vlgte en mengde som var mindre enn 35000!")

nux = 0  # nermeste under index
nolx = 0  # nermeste over/lik
fm = 0  # folkemengde
for counter, value in enumerate(y):
    if value < BVF:
        nux = counter
    else:
        nolx = counter
        break

if np.abs(BVF - y[nolx]) < np.abs(BVF - y[nux]):
    fm = nolx
else:
    fm = nux

print("nermeste folkemengde kalkulert er: ", y[fm])
print("det var det folketallet i dette år-et  : ", x[fm])
