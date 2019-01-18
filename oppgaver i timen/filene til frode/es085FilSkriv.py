from pylab import *

N=10
t=linspace(0,N-1,N) #fom 0 inntil N, med N step
v0=0
a=0.14
s=v0*t+0.5*a*t**2
fil = open("bevegelse.txt", "w") #Åpne textfila "" til skriving "w"
fil.write("Tid     Akselrasjon \n")

for i in range(N):   #gå gjennom N ganger fom 0 med step på 1 
    fil.write(str(t[i]))
    fil.write("   ")
    fil.write(str(s[i]) + '\n')

fil.close