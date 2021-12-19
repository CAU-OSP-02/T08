import random
import math

from constant import ItemType


def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def get_random_direction():
    a = [[0, +1], [0, -1], [1, 0], [-1, 0], [0, 0]]
    r = random.randrange(0, 5)
    return a[r]


def get_distance(a_x, a_y, b_x, b_y):
    return math.sqrt(abs(a_x - b_x)**2 + abs(a_y - b_y)**2)


class MapStuff():
    def __init__(self, stuff_type, x, y, idx):
        self.stuff_type = stuff_type
        self.x = x
        self.y = y
        self.idx = idx

def get_random_item():
    a = [ItemType.MAKE_GHOST_BIGGER, ItemType.MAKE_GHOST_SLOWER, ItemType.MAKE_PACMAN_FASTER]
    r = random.randrange(0,3)
    return a[r]
