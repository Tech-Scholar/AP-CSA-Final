import pygame

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, 'blue', pygame.Rect(self.x, self.y, 60, 60))