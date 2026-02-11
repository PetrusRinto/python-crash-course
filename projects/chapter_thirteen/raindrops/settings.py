# Patrick 10.02.2026.
# 13-3 Raindrops.

class Settings:
    """A class to store all settings for Raindrops"""

    def __init__(self):
        """Initialize the simulation's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = 'black'

        # Droplet settings.
        self.droplet_speed = 1.0