# Patrick 11.12.2025 / 15.12.2025.
# 12-4 Rocket.

import sys

import pygame

class RocketMan:
    """Creating a pygame where you control a rocket."""

    def __init__(self):
        """Initializing the game, and create resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Rocket Man")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    # Make a game instance, and run the game.
    rm = RocketMan()
    rm.run_game()