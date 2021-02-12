import pygame
import random

pygame.init()
clock = pygame.time.Clock()

sw = 800
sh = 600

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("TILES")

font_32 = pygame.font.Font("freesansbold.ttf", 32)
font_64 = pygame.font.Font("freesansbold.ttf", 64)

score = 0

def arcade_mode():
    life = 10

    game_font = pygame.font.Font("freesansbold.ttf", 32)

    xy = [random.randint(0, 700), random.randint(0, 500)]

    def generate_box(x, y):
        return pygame.Rect(x, y, 100, 100)

    def print_score(scr):
        screen.blit(game_font.render("Score:"+ str(scr), True, (0, 0, 0)), (10, 10))

    def isClicked(xy, mx, my):
        if xy[0] < mx < xy[0]+100 and xy[1]< my< xy[1]+100:
            return True
        return False

    def draw_lifes(l):
        lifes = l
        for i in range(lifes):
            pygame.draw.circle(screen, (100, 100, 0), (760 - 30*i, 20), 15)

    clicked = False
    ArcadeRun = True
    start = pygame.time.get_ticks()
    while ArcadeRun:
        screen.fill((200, 200, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ArcadeRun = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = False

        box = generate_box(xy[0],xy[1])
        pygame.draw.rect(screen, (255, 0, 0), box)

        mx, my = pygame.mouse.get_pos()
        current_time = pygame.time.get_ticks()
        if current_time - start > 1000 and not(clicked):
            life -=1
            xy = [random.randint(0, 700), random.randint(0, 500)]
            start = pygame.time.get_ticks()

        if clicked:
            if (current_time-start < 1000) and isClicked(xy, mx, my):
                global score
                score += 1
                clicked = False
                xy = [random.randint(0, 700), random.randint(0, 500)]
                start = pygame.time.get_ticks()
            elif (current_time-start < 1000) and not isClicked(xy, mx, my):
                clicked = False
                life -= 1
                xy = [random.randint(0, 700), random.randint(0, 500)]
                start = pygame.time.get_ticks()
        if life <= 0:
            screen.fill((200, 200, 200))
            msg = pygame.font.Font("freesansbold.ttf", 64)
            screen.blit(msg.render("GAME OVER!!", True, (0, 0, 0)), (180, 200))
            screen.blit(game_font.render("Final Score:"+str(score), True, (0, 0, 0)), (280, 300))

        print_score(score)
        draw_lifes(life)
        clock.tick(60)
        pygame.display.update()

clicked = False
mode = 0
state = 0
MainRun = True
while MainRun:
    screen.fill((200, 200, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MainRun = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicked = False

    mx, my = pygame.mouse.get_pos()

    if clicked and state == 0:
        if 205 < mx < 420 and sh-360 < my < sh-323: # Time-Out
            mode = 1
        elif 285 < mx < 420 and sh-320 < my < sh-283: # Arcade
            mode = 2
        elif sw//2-95 < mx < sw//2+95 and sh-105<my<sh-30: # Start
            state = 1

    if mode == 1:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(285, sh-365, 200, 37), 2)
    elif mode == 2:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(285, sh-325, 200, 37),2)
    if state == 1:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(sw//2-95, sh-107, 230, 70), 2)
        if mode == 1:
            MainRun = False
            # time_out_mode()
        elif mode == 2:
            MainRun = False
            arcade_mode()

    Welcome_Message = font_64.render("TILES", True, (0, 0, 200))
    screen.blit(Welcome_Message, (sw//2 - 110, 20))

    Select_Mode = font_32.render("SELECT MODE: ", True, (0, 0, 200))
    screen.blit(Select_Mode, (10, sh-400))

    time_out = font_32.render("TIME-OUT", True, (0, 0, 200))
    screen.blit(time_out, (290, sh-360))

    arcade = font_32.render("ARCADE", True, (0, 0, 200))
    screen.blit(arcade, (290, sh-320))

    Start = font_64.render("START", True, (0, 0, 200))
    screen.blit(Start, (sw//2-80, sh-100))

    pygame.display.update()

