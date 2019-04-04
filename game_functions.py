import sys

import pygame

def check_events():
    """ Respond to keypresses and mouse events """
    # Check for keyboard input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, ship):
    """ Update images on the screen and flip to new screen """
    screen.fill(settings.bg_color)
    ship.blitme()

    # Make most recent screen visible
    pygame.display.flip()

