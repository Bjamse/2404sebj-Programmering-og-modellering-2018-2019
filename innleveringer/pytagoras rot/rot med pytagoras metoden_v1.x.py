def getint():
    while True:
        try:
            x = int(input("Skriv inn et heltall :  "))
            break
        except:
            print("Ikke et heltall, prøv igjen")
    return x


print()
print("Dette programmet finner roten av et tall på pytagoras metoden.")
print("Først må vi ha et tall å finne roten av.")
tall = getint()
print()
print("Velg hvor pressist kalkuleringen skal være (for lave tall velg 100, ellers 1000 +++")
pressisjon = getint()

res = 1.0
htall = tall
ltall = 0

for i in range(pressisjon):
    res = (htall+ltall)/2
    if res**2 == tall:
        print("roten av ", tall, " = ", res)
        break
    elif res**2 > tall:
        htall = res
    else:
        ltall = res

print(res)
