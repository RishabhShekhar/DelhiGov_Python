import pygame
import random

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont("Arial", 30)

snake_pos =[[300, 300], [320, 300], [340, 300], [360, 300]]

apple_pos = [260, 300]

score = 0

timer = 0

step = 20
up = (0, -step)
down = (0, step)
left = (-step, 0)
right = (step, 0)

direction = left

game_over = False
running = True
while running:
    screen.fill((20, 100, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP")
                direction = up
            if event.key == pygame.K_DOWN:
                print("DOWN")
                direction = down
            if event.key == pygame.K_LEFT:
                print("LEFT")
                direction = left
            if event.key == pygame.K_RIGHT:
                print("RIGHT")
                direction = right
    timer += 1

    if snake_pos[0] == apple_pos:
        x = (random.randint(100, 700)//20)*20
        y = (random.randint(100,500)//20)*20
        apple_pos = [x, y]
        score += 1
        snake_pos.append(snake_pos[-1])

    if 800 <= snake_pos[0][0] or snake_pos[0][0] <= 0:
        game_over = True
    if 600 <= snake_pos[0][1] or snake_pos[0][1] <= 0:
        game_over = True

    for i in range(1,len(snake_pos)):
        if snake_pos[i] == snake_pos[0]:
            game_over = True

    if game_over:
        print(score)
        running = False

    if timer == 5:
        snake_pos = [[snake_pos[0][0]+direction[0], snake_pos[0][1]+direction[1]]] + snake_pos[:-1]
        timer = 0

    for x,y in snake_pos:
        pygame.draw.circle(screen, (0, 0, 255), (x, y), 10)

    pygame.draw.circle(screen, (255, 0, 0), apple_pos, 10)

    text = font.render(("SCORE: "+ str(score)), True, (255, 255, 255))

    screen.blit(text, (0,0))

    clock.tick(30)
    pygame.display.update()