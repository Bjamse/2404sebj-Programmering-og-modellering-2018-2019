import numpy
import pylab

A = numpy.array([2, 3])
B = numpy.array([-3, 5])

print("a)\n skalarproduktet mellom a og b er {}".format(numpy.dot(A,B)))
print("b)\n lengden til a er {} og lengden til b er {}".format(pylab.norm(A),pylab.norm(B)))
