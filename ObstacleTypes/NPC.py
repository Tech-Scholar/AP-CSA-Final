import pygame
from ObstacleTypes.Obstacle import Obstacle
from Events import *


class NPC(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, 'NPC', pygame.image.load("Images/npc_front.png"), False)

    def interact(self, eventList):
        new_event = Event('text', 10, 'Hello!')
        eventList.add_event(new_event)

