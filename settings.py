
class Settings():
    """ Class to store all settings for Alien Invasion """

    def __init__(self):
        """ Initialize static settings """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (220, 220, 220)
        
        # Alien settings
        self.fleet_drop_speed = 64
        
        # Bullet settings
        self.bullet_width = 1150
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Ship settings
        self.ship_limit = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.2
        # How quicly the alien_point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game """
        self.alien_speed_factor = 4.0
        self.bullet_speed_factor = 16.0
        self.ship_speed_factor = 16.0
        
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """ Increase the speed settings and alien point values """
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        