# from pylab import *

fil = open("log01.txt", "r")

fil.readline()  # Les inn hodetekst linje

arr = []
print("type arr???", type(arr))  # for å sjekke at det er listeobjekt g ikke array

for rad in fil:  # for hver linje som legges i rad registrer log data
    rad = rad.replace(",", ".")  # bytt "," med "." for det kommer fra excel
    data = rad.split()  # Fungerer bra uten parameter selv om det her er tab og default er space
    arr.append([float(data[0]), float(data[1])])

arrKopi = arr.copy()  # Lag en kopi av Listen arr
arrKopi.insert(0, [24, 0])  # Legg inn element først slik at beregningene ligger parallellt

arr[0].append(0.0)  # Legg inn en 0-verdi i toppen slik at beregningen går greit
arrLengde = len(arr)
print("arrLengde: ", arrLengde)

# print(0,"ffffff ",arr[0])
for i in range(1, arrLengde):  # Starter på andre rad og regner med første rad.
    l = arr[i]
    l2 = arrKopi[i]
    diff = round(l2[0] - l[0], 2)
    arr[i].append(diff)
    diff2 = arr[i][1] - arrKopi[i][1]
    arr[i].append(diff2)

for i in range(1, arrLengde):  # Beregner og registrerer v = farten i km/h fra m/10s
    v = arr[i][3] / 1000 * 360
    v = round(v, 2)
    arr[i].append(v)

# Utskrift
print("KWh     meter  forbr  dist  v=fart")
for rad in arr:
    print(rad)

fil.close