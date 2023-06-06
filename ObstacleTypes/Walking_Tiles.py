import pygame, os
from ObstacleTypes.Obstacle import Obstacle


class Grass(Obstacle):
    def __init__(self, x, y):
        path = open("path.txt").readline()
        super().__init__(x, y, 'GRASS', pygame.image.load(f"{path}/Images/grass.jpeg"),
                         True, False)


class Dirt(Obstacle):
    def __init__(self, x, y):
        path = open("path.txt").readline()
        super().__init__(x, y, 'DIRT', pygame.image.load(f"{path}/Images/dirt.jpeg"), True, False)
