import pygame
import random

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
SCREEN_WIDTH = 680
SCREEN_HEIGHT = 620
one_blocksize = 35
score=0
gamemap = [
        ['벽', '벽', '벽', '벽', '벽', '벽','벽','벽','벽', '벽', '벽', '벽', '벽', '벽','벽','벽'],
        ['벽', 'x', 'x', 'x', '벽', '벽', 'x','벽','x', 'x', 'x', '벽', 'x', 'x', 'x','벽'],
        ['벽', 'x', '벽', 'x', 'x', 'x', 'x','x','x', 'x', 'x', 'x', 'x', '벽', 'x','벽'],
        ['벽', 'x', '벽', 'x', '벽', '벽','x','벽','벽', 'x', '벽', '벽', 'x', '벽', 'x','벽'],
        ['벽', 'x', 'x', 'x', 'x', '벽', 'x','벽','벽', 'x', '벽', 'ghost3', 'x', 'x', 'x','벽'],
        ['벽', '벽', '벽', '벽', 'x', 'x','x','x','x', 'x', 'x', 'x', '벽', '벽', '벽','벽'],
        ['벽', 'x', 'x', 'x', 'x', 'x', 'x','x','x', 'x', 'x', 'x', 'x', 'x', 'x','벽'],
        ['벽', 'x', 'x', 'x', 'x', 'x', 'x','벽','벽', '벽', 'x', 'x', 'x', 'x', 'x','벽'],
        ['벽', 'x', '벽', 'x', 'x', 'x', 'x','벽','x', '벽', 'x', 'x', 'x', '벽', 'x','벽'],
        ['벽', 'x', '벽', 'x', 'x', 'x','x','x','팩맨', '벽', 'x', 'x', 'x', '벽', 'x','벽'],
        ['벽', 'x', '벽', 'x', 'ghost1', 'x', 'x','벽','x', '벽', 'x', 'x', 'x', '벽', 'x','벽'],
        ['벽', 'x', 'x', 'x', 'x', 'x', 'x','벽','벽', '벽', 'x', 'x', 'x', 'x', 'x','벽'],
        ['벽', 'x', 'x', 'x', 'x', 'x', 'x','x','x', 'x', 'x', 'x', 'x', 'x', 'x','벽'],
        ['벽', '벽', '벽', '벽', 'x', 'x', 'x','x','x', 'x', 'x', 'x', '벽', '벽', '벽','벽'],
        ['벽', 'x', 'x', 'x', 'x', '벽','x','벽','벽', 'x', 'x', '벽', 'x', 'x', 'x','벽'],
        ['벽', 'x', '벽', 'x', '벽', '벽', 'x','벽','벽', 'x', '벽','벽', 'x', '벽', 'x','벽'],
        ['벽', 'x', '벽', 'x', 'ghost2', 'x','x','x','x', 'x', 'x', 'x', 'x', '벽', 'x','벽'],
        ['벽', 'x', 'x', 'x', '벽', '벽', 'x','벽','x', 'x', 'x','벽', 'x', 'x', 'x','벽'],
        ['벽', '벽', '벽', '벽', '벽', '벽','벽','벽', '벽', '벽', '벽', '벽','벽','벽','벽','벽'],
    ]


def get_random_color():
  return (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))



def run_game():
    crashed = False
    draw_score()
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_pacman(-1,0)
                if event.key == pygame.K_RIGHT:
                    move_pacman(+1,0)
                if event.key == pygame.K_DOWN:
                    move_pacman(0,+1)
                if event.key == pygame.K_UP:
                    move_pacman(0,-1)

            if event.type == pygame.QUIT:
                crashed = True


        pygame.display.update()

        clock.tick(60)
    pygame.quit()

def draw_score():

    font_01 = pygame.font.SysFont("arial", 30, True, False)
    text_score = font_01.render("Score : " + str(score), True, WHITE, RED)
    gamepad.blit(text_score, [5, 570])


def change_score(a):

    global score

    score+=a
    draw_score()


