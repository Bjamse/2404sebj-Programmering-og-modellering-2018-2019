print()
print("oppgave 1")
print()

for i in range(1,21):
    print(i)
print()
print("oppgave 2")
print()

for i in range(10, 0, -1):
    print(i)
print()
print("oppgave 3")
print()

for i in range(10, 50, 2):
    print(i)

print()
print("oppgave 4")
print()
while True:
    try:
        tall_0 = int(input("skriv innn et heltall : "))
        break
    except:
        print("prøv igjenn")

for i in range(0, tall_0 +1):
    print(i)



print()
print("oppgave 5")
print()

while True:
    try:
        tall_0 = int(input("skriv innn et heltall: "))
        break
    except:
        print("prøv igjenn")

if tall_0 > 5:
    print("tallet er større enn 5")
elif tall_0 < 5:
    print("tallet er mindre enn 5")
else:
    print("tallet er lik 5")




input("trykk enter for å avslutte")