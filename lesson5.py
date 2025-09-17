import pygame

FPS = 60
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 300
SQUARE_SIDE = 20
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

run = True

pygame.init()

# на ЛКМ рисуется красны квадрат
# rect = (экран, цвет, (Х_Лев_Верх_уг, Y_Лев_Верх_Уг, Ширина, Высота))
sc.fill(WHITE)
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        clock.tick(FPS)
        pygame.display.update()

        mouse_pressed = pygame.mouse.get_pressed()


        # if e.type == pygame.MOUSEBUTTONDOWN:
        #     if e.button == 1:
        #         x, y = e.pos
        #         pygame.draw.rect(sc, RED, (x - SQUARE_SIDE / 2, y - SQUARE_SIDE / 2, SQUARE_SIDE, SQUARE_SIDE))
        #         print(vars(e))
        # print(pygame.mouse.get_pressed(3))

        if mouse_pressed[0]:
            x, y = e.pos
            pygame.draw.rect(sc, RED, (x - SQUARE_SIDE / 2, y - SQUARE_SIDE / 2, SQUARE_SIDE, SQUARE_SIDE))
        elif mouse_pressed[2]:
            x, y = e.pos
            pygame.draw.rect(sc, WHITE, (x - SQUARE_SIDE / 2, y - SQUARE_SIDE / 2, SQUARE_SIDE, SQUARE_SIDE))

pygame.quit()
