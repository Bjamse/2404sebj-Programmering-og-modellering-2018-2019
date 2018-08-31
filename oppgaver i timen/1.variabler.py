print("Oppgave 1")
print()

tall_0 = 2
tall_1 = 51

print(tall_0, " + ", tall_1, " = ", tall_0 + tall_1)
print(tall_0, " - ", tall_1, " = ", tall_0 - tall_1)
print(tall_0, " * ", tall_1, " = ", tall_0 * tall_1)
print(tall_0, " / ", tall_1, " = ", tall_0 / tall_1)
print(tall_0, " opphøyd i  ", tall_1, " = ", tall_0 ** tall_1)


print("oppgave 2")
print()
liste_av_variabler = [
    "abc",
    3,
    2.63737,
    [1,2,"abc"],
    (1,2),
    {"nummer1": 2}
]

for i in liste_av_variabler:
    print("dette har datatypen : ", i)


liste_av_variabler.append(liste_av_variabler[1] + int(liste_av_variabler[2]))

print(liste_av_variabler)
print()
print("oppgave 3")
print()
tall_0 = 3

print(" tall_ 0 = ", tall_0, " og har datatypen ", type(tall_0), "\n ved å bruke funksjoinen str() blir tall_0 en tekstvariabel slik", type(str(tall_0)))

print()
print("oppgave 4")
print()
while True:
    try:
        tall_0 = int(input("skriv innn et tall som du vil se om er delelig på 2: "))
        break
    except:
        print("prøv igjenn")

if tall_0 % 2 == 0:
    print(tall_0, " er delelig på 2")
else:
    print(tall_0, " går ikke opp i 2")


print()
print("oppgave 5")
print()

fart = 20
tid = 30

strekning = fart * tid

print("Tilbakelagt strekning er", strekning, "meter.")
print("Farten er ", strekning/tid)

print()
print("oppgave 6")
print()

print("Ja bare å bytte en variabel med tekst eller tid til 0. går ikke å dele på 0")

input("trykk enter for å avslutte")

