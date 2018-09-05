import random # Her importerer vi en modul med funksjoner som vi skal bruke i programmet vårt.

antall_forsok = 0 # Dette er en variabel hvor vi lagrer antall ganger spilleren har gjettet.

print("Hei, hva heter du?")
spillernavn = input() # Vi henter spillerens navn, og lagrer det i en variabel.

tall = random.randint(1, 20) # Nå plukker vi et tilfeldig tall mellom 1 og 20.
print("Ok {}, jeg tenker på et tall mellom 1 og 20.".format(spillernavn))

for antall_forsok in range(6): # Vi gir spilleren 6 forsøk på å gjette riktig.
    print("Gjett hvilket tall det er:")
    gjettet = input() # Venter på at spilleren skal taste inn et tall.
    gjettet = int(gjettet) # Gjør om til heltall (hva skjer om spilleren taster inn noe annet?).

    if gjettet < tall: # Gjettet spilleren lavere enn tallet vårt?
        print("Du gjettet {}, men det er for lavt {}.".format(gjettet, spillernavn))
    elif gjettet > tall: # Gjettet spilleren høyere enn tallet vårt?
        print("Du gjettet {}, men det er for høyt {}.".format(gjettet, spillernavn))
    else: # Ikke for lavt og ikke for høyt, da må det være riktig!
        break # Hopper ut av loopen.

# Her er for-loopen ferdig, legg merke til innrykket på linjene nedenfor.

if gjettet == tall: # Sammenlikner det spilleren gjettet med det vi tenkte på. Er tallene like?
    print("Wow {}, du gjettet riktig på {} forsøk.".format(spillernavn, antall_forsok))
else: # Dersom tallen ikke var like, så må de være ulike.
    print("Dette var litt for vanskelig. Jeg tenkte på tallet {}.".format(tall))