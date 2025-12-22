# Patrick 15.12.2025 / 22.12.2025.
# Rocket module.

import pygame

class Rocket:
    """A class to manage the rocket."""

    def __init__(self, rm_game):
        """Initialize the rocket and set its starting position."""
        self.screen = rm_game.screen
        self.screen_rect = rm_game.screen.get_rect()

        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        # Movement flag.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 20
        if self.moving_left:
            self.rect.x -= 20
        if self.moving_up:
            self.rect.y -= 20
        if self.moving_down:
            self.rect.y += 20

    def blitme(self):
        """Draw the rocket at its current position."""
        self.screen.blit(self.image, self.rect)