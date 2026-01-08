# Patrick 06.01.2026.
# 12-6 Sideways Shooter.

import sys

import pygame

from settings import Settings
from rocket import Rocket

class SidewaysShooter:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initializing the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Sideways Shooter')
        
        self.rocket = Rocket(self)
        # self.bullets = 
    
    def run_game(self):
        """Main loop for the game."""
        while True:
            self._check_events()
            self.rocket.update()
            # self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to key events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _check_keydown_events(self):
        """Respond to keypresses."""
    
    def _check_keyup_events(self):
        """Respond to keyreleases."""
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
    
    def _update_bullets(self):
        """Update position of the bullets and delete old bullets."""
    
    def _update_screen(self):
        """Update images to the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        pygame.display.flip()
    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ss = SidewaysShooter()
    ss.run_game()