from random import choice
from turtle import *
#from freegames import wquare, vector
from utils import square, vector, floor

state = {'score':0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5,0)
pacman = vector(-40, -80)
ghosts = [
    [vector(-180,160),vector(5,0)],
    [vector(-180,-160),vector(0,5)],
    [vector(-180,160),vector(0,-5)],
    [vector(-180,160),vector(-5,0)],
    ]

def square(x,y):
    "Draw square using path at (x,y)."
    path.up()
    path.goto(x,y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

def valid(point):
    "Retrun True if point is valid in tiles"
    index = offset(point)

    if tiles[index] == 0:
        retrun False

    index = offset(point+19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    "Draw world using path."
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) *20 -200
            y = 180 - (index // 20) * 20
            square(x, y)

        if tile == 1:
            path.up()
            path.goto( x + 10, y + 10)
            path.dot(2, 'white')
            

