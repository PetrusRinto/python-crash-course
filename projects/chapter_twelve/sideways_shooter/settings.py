# Patrick 06.01.2026.
# 12-6 Sideways Shooter.

class Settings:
    """A class to store all the settings for Sideways Shooter."""

    def __init__(self):
        """Initialize settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (238,235,255)

        # Rocket settings.
        self.rocket_speed = 10

        # Bullet settings.
        self.bullet_speed = 6.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)