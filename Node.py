import pygame

class Node:
    def __init__(self,screen,x,y,w,h):
        self.x = x
        self.y = y
        self.screen = screen
        self.w = w
        self.h = h
        self.weight = 1

    def draw(self, color, s=1):
        pygame.draw.rect(self.screen, color, (self.x*self.w, self.y*self.h, self.w, self.h),s)
        pygame.display.update()

    def initial_draw(self, color, s=1):
        pygame.draw.rect(self.screen, color, (self.x*self.w, self.y*self.h, self.w, self.h),s)
        
    def path_draw(self,color,path):
        if path == "x":
            pygame.draw.rect((self.screen,color,(self.x*self.w, self.y*self.h, self.w, self.h),0))
            pygame.display.update()

    def mouse_click_draw(self, color, s=0):
        pygame.draw.rect(self.screen, color, (self.x*self.w, self.y*self.h, self.w, self.h),s)
        pygame.display.update()
        if color==(255,0,0):
            self.weight = 0
        else:
            self.weight = 1