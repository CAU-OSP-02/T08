from enum import Enum

# colour
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# length
SCREEN_WIDTH = 680
SCREEN_HEIGHT = 620
ONE_BLOCK_SIZE = 35
BIG_BLOCK_SIZE = 50

# system
REFRESH_RATE = 60


class SystemState(Enum):
    NOT_STARTED = 0
    PLAY = 1
    QUIT = 2


# distance
WALL_VALID_DISTANCE = 0.5
BIG_WALL_VALID_DISTANCE = 0.75
COIN_VALID_DISTANCE = 0.3
GHOST_VALID_DISTANCE = 0.3
BIG_GHOST_VALID_DISTANCE = 0.5
ITEM_VALID_DISTANCE = 0.3
PACMAN_NORMAL_STEP = 0.05
PACMAN_FAST_STEP = 0.25
GHOST_NORMAL_STEP = 0.05
GHOST_SLOW_STEP = 0.03


# score
COIN_SCORE = 10

# map


class MapEvent(Enum):
    PACMAN_MOVE_LEFT = 0
    PACMAN_MOVE_RIGHT = 1
    PACMAN_MOVE_UP = 2
    PACMAN_MOVE_DOWN = 3


class StuffType(Enum):
    GHOST = 0
    COIN = 1
    WALL = 2
    ITEM = 3

class ItemType(Enum):
    MAKE_PACMAN_FASTER = 0
    MAKE_GHOST_SLOWER = 1
    MAKE_GHOST_BIGGER = 2
