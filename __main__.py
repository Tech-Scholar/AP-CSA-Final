import pygame
from Map import Map
from Player import Player
from Events import EventList

pygame.init()

WIDTH = 480
LENGTH = 480
screen = pygame.display.set_mode((WIDTH, LENGTH))

pygame.display.set_caption("RPG")
FPS = 10


def main():
    clock = pygame.time.Clock()
    running = True
    player = Player(3, 3)
    events = EventList(screen)
    board = Map(screen, 3, 3, 9)
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player.update(board, pygame.key.get_pressed(), events)
        board.create_tile()
        player.draw(screen)
        events.draw_events()
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()