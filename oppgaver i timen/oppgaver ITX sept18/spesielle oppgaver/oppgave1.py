def fak(n):
    return 1 if (n < 1) else n * fak(n-1)


print(fak(3))
print(fak(0))
print(fak(-3))
print(fak(4))