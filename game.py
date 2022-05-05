import pygame
import client
import server

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, col, name):
        super().__init__(all)
        self.name = name
        self.image = pygame.Surface([10, 10])
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = 0
        self.dy = 0

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        
    def set_pos(self):
        client.set_positions("localhost:8000", self.name, self.rect.x, self.rect.y)

    def right(self, dx):
        self.dx += dx

    def up(self, dy):
        self.dy += dy

pygame.init()

screen = pygame.display.set_mode((400, 400))

all = pygame.sprite.Group()

p1 = Player(0, 0, (255, 0, 0), "player1")
p2 = Player(390, 390, (0, 0, 255), "player2")

clock = pygame.time.Clock()

done = False
counter = 0

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                p1.up(-1)
            elif event.key == pygame.K_DOWN:
                p1.up(1)
            elif event.key == pygame.K_RIGHT:
                p1.right(1)
            elif event.key == pygame.K_LEFT:
                p1.right(-1)
            elif event.key == pygame.K_w:
                p2.up(-1)
            elif event.key == pygame.K_s:
                p2.up(1)
            elif event.key == pygame.K_d:
                p2.right(1)
            elif event.key == pygame.K_a:
                p2.right(-1)
            elif event.key == pygame.K_SPACE:
                p1.set_pos()
                p2.set_pos()
            elif event.key == pygame.K_RETURN:
                print(p1.rect.topleft)
                print(f'Player1: {client.get_positions("localhost:8000", "player1").split(":")[1]}')
                print(p2.rect.topleft)
                print(f'Player2: {client.get_positions("localhost:8000", "player2").split(":")[1]}')

    all.update()
    screen.fill((0, 0, 0))
    all.draw(screen)
    pygame.display.update()

pygame.quit()