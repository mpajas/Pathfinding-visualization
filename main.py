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
        grid[i][j].initial_draw(colors["black"])
pygame.display.update()

mouse = pygame.mouse


# fpsClock = pygame.time.Clock()


def detect_mouse_over(color):
    mousex, mousey = pygame.mouse.get_pos()
    if 0 < mousex < WIDTH and 0 < mousey < HEIGHT:
        grid[mousex // int(w)][mousey // int(h)].mouse_click_draw(color, s=0)
        # pygame.display.update()

while 1:
    left_pressed, middle_pressed, right_pressed = mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if left_pressed:
        detect_mouse_over(colors["red"])
    if right_pressed:
        detect_mouse_over(colors["black"])
    if middle_pressed:
        screen.fill(colors["gray"])
        for row in grid:
            for element in row:
                element.initial_draw(colors["black"])
        pygame.display.update()
    # detect_mouse_over()
    pygame.display.update()
    # pygame.display.flip()
