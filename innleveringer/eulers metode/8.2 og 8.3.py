# kilde : http://code.activestate.com/recipes/577647-ode-solver-using-euler-method/

"""
Hei frode!
jeg bruker den løsningen for eulers metode som jeg fant på nett.
er samme som din, bare litt mer kompakt
måtte legge til litt her og der fordi noeen resultater går mot uendelig store
"""
# First Order ODE (y' = f(x, y)) Solver using Euler method
# xa: initial value of independent variable
# xb: final value of independent variable
# ya: initial value of dependent variable
# n : number of steps (higher the better)
# Returns value of y at xb.
def Euler(f, xa, xb, ya, n):
    h = (xb - xa) / float(n)
    x = xa
    y = ya
    for i in range(n):
        fxy = f(x, y)
        if (fxy == "too large!"):
            return str(y)+" men den stoppa på x verdi " + str(x)+" fordi tallet y ble for stort"

        y += h * fxy
        x += h
    return y

# Euler(funksjon,startx, sluttx, starty, antall steg)


# oppgave 1
def a(x,y):
    return 1


print(1," ",Euler(a, 0, 5, 0, 1000))


# oppgave 2
def b(x,y):
    return x


print(2," ",Euler(b, 0, 5, 0, 1000))


# oppgave 3
def c(x,y):
    return 4+3*y


print(3," ",Euler(c, 0, 5, 0, 1000))


# oppgave 4
def d(x,y):
    return -4*y-3*x


print(4," ",Euler(d, 0, 5, 0, 1000))


# oppgave 5
def e(x,y):
    if x == 0:
        return 0
    return (3*x**2 + 4*x - y)/x


print(5," ",Euler(e, 0, 5, 0, 1000))


# oppgave 6
def f2(x,y):
    try:
        res = float(x + y ** 2)
        return res
    except:
        return "too large!"


print(6," ",Euler(f2, 0, 5, 0, 1000))



#_________________________________________
# 8.3
"""
vi må ha initsialverdier med for å vite hvor vi skal starte når vi gjør våre kalkluleringer. 
det er utgangspunktet når vi løser diffrensialligninger numerisk
"""

