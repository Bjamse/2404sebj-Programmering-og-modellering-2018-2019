from pylab import *  # importerer pakke
import numpy as np  # importerer numpy (egentlig redundant siden den blir importer t av pylab så blir sikker t fjernet i fremtidig utgaver av programmet)


def getint():  # en funksjon som ikke stoper å kjøre før brukeren skriver inn et heltall
    # altså hvis brukeren skriver inn noe som ike kan tolkes som et tall så prøver den igjen
    while True:
        try:
            return int(input("Skriv inn et heltall : "))
        except:
            print("prøv igjenn. du skrev ikke inn et gyldig heltall")


print(
    "Grunnet måten programmet er utformet på må vi vite hvor \nmange timer inn i fremtiden du antar du har lyst til å kalkulere. \n" +
    "Dette gjør at vi kan kalkulere med høyere presisjon det du vil.\n" +
    "\nSkriv in et antall timer du vil kalkulere")

antTimer = np.abs(getint())

print("skriv in presisjonen du vil ha på kalkuleringen 100 er lite og 10000 er grei presisjon : ")
presisjon = getint()

# Tidssteg
N = presisjon  # antall intervaller (hvor nøye vi skal kalkulere med eulers metode ) (definert med presisjonen brukeren shriver inn)
a = 0.0  # startverdi x
b = antTimer  # sluttverdi x (definert med antall år brukeren shriver inn)
h = (b - a) / (N - 1)  # steglengde beregnet mtp antall intervaller
y0 = 0.5  # initial(start)verdi for y


# Den deriverte av fynksjonen f(x) eller y
# altså diffligningen vi skal berege med
def yder(y, x):
    return 0.02-(1/10)*y


# Matriser
# et par tomme matriser som skal inneholde koordinatene til punktene regnet ut
x = zeros(N)
y = zeros(N)

y[0] = y0  # setter første punkt i ylista til å være initsialverdien for y

# Eulers metode
for i in range(N - 1):
    y[i+1] = y[i]+yder(y[i], x[i])*h
    x[i+1] = x[i]+h


# funksjonenr som blir brukt i besvarelsen
# ----------------------------------------------------------------------------------------------------
def getFloat():  # denne funksjonen får brukeren til å skrive inn et tall og nekter å stoppe å spørre før den får en gyldig float
    while True:
        try:
            return float(input("skriv inn et tall: "))
        except:
            print("du skrev inn noe som ikke var et tall! prøv igjen!")


# en funksjon for å å det nermeste året som er ferdig kalkulert mtp det brukeren ønsker å få vite data om
# returnerer en float med indexen til den  som var nermest
# bør ikke kalles før euklers funksjon er kjørt minst en gang!!!!
# kommer til å fæile...
def getByTime():
    while True:  # lagre en brukerinputt med et antall timer i en variabel
        print("velg et antall timer mer eller lik enn 0 eller mindre den siste timen kalkulert (",b,")")
        BVT = getFloat()  # bruker valgt time

        if b >= BVT >= 0:  # hvis brukeren skrev inn en time som var mindre enn 0 (eller mer en største kalkulerte) så blir Han/hun nødt tyil å prøve på nytt
            break
        else:
            print("du vlgte et antall timer som som ikke var mer eller lik 0 eller mindre enn ", b)

    return (np.where(x == min(x, key=lambda x: np.abs(x - BVT))))[0][0]  # finner nermeste kalkulerte året til det som brukeren har skrevet inn


def getBYKlor():
    while True:  # lagre brukerinputt med en folkemengde i en variabel, stopper ikke før du taster inn en mindre eller lik eller lik
        print("velg en mengde")
        BVMK = getFloat()  # bruker valgt mengde klor
        if 0 <= BVMK <= y0:
            break
        else:
            print("du vlgte en mengde som var større enn ", y0," eller mindre enn null\nprøv igjen!\n")

    fm = (np.where(y == min(y, key=lambda x: np.abs(x - BVMK))))[0][0]  # finner nermeste kalkulerte yverdi til det som brukeren har skrevet inn for klormengde

    # fm er en index for hvor i lista med y verdier som var nermest den som brukeren skrev inn
    # da kan vi bruke den i begge lsiter for å finne y og x verdiene ( selv om vi vet y for di det var jo den som var nermest det brukeren skrev inn)
    return fm


# ______________________________________________________________________________________________


# oppgave a)
print("oppgave a\n")
print("oppgave a er plottet som blir vist")  # plotter diffligninga
plot(x, y)
grid(True)  # slår på rytenett
ylabel("klormengde")
xlabel("Tid (timer)")
show()

# oppgave b)
# vises kun når viduet til a er lokket.
print("\n\noppgave b) \n")
print("velg et antall timer å finne klormengden ved")

EtAntallTimerValgtAvBrukeren = getByTime()  # indexen til det nermeste kalkulerte året mtp det brukeren taster inn

print("nermeste antall timer kalkulert er : ", round(x[EtAntallTimerValgtAvBrukeren], 4), "  timer")
print("mengden klor er da : ", round(y[EtAntallTimerValgtAvBrukeren], 4), " liter klor")
print("prosentvis mengde klor ved dette tidspunktet var da : ", round(y[EtAntallTimerValgtAvBrukeren] / 100, 6), " %")

# oppgave c)

print("\n\noppgave c) \n")
print("finn økningen et år")

EtAntallTimerValgtAvBrukeren = getByTime()  # indexen til det nermeste kalkulerte året mtp det brukeren taster inn

print("nermeste antall timer kalkulert er : ", round(x[EtAntallTimerValgtAvBrukeren], 4), "  timer")
print("stigningen i mengde klor ved dette tidspunktet var da  : ", round(yder(y[EtAntallTimerValgtAvBrukeren], 0), 5), "   liter/time")
print("prosentvis stigningen i mengde klor ved dette tidspunktet var da : ", round(yder(y[EtAntallTimerValgtAvBrukeren], 0) / 100, 6), " %")

# oppgave d)
print("\n\noppgave d)")
print("skriv inn antall liter klor og finn ut når det var så mange (må velge mer en mengde større enn 0 om mindre enn ",y0 ,")")

enKlorMengdeValgtAvBrukeren = getBYKlor()  # indexen til den nermeste kalkulerte folketallet mtp det btrukeren skriver inn

print("nermeste kalkulerte klormengde er: ", round(y[enKlorMengdeValgtAvBrukeren], 4))
print("denne verdien ble oppnådd etter ", round(x[enKlorMengdeValgtAvBrukeren], 4), " timer")
