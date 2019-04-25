from pylab import *  # importerer pakke
import numpy as np # importerer numpy (egentlig redundant siden den blir importer t av pylab så blir sikker t fjernet i fremtidig utgaver av programmet)


def getint(): # en funksjon som ikke stoper å kjøre før brukeren skriver inn et gyldig heltall
    while True:
        try:
            return int(input("Skriv inn et heltall"))
        except:
            print("prøv igjenn. du skre vikke inn et gyldig heltall")


print("Grunnet måten programmet er utformet på må vi vite hvor \nmange år inn i fremtiden du antar du har lyst til å kalkulere. \n"+
      "Dette gjør at vi kan kalkulere med høyere presisjon det du vil.\n"+
      "\n Skriv in et antall år du vil kalkulere")

antAAr = np.abs(getint())

print("skriv in presisjonen du vil ha på kalkuleringen 100 er lite og 10000 er grei presisjon : ")
presisjon = getint()



# Tidssteg
N = presisjon  # antall intervaller (hvor nøye vi skal kalkulere med eulers metode ) (definert med presisjonen brukeren shriver inn)
a = 0.0  # startverdi x
b = antAAr  # sluttverdi x (definert med antall år brukeren shriver inn)
h = (b - a) / (N - 1)  # steglengde beregnet mtp antall intervaller
y0 = 35000  # initial(start)verdi for y


# Den deriverte av fynksjonen f(x) eller y
# altså diffligningen vi skal berege med
def yder(y, x):
    return 0.015 * y


# Matriser
# et par tomme matriser som skal inneholde koordinatene til punktene regnet ut
x = zeros(N)
y = zeros(N)

y[0] = y0 # setter første punkt i ylista til å være initsialverdien for y

# Eulers metode
for i in range(N - 1):
    y[i + 1] = y[i] + yder(y[i], x[i]) * h
    x[i + 1] = x[i] + h


# funksjonenr som blir brukt i besvarelsen
# ----------------------------------------------------------------------------------------------------
def getFloat(): # denne funksjonen får brukeren til å skrive inn et tall om nekter å stoppe å spørre før den får en gyldig float
    while True:
        try:
            return float(input("skriv inn et tall: "))
        except:
            print("du skrev inn noe som ikke var et tall! prøv igjen!")


# en funksjon for å å det nermeste året som er ferdig kalkulert mtp det brukeren ønsker å få vite data om
# returnerer en float med indexen til året som var nermest
# bør ikke kalles før euklers funksjon er kjørt minst en gang!!!!
# kommer til å fæile...
def getEtAar():

    while True: # lagre en brukerinputt med et år i en variabel
        print("velg et år mer eller lik enn 0")
        BVAAR = getFloat()  # bruker valgt år

        if BVAAR >= 0: # hvis brukeren skrev inn et år som var mindre enn 0 så blir Han/hun ødt tyil å prøve på nytt
            break
        else:
            print("du vlgte et år som som ikke var mer eller lik 0!")


    nux = 0  # nermeste under index
    nolx = 0  # nermeste over/lik
    faa = 0  # folketall år
    for counter, value in enumerate(x): # går i gjennom alle kalkulerte år og finner det året som er rett under og rettover/lik det som brukeren har skrevet inn
        if value < BVAAR:
            nux = counter
        else:
            nolx = counter
            break

    if np.abs(BVAAR - x[nolx]) < np.abs(BVAAR - x[nux]): # finner ut om året som var over eller under var det nermeste og lagrer dette i faa
        faa = nolx
    else:
        faa = nux

    return faa # returnerer faa, faa er en index og må brukes som det for å få noe data ut


# ______________________________________________________________________________________________




# oppgave a)
print("oppgave a\n")
print("oppgave a er plottet som blir vist") # plotter diffligninga
plot(x, y)
grid(True)  # slår på rytenett
show()

# oppgave b)
# vises kun når viduet til a er lokket.
print("\n\noppgave b) \n")
print("velg et år å finne folketallet til")

EtAArValgtAvBrukeren = getEtAar() # indexen til det nermeste kalkulerte året mtp det brukeren taster inn

print("nermeste året kalkulert er året: ", x[EtAArValgtAvBrukeren])
print("folketallet dette året er : ", y[EtAArValgtAvBrukeren])

# oppgave c)

print("\n\noppgave c) \n")
print("finn økningen et år")

EtAArValgtAvBrukeren = getEtAar() # indexen til det nermeste kalkulerte året mtp det brukeren taster inn

print("nermeste året kalkulert er året: ", x[EtAArValgtAvBrukeren])
print("stigningen i folketallet dette året er : ", yder(y[EtAArValgtAvBrukeren], 0))

# oppgave d)
print("\n\noppgave d)")
print("skriv inn antall folk og finn ut når det var så mange (må velge mer enn 35000)")

while True: # lagre brukerinputt med en folkemengde i en variabel, stopper ikke før du taster inn en større eller lik 35000
    print("velg en mengde")
    BVF = getFloat()  # bruker valgt folkemende
    if BVF >= 35000:
        break
    else:
        print("du vlgte en mengde som var mindre enn 35000!")

nux = 0  # nermeste under index
nolx = 0  # nermeste over/lik
fm = 0  # folkemengde
for counter, value in enumerate(y): # går i gjennom alle kalkulerte folkemengder og finner den som er rett under og rettover/lik det som brukeren har skrevet inn
    if value < BVF:
        nux = counter
    else:
        nolx = counter
        break

if np.abs(BVF - y[nolx]) < np.abs(BVF - y[nux]): # velger den av de to nermsete som er nermset og lagrer den i fm (folkemengde)
    fm = nolx
else:
    fm = nux

# fm er en index for hvor i lista med y verdier som var nermest den som brukeren skrev inn
# da kan vi bruke den i begge lsiter for å finne y og x verdiene ( selv om vi vet y for di det var jo den som var nermest det brukeren skrev inn)

print("nermeste folkemengde kalkulert er: ", y[fm])
print("det var det folketallet i dette år-et  : ", x[fm])


