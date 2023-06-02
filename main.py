import pygame
from Map import Map
from Player import Player

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
    board = Map(3, 3, 9)
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player.update(board, pygame.key.get_pressed())
        board.create_tile(screen)
        player.draw(screen)
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
