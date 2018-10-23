import sys, pygame
from funcfile import *

pygame.init()
t = 0
x = 1
numWalls = 5
size = width, height = 600, 800
speed = [0, 0]
black = 0, 0, 0
screen = pygame.display.set_mode(size)

car = pygame.image.load("images/car2.png")
carRect = car.get_rect()
carRect = carRect.move(width / 2 - 100, height - 200)

wall = pygame.Surface((50, 50))
wall.fill((255, 255, 255))
wallrects = []
for i in range(numWalls):
    wallrects.append(wall.get_rect())
    wallrects[i].move(randomplace())


score = 0


def printscore():
    global score
    print(score)


def movecar():
    global carRect, speed
    if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
        speed = [-x, 0]
    elif pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
        speed = [x, 0]
    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        speed = [0, 0]
    if carRect.left + speed[0] < 0 or carRect.right + speed[0] > width:
        speed[0] = 0
    carRect = carRect.move(speed)


def moveWall():
    global wallrects, score
    for i in range(len(wallrects)):

        wallrects[i] = wallrects[i].move([0, 1])

        if wallrects[i][1] >= height:
            score += 1
            printscore()
            x, y = randomplace()
            wallrects = wallrects[i].move([x - wallrects[i][0], -wallrects[i][1]])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    movecar()

    moveWall()

    screen.fill(black)
    screen.blit(car, carRect)
    for i in wallrects:
        screen.blit(wall, i)
    pygame.display.flip()
