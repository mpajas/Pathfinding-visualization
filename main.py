import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')


class vertex:
    def __init__(self,x,y,rows,cols):
        self.x = x
        self.y = y

    def show(self, color, s=1):
        pygame.draw.rect(screen, color, (self.x*w, self.y*h, w, h),s)
        pygame.display.update()



pygame.init()

WIDTH = 800
HEIGHT = 800




size = WIDTH, HEIGHT
gray = (100, 100, 100)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
screen = pygame.display.set_mode(size)

rows = 50
cols = 50

w = WIDTH/rows
h = HEIGHT/cols

grid = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(vertex(i,j,rows,cols))
    grid.append(row)


for i in range(cols):
        for j in range(rows):
            grid[i][j].show((255, 255, 255))
pygame.display.update()

def detect_mouse_over():
    mousex,mousey = pygame.mouse.getpos()
    if mousex>0 and mousex<WIDTH and mousey>0 and mousey<HEIGHT:
        grid[mousex//rows][mousey//cols].show(red,0)

while 1:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()

    pygame.display.update()
    #screen.fill(gray)
    #pygame.display.flip()