def make_trees():
   for x in range(len(gamemap)):
        for y in range(len(gamemap[x])):
            if gamemap[x][y] == '벽':
                gamepad.blit(resized_tree, (x*one_blocksize,y*one_blocksize))
            elif gamemap[x][y] == '팩맨':
                gamepad.blit(resized_pacman, (x*one_blocksize, y*one_blocksize))
            elif gamemap[x][y] == 'x':
                gamepad.blit(resized_dot, (x*one_blocksize, y*one_blocksize))
            elif gamemap[x][y] == '0':
                gamepad.blit(resized_zero, (x*one_blocksize, y*one_blocksize))
            elif gamemap[x][y] == 'ghost1':
                gamepad.blit(resized_ghost1, (x*one_blocksize, y*one_blocksize))
            elif gamemap[x][y] == 'ghost2':
                gamepad.blit(resized_ghost2, (x*one_blocksize, y*one_blocksize))
            elif gamemap[x][y] == 'ghost3':
                gamepad.blit(resized_ghost3, (x*one_blocksize, y*one_blocksize))


def find_pacman():
    for p in range(len(gamemap)):
        for q in range(len(gamemap[p])):
            if gamemap[p][q] == '팩맨':
                return [p, q]

def move_pacman(x_diff, y_diff):
    global score

    current_x, current_y = find_pacman()
    next_x = current_x + x_diff
    next_y = current_y + y_diff
    if not check_tree(next_x, next_y):
        if (gamemap[next_x][next_y] == 'x'):
            change_score(10)

        gamemap[current_x][current_y] = '0'
        gamemap[next_x][next_y] = '팩맨'
        make_trees()



def check_tree(x, y):
    if gamemap[x][y] == '벽':
        return True
    else:
        return False



def main():
    global resized_tree, resized_pacman, resized_dot, resized_zero
    global resized_ghost1, resized_ghost2, resized_ghost3

    gamepad.fill((160,212,104))
    pygame.display.set_caption("HamPacHang")
    tree = pygame.image.load('C:/Users/solom/Downloads/tree.png')
    resized_tree = pygame.transform.scale(tree,(one_blocksize,one_blocksize))
    pacman = pygame.image.load('C:/Users/solom/Downloads/pacman.png')
    resized_pacman = pygame.transform.scale(pacman, (one_blocksize,one_blocksize))
    dot = pygame.image.load('C:/Users/solom/Downloads/dot.png')
    resized_dot = pygame.transform.scale(dot, (one_blocksize,one_blocksize))
    zero = pygame.image.load('C:/Users/solom/Downloads/zero.png')
    resized_zero = pygame.transform.scale(zero, (one_blocksize,one_blocksize))
    ghost1 = pygame.image.load('C:/Users/solom/Downloads/ghost1.jpg')
    resized_ghost1 = pygame.transform.scale(ghost1, (one_blocksize,one_blocksize))
    ghost2 = pygame.image.load('C:/Users/solom/Downloads/ghost2.jpg')
    resized_ghost2 = pygame.transform.scale(ghost2, (one_blocksize,one_blocksize))
    ghost3 = pygame.image.load('C:/Users/solom/Downloads/ghost3.jpg')
    resized_ghost3 = pygame.transform.scale(ghost3, (one_blocksize,one_blocksize))



    make_trees()

    clock = pygame.time.Clock()

    run_game()


def start():
    global gamepad, clock

    pygame.init()
    gamepad = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("T08packman")

    font = pygame.font.SysFont("arial", 70, True, False)
    title = font.render("HamPackHang", True, WHITE, get_random_color())
    gamepad.fill((160,212,104))
    gamepad.blit(title, (100,100))
    fontS = pygame.font.SysFont("arial", 40, True, False)
    titleS = fontS.render("Press SPACE to start", True, WHITE, get_random_color())
    gamepad.blit(titleS, (100,400))

    clock = pygame.time.Clock()

    start=0

    while start==0:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start=99

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    start=1

        pygame.display.update()

        clock.tick(60)

    if start==1:
        main()

    elif start==99:
        pygame.quit()

start()
