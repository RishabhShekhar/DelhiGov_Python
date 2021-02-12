import pygame
import random

pygame.init()
clock = pygame.time.Clock()

sw = 800
sh = 600

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("TILES")

game_font = pygame.font.Font("freesansbold.ttf", 32)

xy = [random.randint(0,700), random.randint(0,500)]

score = 0


def generate_box(x, y):
    return pygame.Rect(x, y, 100, 100)


def print_score(scr):
    screen.blit(game_font.render("SCORE: " + str(scr), True, (0, 0, 0)), (10, 10))

def isClicked(cxy, cmx, cmy):
    global score
    if cxy[0]< cmx < cxy[0] + 100 and cxy[1] < cmy <cxy[1] + 100:
        score += 1
        print(score)
        return True
    return False

clicked = False
TimeOut = True
start = pygame.time.get_ticks()
while TimeOut:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            TimeOut = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicked = False

    current_time = pygame.time.get_ticks()
    # BOX MOVEMENT
    if current_time - start > 1000:
        start = pygame.time.get_ticks()
        xy = [random.randint(0,700), random.randint(0,500)]

    # DETECTION
    mx, my = pygame.mouse.get_pos()
    if clicked:
        if (current_time-start < 1000) and isClicked(xy, mx, my):
            pygame.draw.rect(screen, (0, 255, 0), box)
            xy = [random.randint(0, 700), random.randint(0, 500)]
            start = pygame.time.get_ticks()

    box = generate_box(xy[0], xy[1])
    pygame.draw.rect(screen, (255, 0, 0), box)

    print_score(score)
    clock.tick(30)
    pygame.display.update()
