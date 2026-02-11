# Patrick 10.02.2026.
# 13-3 Raindrops.

import pygame
from pygame.sprite import Sprite

class Droplet(Sprite):
    """A class to represent a single raindrop in the grid."""

    def __init__(self, rd_simulation):
        """Initializing the raindrop and set its starting position."""
        super().__init__()
        self.screen = rd_simulation.screen
        self.settings = rd_simulation.settings

        # Load the raindrop image and set its rect attribute.
        self.image = pygame.image.load('images/droplet.bmp')
        self.rect = self.image.get_rect()

        # Start each raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact vertical position.
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the droplet down the screen."""
        self.y += self.settings.droplet_speed
        self.rect.y = self.y