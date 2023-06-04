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

    def hit_test(self, tile, x, y):
        test_dummy = pygame.Rect(x, y, 60, 60)
        for i in tile.collidable:
            if pygame.Rect.colliderect(i.rect, test_dummy) is True:
                return i
        return None

    def check_and_move(self, tile, change, xOrY):
        x, y = self.rect.x, self.rect.y
        if xOrY == "x":
            x += change
        elif xOrY == "y":
            y += change
        if self.hit_test(tile, x, y) is None:
            self.rect.x = x
            self.rect.y = y

    def update(self, tile, keys):
        if keys[K_UP]:
            self.image = pygame.image.load("Images/player_back.png")
            self.check_and_move(tile, -60, "y")
        elif keys[K_DOWN]:
            self.image = pygame.image.load("Images/player_front.png")
            self.check_and_move(tile, 60, "y")
        elif keys[K_RIGHT]:
            self.image = pygame.image.load("Images/player_right.png")
            self.check_and_move(tile, 60, "x")
        elif keys[K_LEFT]:
            self.image = pygame.image.load("Images/player_left.png")
            self.check_and_move(tile, -60, "x")
        tile.updateCurrentTile(self)

    #Fix
    def interact(self, tile):
        for i in range(0, 4):
            for j in range(-60, 61, 60):
                pass

        above, below = self.hit_test(tile, -60, "y"), self.hit_test(tile, 60, "y")
        right, left = self.hit_test(tile, 60, "x"), self.hit_test(tile, -60, "x")




