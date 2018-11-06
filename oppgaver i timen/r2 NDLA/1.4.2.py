from pylab import * #importer pakke

A=array([4,0,2])
B=array([3,5,1])
C=array([0,7,2])
AB=B-A
AC=C-A
ABXAC=cross(AB,AC)
FTrekant= norm(ABXAC)/2
print("1.4.2 ---------------------")
print('\n',"AB x AC=",ABXAC)
print('\n',"Areal trekant=",FTrekant)
print('\n',3/2*sqrt(26))