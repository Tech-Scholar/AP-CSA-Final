import pygame
import numpy as np

class Map:
    def __init__(self, height, width, tileAmt):
        self.height = height
        self.width = width
        self.tileAmt = tileAmt
        self.currentTile = 0
        self.tileBlueprints = [self.loadtile(i) for i in range(self.tileAmt)]
        self.L_Tiles = [i * self.width for i in range(0, self.height)]
        self.R_Tiles = [(i * self.width) - 1 for i in range(1, self.height + 1)]
        self.U_Tiles = [i for i in range(0, self.width)]
        self.D_Tiles = [i + self.width * (self.height - 1) for i in range(0, self.width)]

    def updateCurrentTile(self, player):
        if player.x < 0:
            if self.currentTile not in self.L_Tiles:
                self.currentTile -= 1
                player.x = 420
            else:
                player.x = 0
        if player.x > 420:
            if self.currentTile not in self.R_Tiles:
                self.currentTile += 1
                player.x = 0
            else:
                player.x = 420
        if player.y < 0:
            if self.currentTile not in self.U_Tiles:
                self.currentTile -= self.width
                player.y = 420
            else:
                player.y = 0
        if player.y > 420:
            if self.currentTile not in self.D_Tiles:
                self.currentTile += self.width
                player.y = 0
            else:
                player.y = 420

    def loadtile(self, tileNum):
        data = open(f"tile#{tileNum}.csv")
        return np.loadtxt(data, delimiter=",")

    def blueprints(self):
        return self.tileBlueprints

    def createTile(self, screen):
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