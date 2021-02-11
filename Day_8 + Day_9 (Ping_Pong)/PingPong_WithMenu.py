import pygame

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

WelcomeScreen = True
while WelcomeScreen:
    screen.fill(bg_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            WelcomeScreen = False
        if event.type == pygame.KEYDOWN:
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