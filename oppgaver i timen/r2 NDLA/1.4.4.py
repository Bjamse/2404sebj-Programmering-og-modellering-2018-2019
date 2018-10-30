import numpy as np

a = np.array([4,0,2])
b = np.array([3,5,1])
c = np.array([0,7,2])
d = np.array([3,5,4])

AB = b-a
AC = c-a
AD = d - a

# a)
# denne var veldi fin syns jeg :D
# eller så kan du bare bruke np.abs(<tall>) og få det samme...
# men det er ikke like morro !
volumA = (np.dot(np.cross(AB, AC), AD) if np.dot(np.cross(AB, AC), AD) >= 0 else np.dot(np.cross(AB, AC), AD) * -1)

# b)

volumB = volumA / 3

# c)

volumC = volumA / 6


# print resultat

print(" volumet av parallellepipedet utspent av AB , AC og AD  er : {} ".format(volumA),
      "\n volumet av pyramiden med firkantet grunnflate utspent av AB, AC og AD er : {}".format(volumB),
      "\n volumet av pyramiden med trekantet grunnflate (tetraederet) utspent av AB , AC og AD er : {}".format(volumC))
