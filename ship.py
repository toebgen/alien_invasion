import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, settings, screen):
        """ Initialize ship and set starting position """
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load the image and get its rect
        self.image = pygame.transform.scale(
            pygame.image.load('images/ship.png'),
            [60,30])
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store decimal value for ship's center
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """ Center the ship on the screen """
        self.center = self.screen_rect.centerx

    def update(self):
        """ Update the ship's position based on the movement flag """
        # Update ship's center valute, not the rect
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.center += self.settings.ship_speed_factor
        if self.moving_left and (self.rect.left > 0):
            self.center -= self.settings.ship_speed_factor

        # Update rect from center
        self.rect.centerx = self.center

    def blitme(self):
        """ Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)
