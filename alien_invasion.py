import sys
import pygame

from settings import Settings

def run_game():
    # Initialize settings, game and screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Set background color
    bg_color = (220, 220, 220)

    # main loop of the game
    while True:
        # Check for keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make most recent screen visible
        screen.fill(settings.bg_color)
        pygame.display.flip()

run_game()
