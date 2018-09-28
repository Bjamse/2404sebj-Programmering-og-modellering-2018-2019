import random

antall_forsok = 0

print("Hei, hva heter du?")
spillernavn = input()

tall = random.randint(1, 300)
print("Ok {}, jeg tenker på et tall mellom 1 og 300.".format(spillernavn))

fors0k = input("Skriv inn et antall for hvor mange gjettninger du skal få : ")  # spillern kan skrive inn et eget anntall forsøk

fors0k = int(fors0k)  # konverterer inputen til spilleren som et tall


for antall_forsok in range(fors0k):  # inputen fra spilleren blir satt inn som i antall forsøk mulige å gjøre
    print("Gjett hvilket tall det er:")
    gjettet = input()
    gjettet = int(gjettet)

    if gjettet < tall:
        print("Du gjettet {}, men det er for lavt {}.".format(gjettet, spillernavn))
    elif gjettet > tall:
        print("Du gjettet {}, men det er for høyt {}.".format(gjettet, spillernavn))
    else:
        break



if gjettet == tall:
    print("Wow {}, du gjettet riktig på {} forsøk.".format(spillernavn, antall_forsok))
else:
    print("Dette var litt for vanskelig. Jeg tenkte på tallet {}.".format(tall))
