import pygame, os
from ObstacleTypes.Obstacle import Obstacle


class House(Obstacle):
    def __init__(self, x, y):
        path = open("path.txt").readline()
        super().__init__(x, y, 'House', pygame.image.load(f"{path}/Images/house_front.jpeg"),
                         True, False, 180, 180)
