import numpy as np
import pylab as pl

a = np.array([2,1])
b = np.array([7,3])
c = np.array([4,6])
d = np.array([12,5])
e = np.array([10,4])

# a)---------------------------
print("a)")
print("a= {} b={} c={}".format(a,b,c))


# b)---------------------------
print("\nb)")


def tilvektor(n,m):
    # returnerer vektor n til m
    return m-n


AB = tilvektor(a,b)
AC = tilvektor(a,c)
print("AB-vektor = {} AC-vektor = {}".format(AB,AC))

# c) --------------------------
print("\nc)")
def arealTrekant(j,k,l):
    JK = tilvektor(j,k)
    JL = tilvektor(j,l)
    return pl.norm(np.cross(JK,JL))/2


print("areal av trekant ABC er = {}".format(arealTrekant(a,b,c)))

# d) ---------------------------
print("\nd)")

AD = tilvektor(a,d)
AE = tilvektor(a,e)

print("D= {} og E= {} \nAD= {} og AE= {}".format(d,e,AD,AE))

# e )-----------------------------

print("\ne)")


def erParralelle(j,k):
    x = j[0]/k[0]
    y = j[1] / k[1]
    return x == y


if erParralelle(AB,AD):
    print("AB og AD er parralelle, a, b og d ligger på linje")
else:
    print("AB og AD er ikke parralelle, a, b og d ligger ikke på linje")

if erParralelle(AB,AE):
    print("AB og AE er parralelle, a, b og e ligger på linje")
else:
    print("AB og AE er ikke parralelle, a, b og e ligger ikke på linje")

# f) ----------------------------------
print("\nf)")
h = (2*arealTrekant(a,b,c))/pl.norm(AB)
print("høyde = {} grunnlinje = {} areal = {}".format(h,pl.norm(AB),arealTrekant(a,b,c)))