import pygame
import random
import time

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
SCREEN_WIDTH = 680
SCREEN_HEIGHT = 620
one_blocksize = 35
score=0
Gscore=0
gamemap = [
        ['벽', '벽', '벽', '벽', '벽', '벽','벽','벽','벽', '벽', '벽', '벽', '벽', '벽','벽','벽'],
        ['벽', 'x', 'x', 'x', '벽', '벽', 'x','벽','x', 'x', 'x', '벽', 'x', 'x', 'x','벽'],
        ['벽', 'x', '벽', 'x', 'x', 'x', 'x','x','x', 'x', 'x', 'x', 'x', '벽', 'x','벽'],
        ['벽', 'x', '벽', 'x', '벽', '벽','x','벽','벽', 'x', '벽', '벽', 'x', '벽', 'x','벽'],
        ['벽', 'x', 'x', 'x', 'x', '벽', 'x','벽','벽', 'x', '벽', 'x', 'x', 'x', 'x','벽'],
        ['벽', '벽', '벽', '벽', 'x', 'x','x','x','x', 'x', 'x', 'C', '벽', '벽', '벽','벽'],
        ['벽', 'x', 'x', 'x', 'x', 'x', 'x','x','x', 'x', 'x', 'x', 'x', 'x', 'x','벽'],
        ['벽', 'x', 'x', 'x', 'x', 'x', 'x','벽','벽', '벽', 'x', 'x', 'x', 'x', 'x','벽'],
        ['벽', 'x', '벽', 'x', 'B', 'x', 'x','벽','x', '벽', 'x', 'x', 'x', '벽', 'x','벽'],
        ['벽', 'x', '벽', 'x', 'x', 'x','x','x','팩맨', '벽', 'x', 'x', 'x', '벽', 'x','벽'],
        ['벽', 'x', '벽', 'x', 'x', 'x', 'x','벽','x', '벽', 'x', 'x', 'x', '벽', 'x','벽'],
        ['벽', 'x', 'x', 'x', 'x', 'x', 'x','벽','벽', '벽', 'x', 'x', 'x', 'x', 'x','벽'],
        ['벽', 'x', 'x', 'x', 'x', 'x', 'x','x','x', 'x', 'x', 'x', 'x', 'x', 'x','벽'],
        ['벽', '벽', '벽', '벽', 'x', 'x', 'x','x','A', 'x', 'x', 'x', '벽', '벽', '벽','벽'],
        ['벽', 'x', 'x', 'x', 'x', '벽','x','벽','벽', 'x', 'x', '벽', 'x', 'x', 'x','벽'],
        ['벽', 'x', '벽', 'x', '벽', '벽', 'x','벽','벽', 'x', '벽','벽', 'x', '벽', 'x','벽'],
        ['벽', 'x', '벽', 'x', 'x', 'x','x','x','x', 'x', 'x', 'x', 'x', '벽', 'x','벽'],
        ['벽', 'x', 'x', 'x', '벽', '벽', 'x','벽','x', 'x', 'x','벽', 'x', 'x', 'x','벽'],
        ['벽', '벽', '벽', '벽', '벽', '벽','벽','벽', '벽', '벽', '벽', '벽','벽','벽','벽','벽'],
    ]


def get_random_color():
  return (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))



def run_game():
    crashed = False
    draw_score(0)
    draw_score(1)
    while not crashed:

        
        for event in pygame.event.get():

        
            
            if event.type == pygame.KEYDOWN:
                move_ghost('A')
                move_ghost('B')
                move_ghost('C')
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

def draw_score(a):

    font_01 = pygame.font.SysFont("arial", 30, True, False)
    if a == 0:
      text_score = font_01.render("Score : " + str(score), True, WHITE, RED)
      gamepad.blit(text_score, [5, 570])

    else:
      text_score = font_01.render("Score : " + str(Gscore), True, WHITE, BLUE)
      gamepad.blit(text_score, [200, 570])


def change_score(a,c):

    global score
    global Gscore

    if c==0:
      score+=a

    else:
      Gscore+=a
    
    draw_score(c)


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
            elif gamemap[x][y]=='A':
                gamepad.blit(resized_ghostA, (x*one_blocksize, y*one_blocksize))
            elif gamemap[x][y]=='B':
                gamepad.blit(resized_ghostB, (x*one_blocksize, y*one_blocksize))
            elif gamemap[x][y]=='C':
                gamepad.blit(resized_ghostC, (x*one_blocksize, y*one_blocksize))


def find_pacman():
    for p in range(len(gamemap)):
        for q in range(len(gamemap[p])):
            if gamemap[p][q] == '팩맨':
                return [p, q]
           

           
def find_ghost(N):
    for p in range(len(gamemap)):
        for q in range(len(gamemap[p])):
            if gamemap[p][q] == N:
                return [p, q]


def move_pacman(x_diff, y_diff):
    global score

    current_x, current_y = find_pacman()
    next_x = current_x + x_diff
    next_y = current_y + y_diff
    if not check_tree(next_x, next_y):
        if (gamemap[next_x][next_y] == 'x'):
            change_score(10,0)


        gamemap[current_x][current_y] = '0'
        gamemap[next_x][next_y] = '팩맨'
        make_trees()



def check_tree(x, y):
    if gamemap[x][y] == '벽':
        return True
    else:
        return False

def check_ghost(x, y):
    if gamemap[x][y] == 'A':
        return True
    if gamemap[x][y] == 'B':
        return True
    if gamemap[x][y] == 'C':
        return True
    else:
        return False

    
def move_ghost(gN):

    a = [[0,+1], [0,-1], [1,0],[-1,0]]

    r = random.randrange(0,4)


    current_x, current_y = find_ghost(gN)
    next_x = current_x + a[r][0]
    next_y = current_y + a[r][1]
    if not check_tree(next_x, next_y):
        if (gamemap[next_x][next_y] == '팩맨'):
            pygame.quit

        elif (gamemap[next_x][next_y] == 'x'):
            change_score(15,1)

        gamemap[current_x][current_y] = '0'
        gamemap[next_x][next_y] = gN
        make_trees()

    else:
        move_ghost(gN)


    


def main():
    global resized_tree, resized_pacman, resized_dot, resized_zero, resized_ghostA, resized_ghostB, resized_ghostC

    gamepad.fill((160,212,104))
    pygame.display.set_caption("HamPacHang")
    tree = pygame.image.load('tree.png')
    resized_tree = pygame.transform.scale(tree,(one_blocksize,one_blocksize))
    pacman = pygame.image.load('pacman.png')
    resized_pacman = pygame.transform.scale(pacman, (one_blocksize,one_blocksize))
    dot = pygame.image.load('dot.png')
    resized_dot = pygame.transform.scale(dot, (one_blocksize,one_blocksize))
    zero = pygame.image.load('zero.png')
    resized_zero = pygame.transform.scale(zero, (one_blocksize,one_blocksize))
    ghostA = pygame.image.load('ghostA.png')
    resized_ghostA = pygame.transform.scale(ghostA, (one_blocksize,one_blocksize))
    ghostB = pygame.image.load('ghostB.png')
    resized_ghostB = pygame.transform.scale(ghostB, (one_blocksize,one_blocksize))
    ghostC = pygame.image.load('ghostC.png')
    resized_ghostC = pygame.transform.scale(ghostC, (one_blocksize,one_blocksize))



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

