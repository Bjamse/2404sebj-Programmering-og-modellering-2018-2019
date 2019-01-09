fil = open("logfil", "r")

arr = []

for rad in fil:                  # for hver linje som legges i rad registrer log data
    rad = rad.replace(",", ".")  # bytt "," med "." for det kommer fra excel
    data = rad.split()           # Fungerer bra uten parameter selv om det her er tab og default er space
    arr.append([float(data[0]), float(data[1])])


for indeks, linje in enumerate(arr):  # Starter på andre rad og regner med første rad.
    if indeks == 0:
        continue

    diff = round(arr[indeks-1][0] - arr[indeks][0], 2)

    linje.append(diff)
    diff2 = arr[indeks][1] - arr[indeks -1][1]
    linje.append(diff2)

for i in arr[1:]:  # Beregner og registrerer v = farten i km/h fra m/10s, hopper over første linja ford idet ikke har blitt beregnet noe der
    v = i[3] / 1000 * 360
    v = round(v, 2)
    i.append(v)

# Utskrift
print("KWh     meter  forbr  dist  v=fart")
for rad in arr:
    print(rad)

fil.close()
