class GameStats:
    """Class for Alien Invasion game statistics"""

    def __init__(self, ai_game):
        """Initialize game stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True
    

    def reset_stats(self):
        """Resets the stats for the game"""
        # number of ships
        self.ships_left = self.settings.ship_limit