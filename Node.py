import pygame


class Node:
    def __init__(self, screen, x, y, rectwidth, rectheight):
        self.x = x
        self.y = y
        self.screen = screen
        self.rectwidth = rectwidth
        self.rectheight = rectheight
        self.val = 1
        self.neighbours = []
        self.previous = None
        self.f = 0
        self.g = 99999999
        self.h = 0

    def draw(self, color, s=1, mouse=False):
        if mouse:
            pygame.draw.rect(self.screen, color, (self.x * self.rectwidth, self.y * self.rectheight,
                                                  self.rectwidth, self.rectheight), s)
            self.g=0
            pygame.display.update()
            if color == (255, 0, 0):
                self.val = 0
            else:
                self.val = 1
        else:
            pygame.draw.rect(self.screen, color, (self.x * self.rectwidth, self.y * self.rectheight,
                                                  self.rectwidth, self.rectheight), s)
            pygame.display.update()

    def initial_draw(self, color, s=1):
        pygame.draw.rect(self.screen, color, (self.x * self.rectwidth, self.y * self.rectheight,
                                              self.rectwidth, self.rectheight), s)

    def add_neighbours(self, grid):
        pos = (self.x, self.y)
        rows = len(grid)
        cols = len(grid[0]) if rows else 0
        for i in range(max(0, pos[0] - 1), min(rows, pos[0] + 2)):
            for j in range(max(0, pos[1] - 1), min(cols, pos[1] + 2)):
                if (i, j) != pos:
                    self.neighbours.append(grid[i][j])

    def print_neighbours(self):
        for n in self.neighbours:
            pos = (n.x, n.y)
            print(pos)