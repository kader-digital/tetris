import pygame
import sys
from time import sleep
import os
import random

size = width, height = 400, 600
black = 0, 0, 0
pygame.init()
screen = pygame.display.set_mode(size)

def next_color ():
    return random.randrange(7)

red = pygame.image.load(os.path.join('pieces','piece-red.png'))
red = pygame.transform.scale (red, (250, 250))

blue = pygame.image.load(os.path.join('pieces','piece-blue.png'))
blue = pygame.transform.scale (blue, (250, 250))

orange = pygame.image.load(os.path.join('pieces','piece-orange.png'))
orange = pygame.transform.scale (orange, (250,250))

violet = pygame.image.load(os.path.join('pieces','piece-violet.png'))
violet = pygame.transform.scale (violet, (250,250))

yellow = pygame.image.load(os.path.join('pieces','piece-yellow.png'))
yellow = pygame.transform.scale (yellow, (250, 250))

cyan = pygame.image.load(os.path.join('pieces','piece-cyan.png'))
cyan = pygame.transform.scale (cyan, (250, 250))

green = pygame.image.load(os.path.join('pieces','piece-green.png'))
green = pygame.transform.scale (green, (250,250))

running = True
x, y = 0, 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            red = pygame.transform.rotate(red, 90)
        elif keys[pygame.K_DOWN] and y < 425:
            y += 25
        elif keys[pygame.K_LEFT] and x >= -75:
            x -=25
        elif keys[pygame.K_RIGHT] and x < 250:
            x += 25

    screen.fill (black)
    screen.blit(red,(x,y))

    pygame.display.flip()
    pygame.display.update()
    
    
