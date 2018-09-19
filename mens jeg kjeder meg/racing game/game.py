import sys, pygame
pygame.init()
t = 0
x = 1
size = width, height = 600, 800
speed = [0, 0]
black = 0, 0, 0
screen = pygame.display.set_mode(size)

ball = pygame.image.load("car.png")
ballrect = ball.get_rect()
ballrect = ballrect.move(width/2 - 100, height - 200)

def movecar():
    global ballrect, speed
    if (pygame.key.get_pressed()[pygame.K_LEFT] != 0):
        speed = [-x, 0]
    elif (pygame.key.get_pressed()[pygame.K_RIGHT] != 0):
        speed = [x, 0]
    elif (pygame.key.get_pressed()[pygame.K_DOWN]):
        speed = [0, 0]
    if (ballrect.left + speed[0] < -55 or ballrect.right + speed[0] > width + 55 ):
        speed[0] = 0
    ballrect = ballrect.move(speed)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    movecar()

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()