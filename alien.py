import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ A class to represent a single alien in the fleet """

    def __init__(self, settings, screen):
        """ Initialize the alien and set its starting position """
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load alien image and set its rect attribute
        self.image = pygame.transform.scale(
            pygame.image.load('images/alien.png'),
            [60,60]
        )
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exacr position
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """ Return True if alien is at edge of screen """
        if self.rect.right >= self.screen.get_rect().right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """ Move the alienright or left """
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """ Draw the alien at its current location """
        self.screen.blit(self.image, self.rect)
