import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions


def run_game():
    # Initialize settings, game and screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen, settings)
    # Make a group for storing bullets
    bullets = Group()
    # Make a group of aliens
    aliens = Group()
    game_functions.create_fleet(settings, screen, ship, aliens)
    #alien = Alien(settings, screen)

    # main loop of the game
    while True:
        game_functions.check_events(settings, screen, ship, bullets)
        ship.update()
        game_functions.update_bullets(aliens, bullets)
        game_functions.update_aliens(settings, aliens)
        game_functions.update_screen(settings, screen, ship, aliens, bullets)


run_game()
