import pygame
from ObstacleTypes.Obstacle import Obstacle


class Grass(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, pygame.image.load("Images/grass.jpeg"))
