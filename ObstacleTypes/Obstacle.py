import os.path

import pygame


class Obstacle:
    def __init__(self, x, y, version, image, collidable, interactable, width=60, height=60):
        self.x = x
        self.y = y
        self.path = os.path.dirname(__file__)
        self.version = version
        self.rect = pygame.Rect(self.x, self.y,width, height)
        self.image = image
        self.collidable = collidable
        self.interactable = interactable

    def draw(self, screen):
        screen.blit(self.image, self.rect)
