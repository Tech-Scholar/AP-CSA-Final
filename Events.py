import pygame
import os


class EventList:
    def __init__(self, screen):
        self.screen = screen
        self.eventList = [Event("start", 10, "", 0, 0)]

    def add_event(self, event, owner):
        event.owner = owner
        self.eventList.append(event)

    def remove_event(self, event):
        self.eventList.remove(event)

    def clear_all(self):
        self.eventList.clear()

    #
    def draw_events(self):
        for i in self.eventList:
            i.draw(self.screen)
            i.age()
            if i.time == 0:
                i.owner.hasBeenInteractedWith = False
                self.remove_event(i)


class Event:
    def __init__(self, version, time, text, x, y):
        self.version = version
        self.time = time
        self.text = text
        self.x = x
        self.y = y
        self.path = os.path.dirname(__file__)
        self.owner = None

    def draw(self, screen):
        if self.version == "text":
            font = pygame.font.SysFont("Arial", 24)
            txtsurf = font.render(self.text, True, (255, 255, 255))
            screen.blit(txtsurf, (self.x, self.y - 30))
        elif self.version == "end":
            self.time = -1
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen.get_width(), screen.get_height()))
            font = pygame.font.SysFont("Arial", 32)
            txtsurf = font.render("YOU WIN!", True, (255, 255, 255))
            screen.blit(txtsurf, (screen.get_width() // 2 - 75, screen.get_height() // 2))
        elif self.version == "start":
            self.time = -1
            pygame.draw.rect(screen, (109, 117, 110), (0, 0, screen.get_width(), screen.get_height()))
            font = pygame.font.SysFont("Arial", 32)
            text = font.render("The Alien Castaway", True, (255, 255, 255))
            screen.blit(text, (110, 25))
            font2 = pygame.font.SysFont("Arial", 24)
            words = "Robinson the Alien crashed. Seek tools for ship repair.  Use arrows to move, 'p' to interact."
            y = 105
            for i in range(0, len(words), 19):
                text2 = font2.render(words[i:i + 18], True, (255, 255, 255))
                screen.blit(text2, (35, y))
                y += 30
            font = pygame.font.SysFont("Arial", 32)
            text = font.render("Press SPACE to start", True, (255, 255, 255))
            screen.blit(text, (100, 300))
            original_image = pygame.image.load(f"{self.path}/Images/player_front.png")
            resized_image = pygame.transform.scale(original_image, (260, 240))
            screen.blit(resized_image, pygame.Rect(250, 50, 400, 360))

    def age(self):
        self.time -= 1
