from pylab import * #importer pakke

A=array([4,0])
B=array([3,5])
C=array([0,7])
AB=B-A
ABL=norm(AB)

print('AB=',AB)
print('ABL=',ABL)
#print('3*a+2*b-4*c=',suma,'\n')

A=array([2,3])
B=array([-3,5])
APB=dot(A,B)
ABV=angle(A,B)
print('\n',"---------------------")
print('\n',"A prikk B=",APB)
print('\n',"A vinkel B=",APV)
