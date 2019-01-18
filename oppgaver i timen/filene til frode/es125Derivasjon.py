from pylab import * #importer pakke

def f(x):
    return 2*x**2 + x - 5

def derivert(f, x, delta_x):
    fder = (f(x+delta_x) - f(x))/delta_x
    return fder

delta_x = [10**-i for i in range(1,17)] # Listeløkke

for i in range(0, len(delta_x)):
    print("For delta_x =", delta_x[i], derivert(f,1,delta_x[i]))