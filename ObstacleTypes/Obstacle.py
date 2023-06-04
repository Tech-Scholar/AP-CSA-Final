import pygame


class Obstacle:
    def __init__(self, x, y, type, image, collidable):
        self.x = x
        self.y = y
        self.type = type
        self.rect = pygame.Rect(self.x, self.y, 60, 60)
        self.image = image
        self.collidable = collidable

    def draw(self, screen):
        screen.blit(self.image, self.rect)
