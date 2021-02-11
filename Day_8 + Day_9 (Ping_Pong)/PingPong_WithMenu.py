import pygame, random

pygame.init()
clock = pygame.time.Clock()

sw = 800
sh = 600

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("PING PONG")
bg_color = pygame.Color('grey12')
game_font = pygame.font.Font("freesansbold.ttf", 60)

level = 1
opponent_speed = 6

score_time = None

def start_game(OS):
    global score_time
    bg_color = pygame.Color('grey12')

    # LEFT, TOP, WIDTH, HEIGHT
    ball = pygame.Rect(sw // 2 - 15, sh // 2 - 15, 30, 30)
    player = pygame.Rect(sw - 20, sh // 2 - 60, 10, 120)
    opponent = pygame.Rect(10, sh // 2 - 60, 10, 120)

    ball_speed_x = 6 * random.choice((-1, 1))
    ball_speed_y = 6 * random.choice((-1, 1))

    player_speed = 0
    opponent_speed = OS

    player_score = 0
    opponent_score = 0

    score_time = None

    game_font = pygame.font.Font("freesansbold.ttf", 32)

    pong_sound = pygame.mixer.Sound("sound/pong.ogg")
    score_sound = pygame.mixer.Sound("sound/score.ogg")

    def ball_restart():
        global ball_speed_x, ball_speed_y, score_time
        ball.center = (sw // 2, sh // 2)
        current_time = pygame.time.get_ticks()
        if current_time - score_time < 1000:
            ball_speed_x = 0
            ball_speed_y = 0
            number_three = game_font.render("3", False, (200, 200, 200))
            screen.blit(number_three, (sw // 2 - 8, sh // 2 + 50))

        elif current_time - score_time < 2000:
            ball_speed_x = 0
            ball_speed_y = 0
            number_two = game_font.render("2", False, (200, 200, 200))
            screen.blit(number_two, (sw // 2 - 8, sh // 2 + 50))

        elif current_time - score_time < 3000:
            ball_speed_x = 0
            ball_speed_y = 0
            number_one = game_font.render("1", False, (200, 200, 200))
            screen.blit(number_one, (sw // 2 - 8, sh // 2 + 50))
        else:
            ball_speed_x = 6 * random.choice((-1, 1))
            ball_speed_y = 6 * random.choice((-1, 1))
            score_time = None

    running = True
    while running:
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_speed -= 7
                if event.key == pygame.K_DOWN:
                    player_speed += 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player_speed += 7
                if event.key == pygame.K_DOWN:
                    player_speed -= 7

        # PLAYER MOVEMENT
        player.y += player_speed
        if player.top <= 0:
            player.top = 0
        if player.bottom >= sh:
            player.bottom = sh

        # BALL MOVEMENT
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0 or ball.bottom >= sh:
            ball_speed_y *= -1
            pong_sound.play()
        # if ball.left <= 0 or ball.right >= sw:
        #     ball_speed_x *= -1

        # OPPONENT MOVEMENT
        if opponent.bottom < ball.y:
            opponent.bottom += opponent_speed
        if opponent.top > ball.y:
            opponent.top -= opponent_speed

        # COLLISION
        if ball.colliderect(player) or ball.colliderect(opponent):
            ball_speed_x *= -1
            pong_sound.play()

        # SCORE
        if ball.left <= 0:
            player_score += 1
            score_time = pygame.time.get_ticks()
            score_sound.play()
        if ball.right >= sw:
            opponent_score += 1
            score_time = pygame.time.get_ticks()
            score_sound.play()

        if score_time:
            ball_restart()

        player_text = game_font.render(str(player_score), True, (200, 200, 200))
        opponent_text = game_font.render(str(opponent_score), True, (200, 200, 200))

        pygame.draw.rect(screen, (200, 200, 200), player)
        pygame.draw.rect(screen, (200, 200, 200), opponent)
        pygame.draw.ellipse(screen, (200, 200, 200), ball)
        pygame.draw.aaline(screen, (200, 200, 200), (sw // 2, 0), (sw // 2, sh))

        screen.blit(player_text, (sw // 2 + 20, sh // 2 - 16))
        screen.blit(opponent_text, (sw // 2 - 42, sh // 2 - 16))

        clock.tick(60)
        pygame.display.update()

WelcomeScreen = True
while WelcomeScreen:
    screen.fill(bg_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            WelcomeScreen = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_game(opponent_speed)
                WelcomeScreen = False
            if event.key == pygame.K_1:
                level = 1
                opponent_speed = 6
            if event.key == pygame.K_2:
                level = 2
                opponent_speed = 10
            if event.key == pygame.K_3:
                level = 3
                opponent_speed = 15

    if level == 1:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(sw//2-190, sh-410, 350, 70), 2)
    if level == 2:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(sw//2 - 190, sh - 310, 350, 70), 2)
    if level == 3:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(sw//2 - 190, sh- 210, 350, 70), 2)

    Welcome_Message = game_font.render("PING PONG",True, (200, 200, 200))
    screen.blit(Welcome_Message, (sw//2 - 190, 20))

    Select_level = game_font.render("Select Level", True, (200, 200, 200))
    screen.blit(Select_level, (sw//2 - 200, sh - 500))

    Easy = game_font.render("Easy", True, (200, 200, 200))
    screen.blit(Easy, (sw//2-90, sh-400))

    Medium = game_font.render("Medium", True, (200, 200, 200))
    screen.blit(Medium, (sw//2 - 130, sh-300))

    Hard = game_font.render("Hard", True, (200, 200, 200))
    screen.blit(Hard, (sw//2 - 90, sh-200))

    Start = game_font.render("PRESS SPACE TO START", True, (200, 200, 200))
    screen.blit(Start, (sw//2-360, sh-100))

    # pygame.draw.rect(screen, (255,0,0), pygame.Rect(20, 30, 250, 70), 2)
    clock.tick(60)
    pygame.display.update()