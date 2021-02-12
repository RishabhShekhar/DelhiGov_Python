import pygame

pygame.init()

clock = pygame.time.Clock()

sw = 300
sh = 200

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("MOUSE EVENTS")

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # LEFT CLICK
                print("LEFT CLICK")
            if event.button == 2:  # MIDDLE CLICK
                print("MIDDLE CLICK")
            if event.button == 3:  # RIGHT CLICK
                print("RIGHT CLICK")
            if event.button == 4:  # WHEEL UP
                print("WHEEL UP")
            if event.button == 5:  # WHEEL DOWN
                print("WHEEL DOWN")
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # LEFT CLICK
                print("LEFT CLICK RELEASED")
            if event.button == 2:  # MIDDLE CLICK
                print("MIDDLE CLICK RELEASED")

    clock.tick(30)
    pygame.display.update()