import pygame
import random
from game_object import GameObject 
from game_object import Point 

import random

class Food(GameObject):
    def __init__(self, tile_width):
        # Генерация случайных координат для еды
        self.timer = pygame.time.get_ticks()
        random_x = random.randint(0, (400 // tile_width) - 1) * tile_width
        random_y = random.randint(0, (300 // tile_width) - 1) * tile_width
        super().__init__([Point(random_x, random_y)], (0, 255, 0), tile_width)

    def can_eat(self, head_location, tile_width):
        result = None
        for point in self.points:
            if point.X == head_location.X and point.Y == head_location.Y:
                result = point
                break

        if result:
            # Если съели еду, генерируем новую на случайных координатах
            random_x = random.randint(0, (400 // tile_width) - 1) * tile_width
            random_y = random.randint(0, (300 // tile_width) - 1) * tile_width
            self.points = [Point(random_x, random_y)]  # Обновляем позицию еды
        return result
    
    def update_timer(self, time_limit=6000):
        if pygame.time.get_ticks() - self.timer > time_limit:
            random_x = random.randint(0, (400 // self.tile_width) - 1) * self.tile_width
            random_y = random.randint(0, (300 // self.tile_width) - 1) * self.tile_width
            self.points = [Point(random_x, random_y)]  # Обновляем позицию еды
            self.timer = pygame.time.get_ticks()  # Сбрасываем таймер
        
