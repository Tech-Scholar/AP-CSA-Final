from ObstacleTypes.Obstacle import Obstacle
from Events import *


# class InteractableObject(Obstacle):
#    def __init__(self, x, y, version, image, width, height):
#        super().__init__(x, y, version, image, True, True, width, height)
#        self.hasBeenInteractedWith = False


class NPC(Obstacle):
    def __init__(self, x, y, text="Hello"):
        path = open("path.txt").readline()
        self.hasBeenInteractedWith = False
        self.txt = text
        super().__init__(x, y, 'NPC', pygame.image.load(f"{path}/Images/npc_front.png"), False, True)

    def interact(self, eventList, player):
        if not self.hasBeenInteractedWith:
            self.hasBeenInteractedWith = True
            new_event = Event('text', 10, self.txt, self.x + 3.75, self.y)
            eventList.add_event(new_event, self)


class QuestNPC(NPC):
    def __init__(self, x, y, text, take, give):
        self.take, self.give = take, give
        self.hasBeenInteractedWith = False
        super().__init__(x, y, text)

    def interact(self, eventList, player):
        if self.take in player.inventory:
            self.hasBeenInteractedWith = True
            player.inventory.remove(self.take)
            player.inventory.append(self.give)
            new_event = Event('text', 10, f"Here is your {self.give}!", self.x + 3.75, self.y)
            eventList.add_event(new_event, self)
        else:
            super().interact(eventList, player)


class Giver(Obstacle):
    def __init__(self, x, y, version, give):
        path = open("path.txt").readline()
        self.give = give
        self.given = False
        self.hasBeenInteractedWith = False
        super().__init__(x, y, version, pygame.image.load(f"{path}/Images/{version}.jpeg"),
                         False, True, 120, 120)

    def interact(self, eventList, player):
        if not self.hasBeenInteractedWith:
            self.hasBeenInteractedWith = True
            if not self.given:
                self.given = True
                player.inventory.append(self.give)
                new_event = Event('text', 10, f"{self.give} given", self.x + 3.75, self.y)
                eventList.add_event(new_event, self)
            elif self.given:
                new_event = Event('text', 10, f"{self.give} was given", self.x + 3.75, self.y)
                eventList.add_event(new_event, self)


class Spaceship(Obstacle):
    itemsNeeded = ["wrench", "screw", "hammer"]
    status = 0

    def __init__(self, x, y):
        path = open("path.txt").readline()
        self.hasBeenInteractedWith = False
        super().__init__(x, y, 'Spaceship', pygame.image.load(f"{path}/Images/spaceship.jpeg"),
                         True, True, 180, 120)

    def interact(self, eventList, player):
        if not self.hasBeenInteractedWith:
            self.hasBeenInteractedWith = True
            for i in self.itemsNeeded:
                if i in player.inventory:
                    player.inventory.remove(i)
                    self.itemsNeeded.remove(i)
                    Spaceship.status += 1
                    break
            if Spaceship.status == 3:
                new_event = Event('end', 10, "end", self.x, self.y)
                eventList.add_event(new_event, self)
            else:
                text = {0: "Broken", 1: "Not Ready to Fly", 2: "Almost Fixed"}
                new_event = Event('text', 10, text[self.status] + ": " + ",".join(self.itemsNeeded), self.x + 60, self.y)
                eventList.add_event(new_event, self)
