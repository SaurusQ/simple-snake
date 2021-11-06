
import pygame
from helper import *

class Snake:
    def __init__(self, sizeX, sizeY):
        self.size = 1
        self.body = [(0 , 0)]
        self.dir = Dir.RIGHT
        self.sizeX = sizeX
        self.sizeY = sizeY
    
    def setDir(self, dir):
        # don't let snake do 180 turns
        if (self.dir.value + 2) % 4 != dir.value:
            self.dir = dir

    def move(self, fruit):
        cur = self.body[0]
        if self.dir == Dir.UP:
            if cur[1] < 1:
                self.body.insert(0, (cur[0], self.sizeY - 1))
            else:
                self.body.insert(0, (cur[0], cur[1] - 1))
        elif self.dir == Dir.DOWN:
            if cur[1] > (self.sizeY - 2):
                self.body.insert(0, (cur[0], 0))
            else:
                self.body.insert(0, (cur[0], cur[1] + 1))
        elif self.dir == Dir.LEFT:
            if cur[0] < 1:
                self.body.insert(0, (self.sizeX - 1, cur[1]))
            else:
                self.body.insert(0, (cur[0] - 1, cur[1]))
        elif self.dir == Dir.RIGHT:
            if cur[0] > (self.sizeX - 2):
                self.body.insert(0, (0, cur[1]))
            else: 
                self.body.insert(0, (cur[0] + 1, cur[1]))

        selfEat = False
        if self.body[0] in self.body[1:]:
            selfEat = True
            

        if fruit == self.body[0]:
            self.size += 1
            return (selfEat, True)
        else:
            self.body.pop()
            return (selfEat, False)

    def draw(self, win):
        for square in self.body:
            pygame.draw.rect(win, (200, 50, 10), (square[0] * SQUARE_SIZE + SQUARE_SIZE * 0.05, 
                square[1] * SQUARE_SIZE + SQUARE_SIZE * 0.05, SQUARE_SIZE * 0.9, SQUARE_SIZE * 0.9))
            
        
        
