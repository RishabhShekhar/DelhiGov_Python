# sound --> https://drive.google.com/drive/folders/1ByLsTIWsNRgZnXdfPDl58ea2bbv4GCZv?usp=sharing

import pygame

pygame.init()
clock = pygame.time.Clock()

sw = 800
sh = 600
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("PING PONG")

bg_color = pygame.Color('grey12')

# LEFT, TOP, WIDTH, HEIGHT
ball = pygame.Rect(sw // 2 - 15, sh // 2 - 15, 30, 30)
player = pygame.Rect(sw - 20, sh // 2 - 60, 10, 120)
opponent = pygame.Rect(10, sh // 2 - 60, 10, 120)

ball_speed_x = 6
ball_speed_y = 6

player_speed = 0
opponent_speed = 7

player_score = 0
opponent_score = 0

running = True
while running:
    screen.fill(bg_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, (200, 200, 200), player)
    pygame.draw.rect(screen, (200, 200, 200), opponent)
    pygame.draw.ellipse(screen, (200, 200, 200), ball)

    clock.tick(60)
    pygame.display.update()
