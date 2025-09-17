import pygame
# СДЕЛАТЬ ЗАЖАТИЕ МЫШИ
# ФПС
FPS = 60

# размеры
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 300
SQUARE_SIDE = 20
CIRCLE_RADIUS = SQUARE_SIDE / 2

# цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

run = True

# фон
background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT / 2))
bg_x = 0
bg_y = 75

# Главни героу
hero = pygame.Surface((50, 50))
h_x = 100
h_y = 100

background.fill(BLUE)
hero.fill(RED)
background.blit(hero, (h_x, h_y))
sc.blit(background, (bg_x, bg_y))
pygame.display.update()

pygame.init()

x = 0
y = 0
# rect = (экран, цвет, (Х_Лев_Верх_уг, Y_Лев_Верх_Уг, Ширина, Высота))
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        # if e.type == pygame.KEYDOWN:
        #     if e.key == pygame.K_w:
        #         y -= 2
        #     if e.key == pygame.K_s:
        #         y += 2
        #     if e.key == pygame.K_a:
        #         x -= 2
        #     if e.key == pygame.K_d:
        #         x += 2
        #     print((x, y))

    mouse_button_pressed = pygame.mouse.get_pressed()

    if mouse_button_pressed[0]:
        bg_y = pygame.mouse.get_pos()[1]
        sc.fill(BLACK)
        sc.blit(background, (bg_x, bg_y))
        pygame.display.update()

    if mouse_button_pressed[2]:
        h_y = pygame.mouse.get_pos()[1] - bg_y
        sc.fill(BLACK)
        background.fill(BLUE)
        background.blit(hero, (h_x, h_y))
        sc.blit(background, (bg_x, bg_y))
        pygame.display.update()

    # sc.fill(BLACK)
    # pygame.draw.rect(sc, WHITE, (x, y, 20, 20))



    clock.tick(FPS)
    # pygame.display.update()
pygame.quit()
