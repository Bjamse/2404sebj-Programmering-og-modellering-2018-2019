import numpy
import pylab

mat1 = numpy.array([1, 5, 9])
mat2 = numpy.array([2, 2, 3])
mat3 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
skalar = numpy.dot(mat1, mat2)
vektProd = numpy.cross(mat1,mat2)
determinant = numpy.cross([1,4],[2,5])
lengde = pylab.norm(mat1)
print("{}\n{}\n{}\n{}\n{}\n{}\n{}".format(mat1, mat2, mat3, skalar, vektProd, determinant, lengde))
