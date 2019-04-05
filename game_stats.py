class GameStats():
    """ Track statistics for alien invasion """

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
    
    def reset_stats(self):
        """ Initialize statistics that can change during the game """
        self.ships_left = self.settings.ship_limit