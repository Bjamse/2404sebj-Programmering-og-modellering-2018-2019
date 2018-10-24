import numpy
import pylab
# a)
A = numpy.array([6, 0])
B = numpy.array([0, -4])
C = numpy.array([4, 3])
D = numpy.array([3, -3])
E = numpy.array([-8, -6])
F = numpy.array([-4, -2])
G = numpy.array([-3, -4])

print("a)\na ={} \nb ={} \nc ={} \nd ={} \ne ={} \nf ={} \ng ={} \n". format(A, B, C, D, E, F, G))

# b)

print("b)\n a+b = {}\n c-d = {} \n".format(A+B, C-D))

# c)

print("c)\n lengden til e er {} og lengden til g er {} \n".format(pylab.norm(E),pylab.norm(G)))

# d)

if numpy.dot(C,D) == 0:
    print("c og d står vinkelrett på hverandre")
else:
    print("c og d står ikke vinkelrett på hverandre")

# e) orka ikke kl 1 på natta
