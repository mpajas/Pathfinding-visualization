import os, sys
import pygame
from pygame.locals import *
import Node

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

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

grid = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(Node.Node(screen, i, j, w, h))
    grid.append(row)

for i in range(cols):
    for j in range(rows):
        grid[i][j].show(colors["black"])
pygame.display.update()


def detect_mouse_over():
    mousex, mousey = pygame.mouse.getpos()
    if not (not (mousex > 0) or not (mousex < WIDTH)) and 0 < mousey < HEIGHT:
        grid[mousex // rows][mousey // cols].show(colors["red"], s=0)


while 1:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()

    pygame.display.update()
    # screen.fill(gray)
    # pygame.display.flip()
