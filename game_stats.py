class GameStats():
    """ Track statistics for alien invasion """

    def __init__(self, settings):
        self.settings = settings
        self.reset()

        # Start game in inactive state
        self.game_active = False
    
    def reset(self):
        """ Initialize statistics that can change during the game """
        self.score = 0
        self.ships_left = self.settings.ship_limit