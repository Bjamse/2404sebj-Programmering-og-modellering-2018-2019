import numpy as np
import pylab as pl

a = np.array([2,3,4])
b = np.array([-3,5,2])

skalarAB = np.dot(a,b)

la = pl.norm(a)
lb = pl.norm(b)

print("a)\n a*b = {} \nb) \n lengde a = {} og lengde b = {} \n".format(skalarAB,la,lb))

