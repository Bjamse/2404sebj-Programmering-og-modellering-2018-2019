from pylab import * #importer pakke
#from numpy import * #importer pakke
tall1=[1,5,9]
tall2=[2,2,3]
matrise1=array(tall1)
matrise2=array(tall2)
matrise3=array([[4,5], [2,3]]) #Lager 2x2 matrise direkte
skalar=dot(matrise1,matrise2)
vekttorProd=cross(matrise1,matrise2)
deter=cross([1,4],[2,5])
lengde = norm(matrise1)
print(matrise1,'\n',matrise2,'\n',matrise3,'\n',skalar)
print('\n',vekttorProd,'\n',deter,'\n',lengde)