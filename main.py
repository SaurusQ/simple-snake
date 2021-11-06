from world import World
import pygame

FPS = 20
world = World(40, 40)
clock = pygame.time.Clock()

while not world.gameOver():
    world.gameLoop()
    clock.tick(FPS)
