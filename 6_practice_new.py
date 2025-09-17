# круг, треугольник, квадрат, случайных разных цветов и расположений появляются на поверхности, после столкновения со стеной

import random
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

surf = pygame.Surface((180, 135))

surf.fill(WHITE)


# Color carousel
def set_new_colors(triangle_current=0, circle_current=0, square_current=0):
    triangle_new = random.choice(COLORS)
    circle_new = random.choice(COLORS)
    square_new = random.choice(COLORS)
    while triangle_current == triangle_new:
        triangle_new = random.choice(COLORS)
    while triangle_new == circle_new or circle_new == circle_current:
        circle_new = random.choice(COLORS)
    while square_new == circle_new or square_new == triangle_new or square_new == square_current:
        square_new = random.choice(COLORS)
    return triangle_new, circle_new, square_new


# Setting current colors
triangle_current_color, circle_current_color, square_current_color = set_new_colors()

# Triangle
triangle_surf = pygame.Surface((60, 60))
triangle_surf.fill(WHITE)

pygame.draw.polygon(triangle_surf, triangle_current_color, [(30, 0), (60, 60), (0, 60)])
triangle_x, triangle_y = random.randint(0, 120), random.randint(0, 75)

surf.blit(triangle_surf, (triangle_x, triangle_y))

# Circle
circle_x, circle_y = random.randint(30, 150), random.randint(30, 105)
pygame.draw.circle(surf, circle_current_color, (circle_x, circle_y), 30)

# Square
square_x, square_y = random.randint(0, 120), random.randint(0, 75)
pygame.draw.rect(surf, square_current_color, (square_x, square_y, 60, 60))

dx = 4
dy = 3
x = 0
y = 0

sc.fill(BLACK)
sc.blit(surf, (x, y))

pygame.init()

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    pygame.display.update()

    x += dx
    y += dy

    if x > WIN_WIDTH - 180 or x < 0:
        triangle_current_color, circle_current_color, square_current_color = set_new_colors(triangle_current_color,
                                                                                            circle_current_color,
                                                                                            square_current_color)

        triangle_x, triangle_y = random.randint(0, 120), random.randint(0, 75)
        circle_x, circle_y = random.randint(30, 150), random.randint(30, 105)
        square_x, square_y = random.randint(0, 120), random.randint(0, 75)

        surf.fill(WHITE)

        pygame.draw.polygon(triangle_surf, triangle_current_color, [(30, 0), (60, 60), (0, 60)])
        surf.blit(triangle_surf, (triangle_x, triangle_y))

        pygame.draw.circle(surf, circle_current_color, (circle_x, circle_y), 30)

        pygame.draw.rect(surf, square_current_color, (square_x, square_y, 60, 60))

        dx = -dx

    if y > WIN_HEIGHT - 135 or y < 0:
        triangle_current_color, circle_current_color, square_current_color = set_new_colors(triangle_current_color,
                                                                                            circle_current_color,
                                                                                            square_current_color)
        triangle_x, triangle_y = random.randint(0, 120), random.randint(0, 75)
        circle_x, circle_y = random.randint(30, 150), random.randint(30, 105)
        square_x, square_y = random.randint(0, 120), random.randint(0, 75)

        surf.fill(WHITE)

        pygame.draw.polygon(triangle_surf, triangle_current_color, [(30, 0), (60, 60), (0, 60)])
        surf.blit(triangle_surf, (triangle_x, triangle_y))

        pygame.draw.circle(surf, circle_current_color, (circle_x, circle_y), 30)

        pygame.draw.rect(surf, square_current_color, (square_x, square_y, 60, 60))
        dy = -dy

    sc.fill(BLACK)
    sc.blit(surf, (x, y))

    clock.tick(60)

pygame.quit()
