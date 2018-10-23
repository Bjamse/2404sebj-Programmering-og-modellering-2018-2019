import numpy
import pylab


A = numpy.array([4, 0])
B = numpy.array([3, 5])
C = numpy.array([0, 7])
D = numpy.array([-3, 5])
E = numpy.array([-4, 0])
F = numpy.array([-3, -5])
G = numpy.array([3, -5])

# a)
ab = B-A
cd = D-C
ef = F-E
gc = C-G
fa = A-F
ec = C-E
print("a)")
print("ab = {}\ncd = {}\nef = {}\ngc = {} \nfa = {} \nec = {}".format(ab, cd, ef, gc, fa, ec))

# c)
lab = pylab.norm(ab)
lcd = pylab.norm(cd)
lef = pylab.norm(ef)
lgc = pylab.norm(gc)
lfa = pylab.norm(fa)
lec = pylab.norm(ec)

print("\nc)")
print("lengde ab = {}\nlengde cd = {}\nlengde ef = {}\nlengde gc = {} \nlengde fa = {} \nlengde ec = {}".format(lab, lcd, lef, lgc, lfa, lec))