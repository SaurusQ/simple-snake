
import pygame
import random
from snake import Snake
from helper import *

class World:
    def __init__(self, sizeX, sizeY):
        pygame.init()
        self.win = pygame.display.set_mode((SQUARE_SIZE * sizeX, SQUARE_SIZE* sizeY))
        pygame.display.set_caption("Snake")
        self.snake = Snake(sizeX, sizeY)
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.running = True
        self.fail = False
        self.aiMode = False
        random.seed()
        self.setFruit()

    def gameOver(self):
        return not (self.running and not self.fail)

    def setFruit(self):
        while True:
            x = random.randint(0, self.sizeX - 1)
            y = random.randint(0, self.sizeY - 1)
            if not (x, y) in self.snake.body:
                self.fruit = (x, y)
                break

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        keys = pygame.key.get_pressed()

        # toggle ai
        if keys[pygame.K_SPACE]:
            self.aiMode = not self.aiMode

        if not self.aiMode:
            # move snake
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.snake.setDir(Dir.UP)
            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.snake.setDir(Dir.DOWN)
            elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.snake.setDir(Dir.LEFT)
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.snake.setDir(Dir.RIGHT)

            if keys[pygame.K_ESCAPE]:
                self.running = False
        else:
            # ai
            diffx = self.snake.body[0][0] - self.fruit[0]
            diffy = self.snake.body[0][1] - self.fruit[1]
            dirr = Dir.DOWN
            # chasing fruit
            if diffx != 0:
                dirr = Dir.RIGHT
            elif diffy != 0:
                dirr = Dir.DOWN
            
            # avoidance
            sx = self.snake.body[0][0]
            sy = self.snake.body[0][1]
            if dirr == Dir.DOWN and (sx, (sy + 1) % self.sizeY) in self.snake.body:
                dirr = Dir.RIGHT
            elif dirr == Dir.RIGHT and ((sx + 1) % self.sizeX, sy) in self.snake.body:
                dirr = Dir.DOWN
            
            self.snake.setDir(dirr)
        
    def gameLoop(self):
        self.handleInput()
        (self.fail, eatenFruit) = self.snake.move(self.fruit)
        if eatenFruit:
            self.setFruit() # fruit was eaten, reset fruit

        # draw
        self.win.fill((0, 0, 0))
        self.snake.draw(self.win)
        pygame.draw.rect(self.win, (200, 1, 170), (self.fruit[0] * SQUARE_SIZE + SQUARE_SIZE * 0.25, 
            self.fruit[1] * SQUARE_SIZE + SQUARE_SIZE * 0.25, SQUARE_SIZE * 0.5, SQUARE_SIZE * 0.5))
        pygame.display.update()
