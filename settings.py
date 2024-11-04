class Settings:
    """A class to hold the settings for the game"""

    def __init__(self):
        """Initializes settings for game window and various assets"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (210, 230, 230)

        # ship settings
        self.ship_speed = 1.5

        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3 * 3
        self.bullet_height = 15 * 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
         # fleet direction (1 = -> | -1 = <-)
        self.fleet_direction = 1