import pygame
from ObstacleTypes.Obstacle import Obstacle


class Dirt(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, 'DIRT', pygame.image.load("Images/dirt.jpeg"), True)
