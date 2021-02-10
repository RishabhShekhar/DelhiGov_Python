import pygame, random

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("FLAPPY BIRDS")

x = 200
y = 300
jump = False
speed = 1

def draw_circle(x, y):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 30)

pipe1 = [400, 0, 50, random.randint(50, 250)]
pipe2 = [800, 0, 50, random.randint(50, 250)]
# pipe3 = [200, 0, 50, random.randint(50, 250)]

Pipes = []
Pipes.append(pipe1)
Pipes.append(pipe2)
# Pipes.append(pipe3)

def draw_pipe(PIPE):
    # LEFT, TOP, WIDTH, HEIGHT
    # TOP
    pygame.draw.rect(screen, (0, 255, 0),(PIPE[0], PIPE[1], PIPE[2], PIPE[3]))
    # BOTTOM
    pygame.draw.rect(screen, (0, 255, 0),(PIPE[0], PIPE[3]+ 200 ,PIPE[2], PIPE[3]+400))

score = 0
font = pygame.font.Font("freesansbold.ttf", 30)
sCord = (10, 10)

def print_score(scr):
    screen.blit(font.render("SCORE: " + str(scr),True, (255, 255, 255)), sCord)

running =True
while running:
    screen.fill((120, 120, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                jump = False

    draw_circle(x,y)
    if jump:
        y -= 2
    else:
        y += speed

    for i in Pipes:
        draw_pipe(i)
        i[0] -= 4
        if i[0] < 0:
            i[0] = 800
            i[3] = random.randint(50, 250)

    for j in Pipes:
        if j[0] == x:
            if y <= j[3] or y >= 200+j[3]:
                print(score)
                print("GAME OVER")
                running = False
            else:
                score+=1
                print(score)

    clock.tick(30)
    print_score(score)
    pygame.display.update()

