import pygame
from helpers import get_random_color
from map import GameMap
from constant import SystemState, SCREEN_WIDTH, SCREEN_HEIGHT, REFRESH_RATE, WHITE
from threading import Timer


class Game:
    def __init__(self):
        self.crashed = False
        self.gamepad = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.clock.tick(REFRESH_RATE)
        self.init_system()
        self.start_game()

    def init_system(self):
        pygame.init()
        pygame.display.set_caption("T08pacman")

        font = pygame.font.SysFont("arial", 70, True, False)
        title = font.render("HamPackHang", True, WHITE, get_random_color())
        self.gamepad.fill((160, 212, 104))
        self.gamepad.blit(title, (100, 100))

        fontS = pygame.font.SysFont("arial", 40, True, False)
        titleS = fontS.render("Press SPACE to start",
                              True, WHITE, get_random_color())
        self.gamepad.blit(titleS, (100, 400))

    def start_game(self):
        system_state = SystemState.NOT_STARTED
        while system_state == SystemState.NOT_STARTED:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    system_state = SystemState.QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        system_state = SystemState.PLAY
            pygame.display.update()

        if system_state == SystemState.PLAY:
            self.game_map = GameMap(self.gamepad)
            self.game_map.draw()
            self.run_game()

        elif system_state == SystemState.QUIT:
            pygame.quit()

    def move_ghosts(self):
        self.game_map.do_events(0, 0)

    # def repeat_move_ghost(self):
    #     if self.crashed:
    #         return
    #     self.move_ghost()
    #     self.timer = Timer(0.5, self.repeat_move_ghost)
    #     self.timer.start()

    def run_game(self):
        while not self.crashed:
            if self.game_map.game_over:
                pygame.quit()
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                self.game_map.do_events(-1, 0)
            if pressed[pygame.K_RIGHT]:
                self.game_map.do_events(+1, 0)
            if pressed[pygame.K_DOWN]:
                self.game_map.do_events(0, +1)
            if pressed[pygame.K_UP]:
                self.game_map.do_events(0, -1)
            self.move_ghosts()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True
            self.game_map.draw()
            pygame.display.update()
        pygame.quit()
