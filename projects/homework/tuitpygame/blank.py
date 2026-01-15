# Patrick 15.01.2026.
# Homework...

import sys

import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Homework")
clock = pygame.time.Clock()
test_surface = pygame.Surface((100, 200))
test_surface.fill('red')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(test_surface,(200, 100))

    pygame.display.update()
    clock.tick(60)