print()
print("oppgave 1")
print()
def ukedag(x):
    ukedager = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]
    return ukedager[x%7]

print()
print("oppgave 2")
print()
def CelsiusToFarenheit(x):
    return x*(9/5)+32

for i in range(1,101):
    print(i, " grader Celsius er det samme som ", CelsiusToFarenheit(i), " grader Farenheit.")

print()
print("oppgave 3")
print()

def FarenheitToCelsius(x):
    return (x-32)/(9/5)

print(FarenheitToCelsius(1))