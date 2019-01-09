fil = open("logfil", "r")

arr = []

for rad in fil:                  # for hver linje som legges i rad registrer log data
    rad = rad.replace(",", ".")  # bytt "," med "." for det kommer fra excel
    data = rad.split()           # Fungerer bra uten parameter selv om det her er tab og default er space
    arr.append([float(data[0]), float(data[1])])

forrigeLinje = arr[0]
for linje in arr[1:]:  # Starter på andre rad og regner med første rad.
    data1 = round(forrigeLinje[0] - linje[0], 2)
    linje.append(data1)
    data2 = linje[1] - forrigeLinje[1]
    linje.append(data2)
    data3 = round(data2 /1000*360)
    linje.append(data3)
    forrigeLinje = linje

# Utskrift
print("KWh     meter  forbr  dist  v=fart")
for rad in arr:
    print(rad)

fil.close()
