# Importerer nødvendige biblioteker
import matplotlib.pyplot as plt

# Lager to lister (tupler) med tall.
# Hvert tallpar danner et punkt.
x = (0, 1, 2, 3, 4)
y = (0, 1, 4, 9, 16)

# Utskrift av data
plt.plot(x, y)
#plt.show()
z = (0, 1, 8, 27, 64) # Vi lager et datasett til.

plt.grid() # Lager rutenett
plt.xlabel('$x$') # Merker x-aksen
plt.ylabel('$f(x)$') # Merker y-aksen

plt.plot(x, y, 'bx-.', label='$f(x)=x^2$') # bx-- -> blå stiplet linje med x som punktmarkering.
plt.plot(x, z, 'gs:', label='$f(x)=x^3$') # gs-- -> grønne kvadrat med finstiplet linje
plt.legend() # Infoboksen øverst i hjørnet. Bruker data fra label
plt.show()