import pygame
from pygame.locals import *
from game_object import GameObject 
from worm import Worm
from food import Food
from wall import Wall

def create_background(screen, width, height):
        colors = [(255, 255, 255), (212, 212, 212)]
        tile_width = 20
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // tile_width
                        col = x // tile_width
                        pygame.draw.rect(screen, colors[(row + col) % 2],pygame.Rect(x, y, tile_width, tile_width))
                        x += tile_width
                y += tile_width


done = False
pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, (0, 0, 0))

worm = Worm(20)
food = Food(20)
wall = Wall(20)

# Переменные для счета и уровня
score = 0
level = 1

# Шрифт для отображения счета и уровня
score_font = pygame.font.SysFont("Verdana", 20)

while not done:
    # Event filtering
    filtered_events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else:
            filtered_events.append(event)

    worm.process_input(filtered_events)
    worm.move()

    # Проверка столкновений с едой
    pos = food.can_eat(worm.points[0], worm.tile_width)
    if pos is not None:
        worm.increase(pos)
        score += 10  # Увеличиваем счет на 10 за каждую съеденную еду
        if len(worm.points) % 3 == 0:
            wall.next_level()
            level += 1

    # Проверка столкновений с стенами
    if wall.check_collision(worm.points[0]):
        screen.fill((255, 0, 0))
        screen.blit(game_over, (30,250))
        pygame.display.update()
        done = True  # Завершаем игру, если змейка врезалась в стену

    create_background(screen, 400, 300)

    # Отображаем счет и уровень
    score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
    level_text = score_font.render(f"Level: {level}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))  # Отображаем счет в верхнем левом углу
    screen.blit(level_text, (10, 40))  # Отображаем уровень ниже счета

    food.draw(screen)
    wall.draw(screen)
    worm.draw(screen)

    pygame.display.flip()
    clock.tick(3)
