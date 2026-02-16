# Patrick 06.01.2026.
# 12-6 Sideways Shooter.

import sys
from time import sleep

import pygame

from random import randint

from settings import Settings
from rocket import Rocket
from bullet import Bullet
from alien import Alien

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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
    
    def run_game(self):
        """Main loop for the game."""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)
    
    def _create_fleet(self):
        """Create an alien and place it on the right side of the screen."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.x, alien.rect.y

        current_x, current_y = alien_width, alien_height
        self._create_alien(current_x, current_y)
    
    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_alien = Alien(self)
        screen_h = self.settings.screen_height

        offset_y = randint(new_alien.rect.y, (screen_h - 3 * new_alien.rect.y))

        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position + offset_y

        if len(self.aliens.copy()) < self.settings.aliens_allowed:
            self.aliens.add(new_alien)
    
    def _check_events(self):
        """Respond to key events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to keyreleases."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of the bullets and delete old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= 1200:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.remove()
            self._create_fleet()
    
    def _rocket_hit(self):
        """Respond to the rocket being hit by an alien."""
        if self.stats.rockets_left > 0:
            # Decrement rockets_left.
            self.stats.rockets_left -= 1
            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.rocket.center_rocket()
            # Pause.
            sleep(0.5)
        else:
            self.game_active = False
    
    def _update_aliens(self):
        """Update aliens' position on the screen."""
        self.aliens.update()
        position = randint(400, 800)

        for alien in self.aliens.copy():
            if alien.rect.x <= position:
                self._create_fleet()
            if alien.rect.right <= 0:
                self.aliens.remove(alien)
    
    def _update_screen(self):
        """Update images to the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.rocket.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()
    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ss = SidewaysShooter()
    ss.run_game()