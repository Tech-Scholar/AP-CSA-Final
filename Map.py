import pygame
import numpy as np

class Map:
    def __init__(self, height, width, tileAmt):
        self.height = height
        self.width = width
        self.tileAmt = tileAmt
        self.currentTile = 0
        self.tileBlueprints = [self.loadtile(i) for i in range(self.tileAmt)]

    def updateCurrentTile(self, player):
        L_Tiles = [i * self.width for i in range(0, self.height)]
        R_Tiles = [(i * self.width) - 1 for i in range(1, self.height + 1)]
        U_Tiles = []
        D_Tiles = []
        if player.x < 0:
            if self.currentTile not in L_Tiles:
                self.currentTile -= 1
                player.x = 420
            else:
                player.x = 0
        if player.x > 420:
            if self.currentTile not in R_Tiles:
                self.currentTile += 1
                player.x = 0
            else:
                player.x = 420
        if player.y < 0:
            self.currentTile -= self.width
            player.y = 480
        if player.y > 480:
            self.currentTile += self.width
            player.y = 0

    def loadtile(self, tileNum):
        data = open(f"tile#{tileNum}.csv")
        return np.loadtxt(data, delimiter=",")

    def blueprints(self):
        return self.tileBlueprints

    def createtile(self, screen):
        x, y = 0, 0
        for i in self.tileBlueprints[self.currentTile]:
            for j in i:
                if j == 0:
                    pygame.draw.rect(screen, 'brown', pygame.Rect(x, y, 60, 60))
                if j == 1:
                    pygame.draw.rect(screen, 'green', pygame.Rect(x, y, 60, 60))
                x += 60
            x = 0
            y += 60