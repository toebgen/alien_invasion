import sys

import pygame

def check_events(ship):
    """ Respond to keypresses and mouse events """
    # Check for keyboard input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                # Move the ship to the left
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(settings, screen, ship):
    """ Update images on the screen and flip to new screen """
    screen.fill(settings.bg_color)
    ship.blitme()

    # Make most recent screen visible
    pygame.display.flip()

