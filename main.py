import os, sys
import pygame
from pygame.locals import *
import Node
import Astar

pygame.init()

WIDTH = 800
HEIGHT = 800

colors = {"black": (0, 0, 0),
          "gray": (100, 100, 100),
          "red": (255, 0, 0),
          "green": (0, 255, 0),
          "blue": (0, 0, 255)}

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
screen.fill(colors["gray"])

rows = 50
cols = 50

w = WIDTH / rows
h = HEIGHT / cols

#making a grid of Nodes (rectangles)
grid = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(Node.Node(screen, i, j, w, h))
    grid.append(row)
#initial drawing of the grid
for i in range(cols):
    for j in range(rows):
        grid[i][j].initial_draw(colors["black"])
pygame.display.update()
#adding neighbours of each grid member
for i in range(cols):
    for j in range(rows):
        grid[i][j].add_neighbours(grid)

start = grid[10][10]
end = grid[43][48]

mouse = pygame.mouse

fpsClock = pygame.time.Clock()

pathfinder = Astar.Astar(grid,grid[0][0],grid[49][49])

def mouse_click(color):
    mousex, mousey = mouse.get_pos()
    grid[mousex // int(w)][mousey // int(h)].draw(color, s=0, mouse=True)

while 1:
    left_pressed, middle_pressed, right_pressed = mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if left_pressed:
            mouse_click(colors["black"])

        if right_pressed:
            #mouse_click(colors["black"])
            pathfinder.astar()

        if middle_pressed:
            screen.fill(colors["gray"])
            for row in grid:
                for element in row:
                    element.initial_draw(colors["black"])
            pygame.display.update()


    #pygame.display.update()
    pygame.display.flip()
