# sound --> https://drive.google.com/drive/folders/1sHMmkV0BDmGrSAn2ig3_bWZbEpL78S5-?usp=sharing
# imgs --> https://drive.google.com/drive/folders/1Rc5iN4nx6UjoeWuK_A8c41U8FuIHwvZB?usp=sharing

import pygame, random

pygame.init()

screen = pygame.display.set_mode((288, 512))
pygame.display.set_caption("FLAPPY BIRDS")

background = pygame.image.load("imgs/background.png")
base = pygame.image.load("imgs/base.png")

x = 100
y = 300
jump = False
speed = 0.5
birdimg = pygame.image.load("imgs/bird.png")

def draw_bird(x, y):
    screen.blit(birdimg, (x, y))

running = True
while running:
    screen.blit(background,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_bird(x, y)
    screen.blit(base, (0,410))
    pygame.display.update()