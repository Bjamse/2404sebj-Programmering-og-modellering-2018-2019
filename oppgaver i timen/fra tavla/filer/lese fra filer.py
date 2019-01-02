import pylab as pl

fil = open("res.txt", "r")
fil.readline()
t = []
s = []

for rad in fil:
    data = rad.split()
    t.append(float(data[0]))
    s.append(float(data[1]))

print(t)
print(s)

fil.close()