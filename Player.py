import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)


class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("Images/player_front.png")
        self.rect = self.image.get_rect(topleft=(x * 60, y * 60))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_and_move(self, map, change, xOrY):
        x, y = self.rect.x, self.rect.y
        if xOrY == "x":
            x += change
        elif xOrY == "y":
            y += change
        test_dummy = pygame.Rect(x, y, 60, 60)
        checker = True
        for i in map.collidable:
            if pygame.Rect.colliderect(i.rect, test_dummy) is True:
                checker = False
        if checker:
            self.rect.x = x
            self.rect.y = y

    def update(self, map, keys):
        if keys[K_UP]:
            self.image = pygame.image.load("Images/player_back.png")
            self.check_and_move(map, -60, "y")
        elif keys[K_DOWN]:
            self.image = pygame.image.load("Images/player_front.png")
            self.check_and_move(map, 60, "y")
        elif keys[K_RIGHT]:
            self.image = pygame.image.load("Images/player_right.png")
            self.check_and_move(map, 60, "x")
        elif keys[K_LEFT]:
            self.image = pygame.image.load("Images/player_left.png")
            self.check_and_move(map, -60, "x")
        map.updateCurrentTile(self)
