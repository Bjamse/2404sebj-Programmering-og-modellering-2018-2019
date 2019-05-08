from pylab import *  # importerer pakke


def getFloat():  # denne funksjonen får brukeren til å skrive inn et tall om nekter å stoppe å spørre før den får en gyldig float
    while True:
        try:
            return float(input("skriv inn et tall: "))
        except:
            print("du skrev inn noe som ikke var et tall! prøv igjen!")

a= 0
print("tast inn en statverdi for x")
ba = abs(getFloat())  # startverdi x

print("tast inn en sluttverdi for x")
b = abs(getFloat()) # sluttverdi x

if ba >= b:
    ba,b = b,ba

N = 1000*int(b) # antall intervaller (hvor nøye vi skal kalkulere med eulers metode ) (definert med presisjonen brukeren shriver inn)
h = (b - a) / (N - 1) # steglengde beregnet mtp antall intervaller
y0 = 30 # initial(start)verdi for y


# Den deriverte av fynksjonen f(x) eller y
# altså diffligningen vi skal berege med
def yder(y, x):
    return 0.266*(y-((y**2)/6000))


# Matriser
# et par tomme matriser som skal inneholde koordinatene til punktene regnet ut
x = zeros(N)
y = zeros(N)

y[0] = y0  # setter første punkt i ylista til å være initsialverdien for y

# Eulers metode
for i in range(N - 1):
    y[i + 1] = y[i] + yder(y[i], x[i]) * h
    x[i + 1] = x[i] + h


def getbyx(verdi):
    return (np.where(x == min(x, key=lambda x: np.abs(x - verdi))))[0][0]

# oppgave c)
nyX = x[getbyx(ba):]
nyY = y[getbyx(ba):]


title= "Graf kalkulert med eylers metode"
xlabel = "x-verdier"
ylabel = "yverdier"

plot(nyX, nyY)
grid(True)  # slår på rytenett
show()


