# Patrick 06.01.2026.
# 12-6 Sideways Shooter.

import pygame

class Rocket:
    """A class to manage the rocket."""

    def __init__(self, ss_game):
        """Initialize the rocket and set its starting position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag.
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position based on the movement flag."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        
        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        """Draw the rocket at its current position."""
        self.screen.blit(self.image, self.rect)
