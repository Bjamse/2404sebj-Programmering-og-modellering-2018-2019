import numpy
import pylab



vektorA = numpy.array([2, 3])
vektorB = numpy.array([-3, 5])
vektorC = numpy.array([-1, -6])

# a)
sumA = 3*vektorA + 2*vektorB - 4*vektorC
# b)
sumB = -5*vektorA + 3*vektorC - 4*vektorB
print("a = {} \nb = {} \nc = {}".format(vektorA, vektorB, vektorC))
print("a)\n 3*a + 2*b - 4*c = {}\nb)\n -*a + 3*c - 4*b = {}".format(sumA,sumB))