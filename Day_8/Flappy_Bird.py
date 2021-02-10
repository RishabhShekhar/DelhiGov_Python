# sound --> https://drive.google.com/drive/folders/1sHMmkV0BDmGrSAn2ig3_bWZbEpL78S5-?usp=sharing
# imgs --> https://drive.google.com/drive/folders/1Rc5iN4nx6UjoeWuK_A8c41U8FuIHwvZB?usp=sharing

import pygame, random

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((288, 512))
pygame.display.set_caption("FLAPPY BIRDS")

background = pygame.image.load("imgs/background.png")
base = pygame.image.load("imgs/base.png")

x = 100
y = 300
jump = False
speed = 0.5
birdimg = pygame.image.load("imgs/bird.png")

pipeupimg = pygame.image.load("imgs/pipe-up.png")
pipedownimg = pygame.image.load("imgs/pipe-down.png")

pipe1 = [300, -170]
pipe2 = [550, -100]
Pipes = []
Pipes.append(pipe1)
Pipes.append(pipe2)

def draw_pipe(PIPE):
    screen.blit(pipeupimg, (PIPE[0], PIPE[1]))
    screen.blit(pipedownimg, (PIPE[0], PIPE[1] + 420))

def draw_bird(x, y):
    screen.blit(birdimg, (x, y))

score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
sCord = (10, 10)

def print_score(scr):
    screen.blit(font.render("SCORE: "+str(scr), True, (255, 255, 255)), sCord)

dieSound = pygame.mixer.Sound("sounds/die.wav")
hitSound = pygame.mixer.Sound("sounds/hit.wav")
swooshSound = pygame.mixer.Sound("sounds/swoosh.wav")
pointSound = pygame.mixer.Sound("sounds/point.wav")
wingSound = pygame.mixer.Sound("sounds/wing.wav")

running = True
while running:
    screen.blit(background,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                wingSound.play()
                jump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                jump = False
                swooshSound.play()

    draw_bird(x, y)
    if jump:
        y -= 1.5
    else:
        y += speed

    for i in Pipes:
        draw_pipe(i)
        i[0] -= 2
        if i[0] <= 0:
            i[0] = 500
            i[1] = random.randint(-250, -100)

    for i in Pipes:
        if i[0] == x:
            if y <= i[1] + 320 or y >= i[1]+420:
                hitSound.play()
                dieSound.play()
                print("GAME OVER")
                running = False
            else:
                pointSound.play()
                score += 1
                print(score)

    print_score(score)
    screen.blit(base, (0,410))
    clock.tick(50)
    pygame.display.update()