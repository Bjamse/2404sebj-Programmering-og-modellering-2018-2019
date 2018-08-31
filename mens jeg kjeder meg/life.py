import random, sys, pygame

def getinput(text):
    while True:
        try:
            x = int(input(text))
            break
        except:
            print("try again")
    return x

def density(d):
    if random.randint(0, d) == 0:
        return 1
    return 0

def makeworld(widht, height, d=5):
    return [[density(d) for x in range(widht)] for y in range(height)]

def diplayTheWorld(matrix):
    return 0

def testcelle(matrix, y, x):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if matrix[((i+y)+len(matrix)) % len(matrix)][((j+x)+len(matrix[i])) % len(matrix[i])] == 1:
                sum += 1
    sum -= matrix[y][x]
    return sum

pygame.init()
w, h, d = getinput("How many pixels wide should it be? (1-100) :  "), getinput("How many pixels heigh should it be?  (1-100):  "), \
          getinput("How dense should it be?  (recomended: 6):  ")
World = makeworld(w, h, d)
NewWorld = makeworld(w, h)
rects = makeworld(w, h)
size = width, height = w*10, h*10
screen = pygame.display.set_mode(size)
dot = pygame.image.load("dot.png")
pixel = dot.get_rect()
diplayTheWorld(World)

for i in range(len(NewWorld)):
    for j in range(len(NewWorld[i])):
        NewWorld[i][j] = World[i][j]


for i in range(len(rects)):
    for j in range(len(rects[i])):
        rects[i][j] = pixel.copy()
        rects[i][j] = rects[i][j].move([j*10, i*10])

t = 0
while True:
    t+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for i in range(len(World)):
        for j in range(len(World[i])):
            neighbours = testcelle(World, i, j)
            if neighbours == 3 and World[i][j] == 0:
                NewWorld[i][j] = 1
                #print("i shall live")
            elif neighbours <= 1 and World[i][j] == 1:
                NewWorld[i][j] = 0
                #print("i shall die")
            elif neighbours >= 4 and World[i][j] == 1:
                NewWorld[i][j] = 0
                #print("i shall die")
            else:
                NewWorld[i][j] = World[i][j]
                #print("i won't change")

    for i in range(len(NewWorld)):
        for j in range(len(NewWorld[i])):
            World[i][j] = NewWorld[i][j]

    diplayTheWorld(World)
    screen.fill((0, 0, 0))

    for i in range(len(rects)):
        for j in range(len(rects[i])):
            if World[i][j] == 1:
                screen.blit(dot, rects[i][j])

    pygame.display.flip()
    pygame.time.delay(40)
