import pygame
import sys

size = width, height = 400, 600
black = 0, 0, 0
pygame.init()
screen = pygame.display.set_mode(size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill (black)
    pygame.display.flip()
    
