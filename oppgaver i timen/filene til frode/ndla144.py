from pylab import * #importer pakke

A=array([4,0,2])
B=array([3,5,1])
C=array([0,7,2])
D=array([3,5,4])
AB=B-A
AC=C-A
AD=D-A
ABXAC=cross(AB,AC)
volParp=dot(ABXAC,AD)
volParp=abs(volParp)

print("1.4.4 a ---------------------")
print('\n',"AB x AC=",ABXAC)
print('\n',"Volum parallellepiped= ",volParp)

volPyr=volParp/3
print('\n',"1.4.4 b ---------------------")
print('\n',"AB x AC=",ABXAC)
print('\n',"Volum pyramide= ",volPyr)


#print('\n',3/2*sqrt(26))
