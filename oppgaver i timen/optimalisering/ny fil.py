import numpy as np
import pylab as pl
a = np.array([0,1,3])
b = np.array([1,3,3])
c = np.array([2,3,4])

AB = b-a

AC = c-a

print("\n \n kryssproduktet av vektor AB og AC delt på 2 gir arealet = ", pl.norm(np.cross(AC,AB))/2)

