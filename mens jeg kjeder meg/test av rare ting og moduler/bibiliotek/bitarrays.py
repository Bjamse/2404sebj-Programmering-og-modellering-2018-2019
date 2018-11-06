from bitarray import bitarray

# https://pypi.org/project/bitarray/
# et array kan kuyn ha 16 Gigabit med data ( altså 2^34 elementer)
# et bitarray er ingen vanlig liste. kan kun lagre true aeller false verdier

# eksempler
print("a")
a = bitarray()                      # lag et tomt bitarray
a.append(True)                      # legg til en verdi
a.extend([False, True, True])       # legg til mange verdier
print(a)
a[2] = False
print(a)

print("\n------------------------\n")
print("b")
b = bitarray(2**3)                 # bitarray med lengde 2^3 (innhold er tilfeldig?)
print(b)
b.extend("101010")                 # utvid et array med en string
print(b)

print("\n------------------------\n")
c = bitarray([True for x in range(10000)])  # lger et pitarray av en liste, lista er generert i en for loop
print(len(c))