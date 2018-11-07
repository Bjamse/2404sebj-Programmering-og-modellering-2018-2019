import numpy as np
import matplotlib.pyplot as plt
import sympy as spy


def getInt():
    while True:
        try:
            return int(input(" : "))
        except:
            print("funka ikke! prøv igjen", end="")


print("skriv inn verdi for a", end="")
a = getInt()
print("skriv inn verdi for b",end="")
b = getInt()
print("skriv inn verdi for c", end="")
c = getInt()
print("skriv inn verdi for x1", end="")
x_en = getInt()

x = spy.symbols('x')
f = a*x**2 + b*x + c
deriverte = spy.diff(f, x)
fx1 = f.subs(x,x_en)
fdx1 = deriverte.subs(x,x_en)

print("\n\n------------------------------- \n\n")
print("a = {}\nb= {}\nc = {}".format(a,b,c))
print("Nullpunktene til likningen {}*x^2 + {}*x + {} = 0 er ".format(a,b,c), spy.solve(spy.Eq(f, 0), x))
print("x1 har verdien {}, f(x1) er {}, f'(x1) er {}".format(x_en,fx1,fdx1))


x = np.arange(-15.0, 10.0, 0.1)
f = a*x**2 + b*x + c
tangent = fdx1*x - fdx1*x_en + fx1
# for å printe ut denne må vi hånd derivere. vet fortsatt ikke hvordan man gjør om sympy direkte til numpy funksjon
fder = 2*x + 2

plt.plot(x,tangent, 'r-.', label='$tangent til f(x)$')
plt.plot(x,f, 'g:', label='$f(x)={}x^2 + {}x + {}$'.format(a,b,c))
plt.plot(x,fder, 'b-', label="$f'(x)=2x + 2$")
# rakk ikke skrive ut fint hordan formlene ser ut men man kan bruke dette '$f(x)=x^3$' i label for å gjøre det bra
plt.xlim(-4,5)
plt.grid()
plt.ylim(-30,30)
plt.xlabel("x-akse")
plt.ylabel("y-akse")
plt.legend()
plt.title("annengradsfunksjon")
plt.show()



