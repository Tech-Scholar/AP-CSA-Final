import pygame
from ObstacleTypes.Obstacle import Obstacle


class NPC(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, 'NPC', pygame.image.load("Images/npc_front.png"), False)

    def interact(self, tile):
        print('Hello World')
        font = pygame.font.SysFont("Arial", 36)
        txtsurf = font.render("Hello, World", True, (255,255,255))
        tile.screen.blit(txtsurf, (200 - txtsurf.get_width() // 2, 150 - txtsurf.get_height() // 2))
