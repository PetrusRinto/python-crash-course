# Patrick 11.12.2025 / 15.12.2025 / 22.12.2025.
# 12-4 Rocket.

import sys

import pygame

from settings import Settings
from rocket import Rocket

class RocketMan:
    """Creating a pygame where you control a rocket."""

    def __init__(self):
        """Initializing the game, and create resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rocket Man")

        self.rocket = Rocket(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.rocket.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.rocket.moving_left = True
                elif event.key == pygame.K_UP:
                    self.rocket.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.rocket.moving_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.rocket.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.rocket.moving_left = False
                elif event.key == pygame.K_UP:
                    self.rocket.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.rocket.moving_down = False
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance, and run the game.
    rm = RocketMan()
    rm.run_game()