class GameStats():
    """ Track statistics for alien invasion """

    def __init__(self, settings):
        self.settings = settings
        self.reset()

        # Start game in inactive state
        self.game_active = False

        # High score should never be reset
        self.high_score = 0
    
    def reset(self):
        """ Initialize statistics that can change during the game """
        self.score = 0
        self.ships_left = self.settings.ship_limit