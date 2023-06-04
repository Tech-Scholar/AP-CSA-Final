import pygame
from ObstacleTypes.Obstacle import Obstacle


class Grass(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, 'GRASS', pygame.image.load("Images/grass.jpeg"), True)
