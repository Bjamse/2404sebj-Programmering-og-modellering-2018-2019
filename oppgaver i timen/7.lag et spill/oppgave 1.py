import random

antall_forsok = 0

print("Hei, hva heter du?")
spillernavn = input()

tall = random.randint(1, 20)
print("Ok {}, jeg tenker på et tall mellom 1 og 20.".format(spillernavn))

for antall_forsok in range(200): # range ble endret slik at spilleren får lov til å prøve flere ganger. i dette tilfellet: 194 ekstra forsøk
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