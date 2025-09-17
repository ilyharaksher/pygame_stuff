import pygame

FPS = 60
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 300
SQUARE_SIDE = 20
CIRCLE_RADIUS = SQUARE_SIDE / 2
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

run = True
is_fired = False
target = 0
projectile_y = 0
explosion_time = 0
pygame.init()

# rect = (экран, цвет, (Х_Лев_Верх_уг, Y_Лев_Верх_Уг, Ширина, Высота))
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        if e.type == pygame.MOUSEBUTTONDOWN and not is_fired and explosion_time <= 0:
            target = pygame.mouse.get_pos()[1]
            projectile_y = SCREEN_HEIGHT
            is_fired = True

    if is_fired:
        sc.fill(BLACK)
        pygame.draw.circle(sc, RED, (SCREEN_WIDTH / 2, projectile_y), CIRCLE_RADIUS)
        pygame.display.update()
        projectile_y -= 5
        if projectile_y <= target:
            sc.fill(BLACK)
            is_fired = False
            explosion_time = 20
            pygame.draw.rect(sc, WHITE,
                             (SCREEN_WIDTH / 2 - CIRCLE_RADIUS,
                              projectile_y - CIRCLE_RADIUS,
                              SQUARE_SIDE, SQUARE_SIDE)
                             )

    if explosion_time > 0:
        explosion_time -= 1
    else:
        sc.fill(BLACK)

    clock.tick(FPS)
    pygame.display.update()
pygame.quit()
