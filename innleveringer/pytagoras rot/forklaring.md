# Hvordan koden fungerer:
### v1
#### Funksjonene

````
def getint():
    while True:
        try:
            x = int(input("Skriv inn et heltall :  "))
            break
        except:
            print("Ikke et heltall, prøv igjen")
    return x
    
 ````
Funksjonen henter en input fra brukeren og sørger for at det er et heltall. <br>
Får den ikke det prøver den på nytt til den får det. <br>

#### Hovedfunksjonen

```
for i in range(pressisjon):
    res = (htall+ltall)/2
    if res**2 == tall:
        print("roten av ", tall, " = ", res)
        break
    elif res**2 > tall:
        htall = res
    else:
        ltall = res

print(res)
```
Funksjonen er egentilig rellativt enkel.

Man starter med tallet man skal ta roten av og lagrer det i en variabel **tall**. **tall** høy-variabel og 0 i en lav-variabel kalt **htall** og **ltall**.
så tar men gjennomsnittet av disse to og kaller dette for **res**. **res** blir da variablen man tester som en poteniel rot av tallet man ser tar roten av.

Hvis dette stemmer returnerer man res og er ferdig med funksjonen.

Hvis ikke blir res satt som verdi for enten **htall** eller **ltall** alt ettersom **res** opphøyd i 2 er mer eller mindre en **tall**.

Deretter looper koden og man fortsetter helt til man har gjort det like mange ganger som ble spesifisert av brukeren i **pressisjon**

På den måten vil man hele tiden nerme seg tallet som er roten av **tall**.

## v2


#### Funksjonene

````
def getint():
    while True:
        try:
            x = int(input("Skriv inn et heltall :  "))
            break
        except:
            print("Ikke et heltall, prøv igjen")
    return x
    
 ````
Funksjonen henter en input fra brukeren og sørger for at det er et heltall. <br>
Får den ikke det prøver den på nytt til den får det. <br>

```
def getfloat():
    while True:
        try:
            x = float(input("Skriv inn et tall :  "))
            if x < 0.0000000000001:
                print("Ikke så smått da.... :/")
                continue
            break
        except:
            print("Ikke et tall, prøv igjenn")
    print()
    return x

```
Denne funksjonen er også relativt rett frem. Den prøver å mota en input fra brukeren som i form av et tall (gjerne med desimaler).
For at ikke koden senere skal loope for all fremtid er det satt en grense på at tallet ikke kan være mindre enn 0.0000000000001.
Dette ble gjort fordi floating point numbers er lagret i 2 tallsystemet på disken og .... bare se videoen til Tom Scott  
[på youtube.](https://www.youtube.com/watch?v=PZRI1IfStY0)

````
def getdiff(x, y):
    x -= y
    if x < 0:
        x *= -1
    return x
````
Funksjonen finner absoluttverdien av differansen mellom to tall. altså den possitive verdien av differansen mellom input x og y.
#### Hovedfunksjonen

```
while True:
    res = (htall+ltall)/2
    if res**2 == tall:
        print("roten av ", tall, " = ", res)
        break
    elif res**2 > tall:
        htall = res
    else:
        ltall = res

    if getdiff(res**2, tall) < feilmargin:
        print("feilmarginen feilmarginen ble nådd.\n", "Roten av ", tall, " er omtrent ", res, "\n", res, " * ", res, " = ", res**2)
        break
```
Funksjonen er egentilig rellativt enkel.

Man starter med tallet man skal ta roten av og lagrer det i en variabel **tall**. **tall** høy-variabel og 0 i en lav-variabel kalt **htall** og **ltall**.
så tar men gjennomsnittet av disse to og kaller dette for **res**. **res** blir da variablen man tester som en poteniel rot av tallet man ser tar roten av.

Hvis dette stemmer returnerer man res og er ferdig med funksjonen.

Hvis ikke blir res satt som verdi for enten **htall** eller **ltall** alt ettersom **res** opphøyd i 2 er mer eller mindre en **tall**.

Deretter looper koden og man fortsetter helt til **res** i andre har en differanse på mindre enn **feilmargin** til **tall**
.
På den måten vil man hele tiden nerme seg tallet som er roten av **tall**.
