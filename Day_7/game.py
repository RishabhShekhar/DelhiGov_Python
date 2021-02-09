# Space Invader
import pygame, random, math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("SPACE INVADER")
icon = pygame.image.load("imgs/ufo.png")
background = pygame.image.load("imgs/Background.png")
pygame.display.set_icon(icon)

mixer.music.load("sound/background.wav")
mixer.music.play(-1)

# Player
playerImg = pygame.image.load("imgs/space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6


for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("imgs/alien.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load("imgs/bullet.png")
bulletX = 0
bulletY = 460
bulletY_change = 7
bullet_state = "ready"

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
over_font = pygame.font.SysFont("Arial",48)

textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255,255))
    screen.blit(score, (x,y))

def game_over():
    over_text = font.render("GAME OVER", True, (255, 255,255))
    screen.blit(over_text, (250, 230))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2))+(math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    return False


running = True
while running:
    screen.fill((53, 81, 92))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_sound = mixer.Sound("sound/laser.wav")
                bullet_sound.play()
                bulletX = playerX
                fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    for i in range(num_of_enemies):
        if enemyY[i] > 420:
            for i in range(num_of_enemies):
                enemyX[i] = 2000
            game_over()
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound("sound/explosion.wav")
            collision_sound.play()
            bulletY = 460
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY <= 0:
        bulletY = 460
        bullet_state = "ready"

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()
