# Space Invader
import pygame, random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("SPACE INVADER")
icon = pygame.image.load("imgs/ufo.png")
background = pygame.image.load("imgs/Background.png")
pygame.display.set_icon(icon)
# Player
playerImg = pygame.image.load("imgs/space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("imgs/alien.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 2
enemyY_change = 40

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

running = True
while running:
    screen.fill((53, 81, 92))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    enemyX += enemyX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if enemyX <= 0:
        enemyX_change = 2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -2
        enemyY += enemyY_change

    enemy(enemyX, enemyY)
    player(playerX, playerY)

    pygame.display.update()