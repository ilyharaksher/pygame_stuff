# здесь подключаются модули
import pygame
import random

# здесь определяются константы, классы и функции
FPS = 1
run = True
captions = ['сердце', "мышь", "кость", "слабость", "конфета", "храбрый"]

# здесь происходит инициация, создание объектов
pygame.init()
pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# если надо до цикла отобразить какие-то объекты, обновляем экран
pygame.display.update()

# главный цикл
while run:

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    # --------
    # ЛОГИКА (изменение объектов)
    # --------

    # обновление экрана
    pygame.display.set_caption(random.choice(captions))

pygame.quit()
