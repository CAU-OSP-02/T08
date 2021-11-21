import pygame

WHITE=(255,255,255)
BLACK=(0,0,0)
pad_width=512
pad_height=512
tileS=128
class Ground(pygame.sprite.Sprite):
       
       def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x * tileS
        self.y = y * tileS
        pygame.draw.rect(gamepad,BLACK,[-pad_width/2+(2*x+1)*tileS/2, pad_height/2-(2*y+1)*tileS/2,tileS,tileS])


class Wall(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x * tileS
        self.y = y * tileS
        pygame.draw.rect(gamepad,WHITE,[-pad_width/2+(2*x+1)*tileS/2, pad_height/2-(2*y+1)*tileS/2,tileS,tileS])


def BackGround():

    MapData=[[0,0,1,1,1,1,0,0],[1,1,0,0,0,0,1,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1]]
    for col in range(0,3):
        for row in range(0,3):
            if MapData[col][row] == 1:
                Ground(col, row)

            if MapData[col][row] == 0:
                Wall(col, row)

    
def runGame():
    global gamepad, clock

    crashed=False
    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed=True

        BackGround()
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
