# def dekorator(funk):
#     return "kake " + funk()
#
# @dekorator
# def kakepluss():
#     return "spagetti"
#
#
# print(kakepluss)
#
#
#
# def funk1(funk):
#     return "kake " +funk
#
#
# def funk2():
#     return "spagetti"
#
#
# print(funk1(funk2()))



import numpy as np

x = np.array([1,2,3,4,5])

x = x[1:2].append( x[3:])

print(x)