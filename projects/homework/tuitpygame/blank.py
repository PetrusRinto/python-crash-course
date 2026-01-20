# Patrick 15.01.2026.
# Homework...

import sys

import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Homework")
clock = pygame.time.Clock()
sky_surface = pygame.image.load('graphics/sky.png')
ground_surface = pygame.image.load('graphics/ground.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(sky_surface,(0, 0))
    screen.blit(ground_surface,(0, 300))

    pygame.display.update()
    clock.tick(60)