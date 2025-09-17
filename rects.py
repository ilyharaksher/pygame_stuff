import pygame

WIN_WIDTH = 1000
WIN_HEIGHT = 600
FPS = 60

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 127, 0)
PURPLE = (160, 32, 240)
WHITE = (230, 230, 230)
BLACK = (30, 30, 30)
COLORS = [RED, GREEN, BLUE, PINK, CYAN, YELLOW, ORANGE, PURPLE]

run = True

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()


rect1 = pygame.Rect((0, 0, 30, 30))
rect2 = pygame.Rect((250, 30, 30, 30))

print(rect1.bottomright)  # (30, 30)
print(rect2.bottomright)  # (60, 60)

rect2.move_ip(10, 10)
print(rect2.topleft)  # (40, 40)

# rect1.union_ip(rect2)
# print(rect1.width)  # 70

pygame.init()

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            rect1.union_ip(rect2)
    sc.fill(BLACK)
    pygame.draw.rect(sc, BLUE, rect1)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
