import random
import sympy
import matplotlib.pyplot as plt
import numpy as np

def getfloat():
    while True:
        try:
            x = float(input("Skriv inn et tall :  "))
            break
        except:
            print("Ikke et tall, prøv igjenn")
    print()
    return x



print()
print("oppgave 1")
print()




kupong = []
temp = 0
for i in range(7):
    while True:
        temp = random.randint(1, 34)
        if temp in kupong:
            continue
        kupong.append(temp)
        break

print("Vinnertallene var = ", kupong)





print()
print("oppgave 2")
print()

a = getfloat()
b = getfloat()
c = getfloat()

x = sympy.symbols('x')
expr = a*x**2 + b*x + c

print("Nullpunktene til likningen {}*x^2 + {}*x + {} = 0 er ".format(a,b,c), sympy.solve(sympy.Eq(expr, 0), x))

print()
print("oppgave 3")
print()

a = getfloat()
b = getfloat()
c = getfloat()


x = np.arange(0.0, 10.0, 0.01)
y = a*x**2 + b*x + c
plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('{}*x^2 + {}*x + {}'.format(a,b,c))
plt.grid(True)
plt.savefig("output.png")
plt.show()

print()
print("oppgave 4")
print()

a = getfloat()
b = getfloat()


x = np.arange(0.0, 10.0, 0.01)
y = np.sin(a*x)*b
plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('sinus(ax)*b')
plt.grid(True)
plt.savefig("output.png")
plt.show()