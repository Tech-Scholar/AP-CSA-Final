import pygame


class Obstacle:
    def __init__(self, x, y, version, image, collidable, width=60, height=60):
        self.x = x
        self.y = y
        self.type = version
        self.rect = pygame.Rect(self.x, self.y, width, height)
        self.image = image
        self.collidable = collidable

    def draw(self, screen):
        screen.blit(self.image, self.rect)
