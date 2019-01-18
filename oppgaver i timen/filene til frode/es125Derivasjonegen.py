from pylab import * #importer pakke

def f(x):
    return 2*x**2 + x - 5

def derSymb(x):
    return(4*x+1)

x=1
x=float(input("\n Tast inn x-verdi for derivert: "))
print("\n f derivert symbolsk for x=",x," fSymb=",derSymb(x),"\n")





def derivert(f, x, delta_x):
    fder = (f(x+delta_x) - f(x))/delta_x
    return fder

delta_x = [10**-i for i in range(1,17)] # Listeløkke
#print(delta_x,"\n")

#Her lar vi delta_x bli stadig mindre og kaller derivertfunk.
for i in range(0, len(delta_x)):
    print("For delta_x =", delta_x[i], derivert(f,x,delta_x[i]))