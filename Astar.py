import pygame
import math


class Astar:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = graph[0][0]  # start
        self.goal = graph[49][49]  # goal
        self.open_set = [self.start]
        self.start.g = 0
        self.start.h = self.heuristic(self.start, self.goal)
        self.start.f = 0
        self.start.f += self.start.h
        self.closed_set = []
        self.start.draw((0, 0, 0), s=0)
        self.goal.draw((0, 0, 0), s=0)

    def draw_path(self, total_path):
        for node in total_path:
            node.draw((0, 255, 0), s=0)
            pygame.display.update()

    def heuristic(self, a, b):
        p1 = (a.x, a.y)
        p2 = (b.x, b.y)
        d = math.dist(p1, p2)
        return d

    def reconstruct_path(self, current):
        total_path = [current]
        while current.previous is not None:
            total_path.append(current.previous)
            current = current.previous
        self.draw_path(total_path)
        # return total_path

    def astar(self):
        while self.open_set:
            fmin = min([x.f for x in self.open_set])
            current = None
            for x in self.open_set:
                if x.f == fmin:
                    current = x
                    break

            if current == self.goal:
                self.reconstruct_path(current)
                break

            self.open_set.remove(current)
            self.closed_set.append(current)
            current.draw((255, 0, 0), s=0)
            for neighbour in current.neighbours:
                if neighbour in self.closed_set:
                    continue
                #neighbour.draw((255, 0, 0), s=0)
                p1 = (neighbour.x, neighbour.y)
                p2 = (current.x, current.y)
                tentative_g = current.g + math.dist(p1, p2)
                if tentative_g < neighbour.g:
                    # better path to neighbour than previous one
                    neighbour.previous = current
                    neighbour.g = tentative_g
                    neighbour.h = self.heuristic(neighbour, self.goal)
                    neighbour.f = neighbour.g + neighbour.h
                    if neighbour not in self.open_set:
                        self.open_set.append(neighbour)
