import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    # Initialize settings, game and screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    # main loop of the game
    while True:
        # Check for keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make most recent screen visible
        screen.fill(settings.bg_color)
        ship.blitme()

        pygame.display.flip()

run_game()
