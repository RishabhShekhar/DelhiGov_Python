# imgs --> https://drive.google.com/drive/folders/1nI20V1rZaBBRcSNyy_KBxK908N-i9bgP?usp=sharing
# sounds --> https://drive.google.com/drive/folders/1k8hZwgDzzcNAy1TFIWC0aZevAU8OL6Lj?usp=sharing

import pygame
import random

pygame.init()
clock = pygame.time.Clock()

screen_width = 640
screen_height = 480
half_screen_height = screen_height // 2
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ROAD RUSH")

light_road = pygame.image.load("imgs/light_road.png")
dark_road = pygame.image.load("imgs/dark_road.png")
car = pygame.image.load("imgs/car.png")
truck = pygame.image.load("imgs/truck.png")
rock = pygame.image.load("imgs/rock.png")
health = pygame.image.load("imgs/health.png")

health_sound = pygame.mixer.Sound("sounds/health.wav")
rock_sound = pygame.mixer.Sound("sounds/rock.wav")

# Gradient
texture_position = 0
ddz = 0.002
dz = 0
z = 0

road_pos = 0  # Our position on road
road_accelaration = 80
texture_position_acceleration = 4
texture_position_threshold = 300
half_texture_position_threshold = texture_position_threshold // 2

car_x = 260
car_y = 360
stone_x = random.randint(250, 350)
stone_y = 240
health_x = random.randint(250, 350)
health_y = 240

state = 0

score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)
sCord = (10, 10)


def print_score(scr):
    screen.blit(game_font.render("SCORE: " + str(scr), True, (0, 0, 0)), sCord)


def isCollided(Cx, Cy, Sx, Sy):
    if Cx + 20 < Sx + 15 < Cx + 110 and Cy + 20 < Sy + 11 < Cy + 110:
        return True
    return False


def draw_lives(l):
    pygame.draw.rect(screen, (200, 0, 0), (600 - 30 * 4, 10, 30 * 5, 15))
    for i in range(l):
        pygame.draw.rect(screen, (0, 200, 0), (600 - 30 * i, 10, 30, 15))

life = 5
game = 1
start_time = pygame.time.get_ticks()
life_time = pygame.time.get_ticks()
health_piece = 0

running = True
while running:
    screen.fill((0, 0, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # pygame.quit()

    keys = pygame.key.get_pressed()

    # if keys[pygame.K_UP]:
    #     print("UP")
    #     road_pos += road_accelaration
    #     if road_pos >= texture_position_threshold:
    #         road_pos = 0
    # if keys[pygame.K_DOWN]:
    #     print("DOWN")
    #     road_pos -= road_accelaration
    #     if road_pos <= 0:
    #         road_pos = texture_position_threshold

    if keys[pygame.K_RIGHT]:
        car_x += 5
        if car_x >= 450:
            car_x -= 5
    if keys[pygame.K_LEFT]:
        car_x -= 5
        if car_x <= 50:
            car_x += 5

    if life > 0:
        road_pos += road_accelaration
        if road_pos >= texture_position_threshold:
            road_pos = 0

    texture_position = road_pos
    dz = 0
    z = 0

    for i in range(half_screen_height - 1, -1, -1):
        if texture_position < half_texture_position_threshold:
            screen.blit(light_road, (0, i + half_screen_height), (0, i, screen_width, 1))
        else:
            screen.blit(dark_road, (0, i + half_screen_height), (0, i, screen_width, 1))

        dz += ddz
        z += dz

        texture_position += texture_position_acceleration + z
        if texture_position >= texture_position_threshold:
            texture_position = 0

    # STONE
    game_time = pygame.time.get_ticks()
    if game_time - start_time > 1000 and state == 0 and health_piece == 0 and game==1:
        state = 1
        stone_x = random.randint(250, 350)
        stone_y = 240
        chng = 0

    if state == 1 and life > 0:
        stone_y += 5
        if stone_x < 280:
            chng = -4
        elif stone_x > 330:
            chng = 4
        stone_x += chng
        screen.blit(rock, (stone_x, stone_y))
        collide = isCollided(car_x, car_y, stone_x, stone_y)
        if collide:
            life -= 1
            state = 0
            start_time = pygame.time.get_ticks()
        if stone_y >= 480:
            state = 0
            score += 1
            start_time = pygame.time.get_ticks()

    game_life_time = pygame.time.get_ticks()
    if game_life_time - life_time > 10000 or health_piece == 1:
        health_piece = 1
        game = 0
        health_y += 5
        if health_x < 280:
            chng = -4
        elif health_x > 330:
            chng = 4
        health_x += chng
        screen.blit(health, (health_x, health_y))
        collided_health = isCollided(car_x, car_y, health_x, health_y)
        if collided_health:
            score += 2
            life += 1
            game = 1
            if life > 5:
                life = 5
            health_piece = 0
            health_x = random.randint(250, 350)
            health_y = 240

        if health_y >= 400:
            game = 1
            health_x = random.randint(250, 350)
            health_y = 240

        life_time = pygame.time.get_ticks()



    screen.blit(car, (car_x, car_y))
    screen.blit(truck, (270, 210))
    print_score(score)
    draw_lives(life)
    clock.tick(30)
    pygame.display.update()
