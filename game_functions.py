import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(settings, screen, ship, bullets):
    """ Respond to keypresses and mouse events """
    # Check for keyboard input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def fire_bullet(settings, screen, ship, bullets):
    """ Fire a bullet if limit is not reached yet """
    # Create a new bullet and add to bullets group
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    """ Update position of bullets and get rid of old bullets """
    # Update positions
    bullets.update()

    # Remove bullets that have left the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(settings, screen, ship, bullets):
    """ Update images on the screen and flip to new screen """
    screen.fill(settings.bg_color)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()

    # Make most recent screen visible
    pygame.display.flip()

