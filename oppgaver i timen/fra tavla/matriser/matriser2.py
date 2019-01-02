import numpy

tall1 = [1,2,3]
tall2 = [4,5,6]
mat1 = numpy.array(tall1)
mat2 = numpy.array(tall2)

mat3 = mat1 + mat2
mat4 = mat1 * mat2
mat5 = mat1 + 1
mat6 = mat1 * 3
print("tall1{}\ntall2{}\nmat1{}\nmat2{}\nmat3{}\nmat4{}\nmat5{}\nmat6{}".format(tall1, tall2, mat1, mat2, mat3, mat4, mat5, mat6))

