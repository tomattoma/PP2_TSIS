import pygame
from game_object import GameObject 
from game_object import Point 

class Wall(GameObject):
    def __init__(self, tile_width):
        super().__init__([], (255, 0, 0), tile_width)
        self.level = 1
        self.load_level()

    def load_level(self):
        # Загружаем уровень
        f = open("levels/level{}.txt".format(self.level), "r")
        row = -1
        col = -1
        for line in f:
            row = row + 1
            col = -1
            for c in line:
                col = col + 1
                if c == '#':
                    self.points.append(Point(col * self.tile_width, row * self.tile_width))
        f.close()

    def next_level(self):
        self.points = []
        self.level = (self.level + 1) % 2
        self.load_level()

    def check_collision(self, head_location):
        # Проверка, не находится ли голова змейки в точке стены
        for point in self.points:
            if point.X == head_location.X and point.Y == head_location.Y:
                return True  # Столкновение произошло
        return False  # Столкновения нет
