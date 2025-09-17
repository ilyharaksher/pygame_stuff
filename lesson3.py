import pygame

run = True
FPS = 500
WIN_WIDTH = 200
WIN_HEIGHT = 100
SQUARE_SIDE = 60
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
step = 1

clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# здесь будут рисоваться фигуры

x = 0
y = WIN_HEIGHT / 2 - SQUARE_SIDE / 2

pygame.init()

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            # print(pygame.event.event_name(e.type))
            run = False

    sc.fill(WHITE)
    pygame.draw.rect(sc, ORANGE, (x, y, SQUARE_SIDE, SQUARE_SIDE))

    if x == WIN_WIDTH - SQUARE_SIDE:
        step = -1
    elif x == 0:
        step = 1

    x += step

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
