import pygame
from ObstacleTypes.Obstacle import Obstacle


class NPC(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, pygame.image.load("Images/npc_front.png"))
