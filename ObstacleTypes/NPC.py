import pygame
from ObstacleTypes.Obstacle import Obstacle
from Events import *


class NPC(Obstacle):
    def __init__(self, x, y):
        self.hasBeenInteractedWith = False
        super().__init__(x, y, 'NPC', pygame.image.load("Images/npc_front.png"), False)

    def interact(self, eventList):
        if not self.hasBeenInteractedWith:
            self.hasBeenInteractedWith = True
            new_event = Event('text', 10, 'Hello!', self.x, self.y)
            eventList.add_event(new_event, self)


