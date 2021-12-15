import pygame

BLACK = (0, 0, 0)
pad_width = 960
pad_height = 720

def runGame():
    global gamepad, clock

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gamepad.fill(BLACK)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


def initGame():
    global gamepad, clock

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('HamPacHang')

    clock = pygame.time.Clock()
    runGame()

initGame()
