[C언어] [오후 6:23] import pygame
import random

BLACK = (0,0,0)
WHITE = (255,255,255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def get_random_color():
  return (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

def runGame():
    global gamepad, clock

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

    
def main() 

