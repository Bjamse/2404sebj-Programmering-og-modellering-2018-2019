fil = open("logfil", "r")

arr = []

for rad in fil:
    rad = rad.replace(",", ".")
    data = rad.split()
    arr.append([float(data[0]), float(data[1])])

forrigeLinje = arr[0]
for linje in arr[1:]:
    tmp = linje[1] - forrigeLinje[1]
    linje.append(round(forrigeLinje[0] - linje[0], 2))
    linje.append(tmp)
    linje.append(round(tmp / 1000 * 360))
    forrigeLinje = linje

# Utskrift
print("KWh     meter  forbr  dist  v=fart")
for rad in arr:
    print(rad)

fil.close()
