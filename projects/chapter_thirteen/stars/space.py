# Patrick 09.02.2026.
# 13-1 Stars.

import sys
import pygame

from settings import Settings
from star import Star

class Space:
    """Overall class to manage stars in space."""

    def __init__(self):
        """Initializing the program, and create resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Space')

        self.stars = pygame.sprite.Group()

        self._create_cluster()
    
    def run_program(self):
        """The main loop for the program."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
    
    def _create_cluster(self):
        """Create the cluster of stars."""
        # Create a star and keep adding stars until there's no room left.
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (self.settings.screen_height - 1 * star_height):
            while current_x < (self.settings.screen_width - 1 * star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width
            
            # Finished a row; reset x value, and increment y value.
            current_x = star_width
            current_y += 2 * star_height

    def _create_star(self, x_position, y_position):
        """Create a star and place it in the cluster."""
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    
    def _check_events(self):
        """Respond to keypresses and mouse clicks."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a instance for the program, and run it.
    sp = Space()
    sp.run_program()