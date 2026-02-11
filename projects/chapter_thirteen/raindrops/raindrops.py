# Patrick 10.02.2026.
# 13-3 Raindrops.

import sys
import pygame

from settings import Settings
from droplet import Droplet

class Raindrops:
    """Overall class to manage simulation assets and behavior."""

    def __init__(self):
        """Initializing the simulation, and create resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrops")

        self.droplets = pygame.sprite.Group()

        self._create_raindrops()

    def run_simulation(self):
        """Start the main loop for the simulation."""
        while True:
            self._check_events()
            self._update_droplets()
            self._update_screen()
            self.clock.tick(60)

    def _create_raindrops(self):
        """Create the grid of raindrops."""
        # Create a raindrop(droplet) and keep adding raindrops until covered.
        # Spacing between raindrops is on droplet width.
        droplet = Droplet(self)
        droplet_width, droplet_height = droplet.rect.size

        current_x, current_y = droplet_width, droplet_height
        while current_y < (self.settings.screen_height - 1 * droplet_height):
            while current_x < (self.settings.screen_width - 1 * droplet_width):
                self._create_droplet(current_x, current_y)
                current_x += 2 * droplet_width

            # Finished a row; reset x value, and increment y value.
            current_x = droplet_width
            current_y += 2 * droplet_height

    def _create_droplet(self, x_position, y_position):
        """Create a droplet and place it in the row."""
        new_droplet = Droplet(self)
        new_droplet.y = y_position
        new_droplet.rect.x = x_position
        new_droplet.rect.y = y_position
        self.droplets.add(new_droplet)
    
    def _check_events(self):
        """Respond to keypresses."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_droplets(self):
        """Update the position of all droplets on the grid."""
        self.droplets.update()

        # Get rid of droplets that have disappeared.
        for droplet in self.droplets.copy():
            if droplet.rect.top >= 800:
                self.droplets.remove(droplet)
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.droplets.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the simulation.
    rd = Raindrops()
    rd.run_simulation()