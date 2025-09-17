import pygame

FPS = 60
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 300
WHITE = (255, 255, 255)
RED = (255, 0, 0)

sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

x = SCREEN_WIDTH // 2
y = SCREEN_HEIGHT // 2
r = 50

step = 0

run = True

pygame.init()

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    clock.tick(FPS)

    sc.fill(WHITE)
    pygame.draw.circle(sc, RED, (x, y), r)
    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] and keys[pygame.K_a]:
        x = x
    elif keys[pygame.K_d]:
        x += 3
    elif keys[pygame.K_a]:
        x -= 3
    elif x < SCREEN_WIDTH // 2:
        x += 3
    elif x > SCREEN_WIDTH // 2:
        x -= 3


pygame.quit()
