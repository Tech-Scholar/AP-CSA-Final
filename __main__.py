import pygame
from Map import Map
from Player import Player
from Events import EventList
import os
from pygame.locals import K_SPACE

pygame.init()
WIDTH = 480
LENGTH = 480
screen = pygame.display.set_mode((WIDTH, LENGTH))

pygame.display.set_caption("RPG")
FPS = 10


def path_finder():
    path = os.path.dirname(__file__)
    with open("path.txt", "w") as f:
        f.write(path)


def main():
    clock = pygame.time.Clock()
    running = True
    gameStarted = False
    player = Player(3, 3)
    events = EventList(screen)
    board = Map(screen, 3, 3, 9)
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if gameStarted:
            player.update(board, pygame.key.get_pressed(), events)
            board.create_tile()
            player.draw(screen)
        elif not gameStarted and pygame.key.get_pressed()[K_SPACE]:
            events.clear_all()
            gameStarted = True

        events.draw_events()
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    path_finder()
    main()
    os.remove("path.txt")
