def getint():
    while True:
        try:
            x = int(input("Skriv inn et heltall :  "))
            break
        except:
            print("Ikke et heltall, prøv igjenn")
    print()
    return x


def getfloat():
    while True:
        try:
            x = float(input("Skriv inn et tall :  "))
            if x < 0.0000000000001:
                print("Ikke så smått da.... :/")
                continue
            break
        except:
            print("Ikke et tall, prøv igjenn")
    print()
    return x


def getdiff(x, y):
    x -= y
    if x < 0:
        x *= -1
    return x


print()
print("Dette programmet finner roten av et tall på pytagoras metoden.")
print("Først må vi ha et tall å finne roten av.")

tall = getint()
print("Velg en feilmargin for hvor nøye kalkuleringen skal være. \n(f.eks resultat^2 har '0.00001' i feilmargin fra", tall)
feilmargin = getfloat()
res = 1.0
htall = tall
ltall = 0

while True:
    res = (htall+ltall)/2
    if res**2 == tall:
        print("roten av ", tall, " = ", res)
        break
    elif res**2 > tall:
        htall = res
    else:
        ltall = res

    if getdiff(res**2, tall) < feilmargin:
        print("kravet om feilmarginen ", feilmargin , " ble nådd.\n", "Roten av ", tall, " er omtrent ", res, "  fordi :\n", res, " * ", res, " = ", res**2)
        break

