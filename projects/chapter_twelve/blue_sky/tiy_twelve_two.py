# Patrick 09.12.2025.
# 12-2 Game Character.

import pygame

class GameCharacter:
    """A class to manage the game character."""

    def __init__(self, bsg_game):
        """Initializing the game character and set its position."""
        self.screen = bsg_game.screen
        self.screen_rect = bsg_game.screen.get_rect()

        # Load the game character image and get its rect.
        self.image = pygame.image.load('images/gamecharacter.bmp')
        self.rect = self.image.get_rect()

        # Start the game character at the center of the screen.
        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        """Draw the game character at its current location."""
        self.screen.blit(self.image, self.rect)