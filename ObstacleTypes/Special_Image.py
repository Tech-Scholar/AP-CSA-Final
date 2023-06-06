from ObstacleTypes.Obstacle import Obstacle
from Events import *


class House(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, 'House', pygame.image.load("Images/house_front.jpeg"), False,
                         180, 180)
