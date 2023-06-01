import pygame


class Obstacle:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 60, 60)
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, self.rect)
