import sys
import pygame
import math

while True:
    userDefinedHeight = 50
    break

    try:
        userDefinedHeight = int(input("hvor høyt skal vi fylle med veske (0-80 cm): "))
        if 0 <= userDefinedHeight <= 80:
            break
        else:
            userDefinedHeight = int("ø") # bare for å kræsje testen slik at vi får
    except:
        print("prøv igjen")




pygame.init()

# Farge-definisjoner, RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (211,211,211)
SEA_BLUE = (0,105,148)

# Dimensjonene til programvinduet
SIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SIZE)
CENTER_HORIZ = WIDTH // 2
CENTER_VERT = HEIGHT // 2

# Hvor mange bilder i sekundet (FPS) skal vi tegne?
FPS = 10
timer = pygame.time.Clock()
timer_txt = pygame.font.SysFont('Consolas', 30)



FmCmP = (500/8) #forhold mellom pixler og cm

tankHoyde = 80/10*FmCmP
tankBredde = 5*FmCmP

hoydepaaveske = userDefinedHeight/10*FmCmP

hoydekloss = FmCmP * 2
breddekloss =FmCmP * 2

volumkloss = breddekloss* breddekloss * hoydekloss

addTerning = False

tank_params = {
    "left": CENTER_HORIZ - tankBredde/2,  # Trekker fra halvparten av bredden
    "top": CENTER_VERT - tankHoyde/2,   # Trekker fra halvparten av høyden
    "width": tankBredde,               # Tankens høyde
    "height": tankHoyde,              # Tankens bredde
    "level": 10,                # Nivået vi starter med
    "fill_color": SEA_BLUE,     # Farge på innholdet i tanken
    "outline_color": WHITE,     # Farge på omrisset av tanken
    "border_width": 3           # Bredde på omrisset av tanken
}

# Endring av nivå mellom hvert bilde som vises (FPS)
level_change = 2


print("dersom tanken er kvadratisk er volumet på vannet = {} liter \ndersom tanken er en sylynder er volumet på "
      "vannet = {} liter".format((hoydepaaveske/FmCmP)*(tankBredde/FmCmP)**2, ((tankBredde/FmCmP)/2)**2*math.pi*(
        hoydepaaveske/FmCmP)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if pygame.key.get_pressed()[pygame.K_RETURN] != 0 and addTerning == False:
        addTerning = True
        level_change = 5
        tank_params["level"] = min(tank_params["height"] ,hoydepaaveske+20*FmCmP)
    # Bakgrunnsfargen
    screen.fill(BLACK)

    # Tegner inn tanknivået
    pygame.draw.rect(screen, SEA_BLUE,
                     pygame.Rect(tank_params["left"],
                                 tank_params["top"] + (tank_params["height"] - tank_params["level"]),
                                 tank_params["width"],
                                 tank_params["level"]))
    # Tegner omrisset av tanken
    pygame.draw.rect(screen, WHITE,
                     pygame.Rect(tank_params["left"],
                                 tank_params["top"],
                                 tank_params["width"],
                                 tank_params["height"]),
                     tank_params["border_width"])

    # Sjekk om vi har nådd topp eller bunn, og endre fortegn på level_change
    if tank_params["level"] > hoydepaaveske:
        level_change *= 0

    # Endrer nivået i tanken
    tank_params["level"] += level_change

    # Tegner inn "vannstrålen" inn i eller ut av tanken
    if level_change > 0: # tanken fylles
        pygame.draw.line(screen, SEA_BLUE,
                    (CENTER_HORIZ,0),
                    (CENTER_HORIZ, tank_params["top"] + tank_params["height"] - tank_params["border_width"]), 4)

    if addTerning:
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(CENTER_HORIZ-(breddekloss/2), CENTER_VERT + tankHoyde/2 - hoydekloss, hoydekloss, breddekloss))

    timer_string = "Medgått tid: {} sekunder".format(round(pygame.time.get_ticks() / 1000, 1))
    screen.blit(timer_txt.render(timer_string, True, LIGHT_GRAY), (CENTER_HORIZ // 2, 10))
    pygame.display.flip()
    timer.tick(FPS)