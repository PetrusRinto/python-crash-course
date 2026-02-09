# Patrick 15.01.2026.
# Homework...

import sys

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Homework")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('My game', False, 'black')
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('collision')
    
    screen.blit(sky_surface,(0, 0))
    screen.blit(ground_surface,(0, 300))
    pygame.draw.rect(screen, 'pink', score_rect.inflate(0, 10))
    pygame.draw.rect(screen, 'pink', score_rect.inflate(10, 0))
    screen.blit(score_surf, score_rect)

    snail_rect.x -= 4
    if snail_rect.right < 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print('Hit')

    pygame.display.update()
    clock.tick(60)