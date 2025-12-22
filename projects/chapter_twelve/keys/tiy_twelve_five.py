# Patrick 22.12.2025.
# 12-5 Keys.

import sys

import pygame

from settings import Settings

class Keys:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initializing the game, and creating game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Keys")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

    def _check_events(self):
        """Respond to key events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                # Output is different numbers.

if __name__ == "__main__":
    k = Keys()
    k.run_game()