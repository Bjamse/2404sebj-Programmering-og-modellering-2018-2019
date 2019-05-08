from pylab import *  # importerer pakke

# Tidssteg
N = 200  # antall intervaller (hvor nøye vi skal kalkulere med eulers metode ) (definert med presisjonen brukeren shriver inn)
a = 0  # startverdi x
b = 15  # sluttverdi x
h = (b - a) / (N - 1)  # steglengde beregnet mtp antall intervaller
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


# oppgave a)
plot(x, y)
grid(True)  # slår på rytenett
title= "Graf kalkulert med eylers metode"
xlabel = "x-verdier"
ylabel = "yverdier"

show()



