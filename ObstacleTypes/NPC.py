from ObstacleTypes.Obstacle import Obstacle
from Events import *


class NPC(Obstacle):
    def __init__(self, x, y):
        path = open("path.txt").readline()
        self.hasBeenInteractedWith = False
        super().__init__(x, y, 'NPC', pygame.image.load(f"{path}/Images/npc_front.png"), False, True)

    def interact(self, eventList):
        if not self.hasBeenInteractedWith:
            self.hasBeenInteractedWith = True
            new_event = Event('text', 10, 'Hello!', self.x, self.y)
            eventList.add_event(new_event, self)
