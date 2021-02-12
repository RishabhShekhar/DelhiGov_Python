import pygame
import random

pygame.init()

sw = 800
sh = 600

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("TILES")

font_32 = pygame.font.Font("freesansbold.ttf", 32)
font_64 = pygame.font.Font("freesansbold.ttf", 64)

score = 0

MainRun = True
while MainRun:
    screen.fill((200, 200, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MainRun = False

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

