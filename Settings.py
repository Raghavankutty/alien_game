class Settings:
    """A class to store all settings for Alien Inversion"""

    def __init__(self):
        """initialize the game's settings."""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 400
        self.bg_colour = (230,230,230)

        #ship settings
        self.ship_speed = 1.5

        #bullet  setting
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)