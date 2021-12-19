import pygame
from pacman import PacMan
from ghost import Ghost
from score import Score
from helpers import get_distance, MapStuff, get_random_direction, get_random_item
from constant import BIG_BLOCK_SIZE, BIG_GHOST_VALID_DISTANCE, ITEM_VALID_DISTANCE, ONE_BLOCK_SIZE, COIN_VALID_DISTANCE, WALL_VALID_DISTANCE, GHOST_VALID_DISTANCE, COIN_SCORE, GHOST_NORMAL_STEP, ItemType, StuffType
from typing import List

INIT_MAP = [
    ['벽', '벽', '벽', '벽', '벽', '벽', '벽', '벽',
        '벽', '벽', '벽', '벽', '벽', '벽', '벽', '벽'],
    ['벽', 'X', 'X', 'X', '벽', '벽', 'X', '벽',
     'X', 'X', 'X', '벽', 'X', 'X', 'ghost', '벽'],
    ['벽', 'X', '벽', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', '벽', 'X', '벽'],
    ['벽', 'ghost', '벽', 'X', '벽', '벽', 'X', '벽',
     '벽', 'X', '벽', '벽', 'X', '벽', 'X', '벽'],
    ['벽', 'X', 'X', 'item', 'X', '벽', 'X', '벽',
     '벽', 'X', '벽', 'X', 'X', 'X', 'X', '벽'],
    ['벽', '벽', '벽', '벽', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', '벽', '벽', '벽', '벽'],
    ['벽', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', '벽'],
    ['벽', 'X', 'X', 'X', 'X', 'item', 'X', '벽',
     '벽', '벽', 'X', 'X', 'X', 'X', 'X', '벽'],
    ['벽', 'X', '벽', 'X', 'X', 'X', 'X', '벽',
     'X', '벽', 'X', 'X', 'X', '벽', 'X', '벽'],
    ['벽', 'X', '벽', 'X', 'X', 'X', 'X', 'X',
     '팩맨', '벽', 'X', 'X', 'X', '벽', 'X', '벽'],
    ['벽', 'X', '벽', 'X', 'X', 'X', 'X', '벽',
     'X', '벽', 'X', 'X', 'X', '벽', 'X', '벽'],
    ['벽', 'X', 'X', 'X', 'X', 'X', 'X', '벽',
     '벽', '벽', 'X', 'X', 'item', 'X', 'X', '벽'],
    ['벽', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', '벽'],
    ['벽', '벽', '벽', '벽', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', '벽', '벽', '벽', '벽'],
    ['벽', 'X', 'X', 'X', 'X', '벽', 'X', '벽',
     '벽', 'X', 'X', '벽', 'X', 'X', 'X', '벽'],
    ['벽', 'X', '벽', 'X', '벽', '벽', 'X', '벽',
     '벽', 'X', '벽', '벽', 'X', '벽', 'X', '벽'],
    ['벽', 'X', '벽', 'ghost', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', '벽', 'X', '벽'],
    ['벽', 'X', 'X', 'X', '벽', '벽', 'X', '벽',
     'X', 'X', 'X', '벽', 'X', 'X', 'X', '벽'],
    ['벽', '벽', '벽', '벽', '벽', '벽', '벽', '벽',
        '벽', '벽', '벽', '벽', '벽', '벽', '벽', '벽'],
]


class GameMap:
    def __init__(self, gamepad):
        self.gamepad = gamepad
        self.game_over = False
        self.pacman = PacMan(0, 0)
        self.ghosts = [Ghost(0, 0), Ghost(0, 0), Ghost(0, 0)]
        self.score = Score(gamepad)

        self.coins = []
        self.walls = []
        self.items = []

        self.load_image()
        self.init_map()

    def init_map(self):
        map = INIT_MAP
        ghost_number = 0

        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 'X':
                    self.coins.append((i, j))
                elif map[i][j] == '벽':
                    self.walls.append((i, j))
                elif map[i][j] == 'item':
                    self.items.append((i, j))
                elif map[i][j] == '팩맨':
                    self.pacman.set_location(i, j)
                elif map[i][j] == 'ghost':
                    self.ghosts[ghost_number].set_location(i, j)
                    ghost_number += 1

    def set_game_over(self):
        self.game_over = True

    def get_pacman_location(self):
        return self.pacman.get_location()

    def check_stuff_is_in_pacman_boundary(self, pacman_x_diff, pacman_y_diff, stuff_x, stuff_y, stuff_type):
        next_pacman_x, next_pacman_y = self.pacman.get_next_location(
            pacman_x_diff, pacman_y_diff)

        if stuff_type == StuffType.COIN:
            valid_distance = COIN_VALID_DISTANCE
        elif stuff_type == StuffType.WALL:
            valid_distance = WALL_VALID_DISTANCE
        elif stuff_type == StuffType.ITEM:
            valid_distance = ITEM_VALID_DISTANCE
        elif stuff_type == StuffType.GHOST:
            if self.ghosts[0].big:
                valid_distance = BIG_GHOST_VALID_DISTANCE
            else:
                valid_distance = GHOST_VALID_DISTANCE

        if get_distance(next_pacman_x, next_pacman_y, stuff_x, stuff_y) <= valid_distance:
            return True
        return False

    def get_stuffs_in_pacman_boundary(self, pacman_x_diff, pacman_y_diff):
        result: List[MapStuff] = []

        for idx, coin in enumerate(self.coins):
            coin_x, coin_y = coin[0], coin[1]
            if self.check_stuff_is_in_pacman_boundary(pacman_x_diff, pacman_y_diff, coin_x, coin_y, StuffType.COIN):
                result.append(MapStuff(StuffType.COIN, coin_x, coin_y, idx))

        for idx, wall in enumerate(self.walls):
            wall_x, wall_y = wall[0], wall[1]
            if self.check_stuff_is_in_pacman_boundary(pacman_x_diff, pacman_y_diff, wall_x, wall_y, StuffType.WALL):
                result.append(MapStuff(StuffType.WALL, wall_x, wall_y, idx))

        for idx, item in enumerate(self.items):
            item_x, item_y = item[0], item[1]
            if self.check_stuff_is_in_pacman_boundary(pacman_x_diff, pacman_y_diff, item_x, item_y, StuffType.ITEM):
                result.append(MapStuff(StuffType.ITEM, item_x, item_y, idx))

        for idx, ghost in enumerate(self.ghosts):
            ghost_x, ghost_y = ghost.get_location()
            if self.check_stuff_is_in_pacman_boundary(pacman_x_diff, pacman_y_diff, ghost_x, ghost_y, StuffType.GHOST):
                result.append(MapStuff(StuffType.GHOST, ghost_x, ghost_y, idx))
        return result

    def move_pacman(self, x_diff, y_diff):
        next_x, next_y = self.pacman.get_next_location(x_diff, y_diff)
        stuffs = self.get_stuffs_in_pacman_boundary(x_diff, y_diff)

        if len(stuffs) == 0:
            self.pacman.set_location(next_x, next_y)
            return
        for stuff in stuffs:
            if stuff.stuff_type == StuffType.GHOST:
                self.set_game_over()
            elif stuff.stuff_type == StuffType.WALL:
                continue
            else:
                if stuff.stuff_type == StuffType.COIN:
                    self.coins.pop(stuff.idx)
                    self.score.add_score(COIN_SCORE)
                elif stuff.stuff_type == StuffType.ITEM:
                    self.items.pop(stuff.idx)
                    item_effect = get_random_item()
                    if item_effect == ItemType.MAKE_PACMAN_FASTER:
                        self.pacman.make_fast_step()
                    elif item_effect == ItemType.MAKE_GHOST_SLOWER:
                        for ghost in self.ghosts:
                            ghost.make_slow_step()
                    elif item_effect == ItemType.MAKE_GHOST_BIGGER:
                        for ghost in self.ghosts:
                            ghost.make_size_big()

                self.pacman.set_location(next_x, next_y)

    def check_wall_is_in_ghost_boundary(self, ghost: Ghost, ghost_x_diff, ghost_y_diff, stuff_x, stuff_y):
        next_ghost_x, next_ghost_y = ghost.get_next_location(
            ghost_x_diff, ghost_y_diff)

        if get_distance(next_ghost_x, next_ghost_y, stuff_x, stuff_y) <= WALL_VALID_DISTANCE:
            return True
        return False

    def get_walls_in_ghost_boundary(self, ghost, ghost_x_diff, ghost_y_diff):
        result: List[MapStuff] = []

        for idx, wall in enumerate(self.walls):
            wall_x, wall_y = wall[0], wall[1]
            if self.check_wall_is_in_ghost_boundary(ghost, ghost_x_diff, ghost_y_diff, wall_x, wall_y):
                result.append(MapStuff(StuffType.WALL, wall_x, wall_y, idx))
        return result

    def move_ghost(self, ghost: Ghost):
        x_dir, y_dir = get_random_direction()
        x_diff, y_diff = x_dir * ghost.step, y_dir * ghost.step
        next_x, next_y = ghost.get_next_location(x_diff, y_diff)
        stuffs = self.get_walls_in_ghost_boundary(
            ghost, x_diff, y_diff)
        if len(stuffs) == 0:
            ghost.set_location(next_x, next_y)

    def do_events(self, x_diff, y_diff):
        for ghost in self.ghosts:
            self.move_ghost(ghost)
        self.move_pacman(x_diff * self.pacman.step, y_diff * self.pacman.step)

    def load_image(self):
        tree = pygame.image.load('tree.png')
        pacman = pygame.image.load('pacman.png')
        dot = pygame.image.load('dot.png')
        zero = pygame.image.load('zero.png')
        ghostA = pygame.image.load('ghostA.png')
        ghostB = pygame.image.load('ghostB.png')
        ghostC = pygame.image.load('ghostC.png')
        item = pygame.image.load('item.png')

        self.resized_tree = pygame.transform.scale(
            tree, (ONE_BLOCK_SIZE, ONE_BLOCK_SIZE))
        self.resized_pacman = pygame.transform.scale(
            pacman, (ONE_BLOCK_SIZE, ONE_BLOCK_SIZE))
        self.resized_dot = pygame.transform.scale(
            dot, (ONE_BLOCK_SIZE, ONE_BLOCK_SIZE))
        self.resized_zero = pygame.transform.scale(
            zero, (ONE_BLOCK_SIZE, ONE_BLOCK_SIZE))
        self.resized_ghostA = pygame.transform.scale(
            ghostA, (ONE_BLOCK_SIZE, ONE_BLOCK_SIZE))
        self.resized_ghostB = pygame.transform.scale(
            ghostB, (ONE_BLOCK_SIZE, ONE_BLOCK_SIZE))
        self.resized_ghostC = pygame.transform.scale(
            ghostC, (ONE_BLOCK_SIZE, ONE_BLOCK_SIZE))
        self.resized_big_ghostA = pygame.transform.scale(
            ghostA, (BIG_BLOCK_SIZE, BIG_BLOCK_SIZE))
        self.resized_big_ghostB = pygame.transform.scale(
            ghostB, (BIG_BLOCK_SIZE, BIG_BLOCK_SIZE))
        self.resized_big_ghostC = pygame.transform.scale(
            ghostC, (BIG_BLOCK_SIZE, BIG_BLOCK_SIZE))
        self.resized_item = pygame.transform.scale(
            item, (ONE_BLOCK_SIZE, ONE_BLOCK_SIZE))
        

    def draw(self):
        self.gamepad.fill((160, 212, 104))
        for wall in self.walls:
            self.gamepad.blit(
                self.resized_tree, (wall[0] * ONE_BLOCK_SIZE, wall[1] * ONE_BLOCK_SIZE))
        for coin in self.coins:
            self.gamepad.blit(
                self.resized_dot, (coin[0] * ONE_BLOCK_SIZE, coin[1] * ONE_BLOCK_SIZE))
        for item in self.items:
            self.gamepad.blit(
                self.resized_item, (item[0] * ONE_BLOCK_SIZE, item[1] * ONE_BLOCK_SIZE))
        for idx, ghost in enumerate(self.ghosts):
            ghost_x, ghost_y = ghost.get_location()
            if idx == 0:
                if ghost.big:
                    ghost_image = self.resized_big_ghostA
                else:
                    ghost_image = self.resized_ghostA
            elif idx == 1:
                if ghost.big:
                    ghost_image = self.resized_big_ghostB
                else:
                    ghost_image = self.resized_ghostB
            else:
                if ghost.big:
                    ghost_image = self.resized_big_ghostC
                else:
                    ghost_image = self.resized_ghostC
            self.gamepad.blit(
                ghost_image, (ghost_x * ONE_BLOCK_SIZE,
                              ghost_y * ONE_BLOCK_SIZE)
            )
        pacman_x, pacman_y = self.pacman.get_location()
        self.gamepad.blit(self.resized_pacman, (pacman_x *
                          ONE_BLOCK_SIZE, pacman_y * ONE_BLOCK_SIZE))
        self.score.draw()
