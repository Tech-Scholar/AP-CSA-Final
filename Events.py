import pygame


class EventList:
    def __init__(self, screen):
        self.screen = screen
        self.eventList = []

    def add_event(self, event):
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
                self.remove_event(i)

class Event:
    def __init__(self, version, time, text):
        self.version = version
        self.time = time
        self.text = text

    def draw(self, screen):
        font = pygame.font.SysFont("Arial", 36)
        txtsurf = font.render(self.text, True, (255, 255, 255))
        screen.blit(txtsurf, (200 - txtsurf.get_width() // 2, 150 - txtsurf.get_height() // 2))

    def age(self):
        self.time -= 1
