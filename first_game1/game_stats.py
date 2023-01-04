class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an active state. = True
        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0
    
    def reset_stats(self):
        """Initialize statistics that can change during"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0