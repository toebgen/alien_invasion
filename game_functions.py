import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_play_button(settings, screen, stats, scoreboard, play_button, ship,
                      aliens, bullets, mouse_x, mouse_y):
    """ Start new game when the player clocks play """
    # TODO Countdown 3-2-1 before start of new level

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings
        settings.initialize_dynamic_settings()

        # Reset game statistics
        stats.reset()
        stats.game_active = True

        # Reset scoreboard images
        scoreboard.prep_score()
        scoreboard.prep_high_score()
        scoreboard.prep_level()
        scoreboard.prep_ships()
        
        # Empty list of bullets and aliens.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

        # Hide mouse cursor
        pygame.mouse.set_visible(False)


def check_events(settings, screen, stats, scoreboard, play_button, ship,
                 aliens, bullets):
    """ Respond to keypresses and mouse events """
    # Check for keyboard input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, scoreboard, play_button,
                              ship, aliens, bullets, mouse_x, mouse_y)

def fire_bullet(settings, screen, ship, bullets):
    """ Fire a bullet if limit is not reached yet """
    # Create a new bullet and add to bullets group
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)
        # TODO Display message about max number of bullets

def update_bullets(settings, screen, ship, stats, scoreboard, aliens, bullets):
    """ Update position of bullets and get rid of old bullets """
    # Update positions
    bullets.update()

    # Remove bullets that have left the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(settings, screen, stats, scoreboard, ship,
                                  aliens, bullets)
    
def check_bullet_alien_collisions(settings, screen, stats, scoreboard, ship,
                                  aliens, bullets):
    """ Respond to bullet alien collisions """
    #TODO Check rect between previous bullet position and current, bullet might
    # fly past alien right now

    # Remove any aliens and bullets that have collided
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += settings.alien_points * len(aliens)
            scoreboard.prep_score()
        check_high_score(stats, scoreboard)

    if len(aliens) == 0:
        # Start a new level!
        stats.level += 1
        scoreboard.prep_level()

        # Destroy existing bullets, speedup game and create new fleet
        bullets.empty()
        settings.increase_speed()
        create_fleet(settings, screen, ship, aliens)

def check_aliens_bottom(settings, screen, stats, scoreboard, ship, aliens,
                        bullets):
    """ Check if any aliens habe reached the bottom of the screen """
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen.get_rect().bottom:
            # Treat hits the same as if ship got hit
            print('Alien has reached the bottom!')
            ship_hit(settings, screen, stats, scoreboard, ship, aliens,
                     bullets)
            break

def get_number_aliens_x(settings, alien_width):
    """ Determine the number of aliens that fit in a row """
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(settings, ship_height, alien_height):
    """ Determine the number of rows of aliens that fit on the screen """
    available_space_y = settings.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(settings, screen, aliens, alien_number, row_number):
    """ Create an alien and place it in the row """
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(settings, screen, ship, aliens):
    """ Create a full fleet of aliens """
    # Create an alien and find the number of aliens in a row
    # Spacing between each alien is equal to one alien width
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)
    
    # Create fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row
            create_alien(settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(settings, aliens):
    """ Respond appropriatly if any aliens have reached an edge """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    """ Drop the entire fleet and change the fleet's direction """
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1

def update_aliens(settings, screen, stats, scoreboard, ship, aliens, bullets):
    """
    Check if the fleet is at an edge,
    then update the positions of all aliens in the fleet
    """
    check_fleet_edges(settings, aliens)
    aliens.update()

    # Look for alien ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, screen, stats, scoreboard, ship, aliens, bullets)
    
    # Look for aliens hitting the bottom of the screen
    check_aliens_bottom(settings, screen, stats, scoreboard, ship, aliens,
                        bullets)

def ship_hit(settings, screen, stats, scoreboard, ship, aliens, bullets):
    """ Respond to ship being hit by alien """
    if stats.ships_left > 0:
        # Decrement ships_left
        stats.ships_left -= 1

        # Update scoreboard
        scoreboard.prep_ships()

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create new fleet and center the ship
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_high_score(stats, scoreboard):
    """ Check to see if there's a new high score """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()
        
def update_screen(settings, screen, stats, scoreboard, ship, aliens,
                  bullets, play_button):
    """ Update images on the screen and flip to new screen """
    screen.fill(settings.bg_color)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets:
        bullet.draw_bullet()

    aliens.draw(screen)
    ship.blitme()

    # Draw score information
    scoreboard.show()

    # Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw()
    
    # Make most recent screen visible
    pygame.display.flip()

