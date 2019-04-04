import pygame

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

    # main loop of the game
    while True:
        game_functions.check_events(ship)
        ship.update()
        game_functions.update_screen(settings, screen, ship)

run_game()
