import pygame
from constant import WHITE, RED

class Score:
    def __init__(self, gamepad):
        self.gamepad = gamepad
        self.score = 0
    
    def add_score(self, score: int):
        self.score += score

    def get_score(self):
        return self.score

    def reset_score(self):
        self.score = 0

    def draw(self):
        font_01 = pygame.font.SysFont("arial", 30, True, False)
        score_text = font_01.render("Score : " + str(self.score), True, WHITE, RED)
        self.gamepad.blit(score_text, [5, 570])
