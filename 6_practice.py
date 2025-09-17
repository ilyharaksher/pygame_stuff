import random
import pygame

WIN_WIDTH = 1000
WIN_HEIGHT = 600
FPS = 60

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, GREEN, BLUE, WHITE]

run = True

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

surf = pygame.Surface((180, 135))
current_color = WHITE
surf.fill(current_color)

sc.blit(surf, (0, 0))

new_color = random.choice(COLORS)

dx = 4
dy = 3
x = 0
y = 0
pygame.init()

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    pygame.display.update()

    x += dx
    y += dy

    if x > WIN_WIDTH - 180 or x < 0:
        while new_color == current_color:
            new_color = random.choice(COLORS)
        current_color = new_color
        surf.fill(new_color)
        dx = -dx
    if y > WIN_HEIGHT - 135 or y < 0:
        while new_color == current_color:
            new_color = random.choice(COLORS)
        current_color = new_color
        surf.fill(new_color)
        dy = -dy

    sc.fill(BLACK)
    sc.blit(surf, (x, y))

    # print(surf.get_offset())

    clock.tick(60)

pygame.quit()
