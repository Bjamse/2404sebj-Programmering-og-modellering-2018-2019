import sympy as spy

a = 3
b = -6
c = 3

x = spy.symbols('x')
f = a*x**2 + b*x + c

deriverte = spy.diff(f, x)

print("funksjonen =",f)
print("deriverte av funksjonen",deriverte)
print(f.subs(x,32))
print(deriverte.subs(x,32))