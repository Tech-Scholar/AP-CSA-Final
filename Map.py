import numpy as np
from ObstacleTypes.Walking_Tiles import Dirt, Grass
from ObstacleTypes.NPC import NPC
from ObstacleTypes.Special_Image import House


class Map:
    def __init__(self, screen, height, width, tileAmt):
        self.screen = screen
        self.height = height
        self.width = width
        self.tileAmt = tileAmt
        self.currentTile = 0
        self.collidable = []
        self.tileBlueprints = [self.load_tile(i) for i in range(self.tileAmt)]
        self.L_Tiles = [i * self.width for i in range(0, self.height)]
        self.R_Tiles = [(i * self.width) - 1 for i in range(1, self.height + 1)]
        self.U_Tiles = [i for i in range(0, self.width)]
        self.D_Tiles = [i + self.width * (self.height - 1) for i in range(0, self.width)]

    def updateCurrentTile(self, player, eventList):
        if player.rect.x < 0:
            if self.currentTile not in self.L_Tiles:
                self.currentTile -= 1
                player.rect.x = 420
                eventList.clear_all()
            else:
                player.rect.x = 0
        if player.rect.x > 420:
            if self.currentTile not in self.R_Tiles:
                self.currentTile += 1
                player.rect.x = 0
                eventList.clear_all()
            else:
                player.rect.x = 420
        if player.rect.y < 0:
            if self.currentTile not in self.U_Tiles:
                self.currentTile -= self.width
                player.rect.y = 420
                eventList.clear_all()
            else:
                player.rect.y = 0
        if player.rect.y > 420:
            if self.currentTile not in self.D_Tiles:
                self.currentTile += self.width
                player.rect.y = 0
                eventList.clear_all()
            else:
                player.rect.y = 420

    def load_tile(self, tileNum):
        data = open(f"Tiles/tile#{tileNum}.csv")
        return np.loadtxt(data, delimiter=",")

    def blueprints(self):
        return self.tileBlueprints

    def create_tile(self):
        x, y = 0, 0
        for i in self.tileBlueprints[self.currentTile]:
            for j in i:
                if j == 0:
                    dirt_tile = Dirt(x, y)
                    dirt_tile.draw(self.screen)
                if j == 1:
                    grass_tile = Grass(x, y)
                    grass_tile.draw(self.screen)
                if j == 2:
                    npc = NPC(x, y)
                    self.collidable.append(npc)
                    npc.draw(self.screen)
                if j == 3:
                    house = House(x, y)
                    self.collidable.append(house)
                    house.draw(self.screen)
                x += 60
            x = 0
            y += 60
