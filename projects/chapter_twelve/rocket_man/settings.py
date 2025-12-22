# Patrick 15.12.2025 / 22.12.2025.
# Settings module for the rocket game.

class Settings:
    """A class to store all the settings for Rocket Man."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Rocket settings.
        self.rocket_speed = 15