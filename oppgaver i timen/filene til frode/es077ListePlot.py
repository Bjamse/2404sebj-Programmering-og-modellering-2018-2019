from numpy import * #importer pakke
tall1 = [1,2,3] #dette er lister
tall2 = [4,5,6]
matrise1 = array(tall1) #konverterer lister til matriser
matrise2 = array(tall2)

matrise3 = matrise1+matrise2
matrise4 = matrise1*matrise2
matrise5 = matrise1+1
matrise6 = matrise1*3
print(matrise1,'\n',matrise2,'\n',matrise3,'\n',matrise4,'\n',matrise5,'\n',matrise6)