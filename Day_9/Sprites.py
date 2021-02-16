import pygame
import random

clock = pygame.time.Clock()

blackC = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()


pygame.init()

sw = 700
sh = 400

screen = pygame.display.set_mode((sw, sh))
black_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(random.randint(10, 30)):
    black = Block(blackC, 30, 30)

    black.rect.x = random.randrange(sw)
    black.rect.y = random.randrange(sh)

    black_list.add(black)
    all_sprite_list.add(black)

player = Block(red, 30, 30)
all_sprite_list.add(player)

score = 0

running = True
while running:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pos = pygame.mouse.get_pos()
    # print(pos)

    black_hit_list = pygame.sprite.spritecollide(player, black_list, True)

    for black in black_hit_list:
        score += 1
        print(score)

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # black_list.draw(screen)
    all_sprite_list.draw(screen)

    clock.tick(20)
    pygame.display.update()
