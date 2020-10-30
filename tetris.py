import pygame
import sys
import os

size = width, height = 400, 600
black = 0, 0, 0
pygame.init()
screen = pygame.display.set_mode(size)

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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill (black)
    screen.blit(red,(0,0))
    screen.blit(blue,(100,100))
    screen.blit(orange,(200,150))
    screen.blit(violet,(200,50))
    screen.blit(yellow,(200,300))
    screen.blit(cyan,(100,400))
    screen.blit(green,(150, 450))

    pygame.display.flip()
    pygame.display.update()
    
    
