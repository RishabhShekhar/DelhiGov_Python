import pygame

pygame.init()

sw = 800
sh = 600
screen = pygame.display.set_mode((sw, sh))

def bluescreen(clock):
    bluerunning = True
    while bluerunning:
        screen.fill((0, 0, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bluerunning = False

    pygame.display.update()

running = True
while running:
    screen.fill((255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bluescreen()
                running = False

    pygame.display.update()