import numpy as np

a = np.array([1, -1])
b = np.array([6, 1])
c = np.array([2, 2])
cm= np.array([7, 4])  # bare for feiltesting seinere
d = np.array([4, 6])

print("a = {}, b = {}, AB vektor = ".format(a,b), end="")
AB = b-a
print(AB)

print("a = {}, c = {},AC vektor = ".format(a,c), end="")
AC = c-a
print(AC)
print()

print("beregner CM ...")

cmBeregnet = a + AB + AC  # kunne bare skrevet c + AB men du ville bruke begge vektoene så da ble det sånn

print("cmberegnet = ", cmBeregnet)
print()

print("feiltester ... ")

if cm.all() == cmBeregnet.all(): # samenligner alle verdiene i begge arraya
    print("cmBeregnet og cm fra oppgavearket er like" )

else:
    print("beregningen var feil, cm fra oppgavearket er  ikke lik cm beregnet")