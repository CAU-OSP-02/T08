import pygame
import random

WHITE=(255,255,255)
BLACK=(0,0,0)
pad_width=800
pad_height=400
tileS=100
class Ground(pygame.sprite.Sprite):
       
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)


        pygame.draw.rect(gamepad,BLACK,[(2*x)*tileS/2,(2*y)*tileS/2,tileS,tileS])


class Wall(pygame.sprite.Sprite):
    
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)

        pygame.draw.rect(gamepad,WHITE,[(2*x)*tileS/2,(2*y)*tileS/2,tileS,tileS])


def BackGround():

    MapData=[[1,1,0,0,0,0,1,1],[1,0,1,0,1,0,1,0],[1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0]]
    for col in range(0,4):
        for row in range(0,8):
            if MapData[col][row] == 1:
                Wall(row,col)
                print(-pad_width/2+(2*row+1)*tileS/2, pad_height/2-(2*col+1)*tileS/2)

            if MapData[col][row] == 0:
                Ground(row,col)
                print(-pad_width/2+(2*row+1)*tileS/2, pad_height/2-(2*col+1)*tileS/2)

    
def runGame():
    global gamepad, clock

    crashed=False
    BackGround()
    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed=True

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def initGame():
    global gamepad, clock

    pygame.init()
    gamepad=pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_caption('HamPacHang')

    clock=pygame.time.Clock()
    runGame()

initGame()
