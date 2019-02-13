# denne gir deg en liste på de 995~ første fibonacci talla
# 996 ble satt som grense fordi det er ner hvor dypt python kan gå uten å få en stack overflow
# (det faktiske tallet varierer fra  funksjon til funksjon tror jeg...)
# grensa kan bli økt med: sys.setrecursionlimit(x)
# men det anbefales ikke da det kan gå ut over systemet ditt.
# her snakker vi om faktisk minne og hvor mye plass programmet har til å lagre midlertidige ting osv...
# du kan lese mer om det her :
# https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it#3323013


def fibAll(n, z=996):
    n.append(n[-1] + n[-2])
    if z > 0:
        fibAll(n, z - 1)
    return n


print(fibAll([1, 1]))


# skal du ha et spesifikt tall bruker du den under
# (!NB: mye tregere da den gjør mange regne oprasjoner etter hverandre, se forklaring)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# dette vil returnere det 5 fibbonasci tallet
print(fib(10))

# dette kann forklares med at:
# fib(2) vet vi skal være lik 1 hvis vi tenker på fibonacci som [0,1,1,2,3,5....]
# koden vil tenke mer sonn som dette:
# fib(2) = fib(1)+fib(0)
# fib(1) = 1
# fib(0) = 0
# fib(2) = 1 + 0 = 1
#
# slik vil det også være for høyere tall
#
# fib(5) = fib(4) + fib(3)
# fib(4) = fib(3) + fib(2)
# fib(3) = fib(2) + fib(1)
# fib(2) = fib(1)+fib(0)
# fib(1) = 1
# fib(0) = 0
# fib(2) = 1 + 0 = 1
# fib(3) = 1 + 1 = 2
# fib(4) = 2 + 1 = 3
# fib(5) = 3+2 = 5
# eller skrevet på en annen måte:
# fib(5) =
# fib(4) + fib(3) =
# ( fib(3) + fib(2) ) + ( fib(2) + fib(1) )=
# ( ( fib(2) + fib(1) ) + ( fib(1) + fib(0) ) ) + ( ( fib(1) + fib(0) ) + fib(1) )=
# ( ( ( fib(1) + fib(0) ) + fib(1) ) + ( fib(1) + fib(0) ) ) + ( ( fib(1) + fib(0) ) + fib(1) )=
# ( ( ( 1 + 0 ) + 1 ) + ( 1 + 0 ) ) + ( ( 1 + 0 ) + 1 )=
# 5



# oppgave a
for i in range(2, 150):
    print(fib(i)/fib(i-1))
# du kan tydelig se at outputen blir det gyldne snitt etterhvert men koden bruker veldig! lang tid på å bli færdig!
# det hadde vært mye raskere å prionte ut en liste for akkurat det ene
