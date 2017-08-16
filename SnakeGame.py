import random
import pygame,sys
from pygame.locals import *

FPS=10
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
CELLWIDTH = int(WINDOWWIDTH/CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT/CELLSIZE)

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
DARKGREEN = (0,100,0)
DARKGRAY = (40,40,40)
BGCOLOR = BLACK

#Direction
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

#SnakeHead
HEAD = 0

def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))

def drawApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleRect)


def drawSnake(snakeCords):
    for cord in snakeCords:
        x = cord['x'] * CELLSIZE
        y = cord['y'] * CELLSIZE
        snakeSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, DARKGREEN, snakeSegmentRect)
        snakeInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, GREEN, snakeInnerSegmentRect)


def getRandomLocation():
    return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}


def RunGame():
    startX = random.randint(5,CELLWIDTH-5)
    startY = random.randint(5, CELLHEIGHT - 5)

    snakeCord = [{'x' : startX , 'y' : startY},
                 {'x' : startX-1 , 'y' : startY },
                 {'x' : startX-2 , 'y' : startY}]
    direction = RIGHT
    apple = getRandomLocation()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        #Checks:- Hit boundary
        if snakeCord[HEAD]['x'] == -1 or snakeCord[HEAD]['x'] == CELLWIDTH or snakeCord[HEAD]['y'] ==  -1 or snakeCord[HEAD]['y'] == CELLHEIGHT:
                return
        #Checks:- Hit itself
        for wormBody in snakeCord[1:]:
            if wormBody['x'] == snakeCord[HEAD]['x'] and wormBody['y'] == snakeCord[HEAD]['y']:
                return

        #Checks:- For Apple Found
        if snakeCord[HEAD]['x'] == apple['x'] and snakeCord[HEAD]['y'] == apple['y']:
            apple = getRandomLocation()  # if found set a new apple somewhere
        else:
            del snakeCord[-1]  # remove snake's tail segment


        if direction == UP:
            newHead = {'x': snakeCord[HEAD]['x'], 'y': snakeCord[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': snakeCord[HEAD]['x'], 'y': snakeCord[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': snakeCord[HEAD]['x'] - 1, 'y': snakeCord[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': snakeCord[HEAD]['x'] + 1, 'y': snakeCord[HEAD]['y']}

        snakeCord.insert(0,newHead)
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawSnake(snakeCord)
        drawApple(apple)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


#def ShowGameOverScreen():

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf',18)
    pygame.display.set_caption('Snake_Game')


    while True:
        RunGame()

if __name__ == '__main__':
    main()
