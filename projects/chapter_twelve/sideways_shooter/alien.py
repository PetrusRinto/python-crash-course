# Patrick 11.02.2026
# 13-5 Sideways Shooter Part 2.

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien."""

    def __init__(self, ss_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien on the right edge of the screen.
        self.rect.x = self.settings.screen_width - 100
        self.rect.y = self.rect.height
        
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        print(self.x)