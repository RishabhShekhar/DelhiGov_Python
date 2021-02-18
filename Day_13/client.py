import pygame

pygame.init()

sw = 500
sh = 500
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.val = 3

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.y -= self.val
        if keys[pygame.K_DOWN]:
            self.y += self.val
        if keys[pygame.K_LEFT]:
            self.x -= self.val
        if keys[pygame.K_RIGHT]:
            self.x += self.val

        self.update()
        
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def drawWindow(screen, player):
    screen.fill((207, 185, 151))
    player.draw(screen)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    p = Player(50, 50, 100, 100, (0, 255, 0))
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        p.move()
        drawWindow(screen, p)

main()