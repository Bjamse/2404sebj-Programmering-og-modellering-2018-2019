from pylab import *
x=linspace(0,10,101)
y=sin(x)
#print(x)
subplot(2,1,1)   #To rader, en kolonne, figur 1
plot(x,y,'g--')  #g = grønn, -- = stipla linje
ylim(-1.1, 1.1)  #Verdimengde må spesifiseres for hver figur
xlim(-3,17)
title("Grønn stiplet linje")

subplot(2,1,2)
plot(x,y,'ro')    #r=rød,  o = prikker
show()
