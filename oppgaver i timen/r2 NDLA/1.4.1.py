import numpy as np
import pylab as pl

a = np.cross(np.array([2,5,1]), np.array([1,2,3]))
b = np.cross(np.array([1,2,3]), np.array([2,5,1]))
c = np.cross(np.array([3,2,3]), np.array([4,2,6]))
d = np.cross(np.array([-4,0,-2]), np.array([3,-1,2]))
e = np.cross(np.array([-3,-2,0]), np.array([-4,5,0]))
f = np.cross(np.array([0,2,1]), np.array([0,-3,4]))
g = np.cross(np.array([2,0,3]), np.array([-4,0,1]))
h = np.cross(np.array([1,0,0]), np.array([0,1,0]))
i = np.cross(np.array([1,0,0]), np.array([0,0,1]))
j = np.cross(np.array([0,1,0]), np.array([0,0,1]))
k = np.cross(np.array([0,1,0]), np.array([1,0,0]))

print("a) {} \nb) {} \nc) {} \nd) {} \ne) {} \nf) {} \ng) {} \nh) {} \ni) {} \nj) {} \nk) {} \n".format(a,b,c,d,e,f,g,h,i,j,k))
