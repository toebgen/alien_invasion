
class Settings():
    """ Class to store all setting for Alien Invasion """

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (220, 220, 220)
        
        # Ship settings
        self.ship_speed_factor = 32.0

        # Alien settings
        self.alien_speed_factor = 8.0
        self.fleet_drop_speed = 32
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Bullet settings
        self.bullet_speed_factor = 32.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3