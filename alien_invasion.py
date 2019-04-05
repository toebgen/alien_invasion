import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
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

    # main loop of the game
    while True:
        game_functions.check_events(settings, screen, ship, bullets)
        ship.update()
        game_functions.update_bullets(bullets)
        game_functions.update_screen(settings, screen, ship, bullets)


run_game()
