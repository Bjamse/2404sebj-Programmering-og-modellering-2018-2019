import pylab as pl


def getFloat():
    while True:
        try:
            return float(input("skriv inn et tall :"))
        except:
            print("prøv igjenn!")


def f(x):
    return 2*x**2 + x - 5


def fder(x):
    return 4 * x + 1


x = getFloat()

print("\n f derivert symbolsk for x={}  er  {}".format(x, fder(x)))


def derivert(f, x, delta_x):
    return (f(x+delta_x) - f(x))/delta_x


deltaX = [10**-i for i in range(1,17)]

for i in deltaX:
    print("For deltaX = {} da blir den deriverte {}".format(i, derivert(f,x,i)))