import pygame

class Node:
    def __init__(self,screen,x,y,w,h):
        self.x = x
        self.y = y
        self.screen = screen
        self.w = w
        self.h = h

    def show(self, color, s=1):
        pygame.draw.rect(self.screen, color, (self.x*self.w, self.y*self.h, self.w, self.h),s)
        pygame.display.update()