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
            pygame.image.load('images/alien.bmp'),
            [60,60]
        )
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exacr position
        self.x = float(self.rect.x)
    
    def blitme(self):
        """ Draw the alien at its current location """
        self.screen.blit(self.image, self.rect)
