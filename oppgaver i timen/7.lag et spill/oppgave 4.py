"""


dette er ikke fint koda...
koden skal bli oppdatert i fremtiden men intil videre så fungerer den... :D


"""



import random

def gjett(riktig, fors0k):
    for antall_forsok in range(fors0k):
        print("Gjett hvilket tall det er:")
        gjettet = input()
        gjettet = int(gjettet)

        if gjettet < tall:
            print("Du gjettet {}, men det er for lavt {}.".format(gjettet, spillernavn))
        elif gjettet > tall:
            print("Du gjettet {}, men det er for høyt {}.".format(gjettet, spillernavn))
        else:
            break
    return gjettet, antall_forsok


antall_forsok = 0

print("Hei, hva heter du?")
spillernavn = input()

tall = random.randint(1, 100)
print("Ok {}, jeg tenker på et tall mellom 1 og 300.".format(spillernavn))

fors0k = input("Skriv inn et antall for hvor mange gjettninger du skal få : ")
fors0k = int(fors0k)

res = gjettet, antall_forsok = gjett(tall, fors0k)

if gjettet == tall:
    print("Wow {}, du gjettet riktig på {} forsøk.".format(spillernavn, antall_forsok))
else:
    print("Dette var litt for vanskelig. Jeg tenkte på tallet {}.".format(tall))
