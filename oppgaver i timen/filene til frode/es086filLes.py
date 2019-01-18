from pylab import *

fil = open("bevegelse.txt", "r")

fil.readline()
#print("fil",fil.readline())
t = []
s = []

for rad in fil: # for hver linje som legges i rad
    data = rad.split()
    print(rad)
    print(data)
    t.append(float(data[0]))
    s.append(float(data[1]))
print(t)
print(s)
fil.close